import pytest
import allure
from selenium import webdriver
from pages.main_page import MainPage
from pages.results_page import ResultsPage
from pages.book_page import BookPage
from pages.cart_page import CartPage


@allure.feature("Поиск книг")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Тест: поиск книги по названию")
@allure.description("Проверяет, что поиск книги по ключевому слову возвращает результаты.")
def test_search_books(browser):
    with allure.step("Открытие главной страницы"):
        main_page = MainPage(browser)
        main_page.open()

    with allure.step("Выполнение поиска книги '1984'"):
        main_page.search_book("1984")

    with allure.step("Проверка наличия результатов"):
        results_page = ResultsPage(browser)
        titles = results_page.get_book_titles()
        assert len(titles) > 0, "Не найдено ни одной книги"


@allure.feature("Добавление в корзину")
@allure.severity(allure.severity_level.NORMAL)
@allure.title("Тест: добавление книги в корзину")
@allure.description("Проверяет возможность добавить книгу в корзину с её страницы.")
def test_add_book_to_cart(browser, book_url):
    with allure.step(f"Переход на страницу книги: {book_url}"):
        browser.get(book_url)

    with allure.step("Нажатие кнопки 'Купить/В корзину'"):
        book_page = BookPage(browser)
        book_page.click_buy_button()


@allure.feature("Работа с корзиной")
@allure.severity(allure.severity_level.NORMAL)
@allure.title("Тест: открытие корзины из шапки сайта")
@allure.description("Проверяет переход в корзину через кнопку в верхней части сайта.")
def test_click_cart_button(browser):
    with allure.step("Открытие главной страницы"):
        main_page = MainPage(browser)
        main_page.open()

    with allure.step("Открытие корзины через шапку сайта"):
        cart_page = CartPage(browser)
        cart_page.open_from_header()

    with allure.step("Ожидание загрузки корзины"):
        cart_page.wait_for_cart_to_load()


@allure.feature("Полный сценарий покупки")
@allure.severity(allure.severity_level.BLOCKER)
@allure.title("Тест: добавление книги и переход в корзину")
@allure.description("Проверяет полный сценарий: добавление книги → переход в корзину → увеличение количества.")
def test_add_book_and_go_to_cart(browser, book_url):
    with allure.step(f"Переход на страницу книги: {book_url}"):
        browser.get(book_url)

    with allure.step("Добавление книги в корзину"):
        book_page = BookPage(browser)
        book_page.click_buy_button()

    with allure.step("Переход в корзину через шапку сайта"):
        cart_page = CartPage(browser)
        cart_page.open_from_header()
        cart_page.wait_for_cart_to_load()

    with allure.step("Увеличение количества товара на 1"):
        cart_page.increase_item_quantity()


@allure.feature("Управление корзиной")
@allure.severity(allure.severity_level.NORMAL)
@allure.title("Тест: удаление товара из корзины")
@allure.description("Проверяет возможность удалить товар из корзины.")
def test_add_book_and_remove_from_cart(browser, book_url):
    with allure.step(f"Переход на страницу книги: {book_url}"):
        browser.get(book_url)

    with allure.step("Добавление книги в корзину"):
        book_page = BookPage(browser)
        book_page.click_buy_button()

    with allure.step("Переход в корзину и ожидание загрузки"):
        cart_page = CartPage(browser)
        cart_page.open_from_header()
        cart_page.wait_for_cart_to_load()

    with allure.step("Удаление товара из корзины"):
        cart_page.remove_item_from_cart()
