from django.urls import path
from app import views

urlpatterns = [
    path('', views.home, name="home"),
    path('catalog/', views.catalog, name='catalog'),
    path('signin/', views.signin, name="signin"),
    path('signup/', views.signup, name="signup"),
    path('contact/', views.contact, name="contact"),
    path('about/', views.about, name="about")
]
