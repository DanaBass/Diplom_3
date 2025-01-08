import allure

from locators.forgot_password_page_locators import ForgotPasswordPageLocators
from locators.profile_page_locators import ProfilePageLocators
from pages.login_page import LoginPage


class TestLoginPage:
    @allure.title('После клика по кнопке "Восстановить пароль" происходит переход на страницу восстановления пароля')
    def test_click_recover_password_switch_to_recover_page(self, login_page_driver):
        login_page = LoginPage(login_page_driver)

        login_page.open_forgot_password_page()

        password_recover_button = login_page.find_element_with_wait(ForgotPasswordPageLocators.RECOVER_PASSWORD_BUTTON)

        assert password_recover_button is not None

    @allure.title('Для авторизованного пользователя после клика по ссылке на личный кабинет происходит переход в его личный кабинет')
    def test_click_at_personnal_account_switched_to_personnal_account_page(self, main_page_with_logged_in_user):
        main_page_with_logged_in_user.go_to_personal_account()

        profile_element = main_page_with_logged_in_user.find_element_with_wait(ProfilePageLocators.PROFILE_ELEMENT)

        assert profile_element is not None

