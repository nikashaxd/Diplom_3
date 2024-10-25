import allure
import pytest
import requests
from selenium import webdriver
from utilities.data import DataUrl
from utilities.generate_user import generate_random_string


@pytest.fixture(params=['firefox', 'chrome'], scope='function')
@allure.title('Фикстура запускает браузеры chrome и firefox с одинаковыми параметрами')
def driver(request):
    driver = None

    if request.param == 'firefox':
        driver = webdriver.Firefox()
    elif request.param == 'chrome':
        driver = webdriver.Chrome()

    driver.maximize_window()
    driver.get(DataUrl.MAIN_PAGE)
    yield driver
    driver.quit()


@pytest.fixture
@allure.title('Фикстура создает и удаляет пользователя через АПИ')
def create_and_delete_user():
    # Регистрация пользователя
    user_data = {
        "email": f"user_{generate_random_string(5)}@example.com",
        "password": generate_random_string(10),
        "name": f"User_{generate_random_string(5)}"
    }

    # Создаем пользователя через API
    response = requests.post(DataUrl.USER_REGISTER_PAGE, json=user_data)

    assert response.status_code == 200, "User registration failed"
    access_token = response.json()['accessToken']

    # Возвращаем данные пользователя для использования в тестах
    yield user_data
    with allure.step("Удаление пользователя"):
        headers = {"Authorization": f"Bearer {access_token}"}
        requests.delete(DataUrl.USER_DELETE, headers=headers)
