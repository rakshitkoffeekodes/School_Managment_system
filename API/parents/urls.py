from django.urls import path
from parents import views
urlpatterns = [
    path('', views.home, name='home')
]
