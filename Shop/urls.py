from django.urls import path
from . import views

urlpatterns = [
    path('base', views.base, name="ShopHome"),
    path('index/', views.index, name="ShopHome"),
    path('about/', views.about, name="AboutUs"),
    path('contact/', views.contact, name="ContactUs"),
    path('tracker/', views.tracker, name="Tracker"),
    path('search/', views.search, name="Search"),
    path('productview/<int:myid>', views.productview, name="ProductView"),
    path('checkout/', views.checkout, name="Checkout"),
]





