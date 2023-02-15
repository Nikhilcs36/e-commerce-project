from django.urls import path
from e_commerce_auth import views

urlpatterns = [
    path('signup/',views.signup,name='signup')
    
]