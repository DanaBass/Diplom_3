from selenium.webdriver.common.by import By

class ProfilePageLocators:
    PROFILE_ELEMENT = By.XPATH, "//a[@class='Account_link__2ETsJ text text_type_main-medium text_color_inactive Account_link_active__2opc9' and @href='/account/profile']"
    LOGOUT_BUTTON = By.XPATH, "//button[contains(text(), 'Выход')]"
    ORDER_HISTORY_LINK = By.XPATH, "//a[contains(@class, 'Account_link__2ETsJ') and contains(@class, 'text_type_main-medium') and contains(@class, 'text_color_inactive') and text()='История заказов']"