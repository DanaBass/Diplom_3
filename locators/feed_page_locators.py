from selenium.webdriver.common.by import By

class FeedPageLocators:
    FEED_PAGE_TEXT_ELEMENT = By.XPATH, "//div[@class='OrderFeed_orderFeed__2RO_j']//h1[text()='Лента заказов']"
    ORDER_ELEMENT_CLASS = By.XPATH, "//a[contains(@class, 'OrderHistory_link__1iNby')]"
    ORDER_DETAILS_ELEMENT = By.XPATH, "//div[contains(@class, 'Modal_orderBox__1xWdi') and contains(@class, 'Modal_modal__contentBox__sCy8X') and contains(@class, 'p-10')]"
    TOTAL_ORDERS_COUNTER = By.XPATH, '//p[contains(@class, "OrderFeed_number__2MbrQ") and contains(@class, "text_type_digits-large")]'
    CURRENT_DAY_ORDERS_COUNTER = By.XPATH, "//p[contains(@class, 'OrderFeed_number__2MbrQ')]"

    @staticmethod
    def get_order_number_element(order_number: str):
        return By.XPATH, f"//p[contains(@class, 'text') and contains(@class, 'text_type_digits-default') and text()='{order_number}']"

    @staticmethod
    def get_order_number_at_work(order_number: str):
        return By.XPATH, f"//li[contains(@class, 'text') and contains(@class, 'text_type_digits-default') and contains(@class, 'mb-2') and text()='{order_number}']"
