from django.urls import path
from .views import *

urlpatterns = [
    path('', base, name='base'),
    # Add more paths as needed
]
