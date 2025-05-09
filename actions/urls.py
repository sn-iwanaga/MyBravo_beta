from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.action_list, name='action_list'),
    path('create/', views.action_create, name='action_create'),
    path('update/<int:pk>/', views.action_update, name='action_update'),
    path('delete/<int:pk>/', views.action_delete, name='action_delete'),
]