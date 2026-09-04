import pytest
import requests
import allure
from url import ORDERS_LIST_URL


class TestOrderList:
    @allure.title("Получение списка заказов")
    def test_get_order_list(self):
        response = requests.get(ORDERS_LIST_URL)

        assert response.status_code == 200
        assert "orders" in response.json()
        assert isinstance(response.json()["orders"], list)