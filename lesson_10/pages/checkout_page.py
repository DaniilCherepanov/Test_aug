from selenium.webdriver.common.by import By
from .base_page import BasePage
import allure


class CheckoutPage(BasePage):
    FIRSTNAME = (By.ID, "first-name")
    LASTNAME = (By.ID, "last-name")
    POSTALCODE = (By.ID, "postal-code")
    CONTINUE_BTN = (By.ID, "continue")
    FINISH_BTN = (By.ID, "finish")
    TOTAL = (By.CLASS_NAME, "summary_total_label")

    @allure.step("Заполнение формы заказа")
    def fill_form(self, firstname: str, lastname: str, zipcode: str) -> None:
        """
        Заполняет форму заказа и завершает оформление.

        :param firstname: Имя
        :param lastname: Фамилия
        :param zipcode: Почтовый индекс
        """
        self.fill(self.FIRSTNAME, firstname)
        self.fill(self.LASTNAME, lastname)
        self.fill(self.POSTALCODE, zipcode)
        self.click(self.CONTINUE_BTN)
        self.click(self.FINISH_BTN)

    @allure.step("Получение итоговой суммы")
    def get_total(self) -> str:
        """
        Возвращает итоговую сумму заказа.

        :return: Итоговая сумма
        """
        return self.get_text(self.TOTAL)
