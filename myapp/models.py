from django.db import models
from django.utils import timezone
# from django.contrib.auth.models import User
# id | name | date_of_booking | in_time | out_time | occupancy

class BookingList(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=50)
    date_of_booking = models.DateTimeField(default=timezone.now)
    in_time= models.DateTimeField(blank=True, null=True)
    out_time= models.DateTimeField(blank=True, null=True)
    occupancy =models.IntegerField()
    # user1= models.ForeignKey(User,on_delete=models.CASCADE)
    dues = models.IntegerField(default=0)
    advance = models.IntegerField(default=0)