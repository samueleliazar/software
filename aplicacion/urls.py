from django.urls import path, include
from .views import index, about, contact, gallery, testimonial


urlpatterns = [
    path('', index, name='index'),
    path('about', about, name='about'),
    path('contact', contact, name='contact'),
    path('gallery', gallery, name='gallery'),
    path('testimonial', testimonial, name='testimonial'),
]