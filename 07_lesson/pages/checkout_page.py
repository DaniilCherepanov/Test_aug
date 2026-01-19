from selenium.webdriver.common.by import By
from .base_page import BasePage

class CheckoutPage(BasePage):
    FIRSTNAME = (By.ID, "first-name")
    LASTNAME = (By.ID, "last-name")
    POSTALCODE = (By.ID, "postal-code")
    CONTINUE_BTN = (By.ID, "continue")
    FINISH_BTN = (By.ID, "finish")
    TOTAL = (By.CLASS_NAME, "summary_total_label")

    def fill_form(self, firstname, lastname, zipcode):
        self.fill(self.FIRSTNAME, firstname)
        self.fill(self.LASTNAME, lastname)
        self.fill(self.POSTALCODE, zipcode)
        self.click(self.CONTINUE_BTN)
        self.click(self.FINISH_BTN)

    def get_total(self):
        return self.get_text(self.TOTAL)
