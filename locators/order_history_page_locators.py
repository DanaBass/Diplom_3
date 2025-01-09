from selenium.webdriver.common.by import By

class OrderHistoryPageLocators:
    ORDER_HISTORY_LIST = By.XPATH, "//div[@class='OrderHistory_orderHistory__qy1VB']"
    ORDER_HISTORY_ITEMS = By.XPATH, "//li[contains(@class, 'OrderHistory_listItem__2x95r') and contains(@class, 'mb-6')]"