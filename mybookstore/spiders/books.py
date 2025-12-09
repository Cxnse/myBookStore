"""
The main Scrapy Spider responsible for crawling the books.toscrape.com website.
"""
import scrapy
from mybookstore.items import BookItem

class BooksSpider(scrapy.Spider):
    """
    Spider class that traverses the book catalog, extracts data, and handles
    pagination across multiple pages.
    """
    name = "books"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["http://books.toscrape.com/catalogue/category/books_1/index.html"]

    def parse(self, response, **kwargs):
        """Processes the page source and extracts individual book items."""
        # Finds all book containers on the current page
        books = response.css('article.product_pod')

        for book in books:
            # Data extraction using CSS Selectors
            title = book.css('h3 a::attr(title)').get()
            price_text = book.css('p.price_color::text').get()
            url = book.css('h3 a::attr(href)').get()

            # Extracts the rating word (e.g., 'Three') from the CSS class
            rating_class = book.css('p.star-rating::attr(class)').get()
            rating_text = rating_class.split(' ')[-1] if rating_class else "Zero"

            # Extracts and strips the stock status text
            stock = book.css('p.instock.availability::text').getall()
            stock = "".join(stock).strip()

            # Creates the data item, which triggers the cleanup logic in items.py
            book_item = BookItem(
                title=title,
                price_raw=price_text,
                rating_raw=rating_text,
                url=response.urljoin(url),
                stock_raw=stock
            )

            yield book_item

        # Pagination logic: checks for the 'next' button and follows it
        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)