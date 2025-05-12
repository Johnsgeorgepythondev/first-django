from django.db import models
from django.contrib.auth.models import User


class Event(models.Model):
    objects = None
    name = models.CharField(max_length=150)
    description = models.TextField(null=True, blank=True)
    date = models.DateField()
    location = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Participant(models.Model):
    objects = None
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)


class Result(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    participant = models.ForeignKey(Participant, on_delete=models.CASCADE)
    score = models.IntegerField()
