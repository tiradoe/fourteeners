from django.db import models
from django.contrib.auth.models import User

class Mountain(models.Model):
    name = models.CharField(max_length=255)
    elevation = models.PositiveIntegerField(default=0)
    difficulty = models.CharField(max_length=20)
    lat = models.DecimalField(max_digits=7, decimal_places=4)
    long = models.DecimalField(max_digits=7, decimal_places=4)

    def calculateClimbs(self, user_id):
        return Climb.objects.filter(mountain=self, climber_id=user_id).count()

    climbs = property(calculateClimbs)

    def __str__(self):
        return self.name

class Climb(models.Model):
    climber = models.ForeignKey(User, default=None)
    mountain = models.CharField(max_length=255)
    start_date = models.DateField()
    start_time = models.TimeField()
    summit_date = models.DateField()
    summit_time = models.TimeField()
    finish_date = models.DateField()
    finish_time = models.TimeField()
    total_distance = models.PositiveIntegerField()
    notes = models.TextField()

    def __str__(self):
        return self.mountain


class Weather(models.Model):
    mountain = models.ForeignKey(Mountain, default=None)
    day = models.IntegerField(default=0)
    county = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    image = models.CharField(max_length=255)
    speed = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    temp = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    cloud = models.IntegerField(default=0)
    humidity = models.IntegerField(default=0)
