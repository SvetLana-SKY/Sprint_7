import pytest
import requests
import allure
from url import COURIER_CREATE_URL, COURIER_LOGIN_URL
from helpers import generate_random_string

@pytest.fixture
def created_courier():
    
    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    
    with allure.step("Создание курьера в фикстуре"):
        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }
        response = requests.post(COURIER_CREATE_URL, json=payload)
        assert response.status_code == 201

    
    yield login, password, first_name

    
    with allure.step("Удаление курьера в фикстуре"):
        login_response = requests.post(COURIER_LOGIN_URL, json={
            "login": login,
            "password": password
        })
        if login_response.status_code == 200 and "id" in login_response.json():
            courier_id = login_response.json()["id"]
            requests.delete(f"{COURIER_CREATE_URL.rstrip('/')}/{courier_id}")



