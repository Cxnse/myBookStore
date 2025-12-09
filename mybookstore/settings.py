# --- ZORUNLU SCRAPY AYARLARI (Bunlar olmazsa "Spider not found" hatası alırsın) ---
BOT_NAME = "mybookstore"

SPIDER_MODULES = ["mybookstore.spiders"]
NEWSPIDER_MODULE = "mybookstore.spiders"

# --- BİZİM EKLEDİĞİMİZ AYARLAR ---

# 1. Pipeline Aktifleştirme (MongoDB Kaydı İçin)
ITEM_PIPELINES = {
   'mybookstore.pipelines.MongoPipeline': 300,
}

# 2. MongoDB Bağlantı Bilgileri
MONGO_URI = 'mongodb://localhost:27017'
MONGO_DATABASE = 'MyBookStoreDB'

# 3. Kibar Bot Kuralları
ROBOTSTXT_OBEY = True
DOWNLOAD_DELAY = 1  # 1 saniye bekleme süresi
