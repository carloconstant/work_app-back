from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.exceptions import PermissionDenied
from rest_framework import generics, status
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user, authenticate, login, logout
from django.middleware.csrf import get_token

from ..models.set import Set
from ..serializers import SetSerializer, UserSerializer

# Create your views here.
class Sets(generics.ListCreateAPIView):
    permission_classes=(IsAuthenticated,)
    serializer_class = SetSerializer
    def get(self, request):
        """Index request"""
        # Get all the sets:
        # sets = set.objects.all()
        # Filter the sets by owner, so you can only see your owned sets
        sets = Set.objects.filter(owner=request.user.id)
        # Run the data through the serializer
        data = SetSerializer(sets, many=True).data
        return Response({ 'sets': data })

    def post(self, request):
        """Create request"""
        print(request.user)
        # Add user to request data object
        new_set = request.data['set']
        # Serialize/create set
        new_set['owner'] = request.user.id
        set = SetSerializer(data=new_set)
        # If the set data is valid according to our serializer...
        if set.is_valid():
            # Save the created set & send a response
            set.save()
            return Response({ 'set': set.data }, status=status.HTTP_201_CREATED)
        # If the data is not valid, return a response with the errors
        return Response(set.errors, status=status.HTTP_400_BAD_REQUEST)

class SetDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=(IsAuthenticated,)
    def get(self, request, pk):
        """Show request"""
        # Locate the set to show
        set = get_object_or_404(Set, pk=pk)
        # Only want to show owned sets?
        if not request.user.id == set.owner.id:
            raise PermissionDenied('Unauthorized, you do not own this set')

        # Run the data through the serializer so it's formatted
        data = SetSerializer(set).data
        return Response({ 'set': data })

    def delete(self, request, pk):
        """Delete request"""
        # Locate set to delete
        set = get_object_or_404(Set, pk=pk)
        # Check the set's owner agains the user making this request
        if not request.user.id == set.owner.id:
            raise PermissionDenied('Unauthorized, you do not own this set')
        # Only delete if the user owns the  set
        set.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def partial_update(self, request, pk):
        """Update Request"""
        # Remove owner from request object
        # This "gets" the owner key on the data['set'] dictionary
        # and returns False if it doesn't find it. So, if it's found we
        # remove it.
        if request.data['set'].get('owner', False):
            del request.data['set']['owner']

        # Locate set
        # get_object_or_404 returns a object representation of our set
        set = get_object_or_404(Set, pk=pk)
        # Check if user is the same as the request.user.id
        if not request.user.id == set.owner.id:
            raise PermissionDenied('Unauthorized, you do not own this set')

        # Add owner to data object now that we know this user owns the resource
        request.data['set']['owner'] = request.user.id
        # Validate updates with serializer
        data = SetSerializer(set, data=request.data['set'])
        if data.is_valid():
            # Save & send a 204 no content
            data.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        # If the data is not valid, return a response with the errors
        return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)
