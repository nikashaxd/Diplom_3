import allure
from pages.main_page import MainPage
from locators.main_page_locators import MainPageLocators
from utilities.data import DataUser, DataUrl


class TestMainFunctions:

    @allure.title("Переход на страницу конструктора")
    def test_go_to_constructor(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_constructor()
        assert driver.current_url == DataUrl.MAIN_PAGE

    @allure.title("Переход на страницу ленты заказов")
    def test_go_to_order_feed(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_order_feed()
        assert driver.current_url == DataUrl.FEED_PAGE

    @allure.title("Проверка появления всплывающего окна с деталями ингредиента")
    def test_ingredient_details_popup(self, driver):
        main_page = MainPage(driver)
        main_page.click_ingredient(MainPageLocators.BUN_LINK1)
        assert driver.current_url == DataUrl.INGREDIENT_PAGE

    @allure.title("Закрытие всплывающего окна")
    def test_close_ingredient_details(self, driver):
        main_page = MainPage(driver)
        main_page.click_ingredient(MainPageLocators.BUN_LINK1)
        main_page.close_details_window()
        assert main_page.is_element_invisible(MainPageLocators.OPEN_DETAILS)

    @allure.title("Проверка увеличения счетчика ингредиента")
    def test_ingredient_counter_increase(self, driver):
        main_page = MainPage(driver)
        counter_before = main_page.counter_value(MainPageLocators.FILLING_COUNTER)
        main_page.drag_ingredient_to_basket(MainPageLocators.LINK_FILLING)
        counter_after = main_page.counter_value(MainPageLocators.FILLING_COUNTER)
        assert counter_before < counter_after

    @allure.title("Оформление заказа для залогиненного пользователя")
    def test_place_order(self, driver):
        main_page = MainPage(driver)

        main_page.login(DataUser.EMAIL, DataUser.PASSWORD)
        main_page.drag_ingredient_to_basket(MainPageLocators.BUN_LINK1)
        main_page.drag_ingredient_to_basket(MainPageLocators.LINK_FILLING)

        order_id_before = main_page.text_element(MainPageLocators.ORDER_ID)

        main_page.wait_for_element_to_disappear(MainPageLocators.MODAL_OVERLAY)

        main_page.scroll_to_element(MainPageLocators.MAKING_ORDER_BUTTON)
        main_page.click_element_and_wait_for_element(MainPageLocators.MAKING_ORDER_BUTTON, MainPageLocators.ORDER_ID)

        order_id_after = main_page.text_element(MainPageLocators.ORDER_ID)
        assert order_id_after != order_id_before
