import allure
import pytest
from data.urls import UrlsContainer
from locators.feed_page_locators import FeedPageLocators
from locators.main_page_locators import MainPageLocators
from pages.feed_page import FeedPage
from pages.constructor_page import ConstructorPage
from pages.profile_page import ProfilePage
import re


class TestFeedPage:
    @allure.title('Переход в конструктор после клика по ссылке на конструктор')
    def test_click_constructor_link_element_from_feed_page_switched_to_constructor(self, main_page_with_logged_in_user: ConstructorPage):
        main_page_with_logged_in_user.go_to_order_feed()
        main_page_with_logged_in_user.go_to_constructor()

        create_order_button = main_page_with_logged_in_user.find_element_with_wait(MainPageLocators.LOCATOR_PLACE_AN_ORDER)

        assert create_order_button is not None

    @allure.title('Клик по заказу открывает детальную информацию о нём')
    def test_click_to_order_opens_detailed_order_page(self, feed_page_with_logged_in_user):
        last_created_order = feed_page_with_logged_in_user.find_all_elements_with_wait(FeedPageLocators.ORDER_ELEMENT_CLASS)[0]
        last_created_order.click() # Кликаем по последнему заказу в ленте заказов.
        order_details_element = feed_page_with_logged_in_user.find_element_with_wait(FeedPageLocators.ORDER_DETAILS_ELEMENT) # Ищем всплывающее окно с деталями заказа.

        assert  order_details_element is not None

    @allure.title('Заказы из истории заказов отображаются в ленте заказов')
    def test_orders_from_order_history_shows_at_feed_page(self, main_page_with_logged_in_user):
        main_page_with_logged_in_user.prepare_order() # Подготовка бургера перед заказом.
        main_page_with_logged_in_user.click_to_element(MainPageLocators.LOCATOR_PLACE_AN_ORDER) # Оформление заказа.

        main_page_with_logged_in_user.click_to_element(MainPageLocators.CLOSE_DETAILED_WINDOW_BUTTON)
        # Ожидание, пока элемент точно не пропадёт после закрытия.
        main_page_with_logged_in_user.wait_until_element_disappears(MainPageLocators.DETAILS_WINDOW_ELEMENT)

        main_page_with_logged_in_user.go_to_personal_account() # Переход в личный кабинет.

        profile_page = ProfilePage(main_page_with_logged_in_user.driver)
        profile_page.click_to_order_history() # Переход в историю заказов пользователя.

        last_order_number = re.search(r'#\d+', profile_page.get_all_orders_history()[-1].text).group(0) # Получение номера самого актуального заказа.

        profile_page.go_to_order_feed()
        feed_page = FeedPage(profile_page.driver)

        finded_order_from_feed_page = feed_page.get_order_by_number(last_order_number)

        assert finded_order_from_feed_page is not None, f'Не удалось найти заказ {last_order_number} из профиля пользователя в ленте заказов!'

    @allure.title('После создания заказа его номер появляется в списке "В работе"')
    def test_create_new_order_number_of_order_shows_at_work(self, feed_page_with_logged_in_user: FeedPage):
        feed_page_with_logged_in_user.open_new_tab(UrlsContainer.MAIN_PAGE_URL)
        feed_page_with_logged_in_user.create_order()  # Создаём новый заказ.
        feed_page_with_logged_in_user.wait_until_condition(lambda condition: str(9999) not in feed_page_with_logged_in_user.find_element_with_wait(MainPageLocators.ORDER_CREATED_INFORMATION).text)
        order_number = re.search(r'(\d+)', feed_page_with_logged_in_user.find_element_with_wait(MainPageLocators.ORDER_CREATED_INFORMATION).text).group(1)

        driver = feed_page_with_logged_in_user.driver
        # Переключаемся на вкладку с лентой заказов.
        driver.switch_to.window(driver.window_handles[0])
        # Ждём, пока заказ не появится "в работе".
        finded_order = feed_page_with_logged_in_user.find_element_with_wait(FeedPageLocators.get_order_number_at_work(order_number))

        assert finded_order is not None, f'Созданный заказ с номером {order_number} не найден в списке "В работе" в ленте заказов!'


    @pytest.mark.parametrize(
        # Сразу проверяем два счётчика - общий и за день.
        "counter_locator", [FeedPageLocators.TOTAL_ORDERS_COUNTER, FeedPageLocators.CURRENT_DAY_ORDERS_COUNTER]
    )
    @allure.title('После создания заказа счётчик заказов увеличивается')
    def test_create_new_order_total_orders_counter_increased(self, feed_page_with_logged_in_user: FeedPage, counter_locator: str):
        # Получаем значение счётчика до создания заказа.
        counter_before_order_creating = int(feed_page_with_logged_in_user.find_element_with_wait(counter_locator).text)
        # Открываем вкладку для создания заказа.
        feed_page_with_logged_in_user.open_new_tab(UrlsContainer.MAIN_PAGE_URL)
        feed_page_with_logged_in_user.create_order() # Создаём новый заказ.

        feed_page_with_logged_in_user.wait_until_condition(lambda condition: '9999' not in feed_page_with_logged_in_user.find_element_with_wait(MainPageLocators.ORDER_CREATED_INFORMATION).text)

        order_number = re.search(r'(\d+)', feed_page_with_logged_in_user.find_element_with_wait(MainPageLocators.ORDER_CREATED_INFORMATION).text).group(1)

        driver = feed_page_with_logged_in_user.driver
        # Переключаемся на вкладку с лентой заказов.
        driver.switch_to.window(driver.window_handles[0])
        # Ждём, пока заказ не появится "в работе".
        feed_page_with_logged_in_user.wait_until_element_appears(FeedPageLocators.get_order_number_at_work(order_number))
        # Получаем значение счётчика после создания заказа.
        counter_after_order_creating = int(feed_page_with_logged_in_user.find_element_with_wait(counter_locator).text)

        assert counter_before_order_creating < counter_after_order_creating, f'Ожидалось, что после создания заказа общий счётчик заказов увеличится!'