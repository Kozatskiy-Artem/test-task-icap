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
