from abc import ABCMeta, abstractmethod

from .dto import NewProductDTO, ProductDTO


class ProductRepositoryInterface(metaclass=ABCMeta):
    """
    Interface for product repository.

    This interface defines methods that must be implemented by any class
    acting as a repository for products data. By adhering to this interface,
    classes ensure consistent behavior for accessing product information
    regardless of their specific implementations.

    By using this interface, you can easily swap out different repository
    implementations without affecting other parts of the application that
    depend on products.
    """

    @abstractmethod
    def create_product(self, new_product_dto: NewProductDTO) -> ProductDTO:
        """
        Create a new product

        Args:
            new_product_dto (NewProductDTO): The data model object representing a product.

        Returns:
            ProductDTO - A data transfer object containing the product information.

        """
        pass
