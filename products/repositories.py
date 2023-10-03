from dataclasses import fields as dc_fields

from annoying.functions import get_object_or_None
from django.db.models import QuerySet, Q

from core.exceptions import InstanceDoesNotExistError
from .dto import NewProductDTO, ProductDTO, PartialProductDTO, QueryParamsDTO
from .models import Product
from .interfaces import ProductRepositoryInterface


class ProductRepository(ProductRepositoryInterface):
    """The ProductRepository class handles the retrieval of product data from the data storage."""

    def create_product(self, new_product_dto: NewProductDTO) -> ProductDTO:
        """
        Create a new product

        Args:
            new_product_dto (NewProductDTO): The data model object representing a product.

        Returns:
            ProductDTO - A data transfer object containing the product information.

        """

        product = Product.objects.create(
            name=new_product_dto.name,
            photo=new_product_dto.photo,
            category=new_product_dto.category,
            offer_of_the_month=new_product_dto.offer_of_the_month,
            availability=new_product_dto.availability,
            self_pickup=new_product_dto.self_pickup,
            description1=new_product_dto.description1,
            description2=new_product_dto.description2,
            price=new_product_dto.price,
        )

        return self._product_to_dto(product)

    def get_product_by_id(self, product_id: int) -> ProductDTO:
        """
        Retrieve information about a product using its unique identifier.

        Args:
            product_id (int): The unique identifier of the product.

        Returns:
            ProductDTO - A data transfer object containing the product information.

        Raises:
            InstanceDoesNotExistError: If no product with this id is found.
        """

        product = get_object_or_None(Product, id=product_id)
        if product:
            return self._product_to_dto(product)
        raise InstanceDoesNotExistError(f"Product with id {product_id} not found")

    def partial_update_product(self, product_id: int, partial_product_dto: PartialProductDTO) -> ProductDTO:
        """
        Partial update product

        Args:
            product_id (int): The unique identifier of the product.
            partial_product_dto (PartialProductDTO): The data model object representing partial data of a product.

        Returns:
            ProductDTO - A data transfer object containing the product information.

        Raises:
            InstanceDoesNotExistError: If no product with this id is found.
        """

        product = get_object_or_None(Product, id=product_id)

        if not product:
            raise InstanceDoesNotExistError(f"Product with id {product_id} not found")

        update_fields = {
            field.name: getattr(partial_product_dto, field.name)
            for field in dc_fields(PartialProductDTO)
            if not getattr(partial_product_dto, field.name) is None
        }

        for key, value in update_fields.items():
            setattr(product, key, value)

        product.save()

        return self._product_to_dto(product)

    def delete_product_by_id(self, product_id: int) -> None:
        """
        Delete information about a product using its unique identifier.

        Args:
            product_id (int): The unique identifier of the product.

        Returns:
            None

        Raises:
            InstanceDoesNotExistError: If no product with this id is found.
        """
        product = get_object_or_None(Product, id=product_id)

        if not product:
            raise InstanceDoesNotExistError(f"Product with id {product_id} not found")

        product.delete()

    def get_products(self, query_params_dto: QueryParamsDTO) -> list[ProductDTO]:
        """
        Retrieve a list of products filtered by the provided parameters.

        Args:
            query_params_dto (QueryParamsDTO): A data transfer object containing filter parameters.

        Returns:
            list(ProductDTO) - A list of data transfer objects containing information about products.

        Raises:
            InstanceDoesNotExistError: If no products is found.
        """

        filter_conditions = Q()

        if query_params_dto.offer_of_the_month is not None:
            filter_conditions &= Q(offer_of_the_month=query_params_dto.offer_of_the_month)

        if query_params_dto.availability is not None:
            filter_conditions &= Q(availability=query_params_dto.availability)

        if query_params_dto.self_pickup is not None:
            filter_conditions &= Q(self_pickup=query_params_dto.self_pickup)

        products = Product.objects.filter(filter_conditions)

        if not products.exists():
            raise InstanceDoesNotExistError("Products not found")

        return self._products_to_dto(products)

    @staticmethod
    def _product_to_dto(product: Product) -> ProductDTO:
        """
        Convert a data model object (Product) into a ProductDTO object.

        Args:
            product (Product): An instance of the Product model class.

        Returns:
            ProductDTO - A data transfer object containing the product information.
        """

        return ProductDTO(
            id=product.pk,
            name=product.name,
            photo=product.photo,
            category=product.category,
            offer_of_the_month=product.offer_of_the_month,
            availability=product.availability,
            self_pickup=product.self_pickup,
            description1=product.description1,
            description2=product.description2,
            price=product.price,
        )

    @classmethod
    def _products_to_dto(cls, products: QuerySet[Product]) -> list[ProductDTO]:
        """
        Converts a QuerySet of Product objects to a list of ProductDTO objects.

        Args:
            products (QuerySet[Product]): A QuerySet of Product objects to be converted.

        Returns:
            list[ProductDTO]: A list of ProductDTO objects containing the converted data.
        """

        products_dto = [cls._product_to_dto(product) for product in products]

        return products_dto
