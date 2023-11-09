from django.urls import path
from faculty import views
urlpatterns = [
    path('', views.home, name='home')
]
