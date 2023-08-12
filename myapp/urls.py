from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('adidas/', views.adidas, name='adidas'),
    path('nike/', views.nike, name='nike'),
    path('jordan/', views.jordan, name='jordan'),
    path('puma/', views.puma, name='puma'),
    path('new_balance/', views.new_balance, name='new_balance'),
    path('vans/', views.vans, name='vans'),
    path('reebok/', views.reebok, name='reebok'),
    path('balenciaga/', views.balenciaga, name='balenciaga'),
    path('accouns/register/', views.register, name='register'), 
    path('accounts/login/', views.login, name='login'), 
    path('logout/', views.logout, name='logout'), 
    path('search/', views.search, name='search'), 
    path('product_detail/<int:product_id>/', views.product_detail, name='product_detail'),
    path('cart/', views.cart, name='cart'),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('update_cart/<int:id>/', views.update_cart, name='update_cart'),
    path('empty_cart', views.empty_cart, name='empty_cart'),
]
