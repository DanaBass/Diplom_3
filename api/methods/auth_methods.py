import allure
import requests

import helpers
from api.urls import BASE_URL, AUTH_URL
from data.data import User


class AuthMethods:
    @staticmethod
    @allure.step("Создание нового пользователя")
    def create_new_user(new_user: User):
        response = requests.post(f'{BASE_URL}{AUTH_URL}register', json=new_user.get_register_json())

        response_json = response.json()

        if response_json['success']:
            new_user.set_access_token(response_json["accessToken"])

        return response.status_code, response_json, new_user

    @staticmethod
    @allure.step("Удаление пользователя")
    def delete_user(user: User):
        response = requests.delete(f'{BASE_URL}{AUTH_URL}user', json={'accessToken': user.access_token})
        return response.status_code, response.json(), user