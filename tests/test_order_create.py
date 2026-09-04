
import pytest
import requests
import allure
import json
from url import ORDER_CREATE_URL
from helpers import generate_random_string, generate_phone, generate_address, get_today_date
from datetime import datetime


class TestCreateOrder:


    @allure.title('Создание заказа: проверка цветов и наличия track')
    @pytest.mark.parametrize('color_list', [ ['BLACK'],
        ['GREY'],
        ['BLACK', 'GREY'],
        []], ids=['color_black', 'color_grey', 'color_both', 'color_none'])

    def test_create_order_with_colors(self, color_list):
        payload = {
            "firstName": generate_random_string(8),
            "lastName": generate_random_string(8),
            "address": generate_address(),
            "metroStation": 4,
            "phone": generate_phone(),
            "rentTime": 5,
            "deliveryDate": get_today_date(),
            "color": color_list
        }
        headers = {"Content-type": "application/json"}
        payload_string = json.dumps(payload)
        response = requests.post(ORDER_CREATE_URL, data=payload_string, headers=headers)



        assert response.status_code == 201
        assert "track" in response.json()

        data = response.json()
        assert "track" in data
        track = data["track"]

        requests.delete(f"{ORDER_CREATE_URL.rstrip('/')}/{track}")