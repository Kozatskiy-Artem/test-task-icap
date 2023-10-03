from dataclasses import dataclass


@dataclass(frozen=True)
class NewProductDTO:
    name: str
    photo: str
    category: str
    offer_of_the_month: bool
    availability: bool
    self_pickup: bool
    description1: str
    description2: str
    price: float


@dataclass(frozen=True)
class ProductDTO:
    id: int
    name: str
    photo: str
    category: str
    offer_of_the_month: bool
    availability: bool
    self_pickup: bool
    description1: str
    description2: str
    price: float
