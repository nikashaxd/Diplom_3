from selenium.webdriver.common.by import By


class CabinetPageLocators:
    LOGIN_PAGE_HEADER = [By.XPATH, ".//h2[text()='Вход']"]
    CABINET_HEADER = [By.XPATH, "//p[contains(@class, 'AppHeader_header__linkText') and text() = 'Личный Кабинет']"]
    # Личный Кабинет хэдэр
    FIRST_ORDER_IN_HISTORY = (By.XPATH, "//li[contains(@class, 'OrderHistory_listItem')][1]")
    ORDER_NUMBER = By.XPATH, '(.//p[contains(@class, "text text_type_digits-default")])[1]'
    EMAIL_INPUT_FIELD = [By.XPATH, "//label[text()='Email']/parent::*/input"]  # Поле ввода Email
    PASSWORD_INPUT_FIELD = [By.XPATH, "//input[@name='Пароль']"]  # Поле ввода Пароля
    LOGIN_BUTTON = [By.XPATH, "//button[text()='Войти']"]  # Кнопка Войти
    ORDER_BUTTON = [By.XPATH, './/button[text() = "Оформить заказ"]']  # Кнопка Оформить заказ
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")  # Кнопка Выход

    BUTTON_ORDER_HISTORY = [By.CSS_SELECTOR, "a[href='/account/order-history']"]  # Кнопка История заказов
    ORDER_HISTORY_LIST = [By.CSS_SELECTOR,
                          "div[class = 'OrderHistory_orderHistory__qy1VB']"]  # Список выполненных заказов
    ORDER_HISTORY = [By.CSS_SELECTOR, "a[class = 'OrderHistory_link__1iNby']"]  # Выполненный заказ
