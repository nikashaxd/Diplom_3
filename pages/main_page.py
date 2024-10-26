import allure

from locators.base_page_locators import BasePageLocators
from locators.cabinet_page_locators import CabinetPageLocators
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):

    @allure.step("Переход на страницу конструктора")
    def go_to_constructor(self):
        self.click_element(MainPageLocators.CONSTRUCTOR)

    @allure.step("Переход на страницу ленты заказов")
    def go_to_order_feed(self):
        self.click_element(MainPageLocators.ORDER_FEED)

    @allure.step("Клик по ингредиенту")
    def click_ingredient(self, ingredient_locator):
        self.click_element(ingredient_locator)

    @allure.step("Закрытие окна деталей ингредиента")
    def close_details_window(self):
        self.click_element(MainPageLocators.BUTTON_CLOSE_DETAILS)

    @allure.step("Получить значение счетчика")
    def counter_value(self, ingredient):
        self.scroll_page(ingredient)
        counter = self.text_element(ingredient)
        return int(counter)


