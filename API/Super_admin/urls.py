from django.urls import path
from . import views
# from .views import UserList
urlpatterns = [
    path('', views.home, name='home'),
    # path('reg',UserList.as_view(), name='reg')
    ]
