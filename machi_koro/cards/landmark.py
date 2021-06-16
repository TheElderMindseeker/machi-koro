from dataclasses import dataclass


@dataclass
class Landmark:
    name: str
    price: int
    built: bool = False
