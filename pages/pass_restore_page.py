import allure
from pages.base_page import BasePage
from locators.pass_restore_page_locators import RestorePageLocators


class PassRestorePage(BasePage):

    @allure.step("Нажать на кнопку 'Показать/Скрыть пароль'")
    def toggle_password_visibility(self):
        self.click_element(RestorePageLocators.VISIBLE_BUTTON)
