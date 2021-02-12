from django.db import models
#from django.utils import timezone
#from django.contrib.auth.models import User


class People(models.Model):
    name = models.CharField(max_length=50)
    phone = models.BigIntegerField(max_length=50)
    email = models.CharField(max_length=50)

    #publish = models.DateTimeField(default=timezone.now)

    #class Meta:
        #ordering = ('-publish',)

    def __str__(self):
        return self.name
