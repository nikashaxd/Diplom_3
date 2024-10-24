import allure

from locators.cabinet_page_locators import CabinetPageLocators
from utilities.data import DataUser
from locators.base_page_locators import BasePageLocators
from locators.main_page_locators import MainPageLocators
from pages.order_feed_page import OrderFeedPage
from locators.order_feed_page_locators import OrderFeedPageLocators


class TestOrderFeed:

    @allure.title("Открытие деталей заказа")
    def test_open_order_details(self, driver):
        order_feed_page = OrderFeedPage(driver)

        order_feed_page.click_element_and_wait_for_element(BasePageLocators.ORDER_FEED,
                                                           OrderFeedPageLocators.LAST_ORDER)
        top_order_in_feed = order_feed_page.text_element(OrderFeedPageLocators.LAST_ORDER_NUMBER)
        order_feed_page.click_element_and_wait_for_element(OrderFeedPageLocators.LAST_ORDER,
                                                           OrderFeedPageLocators.WINDOW_ORDER)
        order_in_window = order_feed_page.text_element(OrderFeedPageLocators.ORDER_NUMBER_IN_WINDOW)

        assert top_order_in_feed == order_in_window

    @allure.title('Проверить, что заказы из Истории отображаются в Ленте заказов')
    def test_order_feed_order_in_history_exists_in_feed(self, create_and_delete_user, driver):
        user_data = create_and_delete_user
        email = user_data['email']
        password = user_data['password']

        order_feed_page = OrderFeedPage(driver)
        order_feed_page.login(email, password)

        order_number = order_feed_page.place_order_get_number(MainPageLocators.BUN_LINK2, MainPageLocators.LINK_FILLING)

        order_feed_page.click_element_and_wait_for_element(BasePageLocators.ORDER_FEED,
                                                           OrderFeedPageLocators.LAST_ORDER)

        is_order_in_feed = order_feed_page.is_order_in_feed_displayed(order_number)

        order_feed_page.click_element_and_wait_for_element(BasePageLocators.PERSONAL_CABINET_BUTTON,
                                                           CabinetPageLocators.BUTTON_ORDER_HISTORY)
        order_feed_page.click_element_and_wait_for_element(CabinetPageLocators.BUTTON_ORDER_HISTORY,
                                                           CabinetPageLocators.ORDER_HISTORY_LIST)

        is_order_in_history = order_feed_page.is_displayed_order_in_history(order_number)

        assert is_order_in_feed
        assert is_order_in_history, f"Order number {order_number} not found in order history"

    @allure.title("Проверка увеличения счетчиков заказов после оформления нового заказа")
    def test_order_feed_counters_increase_after_new_order(self, driver):
        order_feed_page = OrderFeedPage(driver)

        order_feed_page.login(DataUser.EMAIL, DataUser.PASSWORD)

        order_feed_page.click_element_and_wait_for_element(BasePageLocators.ORDER_FEED,
                                                           OrderFeedPageLocators.LAST_ORDER)
        completed_all_time_before = int(order_feed_page.text_element(OrderFeedPageLocators.COMPLETED_ALL_TIME_COUNTER))
        completed_today_before = int(order_feed_page.text_element(OrderFeedPageLocators.COMPLETED_TODAY_COUNTER))

        order_feed_page.click_element(BasePageLocators.CONSTRUCTOR_BUTTON)

        order_feed_page.place_order(MainPageLocators.BUN_LINK2, MainPageLocators.LINK_FILLING)

        order_feed_page.click_element_and_wait_for_element(BasePageLocators.ORDER_FEED,
                                                           OrderFeedPageLocators.LAST_ORDER)
        completed_all_time_after = int(order_feed_page.text_element(OrderFeedPageLocators.COMPLETED_ALL_TIME_COUNTER))
        completed_today_after = int(order_feed_page.text_element(OrderFeedPageLocators.COMPLETED_TODAY_COUNTER))

        assert completed_all_time_after > completed_all_time_before
        assert completed_today_after > completed_today_before

    @allure.title("Проверка, что заказ появляется в разделе 'В работе'")
    def test_order_appears_in_process_status(self, driver):
        order_feed_page = OrderFeedPage(driver)

        order_feed_page.login(DataUser.EMAIL, DataUser.PASSWORD)

        order_number = order_feed_page.place_order_get_number(MainPageLocators.BUN_LINK2, MainPageLocators.LINK_FILLING)

        order_feed_page.click_element_and_wait_for_element(BasePageLocators.ORDER_FEED,
                                                           OrderFeedPageLocators.LAST_ORDER)

        is_order_in_process = order_feed_page.is_displayed_order_in_status_box_in_process(order_number)

        assert is_order_in_process
