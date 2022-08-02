from django.urls import path
from . import views

urlpatterns = [
    # Auth applications
    path('signup/', views.signupuser, name='signupuser'),
    path('login/', views.loginuser, name='loginuser'),
    path('logout/', views.logoutuser, name='logoutuser'),

    # Todos applications
    path('', views.home, name='home'),
    path('monuments/', views.monuments, name='monuments'),
]
