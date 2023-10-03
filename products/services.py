from .dto import NewProductDTO, ProductDTO, PartialProductDTO, QueryParamsDTO
from .interfaces import ProductRepositoryInterface


class ProductService:
    """
    The PetService class is responsible for interacting with the data storage layer,
    specifically the PetRepository, to retrieve pet information.
    """

    def __init__(self, product_repository: ProductRepositoryInterface):
        self.product_repository = product_repository

    def create_product(self, new_product_dto: NewProductDTO) -> ProductDTO:
        """
        Create a new product

        Args:
           new_product_dto (NewProductDTO): The data model object representing a product.

        Returns:
           ProductDTO - A data transfer object containing the product information.

        """

        return self.product_repository.create_product(new_product_dto)

    def get_product(self, product_id: int) -> ProductDTO:
        """
        Retrieve information about a product using its unique identifier.

        Args:
            product_id (int): The unique identifier of the product.

        Returns:
            ProductDTO: A data transfer object containing the product information.

        Raises:
            InstanceDoesNotExistError: If no product with this id is found.
        """

        return self.product_repository.get_product_by_id(product_id)

    def partial_update_product(self, product_id: int, partial_product_dto: PartialProductDTO) -> ProductDTO:
        """
        Partial update product

        Args:
            product_id (int): The unique identifier of the product.
            partial_product_dto (PartialProductDTO): The data model object representing partial data of a product.

        Returns:
            ProductDTO: A data transfer object containing the product information.

        Raises:
            InstanceDoesNotExistError: If no product with this id is found.
        """

        return self.product_repository.partial_update_product(product_id, partial_product_dto)

    def delete_product(self, product_id) -> None:
        """
        Delete information about a product using its unique identifier.

        Args:
            product_id (int): The unique identifier of the product.

        Returns:
            None

        Raises:
            InstanceDoesNotExistError: If no product with this id is found.
        """

        self.product_repository.delete_product_by_id(product_id)

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

        return self.product_repository.get_products(query_params_dto)
