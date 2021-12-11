from dataclasses import dataclass
from City import City

@dataclass
class Customer:
    id: int
    name: str
    city: City