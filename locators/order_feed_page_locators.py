from selenium.webdriver.common.by import By


class OrderFeedPageLocators:
    STATUS_ORDER = [By.XPATH, ".//ul[contains(@class, 'OrderFeed_orderListReady')]"]  # Номера заказов в работе
    FIRST_ORDER = [By.XPATH, '(.//a[contains(@class, "OrderHistory_link__1iNby")])[1]']
    LAST_ORDER = [By.XPATH, ".//ul[contains(@class, 'OrderFeed_list')]/li[1]/a"]  # Последний заказ в ленте заказов

    ORDER_NUMBER_IN_WINDOW = [By.XPATH, './/p[contains(@class, "text text_type_digits-default mb-10 mt-5")]']
    # Номер заказа в окне заказа

    LAST_ORDER_NUMBER = [By.XPATH, "(//div[contains(@class, 'OrderHistory_textBox__3lgbs')]//p[contains(@class, "
                                   "'text_type_digits-default')])[1]"]
    # Номер последнего заказа в ленте заказов

    WINDOW_ORDER = [By.XPATH, ".//section[contains(@class, 'modal_opened')]"]  # Окно заказа

    NUMBER_NEW_ORDER = [By.XPATH, ".//section[contains(@class, 'modal_opened')]//"
                                  "div[contains(@class, 'Modal_modal__contentBox')]/"
                                  "h2[contains(@class, 'text_type_digits-large')]"]
    # Номер заказа в окне заказа

    COMPLETED_ALL_TIME_COUNTER = [By.XPATH, ".//p[text()='Выполнено за все время:']/../p[contains(@class, 'OrderFeed_number')]"]
    # Счетчик выполненных заказов за все время

    COMPLETED_TODAY_COUNTER = [By.XPATH, ".//p[text()='Выполнено за сегодня:']/../p[contains(@class, 'OrderFeed_number')]"]
    # Счетчик выполненных заказов за сегодня

    @staticmethod
    def order_locator_by_number(order_number):
        return By.XPATH, f".//ul[contains(@class, 'OrderFeed_list')]//p[contains(text(), '#0{order_number}')]"

    # Статический метод для определения номера заказа

    @staticmethod
    def order_in_history_locator(order_number):
        return By.XPATH, f"//p[contains(@class, 'text_type_digits-default') and contains(text(), '#0{order_number}')]"

    # Статический метод для определения номера заказа в истории заказов

    @staticmethod
    def order_in_status_box_locator(order_number):
        return By.XPATH, f".//p[contains(text(), '#0{order_number}')]"

    # Статический метод для определения номера заказа в области "в работе"