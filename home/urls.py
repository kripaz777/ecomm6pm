from django.urls import path
from .views import *


app_name = "home" 

urlpatterns = [
     path('', HomeView.as_view(), name='home'),
     path('subcategory/<slug>', SubCategoryViews.as_view(), name='subcategory'),
     path('brand/<slug>', BrandViews.as_view(), name='brand'),
     path('product/<slug>', PrductDetailView.as_view(), name='product'),
     path('search', Search.as_view(), name='search'),
     path('signup', signup, name='signup'),
     path('add-to-cart', add_to_cart, name='add-to-cart'),
     path('cart', CartView.as_view(), name='cart'),
     path('remove-cart/<slug>', remove_cart, name='remove-cart'),
]