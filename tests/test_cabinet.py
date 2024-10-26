import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.base_page_locators import BasePageLocators
from pages.cabinet_page import CabinetPage
from locators.cabinet_page_locators import CabinetPageLocators
from utilities.data import DataUser, DataUrl


class TestCabinet:

    @allure.title("Переход на страницу 'Личный кабинет'")
    def test_go_to_cabinet(self, driver):
        cabinet_page = CabinetPage(driver)
        cabinet_page.click_element(BasePageLocators.PERSONAL_CABINET_BUTTON)
        cabinet_page.wait_element(CabinetPageLocators.LOGIN_PAGE_HEADER)
        cabinet_page.set_value(CabinetPageLocators.EMAIL_INPUT_FIELD, DataUser.EMAIL)
        cabinet_page.set_value(CabinetPageLocators.PASSWORD_INPUT_FIELD, DataUser.PASSWORD)
        cabinet_page.click_element(CabinetPageLocators.LOGIN_BUTTON)
        cabinet_page.click_element(CabinetPageLocators.CABINET_HEADER)
        with allure.step("Ожидание перехода на страницу личного кабинета"):
            WebDriverWait(driver, 10).until(EC.url_to_be(DataUrl.PROFILE_PAGE))

        assert driver.current_url == DataUrl.PROFILE_PAGE

    @allure.title("Переход в раздел 'История заказов'")
    def test_go_to_order_history(self, driver):
        cabinet_page = CabinetPage(driver)

        cabinet_page.click_element(BasePageLocators.PERSONAL_CABINET_BUTTON)
        cabinet_page.wait_element(CabinetPageLocators.LOGIN_PAGE_HEADER)

        cabinet_page.set_value(CabinetPageLocators.EMAIL_INPUT_FIELD, DataUser.EMAIL)
        cabinet_page.set_value(CabinetPageLocators.PASSWORD_INPUT_FIELD, DataUser.PASSWORD)

        cabinet_page.click_element(CabinetPageLocators.LOGIN_BUTTON)
        cabinet_page.click_element(CabinetPageLocators.CABINET_HEADER)
        cabinet_page.click_element_when_visible(CabinetPageLocators.BUTTON_ORDER_HISTORY)

        assert driver.current_url == DataUrl.ORDER_HISTORY_PAGE

    @allure.title("Выход из аккаунта")
    def test_logout(self, driver):
        cabinet_page = CabinetPage(driver)

        cabinet_page.click_element(BasePageLocators.PERSONAL_CABINET_BUTTON)
        cabinet_page.wait_element(CabinetPageLocators.LOGIN_PAGE_HEADER)

        cabinet_page.set_value(CabinetPageLocators.EMAIL_INPUT_FIELD, DataUser.EMAIL)
        cabinet_page.set_value(CabinetPageLocators.PASSWORD_INPUT_FIELD, DataUser.PASSWORD)

        cabinet_page.click_element(CabinetPageLocators.LOGIN_BUTTON)
        cabinet_page.go_to_cabinet()

        cabinet_page.click_element_when_visible(CabinetPageLocators.LOGOUT_BUTTON)
        cabinet_page.wait_element(CabinetPageLocators.LOGIN_PAGE_HEADER)

        assert driver.current_url == DataUrl.LOGIN_PAGE
