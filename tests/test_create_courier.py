import requests
import allure
from helpers import register_new_courier_and_return_login_password, generate_random_string
from url import COURIER_CREATE_URL


class TestCreateCourier:

    @allure.title('создание курьера')
    def test_create_courier_success(self):
        payload = {'login': generate_random_string(8),
            'password': generate_random_string(6),
            'firstName': generate_random_string(8)}
        
        response = requests.post(COURIER_CREATE_URL, data=payload)

        assert response.status_code == 201
        assert response.json() == {"ok": True}