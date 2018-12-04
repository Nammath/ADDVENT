from django.contrib import admin

# Register your models here.

from .models import User, Event, WatchedEvent, Venue, Category, Tag

admin.site.register(User)
admin.site.register(Event)
admin.site.register(WatchedEvent)
admin.site.register(Tag)
admin.site.register(Venue)
admin.site.register(Category)
