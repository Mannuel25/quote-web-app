from django.urls import path
from .views import signinPage, signupPage, signoutPage

urlpatterns = [
    path('signup/', signupPage, name='signup'),
    path('signin/', signinPage, name='login'),
    path('signout/', signoutUser, name='logout'),
]