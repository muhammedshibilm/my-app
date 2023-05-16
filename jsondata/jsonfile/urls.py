
from django.urls import path,include

from . import views


urlpatterns = [
    path('', views.index),
    path('json/',views.json, name='json'),
    path('api/quotes/', views.quote_list, name="quotelist"),
    
]
