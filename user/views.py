from django.views import generic
from django.views.generic import CreateView, View
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from .forms import UserCreate, LoginForm, EventCreate
from .models import User, Event


class IndexView(generic.ListView):
    template_name = 'user/index.html'
    context_object_name = 'all_events'

    def get_queryset(self):
        return Event.objects.all()


class DetailView(generic.DetailView):
    model = Event
    context_object_name = 'event'
    template_name = 'user/detail.html'


def event_create(request):
    form = EventCreate(request.POST or None)
    context = {'form': form}
    if form.is_valid():
        event = form.save(commit=False)
        event.name = form.cleaned_data.get('name')
        event.description = form.cleaned_data.get('description')
        event.event_date = form.cleaned_data.get('event_date')
        event.image = form.cleaned_data.get('image')
        event.venue_id = form.cleaned_data.get('venue_id')
        event.category_id = form.cleaned_data.get('category_id')
        event.owner_id = request.user
        form.save()
    else:
        form = EventCreate()
    return render(request, 'user/event_form.html', context)


def login_view(request):
    form = LoginForm(request.POST or None)
    context = {"form": form}
    if form.is_valid():
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
    return render(request, 'user/register_form.html', context)


def register_view(request):
    if request.method == 'POST':
        form = UserCreate(request.POST)
        if form.is_valid():
            user = form.save(commit=False)

            login_name = form.cleaned_data.get('login')
            password = form.cleaned_data.get('password')
            email = form.cleaned_data.get('email')
            user.set_password(password)
            user.login = login_name
            form.save()
            #user = authenticate(email=email, password=password)
            #login(request, user, backend='django.contrib.auth.backends.ModelBackend')

    else:
        form = UserCreate()

    return render(request, 'user/register_form.html', {'form': form})



