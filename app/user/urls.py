""" Url mappings for the user api """
from django.urls import path

from user import views

app_name = 'user'

urlpatterns = [
    path('signup/', views.CreateUserView.as_view(), name='create'),
    path('token/', views.CreateTokenView.as_view(), name='token'),
    path('login/', views.LoginUserView.as_view(), name='login'),
    path('me/', views.ManageUserView.as_view(), name='me'),
]
