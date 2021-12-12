from dataclasses import dataclass
from City import City

@dataclass
class Customer:
    name: str
    city: City
    id: int = 1