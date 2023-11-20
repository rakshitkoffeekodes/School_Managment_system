from django.urls import path
from . import views

# from .views import UserList
urlpatterns = [
    path('', views.home, name='home'),
    path('Register/<str:fn>/<str:ln>/<str:em>/<str:ps>', views.Register),
    path('Login/<str:em>/<str:ps>', views.Login),
    path('all_register/', views.all_register),
]
