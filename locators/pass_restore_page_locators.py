from selenium.webdriver.common.by import By


class RestorePageLocators:
    RESTORE_PASSWORD = [By.XPATH, ".//a[text()='Восстановить пароль']"]  # Ссылка на восстановление пароля
    RESTORE_INPUT_EMAIL = [By.CSS_SELECTOR, "input[class = 'text input__textfield text_type_main-default']"]
    # Окно ввода почты для восстановления пароля

    RESTORE_BUTTON = [By.XPATH, ".//button[text()='Восстановить']"]  # Кнопка Восстановить

    RESTORE_INPUT_NEW_PASSWORD = [By.CSS_SELECTOR, "input[class='text input__textfield text_type_main-default']"]
    # Окно ввода нового пароля

    RESTORE_NEW_PASSWORD_VISIBLE = [By.CSS_SELECTOR, "input.text.input__textfield"]

    VISIBLE_BUTTON = [By.CSS_SELECTOR, "div[class ='input__icon input__icon-action']"]  # Визибилити пароля
