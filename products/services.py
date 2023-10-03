from .dto import NewProductDTO, ProductDTO
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