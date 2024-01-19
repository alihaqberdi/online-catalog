from django.urls import path

from product import views

app_name = "product"

urlpatterns = [
    path("category/", views.category_main, name="category"),
    path("category-detail/<slug:slug>/", views.category_detail, name="category_detail"),
    path("product-list/<slug:slug>/", views.product_list, name="product_list"),
]
