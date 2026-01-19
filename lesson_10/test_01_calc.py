import pytest
from selenium import webdriver
from pages.calc_page import CalcPage
import allure


@pytest.fixture
def driver():
    """
    Фикстура для инициализации и завершения работы драйвера.
    """
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


@allure.title("Тестирование сложения в калькуляторе")
@allure.description("Тест проверяет корректность сложения чисел в калькуляторе")
@allure.feature("Калькулятор")
@allure.severity(allure.severity_level.CRITICAL)
def test_calc_sum(driver):
    page = CalcPage(driver)

    with allure.step("Открытие страницы калькулятора"):
        page.open()

    with allure.step("Установка задержки 45 секунд"):
        page.set_delay("45")

    with allure.step("Ввод числа 7"):
        page.click_button("7")

    with allure.step("Нажатие кнопки сложения"):
        page.click_button("+")

    with allure.step("Ввод числа 8"):
        page.click_button("8")

    with allure.step("Нажатие кнопки равно"):
        page.click_button("=")

    with allure.step("Получение и проверка результата"):
        result = page.get_result()
        assert result == "15", f"Ожидался результат 15, но получен {result}"

