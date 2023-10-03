from .dto import NewProductDTO, ProductDTO
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
