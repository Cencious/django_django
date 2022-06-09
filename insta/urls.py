from urllib.parse import urlparse
from django.urls import URLPattern, path
from . import views

urlpatterns =[
    path('', views.home, name='insta-home'),
    path('about/', views.about, name='insta-about')
]
