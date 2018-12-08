from django.contrib import admin

# Register your models here.
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

#from .forms import CustomUserCreationForm, CustomUserChangeForm

from django.contrib.auth import get_user_model

from .models import User, Event, WatchedEvent, Venue, Category, Tag, UserType

User = get_user_model()

admin.site.register(User)
admin.site.register(Event)
admin.site.register(WatchedEvent)
admin.site.register(Tag)
admin.site.register(Venue)
admin.site.register(Category)
admin.site.register(UserType)


"""class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = ['email', 'username']"""





