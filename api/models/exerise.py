from django.db import models
from django.contrib.auth import get_user_model, get_set_model

# Create your models here.
class Exerise(models.Model):
  # define fields
  # https://docs.djangoproject.com/en/3.0/ref/models/fields/
  body_part = models.CharField(max_length=1000)

  set_count = models.ForeignKey(get_set_model())
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
        'body_part': self.rep_count,
        'set_count':self.set_count
    }
