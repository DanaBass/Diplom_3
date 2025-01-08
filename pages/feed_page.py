import allure

from locators.feed_page_locators import FeedPageLocators
from pages.constructor_page import ConstructorPage


class FeedPage(ConstructorPage):
    @allure.step("Получение заказа по переданному номеру")
    def get_order_by_number(self, order_number: str):
        return self.find_element_with_wait(FeedPageLocators.get_order_number_element(order_number))