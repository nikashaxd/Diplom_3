import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators.base_page_locators import BasePageLocators
from locators.cabinet_page_locators import CabinetPageLocators
from locators.order_feed_page_locators import OrderFeedPageLocators
from utilities.data import DataUrl


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Открыть страницу")
    def open(self, url):
        self.driver.get(url)

    @allure.step("Найти элемент на странице")
    def find_element(self, locator):
        return self.driver.find_element(*locator)

    @allure.step("Кликнуть на элемент")
    def click_element(self, locator):
        element = self.find_element(locator)
        element.click()

    @allure.step("Получить текст элемента")
    def text_element(self, locator):
        return self.driver.find_element(*locator).text

    @allure.step("Ввести значение в поле")
    def set_value(self, locator, value):
        self.driver.find_element(*locator).send_keys(value)

    @allure.step("Скроллить страницу до элемента")
    def scroll_page(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step("Проверить, что элемент виден")
    def is_element_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    @allure.step("Проверить, что элемент не виден")
    def is_element_invisible(self, locator):
        return self.wait.until(EC.invisibility_of_element_located(locator))

    @allure.step("Получить значение аттрибута элемента")
    def get_attribute(self, locator, attribute):
        element = self.driver.find_element(*locator)
        return element.get_attribute(attribute)

    @allure.step("Подождать загрузку элемента")
    def wait_element(self, locator, timeout=5):
        WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    @allure.step("Скроллить до элемента")
    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    @allure.step("Получить текст")
    def get_text(self, locator):
        element = self.find_element(locator)
        return element.text

    @allure.step("Кликнуть элемент и ждать его загрузки")
    def click_element_and_wait_for_element(self, click_locator, wait_locator):
        self.click_element(click_locator)
        self.wait_element(wait_locator)

    @allure.step("Выполнить перетаскивание элемента")
    def perform_drag_and_drop(self, source_element, target_element):
        actions = ActionChains(self.driver)
        actions.drag_and_drop(source_element, target_element).perform()

    @allure.step("Перетащить ингредиенты в конструктор")
    def drag_ingredient_to_basket(self, ingredient_locator):
        ingredient = self.driver.find_element(*ingredient_locator)
        target = self.driver.find_element(*BasePageLocators.BURGER_WINDOW)
        self.perform_drag_and_drop(ingredient, target)

    @allure.step("Сделать заказ и получить номер заказа")
    def place_order_get_number(self, first_ingredient, second_ingredient):
        self.drag_ingredient_to_basket(first_ingredient)
        self.drag_ingredient_to_basket(second_ingredient)

        self.click_element(BasePageLocators.CHECKOUT_BUTTON)
        self.wait_element(BasePageLocators.NEW_ORDER_NUMBER)

        # Используем явное ожидание до тех пор, пока номер заказа не станет отличным от '9999'
        WebDriverWait(self.driver, 10).until(
            lambda driver: self.text_element(BasePageLocators.NEW_ORDER_NUMBER) != '9999'
        )

        number = self.text_element(BasePageLocators.NEW_ORDER_NUMBER)
        self.click_element(BasePageLocators.BUTTON_CLOSE_INGREDIENT)

        return number

    @allure.step("Оформить новый заказ")
    def place_order(self, first_ingredient, second_ingredient):
        self.wait_element(first_ingredient)  # Ждем загрузки первого ингредиента
        self.drag_ingredient_to_basket(first_ingredient)

        self.wait_element(second_ingredient)  # Ждем загрузки второго ингредиента
        self.drag_ingredient_to_basket(second_ingredient)

        self.click_element(BasePageLocators.CHECKOUT_BUTTON)
        self.wait_element(BasePageLocators.NEW_ORDER_NUMBER)

        # Ждем, пока номер заказа изменится с '9999'
        WebDriverWait(self.driver, 10).until(
            lambda driver: self.text_element(BasePageLocators.NEW_ORDER_NUMBER) != '9999'
        )

        self.click_element(BasePageLocators.BUTTON_CLOSE_INGREDIENT)

    @allure.step("Ждать, когда элемент станет видимым")
    def wait_for_element_to_be_visible(self, locator, timeout=30):
        WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator),
                                                  f"Element with locator {locator} not found within {timeout} seconds")

    @allure.step("Кликнуть элемент, когда он видимый")
    def click_element_when_visible(self, locator):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator)).click()

    @allure.step("Ожидание исчезновения элемента")
    def wait_for_element_to_disappear(self, locator, timeout=10):
        self.wait.until(EC.invisibility_of_element_located(locator), f"Элемент {locator} не исчез за {timeout} секунд")

    @allure.step("Войти в систему")
    def login(self, email, password):
        self.click_element(BasePageLocators.PERSONAL_CABINET_BUTTON)
        # Шаг 1: Ожидание элементов для ввода email и пароля
        self.wait_element(CabinetPageLocators.EMAIL_INPUT_FIELD)
        self.wait_element(CabinetPageLocators.PASSWORD_INPUT_FIELD)

        # Шаг 2: Ввести email и пароль
        self.set_value(CabinetPageLocators.EMAIL_INPUT_FIELD, email)
        self.set_value(CabinetPageLocators.PASSWORD_INPUT_FIELD, password)

        # Шаг 3: Нажать на кнопку "Войти"
        self.click_element(CabinetPageLocators.LOGIN_BUTTON)

        # Ожидание успешного входа
        self.wait_element(CabinetPageLocators.ORDER_BUTTON)  # Например, кнопка для оформления заказа
