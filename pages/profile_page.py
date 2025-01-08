import allure

from locators.order_history_page_locators import OrderHistoryPageLocators
from locators.profile_page_locators import ProfilePageLocators
from pages.base_page import BasePage

class ProfilePage(BasePage):
    @allure.step("Клик по ссылке на историю заказов")
    def click_to_order_history(self):
        self.click_to_element(ProfilePageLocators.ORDER_HISTORY_LINK)

    @allure.step("Получение истории заказов пользователя")
    def get_all_orders_history(self):
        return self.find_all_elements_with_wait(OrderHistoryPageLocators.ORDER_HISTORY_ITEMS)

    @allure.step("Выход из учётной записи пользователя")
    def logout(self):
        self.click_to_element(ProfilePageLocators.LOGOUT_BUTTON)