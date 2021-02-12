from django.db import models
#from django.utils import timezone
#from django.contrib.auth.models import User


class Selection(models.Model):
    Preference = models.CharField(max_length=50)
    Budget_Dollar = models.IntegerField(max_length=6)
    Time_Frame_Hour = models.IntegerField(max_length=2)


    #publish = models.DateTimeField(default=timezone.now)

    #class Meta:
        #ordering = ('-publish',)

    def __str__(self):
        return self.Preference

