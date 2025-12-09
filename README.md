# 📚 Smart Inventory Manager (MyBookStore)

![Python](https://img.shields.io/badge/Python-3.12-blue?style=flat&logo=python)
![Scrapy](https://img.shields.io/badge/Scrapy-2.11-green?style=flat&logo=scrapy)
![MongoDB](https://img.shields.io/badge/MongoDB-NoSQL-green?style=flat&logo=mongodb)
![Docker](https://img.shields.io/badge/Docker-Container-blue?style=flat&logo=docker)

## 📖 Project Overview

**Smart Inventory Manager** is a robust web scraping solution designed to extract, transform, and load (ETL) book data from [books.toscrape.com](http://books.toscrape.com).

This project demonstrates strong **OOP** principles using Python `Dataclasses` for strict type checking and data validation. It implements a critical **Business Logic** filter that saves **only "high-value"** items into a **MongoDB** database.

## 🚀 Key Features

* **Advanced Scraping:** Uses **Scrapy** for fast, asynchronous data retrieval.
* **Data Validation (OOP):** Utilizes Python **Dataclasses** to clean raw strings (e.g., converting `"£51.77"` to `51.77` float) and ensure type safety.
* **NoSQL Integration:** Persistent storage using **MongoDB**.
* **Business Logic Filtering:** The pipeline automatically filters and saves **only** books that meet specific criteria:
    * Rating: **5 Stars** ⭐⭐⭐⭐⭐
    * Price: **< £30** 💸

## 📂 Project Structure

* `spiders/book.py`: Main spider logic (crawling & parsing).
* `items.py`: Data models & cleaning logic (Dataclasses).
* `pipelines.py`: Filtering logic & MongoDB insertion.
* `settings.py`: Configuration (DB connection, user-agents).

## ⚙️ Installation & Setup

Follow these steps to get the project running on your local machine.

### 1. Clone the Repository
```bash
git clone [https://github.com/Cxnse/myBookStore.git](https://github.com/Cxnse/myBookStore.git)
cd myBookStore

# Create virtual environment
python -m venv venv

# Activate it
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt


docker-compose up -d


scrapy crawl books


# 1. Connect to the running MongoDB container
docker exec -it mongodb_container_name mongosh

# 2. Switch to the database (Defined in settings.py)
use MyBookStoreDB

# 3. Query the collection (Defined in pipelines.py)
db.scraped_books.find().pretty()

# 4. Check count (Should be low due to strict filtering)
db.scraped_books.countDocuments()
