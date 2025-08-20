from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout_view/', views.logout_view, name='logout_view'),
    path('headphones/', views.headphones_view, name='headphones'),
    path('watch/', views.watch, name='watch'),
    path('backpack/', views.backpack, name='backpack'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
    path('cart/<int:pk>/', views.cart, name='cart'),
    path('cart/', views.cart, name='cart'),
    path('cart/delete/<int:pk>/', views.delete_cart, name='delete_cart'),
]
