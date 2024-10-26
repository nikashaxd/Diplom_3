from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from locators.base_page_locators import BasePageLocators
from locators.cabinet_page_locators import CabinetPageLocators
from pages.base_page import BasePage
import allure
from locators.order_feed_page_locators import OrderFeedPageLocators


class OrderFeedPage(BasePage):

    @allure.step("Проверить отображение заказа в ленте заказов по номеру")
    def is_order_in_feed_displayed(self, order_number):
        order_locator = OrderFeedPageLocators.order_locator_by_number(order_number)
        return self.is_element_visible(order_locator)

    @allure.step("Проверить отображение заказа в ленте заказов по номеру")
    def is_displayed_order_in_feed(self, order_number):
        order_locator = OrderFeedPageLocators.order_locator_by_number(order_number)
        return self.is_element_visible(order_locator)

    @allure.step("Проверить отображение заказа в истории заказов по номеру")
    def is_displayed_order_in_history(self, order_number):
        order_locator = OrderFeedPageLocators.order_in_history_locator(order_number)
        return self.is_element_visible(order_locator)

    @allure.step('Получить номер последнего сделанного заказа пользователем')
    def get_last_number_order(self):
        self.click_element(BasePageLocators.PERSONAL_CABINET_BUTTON)
        self.click_element(CabinetPageLocators.BUTTON_ORDER_HISTORY)
        return self.get_text(OrderFeedPageLocators.LAST_ORDER)

    @allure.step("Проверить отображение заказа в списке заказов в работе по номеру")
    def is_displayed_order_in_status_box_in_process(self, order_number):
        order_locator = OrderFeedPageLocators.order_in_status_box_locator(order_number)
        return self.is_element_visible(order_locator)