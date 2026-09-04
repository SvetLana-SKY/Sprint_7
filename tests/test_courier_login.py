import requests
import allure
from helpers import generate_random_string
from url import COURIER_LOGIN_URL


class TestLoginCourier:

    @allure.title('Успешная авторизация курьера: возвращает id')
    def test_login_courier_success(self, created_courier):
        login, password, first_name = created_courier

        payload = {
            "login": login,
            "password": password
        }
        response = requests.post(COURIER_LOGIN_URL, data=payload)

        assert response.status_code == 200
        assert "id" in response.json()



    @allure.title('Авторизация курьера без логина')
    def test_login_courier_withaut_login(self, created_courier):
        login, password, first_name = created_courier

        payload = {'password': password}
        response = requests.post(COURIER_LOGIN_URL, data=payload)

        assert response.status_code == 400
        assert response.json() == {'message': "Недостаточно данных для входа"}

               



    @allure.title('Авторизация без пароля')
    def test_login_courier_without_password(self, created_courier):
        login, password, first_name = created_courier

        payload = {"login": login}
        response = requests.post(COURIER_LOGIN_URL, data=payload)

        assert response.status_code == 400
        assert response.json() == {'message': "Недостаточно данных для входа"}
        
    



    @allure.title('Авторизация с неверным паролем')
    def test_login_wrong_password(self, created_courier):
        login, password, first_name = created_courier
        wrong_password = generate_random_string(6)

        payload = {
            "login": login,
            "password": wrong_password
        }
        response = requests.post(COURIER_LOGIN_URL, data=payload)

        assert response.status_code == 404
        assert response.json() == {'message': "Учетная запись не найдена"}
        

       


    @allure.title('Авторизация с неверным логином')
    def test_login_wrong_login(self, created_courier):
        login, password, first_name = created_courier
        
   
        payload = {
               "login": login + 'm',
               "password": password
           }
        response = requests.post(COURIER_LOGIN_URL, data=payload)
   
        assert response.status_code == 404
        assert response.json() == {'message': "Учетная запись не найдена"}