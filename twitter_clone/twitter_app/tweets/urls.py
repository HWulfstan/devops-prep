from django.urls import path
from . import views

urlpatterns = [
    path('', views.tweet_list, name='tweet_list'),
    path('add/', views.add_tweet, name='add_tweet'),
    path('edit/<int:tweet_id>/', views.edit_tweet, name='edit_tweet'),
    path('delete/<int:tweet_id>/', views.delete_tweet, name='delete_tweet'),
]
