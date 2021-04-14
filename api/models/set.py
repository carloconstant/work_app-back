from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Set(models.Model):
  # define fields
  # https://docs.djangoproject.com/en/3.0/ref/models/fields/
  rep_count = models.IntegerField()
  set_count = models.IntegerField()
  owner = models.ForeignKey(
      get_user_model(),
      on_delete=models.CASCADE
  )

  def __str__(self):
    # This must return a string
    return f"The set id is:{self.id} the amount of reps: {self.rep_count}. "

  def as_dict(self):
    """Returns dictionary version of set models"""
    return {
        'id': self.id,
        'rep_count': self.rep_count,
        'set_count':self.set_count
    }
