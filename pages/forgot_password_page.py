import allure

from locators.forgot_password_page_locators import ForgotPasswordPageLocators
from pages.base_page import BasePage


class ForgotPasswordPage(BasePage):
    @allure.step("Переход на страницу восстановления пароля")
    def go_to_recover_password_page(self, email: str):
        self.fill_email_for_password_recovering(email)
        self.click_to_recover_password_button()

    @allure.step("Заполнение email для восстановления пароля")
    def fill_email_for_password_recovering(self, email: str):
        self.add_text_to_element(ForgotPasswordPageLocators.EMAIL_PLACEHOLDER, email)

    @allure.step("Клик на кнопку восстановления пароля")
    def click_to_recover_password_button(self):
        self.click_to_element(ForgotPasswordPageLocators.RECOVER_PASSWORD_BUTTON)