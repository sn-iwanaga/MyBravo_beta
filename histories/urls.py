from django.urls import path
from . import views

urlpatterns = [
    path('record_action/<int:action_pk>/', views.record_action, name='record_action'),
    path('exchange_reward/<int:reward_pk>/', views.exchange_reward, name='exchange_reward'),
]