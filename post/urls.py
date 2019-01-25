from django.urls import path
from .views import post_render

urlpatterns = [
    path('<int:id>/', post_render, name='post'),
]