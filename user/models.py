from django.db import models
from datetime import date
from django.urls import reverse
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class UserType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, is_staff=False, is_admin=False, is_active=True):
        if not email:
            raise ValueError("User must have an email address")
        if not password:
            raise ValueError("Password required")
        user_obj = self.model(
            email=self.normalize_email(email)
        )
        user_obj.set_password(password)
        user_obj.staff = is_staff
        user_obj.active = is_active
        user_obj.admin = is_admin
        user_obj.save(using=self._db)
        return user_obj

    def create_staffuser(self, email, password=None):
        user = self.create_user(
            email,
            password=password,
            is_staff=True
        )
        return user

    def create_superuser(self, email, password=None):
        user = self.create_user(
            email,
            password=password,
            is_staff=True,
            is_admin=True
        )
        return user


class User(AbstractBaseUser):
    email = models.EmailField(max_length=255, unique=True)
    login = models.CharField(max_length=255, blank=True, null=True)
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False) #admin, but not superuser
    admin = models.BooleanField(default=False) #superuser

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin

    @property
    def is_active(self):
        return self.active
    """objects = UserManager()
    login = models.CharField(max_length=250)
    password = models.CharField(max_length=25)
    email = models.CharField(max_length=100)
    type_id = models.ForeignKey(UserType, on_delete=models.CASCADE, null=True)



    #USERNAME_FIELD = 'login'

    def __str__(self):
        return self.login + ' ' + self.email"""


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










