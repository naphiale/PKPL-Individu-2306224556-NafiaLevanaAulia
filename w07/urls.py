from django.urls import path
from w07.views import login_view, home_view, logout_view, register_view

urlpatterns = [
    path('login', login_view, name='login'),
    path('', home_view, name='home'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register'),
]
