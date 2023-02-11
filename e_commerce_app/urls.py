from django.urls import path
from e_commerce_app import views

urlpatterns = [
    path('',views.index,name='index')
    
]