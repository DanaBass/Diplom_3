import allure

from locators.reset_password_page_locators import ResetPasswordPageLocators
from pages.forgot_password_page import ForgotPasswordPage


class TestForgotPasswordPage:
    @allure.title('После заполнения email и клику по кнопке "восстановить пароль" происходит переход на страницу восстановления пароля')
    def test_fill_email_and_click_to_recover_button_switch_to_reset_password_page(self, forgot_password_page_driver):
        forgot_password_page = ForgotPasswordPage(forgot_password_page_driver)
        forgot_password_page.go_to_recover_password_page('random_email@mail.ru')

        password_field = forgot_password_page.find_element_with_wait(ResetPasswordPageLocators.PASSWORD_PLACEHOLDER)
        assert password_field is not None