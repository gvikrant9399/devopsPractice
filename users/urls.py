from django.urls import path, include
from . import views

app_name = 'users'

urlpatterns = [
    path('', views.sign_up, name='sign_up'),
    # path('users/', include('users.urls')),
]