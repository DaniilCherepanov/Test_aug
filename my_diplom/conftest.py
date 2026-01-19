import pytest
from selenium import webdriver
import requests
from config import BASE_URL, DEFAULT_HEADERS


@pytest.fixture(scope="function")
def driver():
    """Фикстура для инициализации браузера.

    Returns:
        webdriver.Chrome: экземпляр драйвера Chrome.
    """
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture
def browser(driver):
    """Фикстура для передачи драйвера в тесты.

    Args:
        driver (webdriver.Chrome): экземпляр драйвера.

    Returns:
        webdriver.Chrome: тот же драйвер.
    """
    return driver

@pytest.fixture
def book_url():
    """Фикстура с URL книги для тестов.

    Returns:
        str: URL страницы книги.
    """
    return "https://www.chitai-gorod.ru/product/1984-skotnyy-dvor-2909119"

@pytest.fixture
def api_client():
    """Фикстура для создания HTTP-клиента API.

    Returns:
        requests.Session: сессия для запросов к API.
    """
    session = requests.Session()
    session.headers.update(DEFAULT_HEADERS)
    return session

@pytest.fixture
def search_params():
    """Фикстура с параметрами поиска по умолчанию.

    Returns:
        dict: параметры поиска (customerCityId, per-page и др.).
    """
    from config import DEFAULT_SEARCH_PARAMS
    return DEFAULT_SEARCH_PARAMS.copy()
