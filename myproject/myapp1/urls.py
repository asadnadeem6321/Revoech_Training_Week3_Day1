from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), 
    path('second/', views.secondfiler, name='secondfile'),
    path('about/', views.about, name='About'),
    path('base/', views.base, name='Base'),
    path('contact/', views.contact, name='Contact'),
    path('saveenquiry/', views.save_enquiry, name='SaveEnquiry')
]