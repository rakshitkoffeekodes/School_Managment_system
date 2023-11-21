from django.urls import path
from . import views

# from .views import UserList
urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register),
    path('login/', views.login),
    path('logout/', views.logout),
    path('all_register/', views.all_register),
    path('profile/',views.profile)
]
