"""
This module defines the data models (items) for the scraped book data.
It handles data cleaning, type conversion, and validation using dataclasses.
"""
from dataclasses import dataclass, field, asdict
from typing import Optional

# Business Logic: Mapping string ratings to integers
RATING_MAP = {
    'One': 1, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Zero': 0
}

@dataclass
class BookItem:
    """
    Dataclass to store and process book data scraped by the spider.
    The __post_init__ method automatically cleans and converts raw data.
    """
    # Raw data from the website
    title: str
    price_raw: str
    rating_raw: str
    url: str
    stock_raw: str

    # Processed data
    price: float = field(init=False)
    rating: int = field(init=False)
    in_stock: bool = field(init=False)

    def __post_init__(self):
        """Clean and convert raw data after object initialization."""
        try:
            clean_price = self.price_raw.replace('£', '').strip()
            self.price = float(clean_price)
        except (ValueError, AttributeError):
            self.price = 0.0

        self.rating = RATING_MAP.get(self.rating_raw, 0)
        self.in_stock = "In stock" in self.stock_raw

    def to_dict(self):
        """Converts the dataclass to a dictionary for database insertion."""
        data = asdict(self)
        del data['price_raw']
        del data['rating_raw']
        del data['stock_raw']
        return data
