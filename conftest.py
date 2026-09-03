import pytest
import requests
import allure
from url import COURIER_CREATE_URL
from helpers import register_new_courier_and_return_login_password

@pytest.fixture
@allure.title('Фикстура: создаёт тестового курьера и возвращает логин, пароль, имя')
def created_courier():
    courier = register_new_courier_and_return_login_password()
   
    login, password, first_name = courier
    
    yield login, password, first_name

 

    # Удаление курьера после теста
    login_response = requests.post(COURIER_CREATE_URL, json={
        "login": login,
        "password": password
    })
    if login_response.status_code == 200 and "id" in login_response.json():
        courier_id = login_response.json()["id"]
        requests.delete(f"{COURIER_CREATE_URL}/{courier_id}")