from django.db import models
#from django.utils import timezone
#from django.contrib.auth.models import User


# Create your models here.
class Type(models.Model):
    Recreation_Type_Indoor = models.CharField(max_length=50)
    Recreation_Type_Outdoor = models.CharField (max_length=50)
    Public = models.CharField (max_length=3)
    Private = models.CharField (max_length=3)


    #publish = models.DateTimeField(default=timezone.now)

    #class Meta:
        #ordering = ('-publish',)

    def __str__(self):
        return self.Recreation_Type_Indoor

