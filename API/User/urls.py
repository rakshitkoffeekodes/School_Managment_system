
from django.urls import path
from User import views
urlpatterns = [
    path('', views.home, name='home')
]
