from django.urls import path
from . import views
from .views import *

app_name='blog'

urlpatterns = [
    path('',PostListView.as_view(),name='post_list'),
    path('post/<int:pk>/',views.post_detail,name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit,name='post_edit'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),

]