import os
from dotenv import load_dotenv


load_dotenv()

BASE_URL = os.getenv("BASE_URL")

DEFAULT_HEADERS = {
    "Authorization": f"Bearer {os.getenv('API_TOKEN')}",
    "Content-Type": "application/json",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
}

DEFAULT_SEARCH_PARAMS = {
    "customerCityId": os.getenv("CUSTOMER_CITY_ID"),
    "products[per-page]": os.getenv("DEFAULT_PER_PAGE")
}

SEARCH_PHRASES = {
    "cyrillic": "Война и мир",
    "latin": "War and Peace",
    "digits": "9785171234567"
}

HTTP_STATUS_CODES = {
    "OK": 200,
    "UNAUTHORIZED": 401,
    "METHOD_NOT_ALLOWED": 405,
    "NOT_FOUND": 404
}
