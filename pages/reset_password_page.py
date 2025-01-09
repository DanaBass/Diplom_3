import allure

from locators.reset_password_page_locators import ResetPasswordPageLocators
from pages.base_page import BasePage


class ResetPasswordPage(BasePage):
    @allure.step("Заполнение поля с паролем")
    def fill_password_field(self, password: str):
        self.add_text_to_element(ResetPasswordPageLocators.PASSWORD_PLACEHOLDER, password)

    @allure.step("Клик по иконке 'Показать пароль'")
    def click_show_password(self):
        self.click_to_element(ResetPasswordPageLocators.SHOW_PASSWORD_ELEMENT)

    @allure.step("Проверка, виден ли пароль в виде текста")
    def is_password_active(self):
        password_active_element = self.find_element_with_wait(ResetPasswordPageLocators.PASSWORD_ACTIVE_STATUS_ELEMENT, 1)
        return password_active_element is not None

