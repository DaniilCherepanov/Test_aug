from decouple import config


BASE_URL = config("BASE_URL")
API_TOKEN = config("API_TOKEN")

DEFAULT_HEADERS = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {API_TOKEN}"
}

DEFAULT_SEARCH_PARAMS = {
    "customerCityId": 2,
    "products[page]": 1,
    "products[per-page]": 60
}

SEARCH_PHRASES = {
    "cyrillic": "Триумфальная арка",
    "latin": "coraline",
    "digits": "1984"
}

HTTP_STATUS_CODES = {
    "OK": 200,
    "METHOD_NOT_ALLOWED": 405,
    "UNAUTHORIZED": 401
}
