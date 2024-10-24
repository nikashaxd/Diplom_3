import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.base_page_locators import BasePageLocators
from pages.pass_restore_page import PassRestorePage
from locators.pass_restore_page_locators import RestorePageLocators
from utilities.data import DataUrl, DataUser


class TestPassRestore:

    @allure.title("Переход на страницу восстановления пароля")
    def test_navigate_to_restore_page(self, driver):
        restore_page = PassRestorePage(driver)
        restore_page.click_element(BasePageLocators.PERSONAL_CABINET_BUTTON)
        restore_page.click_element(RestorePageLocators.RESTORE_PASSWORD)
        assert driver.current_url == DataUrl.RESTORE_PAGE_WITH_EMAIL

    @allure.title("Ввод почты и нажатие на кнопку 'Восстановить'")
    def test_recovery_input_email_and_click_restore(self, driver):
        restore_page = PassRestorePage(driver)
        restore_page.click_element(BasePageLocators.PERSONAL_CABINET_BUTTON)

        restore_page.click_element(RestorePageLocators.RESTORE_PASSWORD)

        restore_page.wait_element(RestorePageLocators.RESTORE_INPUT_EMAIL)

        restore_page.set_value(RestorePageLocators.RESTORE_INPUT_EMAIL, DataUser.EMAIL)

        restore_page.click_element(RestorePageLocators.RESTORE_BUTTON)

        WebDriverWait(driver, 10).until(EC.url_contains('reset-password'))

        assert driver.current_url == DataUrl.RESTORE_INPUT_PASSWORD_PAGE

    @allure.title("Проверка видимости пароля при нажатии на кнопку 'Показать/Скрыть' через личный кабинет")
    def test_recovery_password_visibility(self, driver):
        restore_page = PassRestorePage(driver)

        restore_page.click_element(BasePageLocators.PERSONAL_CABINET_BUTTON)

        restore_page.click_element(RestorePageLocators.RESTORE_PASSWORD)

        restore_page.wait_element(RestorePageLocators.RESTORE_INPUT_EMAIL)

        restore_page.set_value(RestorePageLocators.RESTORE_INPUT_EMAIL, DataUser.EMAIL)

        restore_page.click_element(RestorePageLocators.RESTORE_BUTTON)

        WebDriverWait(driver, 10).until(EC.url_contains('reset-password'))

        WebDriverWait(driver, 10).until(
            EC.invisibility_of_element_located((By.CLASS_NAME, "Modal_modal_overlay__x2ZCr")))

        restore_page.set_value(RestorePageLocators.RESTORE_INPUT_EMAIL, DataUser.PASSWORD)

        restore_page.toggle_password_visibility()

        assert restore_page.get_attribute(RestorePageLocators.RESTORE_NEW_PASSWORD_VISIBLE, 'type') == 'text'
