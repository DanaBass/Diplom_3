from selenium.webdriver.common.by import By

class MainPageLocators:
    LOCATOR_PLACE_AN_ORDER = By.XPATH, './/button[text()="Оформить заказ"]'  # Кнока "Оформить заказ", видна только зарегистрированным пользователям.
    LOCATOR_PERSONAL_ACCOUNT = By.XPATH, "//p[text()='Личный Кабинет']"  # Вход в личный кабинет.
    CONSTRUCTOR_LINK_ELEMENT = By.XPATH, "//a[@class='AppHeader_header__link__3D_hX' and @href='/']"
    ORDER_FEED_LINK_ELEMENT = By.XPATH, "//a[contains(@class, 'AppHeader_header__link__3D_hX') and contains(., 'Лента Заказов')]"
    DETAILS_WINDOW_ELEMENT = By.XPATH, "//div[contains(@class, 'Modal_modal__container__Wo2l_')]"
    INGREDIENT_REFERENCES_FOR_DETAILS = By.XPATH, "//a[contains(@class, 'BurgerIngredient_ingredient__1TVf6') and contains(@class, 'ml-4') and contains(@class, 'mr-4') and contains(@class, 'mb-8')]"
    CLOSE_DETAILED_WINDOW_BUTTON = By.XPATH, "//button[contains(@class, 'Modal_modal__close_modified__3V5XS') and contains(@class, 'Modal_modal__close__TnseK')]"
    CART_ELEMENT = By.XPATH, "//div[contains(@class, 'constructor-element') and contains(@class, 'constructor-element_pos_top')]"
    INGREDIENT_COUNTER = "//p[contains(@class, 'counter_counter__num__3nue1')]"
    ORDER_CREATED_INFORMATION = By.XPATH, "//div[contains(@class, 'Modal_modal__container__Wo2l_')]"