import requests
import allure
from helpers import register_new_courier_and_return_login_password, generate_random_string
from url import COURIER_CREATE_URL, COURIER_LOGIN_URL


class TestCreateCourier:

    @allure.title('Создание курьера')
    def test_create_courier_success(self):
        login = generate_random_string(8)
        password = generate_random_string(6)
        first_name = generate_random_string(8)

        payload = {
            'login': login,
            'password': password,
            'firstName': first_name
        }

        response = requests.post(COURIER_CREATE_URL, data=payload)
        assert response.status_code == 201
        assert response.json() == {"ok": True}

        login_response = requests.post(COURIER_LOGIN_URL, json={
                "login": login,
                "password": password
            })
        assert login_response.status_code == 200
        courier_id = login_response.json()["id"]


        with allure.step("Удаление созданного курьера"):
            requests.delete(f"{COURIER_CREATE_URL.rstrip('/')}/{courier_id}")


        
    @allure.title('Создание одинаковых курьеров')
    def test_create_duplicate_courier(self, created_courier):
        login, password, first_name = created_courier

        payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }
        response = requests.post(COURIER_CREATE_URL, data=payload)


        assert response.status_code == 409
        assert response.json() == {'message': 'Этот логин уже используется'}


    @allure.title('Создание курьера без логина')
    def test_create_without_login(self):
        password = generate_random_string(6)
        first_name = generate_random_string(8)

        payload = {
            "password": password,
            "firstName": first_name
        }

        response = requests.post(COURIER_CREATE_URL, data=payload)
        assert response.status_code == 400
        assert response.json() == {"message": "Недостаточно данных для создания учетной записи"}



    @allure.title("Создание курьера без пароля")
    def test_create_without_password(self):
        payload = {'login': generate_random_string(8),
                'firstName': generate_random_string(8)}

        response = requests.post(COURIER_CREATE_URL, data=payload)
        assert response.status_code == 400
        assert response.json() == {"message": "Недостаточно данных для создания учетной записи"}



    @allure.title('Создание курьеров с одинаковым логином')
    def test_create_duplicate_login(self, created_courier):
        login, password, first_name = created_courier

        payload = {
        "login": login,
        "password": generate_random_string(6),
        "firstName": generate_random_string(8)
    }
        response = requests.post(COURIER_CREATE_URL, data=payload)


        assert response.status_code == 409
        assert response.json() == {'message': 'Этот логин уже используется'}            