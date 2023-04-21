from django.urls import path
from .views import *

urlpatterns = [
    path('', homepage, name='home'),
    path('view/<pk>', linkView, name='linkview'),
    path('more/<pk>', viewPage, name='viewPage'),
    path('edit/<pk>', edit, name='edit'),
    path('delete/<pk>', delete, name='delete'),
    path('dashboard/<pk>', adminView, name='adminView'),
    path('login', loginUser, name='loginUser'),
    path('logout', logoutUser, name='logoutUser'),
    path('post/', CreatePost, name='CreatePost'),
]
