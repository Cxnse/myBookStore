# 📚 Smart Inventory Manager (MyBookStore)

![Python](https://img.shields.io/badge/Python-3.14-blue?style=flat&logo=python)
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

## ⚙️ Installation & Setup

Follow these steps to get the project running on your local machine.

### 1. Clone the Repository
```bash
git clone [https://github.com/Cxnse/mybookstore.git](https://github.com/Cxnse/mybookstore.git)
cd mybookstore