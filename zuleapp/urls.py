from django.urls import path
from .import views
urlpatterns =[
    path ('', views.home, name="home"),
    path ('aboutus/', views.about_us, name="about_us"),
    path ('contactus/', views.contact_us, name="contact_us")
]