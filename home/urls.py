from django.urls import path
from .views import index_render, about_render, contact_render

urlpatterns = [
    path('', index_render, name='index'),
    path('about/', about_render, name='about'),
    path('contact/', contact_render, name='contact'),
]