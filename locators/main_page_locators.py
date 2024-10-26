from selenium.webdriver.common.by import By


class MainPageLocators:
    CONSTRUCTOR = [By.XPATH, ".//h1[text()='Соберите бургер']"]
    ORDER_FEED = [By.CSS_SELECTOR, "a[href='/feed'] "]
    BUN_LINK1 = [By.XPATH, ".//a[@href='/ingredient/61c0c5a71d1f82001bdaaa6d']"]  # Ссылка на Флюоресцентную булочку
    BUN_LINK2 = [By.XPATH, ".//a[@href='/ingredient/61c0c5a71d1f82001bdaaa6c']"]  # Ссылка на Краторную булочку
    LINK_FILLING = [By.XPATH, ".//a[@href='/ingredient/61c0c5a71d1f82001bdaaa6e']"]  # Ссылка на начинку
    FILLING_COUNTER = [By.XPATH,
                       ".//a[@href='/ingredient/61c0c5a71d1f82001bdaaa6e']//p[contains(@class, 'counter')]"]
    # Счетчик количества добавленной начинки

    DETAILS_HEADER = [By.XPATH, ".//h2[text()='Детали ингредиента']"] # Заголовок окна Детали ингредиента
    BUTTON_CLOSE_DETAILS = [By.XPATH, ".//button[contains(@class, 'Modal_modal__close')]"]
    # Кнопка закрытия окна деталей ингредиента

    OPEN_DETAILS = [By.XPATH, ".//section[contains(@class, 'modal_opened')]"] # Открытое окно деталей ингредиента
    BURGER_ASSEMBLY = [By.XPATH, ".//ul[contains(@class, 'BurgerConstructor_basket')]"] # Окно сборки бургера
    MAKING_ORDER_BUTTON = [By.XPATH, ".//div[contains(@class, 'BurgerConstructor_basket__container')]/button"]
    # Кнопка оформления заказа

    ORDER_ID = [By.XPATH, ".//p[text()='идентификатор заказа']/../h2"] # Номер заказа

    MODAL_OVERLAY = [By.CSS_SELECTOR, ".Modal_modal_overlay__x2ZCr"]  # Локатор модального перекрывающего элемента
