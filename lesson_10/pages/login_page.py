from selenium.webdriver.common.by import By
from .base_page import BasePage
import allure


class LoginPage(BasePage):
    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN_BTN = (By.ID, "login-button")

    @allure.step("Выполнение авторизации")
    def login(self, username, password):
        """
        Выполняет авторизацию пользователя на странице входа.

        :param username: Имя пользователя
        :param password: Пароль пользователя
        """
        self.fill(self.USERNAME, username)
        self.fill(self.PASSWORD, password)
        self.click(self.LOGIN_BTN)
