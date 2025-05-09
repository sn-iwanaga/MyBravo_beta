from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.reward_list, name='reward_list'),
    path('create/', views.reward_create, name='reward_create'),
    path('update/<int:pk>/', views.reward_update, name='reward_update'),
    path('delete/<int:pk>/', views.reward_delete, name='reward_delete'),
]