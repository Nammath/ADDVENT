from django.views import generic
from django.views.generic import CreateView, View
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from .forms import UserCreate, LoginForm
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


class EventCreate(CreateView):
    model = Event
    fields = ['name', 'description', 'event_date', 'seats', 'image', 'venue_id', 'owner_id', 'category_id']


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



