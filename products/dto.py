from dataclasses import dataclass
from typing import Optional


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


@dataclass(frozen=True)
class PartialProductDTO:
    name: Optional[str] = None
    photo: Optional[str] = None
    category: Optional[str] = None
    offer_of_the_month: Optional[bool] = None
    availability: Optional[bool] = None
    self_pickup: Optional[bool] = None
    description1: Optional[str] = None
    description2: Optional[str] = None
    price: Optional[float] = None
