from selenium import webdriver
from pages.calc_page import CalcPage


def test_calc_sum():
    driver = webdriver.Chrome()
    page = CalcPage(driver)

    page.open()
    page.set_delay("45")
    page.click_button("7")
    page.click_button("+")
    page.click_button("8")
    page.click_button("=")

    result = page.get_result()

    assert result == "15"

    driver.quit()
