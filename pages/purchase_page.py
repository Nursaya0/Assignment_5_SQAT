from selenium.webdriver.common.by import By

class PurchasePage:
    HEADER = (By.CSS_SELECTOR, "h2")
    NAME = (By.ID, "inputName")
    ADDRESS = (By.ID, "address")
    CITY = (By.ID, "city")
    STATE = (By.ID, "state")
    ZIP = (By.ID, "zipCode")
    CARD = (By.ID, "creditCardNumber")
    PURCHASE_BTN = (By.CSS_SELECTOR, "input[type='submit']")

    def __init__(self, driver):
        self.driver = driver

    def header_text(self) -> str:
        return self.driver.find_element(*self.HEADER).text

    def fill_form(self, name="Nursaya B", address="Expo", city="Astana", state="KZ", zip_code="010000", card="4111111111111111"):
        self.driver.find_element(*self.NAME).clear()
        self.driver.find_element(*self.NAME).send_keys(name)
        self.driver.find_element(*self.ADDRESS).clear()
        self.driver.find_element(*self.ADDRESS).send_keys(address)
        self.driver.find_element(*self.CITY).clear()
        self.driver.find_element(*self.CITY).send_keys(city)
        self.driver.find_element(*self.STATE).clear()
        self.driver.find_element(*self.STATE).send_keys(state)
        self.driver.find_element(*self.ZIP).clear()
        self.driver.find_element(*self.ZIP).send_keys(zip_code)
        self.driver.find_element(*self.CARD).clear()
        self.driver.find_element(*self.CARD).send_keys(card)

    def purchase(self):
        self.driver.find_element(*self.PURCHASE_BTN).click()
