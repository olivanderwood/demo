from django.urls import path
from .import views

urlpatterns = [
    path('',views.index), 
    path('home/',views.index), 
    path('games/', views.games),
    path('learn/', views.learn),
    path('faqs/', views.faqs)
]
