from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGO_STELLAR_BURGER = (By.XPATH, "//div[contains(@class, 'logo')]")  # Логотип
    PERSONAL_CABINET_BUTTON = (By.XPATH, "//p[text()= 'Личный Кабинет']")  # Раздел Личный Кабинет
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()= 'Конструктор']")  # Раздел Конструктор
    ORDER_FEED = [By.XPATH, "//p[text()= 'Лента Заказов']"]  # Раздел Ленты заказов
    CHECKOUT_BUTTON = [By.XPATH, "//button[text() = 'Оформить заказ']"]  # Кнопка оформить заказ
    BURGER_WINDOW = [By.XPATH, ".//ul[contains(@class, 'BurgerConstructor_basket')]"]  # Oбласть конструктора бургера
    BUTTON_CLOSE_INGREDIENT = [By.XPATH,
                               ".//button[contains(@class, 'Modal_modal__close')]"] # Кнопка закрытия деталей ингредиента
    NEW_ORDER_NUMBER = [By.CSS_SELECTOR, "h2[class*='Modal_modal__title_shadow']"]  # Номер нового заказа
