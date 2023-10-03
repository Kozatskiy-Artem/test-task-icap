from django.urls import path

from .views import ApiProductListView, ApiProductDetailView

urlpatterns = [
    path("", ApiProductListView.as_view(), name="api-product-list"),
    path("<int:id>/", ApiProductDetailView.as_view(), name="api-product-detail"),
]
