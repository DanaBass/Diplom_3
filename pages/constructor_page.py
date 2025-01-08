import allure
from selenium.common import ElementClickInterceptedException
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage

class ConstructorPage(BasePage):
    @allure.step("Переход в личный кабинет пользователя")
    def go_to_personal_account(self):
        self.click_to_element(MainPageLocators.LOCATOR_PERSONAL_ACCOUNT)

    @allure.step("Получение всех имеющихся ингридиентов")
    def get_all_existing_ingredients(self):
        return self.find_all_elements_with_wait(MainPageLocators.INGREDIENT_REFERENCES_FOR_DETAILS)

    @allure.step("Получение детальной информации первого из доступных ингридиентов")
    def open_first_ingredient_details(self):
        ingredient_references = self.get_all_existing_ingredients()

        fisrt_ingredient = ingredient_references[0]

        try:
            fisrt_ingredient.click()  # Клик по первому найденному в DOM-дереве ингредиенту.
        except ElementClickInterceptedException:
            self.driver.execute_script("arguments[0].click();", fisrt_ingredient)

    @allure.step("Подготовка заказа")
    def prepare_order(self):
        fisrt_ingredient = self.get_all_existing_ingredients()[0]  # Получение первого имеющегося ингридиента.
        cart_element = self.get_cart_element()
        self.drag_and_drop_element(fisrt_ingredient, cart_element)  # Перенос ингридиента в корзину для сборки.

    @allure.step("Получение элемента из корзины")
    def get_cart_element(self):
        return self.find_element_with_wait(MainPageLocators.CART_ELEMENT)

    @allure.step("Создание заказа")
    def create_order(self):
        self.prepare_order() # Подготовка заказа.
        self.click_to_element(MainPageLocators.LOCATOR_PLACE_AN_ORDER)  # Оформление заказа.