from django.urls import path

from .views import ApiProductListView

urlpatterns = [
    path("", ApiProductListView.as_view(), name="api-product-list"),
]
