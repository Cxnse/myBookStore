"""
This module handles the processing and storage of scraped items.
It filters specific items and saves them into a MongoDB database.
"""
import pymongo

class MongoPipeline:
    """
    Pipeline to save scraped items to MongoDB.
    Implements business logic to filter items before saving.
    """
    collection_name = 'scraped_books'

    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db
        self.client = None
        self.database = None

    @classmethod
    def from_crawler(cls, crawler):
        """Create a pipeline instance from the crawler settings."""
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGO_DATABASE', 'items')
        )

    def open_spider(self, spider):
        """Initialize the MongoDB connection when the spider opens."""
        # pylint: disable=unused-argument
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.database = self.client[self.mongo_db]

    def close_spider(self, spider):
        """Close the MongoDB connection when the spider closes."""
        # pylint: disable=unused-argument
        if self.client:
            self.client.close()

    def process_item(self, item, spider):
        """
        Process each item sent by the spider.
        Business Logic: Save only if rating is 5 and price is below 30.
        """
        # pylint: disable=unused-argument
        if item.rating == 5 and item.price < 30.0:
            data = item.to_dict()
            self.database[self.collection_name].insert_one(data)

        return item