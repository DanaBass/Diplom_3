import allure

from locators.login_page_locators import LoginPageLocators
from pages.base_page import BasePage


class LoginPage(BasePage):
    @allure.step("Открытие страницы восстановления пароля")
    def open_forgot_password_page(self):
        self.click_to_element(LoginPageLocators.FORGOT_PASSWORD_LINK)