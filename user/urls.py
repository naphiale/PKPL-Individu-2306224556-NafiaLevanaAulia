from django.urls import path
from user.views import user_form_view

app_name = 'user'

urlpatterns = [
    path('', user_form_view, name='user_form'),
]
