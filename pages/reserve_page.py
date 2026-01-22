from selenium.webdriver.common.by import By

class ReservePage:
    HEADER = (By.CSS_SELECTOR, "h3")
    FLIGHT_ROWS = (By.CSS_SELECTOR, "table tbody tr")
    CHOOSE_FIRST = (By.CSS_SELECTOR, "table tbody tr:nth-child(1) input[type='submit']")

    def __init__(self, driver):
        self.driver = driver

    def header_text(self) -> str:
        return self.driver.find_element(*self.HEADER).text

    def flights_count(self) -> int:
        return len(self.driver.find_elements(*self.FLIGHT_ROWS))

    def choose_first_flight(self):
        self.driver.find_element(*self.CHOOSE_FIRST).click()
