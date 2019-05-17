from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('contacts/',views.contacts,name='contacts'),
    path('about/',views.about,name='about'),
]
