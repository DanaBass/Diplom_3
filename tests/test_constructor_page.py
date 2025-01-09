import allure

from locators.feed_page_locators import FeedPageLocators
from locators.main_page_locators import MainPageLocators
from pages.constructor_page import ConstructorPage


class TestConstructorPage:
    @allure.title('По клику на ссылку "Лента заказов" происходит переход на неё')
    def test_click_at_feed_element_from_constructor_go_to_feed_page(self, main_page_with_logged_in_user: ConstructorPage):
        main_page_with_logged_in_user.go_to_order_feed()

        feed_page_text_element = main_page_with_logged_in_user.find_element_with_wait(FeedPageLocators.FEED_PAGE_TEXT_ELEMENT)

        assert feed_page_text_element is not None

    @allure.title('По клику на ингридиент открывается окно с детальной информацией по нему')
    def test_click_on_ingredient_shows_detailed_window(self, main_page_with_logged_in_user: ConstructorPage):
        main_page_with_logged_in_user.open_first_ingredient_details()
        ingredient_detailed_window = main_page_with_logged_in_user.find_element_with_wait(MainPageLocators.DETAILS_WINDOW_ELEMENT)

        assert ingredient_detailed_window is not None

    @allure.title('По клику на закрытие детального окна ингридиента оно закрывается')
    def test_click_on_close_button_from_opened_detailed_window_closes_it(self, main_page_with_logged_in_user: ConstructorPage):
        main_page_with_logged_in_user.open_first_ingredient_details()

        main_page_with_logged_in_user.click_to_element(MainPageLocators.CLOSE_DETAILED_WINDOW_BUTTON)
        # Ожидание, пока элемент точно не пропадёт после закрытия.
        main_page_with_logged_in_user.wait_until_element_disappears(MainPageLocators.DETAILS_WINDOW_ELEMENT)

        ingredient_detailed_window = main_page_with_logged_in_user.find_element_with_wait(MainPageLocators.DETAILS_WINDOW_ELEMENT, 0.5)

        assert ingredient_detailed_window is None

    @allure.title('Счётчик на ингридиенте при его переносе в корзину увеличивается')
    def test_drag_ingredient_to_cart_counter_at_ingridient_increases(self, main_page_with_logged_in_user: ConstructorPage):
        fisrt_ingredient = main_page_with_logged_in_user.get_all_existing_ingredients()[0] # Получение первого имеющегося ингридиента.
        counter_element = main_page_with_logged_in_user.find_child_element_by_xpath(fisrt_ingredient, MainPageLocators.INGREDIENT_COUNTER)
        counter_value_before_moving = int(counter_element.text) # Получение значения счётчика ингридиента ДО переноса в корзину для сборки.
        cart_element = main_page_with_logged_in_user.find_element_with_wait(MainPageLocators.CART_ELEMENT)
        main_page_with_logged_in_user.drag_and_drop_element(fisrt_ingredient, cart_element) # Перенос ингридиента в корзину для сборки.
        counter_value_after_moving = int(counter_element.text)

        assert counter_value_before_moving < counter_value_after_moving, 'Счётчик ингредиента после переноса не увеличился!'

    @allure.title('Авторизованный пользователь может создать заказ')
    def test_logged_in_user_can_create_order(self, main_page_with_logged_in_user: ConstructorPage):
        main_page_with_logged_in_user.click_to_element(MainPageLocators.LOCATOR_PLACE_AN_ORDER)
        order_created_info_element = main_page_with_logged_in_user.find_element_with_wait(MainPageLocators.ORDER_CREATED_INFORMATION)

        assert order_created_info_element is not None
