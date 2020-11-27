from django.urls import path
from .views import (
    ProductList,
    ProductCreate,
    ProductDetail,
    ProductUpdate,
    ProductDelete,
)

app_name = "store"
urlpatterns = [
    # Product CRUD-related URLs
    path("products/", ProductList.as_view(), name="product_list"),
    path("products/new/", ProductCreate.as_view(), name="product_create"),
    path("products/<slug:slug>/edit/", ProductUpdate.as_view(), name="product_update"),
    path(
        "products/<slug:slug>/delete/", ProductDelete.as_view(), name="product_delete"
    ),
    path("products/<slug:slug>/", ProductDetail.as_view(), name="product_detail"),
]
