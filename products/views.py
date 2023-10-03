from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_spectacular.utils import OpenApiParameter, extend_schema
from drf_spectacular.types import OpenApiTypes

from core.containers import ServiceContainer
from core.permissions import JWTPermissionValidator
from core.exceptions import InstanceDoesNotExistError
from core.responses import ResponseWithErrorSerializer, ValidationErrorResponseSerializer, AccessDeniedDetailSerializer
from .dto import NewProductDTO, PartialProductDTO, QueryParamsDTO
from .serializers import ProductCreateSerializer, ProductSerializer, PartialProductSerializer


class ApiProductListView(APIView):
    """
    The ApiPetListView class defines API endpoints for create product and
    working with a list containing information about products.
    """

    @extend_schema(
        summary="Create a new product",
        request=ProductCreateSerializer,
        responses={
            200: ProductSerializer,
            401: AccessDeniedDetailSerializer,
            403: AccessDeniedDetailSerializer,
        },
        tags=["Products"],
    )
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

    @extend_schema(
        summary="Retrieve information about all products by query params",
        responses={
            200: ProductSerializer(many=True),
            404: ResponseWithErrorSerializer,
        },
        parameters=[
            OpenApiParameter(
                name="is_offer_of_the_month",
                type=OpenApiTypes.BOOL,
                location=OpenApiParameter.QUERY,
                description="Filter products by 'offer of the month' status (True/False).",
            ),
            OpenApiParameter(
                name="is_available",
                type=OpenApiTypes.BOOL,
                location=OpenApiParameter.QUERY,
                description="Filter products by availability status (True/False).",
            ),
            OpenApiParameter(
                name="is_self_pickup",
                type=OpenApiTypes.BOOL,
                location=OpenApiParameter.QUERY,
                description="Filter products by 'self pickup' status (True/False).",
            ),
        ],
        tags=["Products"],
    )
    def get(self, request):
        """Handle GET request to retrieve all products data."""

        query_params_dto = QueryParamsDTO(
            offer_of_the_month=request.query_params.get('is_offer_of_the_month', None),
            availability=request.query_params.get('is_available', None),
            self_pickup=request.query_params.get('is_self_pickup', None)
        )

        product_service = ServiceContainer.product_service()

        try:
            products_dto = product_service.get_products(query_params_dto)
        except InstanceDoesNotExistError as exception:
            return Response({"error": str(exception.message)}, status=status.HTTP_404_NOT_FOUND)

        products = ProductSerializer(products_dto, many=True)

        return Response(
            data=products.data,
            status=status.HTTP_200_OK,
        )


class ApiProductDetailView(APIView):
    """The ApiProductDetailView class defines API endpoints for working with pet information."""

    @extend_schema(
        summary="Retrieve product data by product id",
        responses={
            200: ProductSerializer,
            404: ResponseWithErrorSerializer,
        },
        tags=["Products"],
    )
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

    @extend_schema(
        summary="Delete product data by product id",
        responses={
            204: None,
            404: ResponseWithErrorSerializer,
        },
        tags=["Products"],
    )
    def delete(self, request, id):
        """Handle DELETE request to remove product data."""

        JWTPermissionValidator.is_superuser_or_raise(request)

        product_service = ServiceContainer.product_service()

        try:
            product_service.delete_product(id)
        except InstanceDoesNotExistError as exception:
            return Response({"error": str(exception.message)}, status=status.HTTP_404_NOT_FOUND)

        return Response(
            status=status.HTTP_204_NO_CONTENT,
        )

    @extend_schema(
        summary="Partial update product  data",
        request=PartialProductSerializer,
        responses={
            200: ProductSerializer,
            400: ValidationErrorResponseSerializer,
            401: AccessDeniedDetailSerializer,
            403: AccessDeniedDetailSerializer,
            404: ResponseWithErrorSerializer,
        },
        tags=["Products"],
    )
    def patch(self, request, id):
        """Handle PATCH request to partial update product data."""

        JWTPermissionValidator.is_superuser_or_raise(request)

        product_serializer = PartialProductSerializer(data=request.data)

        if not product_serializer.is_valid():
            return Response(product_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        product_service = ServiceContainer.product_service()

        partial_product_dto = PartialProductDTO(**product_serializer.validated_data)

        try:
            product_dto = product_service.partial_update_product(id, partial_product_dto)
        except InstanceDoesNotExistError as exception:
            return Response({"error": str(exception.message)}, status=status.HTTP_404_NOT_FOUND)

        product = ProductSerializer(product_dto)

        return Response(
            data=product.data,
            status=status.HTTP_200_OK,
        )
