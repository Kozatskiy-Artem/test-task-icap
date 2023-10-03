from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from core.containers import ServiceContainer
from core.permissions import JWTPermissionValidator
from .dto import NewProductDTO
from .serializers import ProductCreateSerializer, ProductSerializer


class ApiProductListView(APIView):
    """
    The ApiPetListView class defines API endpoints for create product and
    working with a list containing information about products.
    """

    def post(self, request):
        """Handle POST request to create product."""

        JWTPermissionValidator.is_superuser_or_raise(request)

        product_serializer = ProductCreateSerializer(data=request.data)

        if not product_serializer.is_valid():
            return Response(product_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        product_service = ServiceContainer.product_service()

        new_product_dto = NewProductDTO(**product_serializer.validated_data)

        product_dto = product_service.create_product(new_product_dto)

        product = ProductSerializer(product_dto)

        return Response(
            data=product.data,
            status=status.HTTP_201_CREATED,
        )
