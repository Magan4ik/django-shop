from django.urls import path, include
from shop import views

app_name = 'shop'

urlpatterns = [
    path('', views.ShopPage.as_view(), name='main'),
    path('shop/', views.CategoriesPage.as_view(), name='categories'),
    path('shop/<str:category_slug>/', views.ProductsPage.as_view(), name='products'),
    path('shop/detail/<str:product_slug>/', views.DetailPage.as_view(), name='detail'),
]
