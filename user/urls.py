
from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<pk>', views.DetailView.as_view(), name='detail'),
    path('event/add/', views.EventCreate.as_view(), name='event-add'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name="login")

]