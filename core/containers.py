from dependency_injector import containers, providers

from products.repositories import ProductRepository
from products.services import ProductService


class RepositoryContainer(containers.DeclarativeContainer):
    """
    A container responsible for providing instances of various repository classes.
    Repositories are data access components used by services to retrieve data.
    """

    product_repository = providers.Factory(ProductRepository)


class ServiceContainer(containers.DeclarativeContainer):
    """
    A container responsible for providing instances of various service classes.
    Services are responsible for interaction with the data storage layer and business logic of the application.
    """

    product_service = providers.Factory(ProductService, product_repository=RepositoryContainer.product_repository)
