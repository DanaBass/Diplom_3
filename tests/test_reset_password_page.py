import allure

from pages.forgot_password_page import ForgotPasswordPage
from pages.reset_password_page import ResetPasswordPage


class TestResetPasswordPage:
    @allure.title('При клике на кнопку "показать пароль" пароль отображается и можно увидеть его в строковом виде')
    def test_click_on_show_password_button_shows_password_value(self, forgot_password_page_driver):
        forgot_password_page = ForgotPasswordPage(forgot_password_page_driver)
        forgot_password_page.go_to_recover_password_page('random_email@mail.ru')

        reset_password_page = ResetPasswordPage(forgot_password_page_driver)
        reset_password_page.fill_password_field('6password6')

        reset_password_page.click_show_password()

        assert reset_password_page.is_password_active()