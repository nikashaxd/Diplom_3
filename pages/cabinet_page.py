import allure
from pages.base_page import BasePage
from locators.cabinet_page_locators import CabinetPageLocators


class CabinetPage(BasePage):

    @allure.step("Переход на страницу 'Личный кабинет'")
    def go_to_cabinet(self):
        self.click_element(CabinetPageLocators.CABINET_HEADER)

    @allure.step("Переход в раздел 'История заказов'")
    def go_to_order_history(self):
        self.click_element(CabinetPageLocators.BUTTON_ORDER_HISTORY)
        self.wait_element(CabinetPageLocators.ORDER_HISTORY_LIST)

    @allure.step("Выход из аккаунта")
    def logout(self):
        self.click_element_when_visible(CabinetPageLocators.LOGOUT_BUTTON)
