from django.db import models
from datetime import date
from django.urls import reverse
from django.contrib.auth.models import AbstractBaseUser


class User(AbstractBaseUser):
    login = models.CharField(max_length=25)
    password = models.CharField(max_length=25)
    email = models.CharField(max_length=100)
    type = models.CharField(max_length=100)

    USERNAME_FIELD = 'login'

    def __str__(self):
        return self.login + ' ' + self.email


class Venue(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Event(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    event_date = models.DateField(default=date.today)
    seats = models.IntegerField()
    image = models.CharField(max_length=500)
    venue_id = models.ForeignKey(Venue, on_delete=models.CASCADE, null=True)
    owner_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    is_favorite = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('user:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name


class WatchedEvent(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    event_id = models.ForeignKey(Event, on_delete=models.CASCADE, null=True)


class Tag(models.Model):
    event_id = models.ForeignKey(Event, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name










