from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from core.containers import ServiceContainer
from core.permissions import JWTPermissionValidator
from core.exceptions import InstanceDoesNotExistError
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


class ApiProductDetailView(APIView):
    """The ApiProductDetailView class defines API endpoints for working with pet information."""

    def get(self, request, id):
        """Handle GET request to retrieve product data."""

        product_service = ServiceContainer.product_service()

        try:
            product_dto = product_service.get_product(id)
        except InstanceDoesNotExistError as exception:
            return Response({"error": str(exception.message)}, status=status.HTTP_404_NOT_FOUND)

        product = ProductSerializer(product_dto)

        return Response(
            data=product.data,
            status=status.HTTP_200_OK,
        )
