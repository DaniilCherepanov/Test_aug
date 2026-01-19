import pytest
import allure
import requests
from config import (
    BASE_URL,
    DEFAULT_HEADERS,
    DEFAULT_SEARCH_PARAMS,
    SEARCH_PHRASES,
    HTTP_STATUS_CODES
)


@allure.feature("API: Поиск книг")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Тест: поиск книги по названию на кириллице")
@allure.description("Проверяет поиск книги по кириллическому названию через API.")
def test_search_book_by_cyrillic_name(api_client, search_params):
    params = search_params.copy()
    params["phrase"] = SEARCH_PHRASES["cyrillic"]

    with allure.step(f"Отправка запроса с фразой: {params['phrase']}"):
        response = api_client.get(
            f"{BASE_URL}/popular-search-phrases",
            params=params,
            timeout=10
        )

    with allure.step("Проверка статуса ответа 200 (OK)"):
        assert response.status_code == HTTP_STATUS_CODES["OK"], \
            f"Ошибка при поиске: {response.text}"

    with allure.step("Проверка наличия поля 'data' в ответе"):
        data = response.json()
        assert "data" in data, "В ответе отсутствует ключ 'data'"


@allure.feature("API: Поиск книг")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Тест: поиск по названию на латинице")
@allure.description("Проверяет поиск книги по латинскому названию через API.")
def test_search_book_by_latin_name(api_client, search_params):
    params = search_params.copy()
    params["phrase"] = SEARCH_PHRASES["latin"]

    with allure.step(f"Отправка запроса с фразой: {params['phrase']}"):
        response = api_client.get(
            f"{BASE_URL}/popular-search-phrases",
            params=params,
            timeout=10
        )

    with allure.step("Проверка статуса ответа 200 (OK)"):
        assert response.status_code == HTTP_STATUS_CODES["OK"], \
            f"Ошибка при поиске: {response.text}"

    with allure.step("Проверка наличия поля 'data' в ответе"):
        data = response.json()
        assert "data" in data, "В ответе отсутствует ключ 'data'"


@allure.feature("API: Поиск книг")
@allure.severity(allure.severity_level.NORMAL)
@allure.title("Тест: поиск без токена")
@allure.description("Проверяет, что публичный эндпоинт доступен без авторизации.")
def test_unauthorized_request(api_client, search_params):
    headers = {"Content-Type": "application/json"}
    params = search_params.copy()
    params["phrase"] = SEARCH_PHRASES["digits"]

    with allure.step("Отправка запроса без токена"):
        response = api_client.get(
            f"{BASE_URL}/popular-search-phrases",
            params=params,
            headers=headers,
            timeout=10
        )

    with allure.step("Проверка статуса 200 (OK)"):
        assert response.status_code == HTTP_STATUS_CODES["OK"], \
            f"Ожидался код 200, получен: {response.status_code}"

    with allure.step("Проверка наличия данных"):
        data = response.json()
        assert "data" in data, "В ответе отсутствует поле 'data'"


@allure.feature("API: Поиск книг")
@allure.severity(allure.severity_level.NORMAL)
@allure.title("Тест: поиск с пустой фразой")
@allure.description("Проверяет, что API корректно обрабатывает пустой поисковый запрос.")
def test_empty_search_phrase(api_client, search_params):
    params = search_params.copy()
    params["phrase"] = ""

    with allure.step("Отправка запроса с пустой фразой"):
        response = api_client.get(
            f"{BASE_URL}/popular-search-phrases",
            params=params,
            timeout=10
        )

    with allure.step("Проверка статуса ответа 200 (OK)"):
        assert response.status_code == HTTP_STATUS_CODES["OK"], \
            f"Ошибка при пустом поиске: {response.text}"

    with allure.step("Проверка наличия поля 'data' в ответе"):
        data = response.json()
        assert "data" in data, "В ответе отсутствует ключ 'data'"


@allure.feature("API: HTTP-методы")
@allure.severity(allure.severity_level.BLOCKER)
@allure.title("Тест: отправка POST вместо GET")
@allure.description("Проверяет, что API отвергает POST-запросы к эндпоинту поиска.")
def test_invalid_method(api_client, search_params):
    params = search_params.copy()
    params["phrase"] = SEARCH_PHRASES["cyrillic"]

    with allure.step("Отправка POST-запроса вместо GET"):
        response = api_client.post(
            f"{BASE_URL}/popular-search-phrases",
            params=params,
            timeout=10
        )

    with allure.step("Проверка статуса ответа 405 (Method Not Allowed)"):
        assert response.status_code == HTTP_STATUS_CODES["METHOD_NOT_ALLOWED"], \
            f"Ожидался код 405, получен: {response.status_code}"
