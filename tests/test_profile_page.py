import allure

from locators.login_page_locators import LoginPageLocators
from locators.order_history_page_locators import OrderHistoryPageLocators
from pages.profile_page import ProfilePage


class TestProfilePage:
    @allure.title('Клик по истории заказов открывает историю заказов пользователя')
    def test_click_at_order_history_switched_to_order_history_list(self, main_page_with_logged_in_user):
        main_page_with_logged_in_user.go_to_personal_account()

        profile_page = ProfilePage(main_page_with_logged_in_user.driver)

        profile_page.click_to_order_history()

        order_history_list_element = profile_page.find_element_with_wait(
            OrderHistoryPageLocators.ORDER_HISTORY_LIST, 10, False)

        assert order_history_list_element is not None

    @allure.title('При клике на кнопку "Выход" происходит выход пользователя из учётной записи')
    def test_logout_from_account(self, main_page_with_logged_in_user):
        main_page_with_logged_in_user.go_to_personal_account()  # Переходим в профиль.
        profile_page = ProfilePage(main_page_with_logged_in_user.driver)

        profile_page.logout()  # Выходим из учетной записи

        login_button = profile_page.find_element_with_wait(LoginPageLocators.LOCATOR_LOGIN_BUTTON, 10)

        assert login_button is not None