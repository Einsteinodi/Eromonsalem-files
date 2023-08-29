from django.urls import path
from Eron_app import views

app_name= 'Eron_app'



urlpatterns = [
    path('about/',views.about, name='about'),
    path('blog/',views.blog, name='blog'),
    path('contact/',views.contact, name='contact'),
    path('FQA/',views.FQa, name='FQA'),
    path('policy/',views.Policy, name='policy'),
    path('privacy/', views.Privacy, name='privacy'),
    path('service/', views.Service, name='service'),
    path('servicedeal/',views.Servicedeal, name='servicedeal'),
]