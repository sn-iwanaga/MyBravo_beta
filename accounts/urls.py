from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('mypage/', views.mypage, name='mypage'),
    path('signout/', views.signout, name='signout'),
]