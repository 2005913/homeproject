from django.urls import path
from .import views

app_name = 'all'

urlpatterns=[
    path('', views.AllView.as_view(),name='all'),
]