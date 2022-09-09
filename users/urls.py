from django.urls import path
from .views import signinPage, signupPage, signoutPage

urlpatterns = [
    path('signup/', signupPage, name='signup'),
    path('login/', signinPage, name='login'),
    path('signout/', signoutPage, name='logout'),
]