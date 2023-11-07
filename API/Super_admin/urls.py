from django.urls import path
from Super_admin import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/<str:fname>/<str:lname>/<str:email>/<str:password>', views.register),
    path('login/<str:first>/<str:second>', views.login),
    path('profile/<int:pk>/<str:pname>/<str:padd>/<str:pgender>/<str:pmnumber>/<str:pdob>/<str:pstatus>',views.profile)
]
