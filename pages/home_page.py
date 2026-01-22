from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class HomePage:
    URL = "https://blazedemo.com/"

    DEPARTURE = (By.NAME, "fromPort")
    DESTINATION = (By.NAME, "toPort")
    FIND_FLIGHTS = (By.CSS_SELECTOR, "input[type='submit']")

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.URL)

    def select_departure(self, city: str):
        Select(self.driver.find_element(*self.DEPARTURE)).select_by_visible_text(city)

    def select_destination(self, city: str):
        Select(self.driver.find_element(*self.DESTINATION)).select_by_visible_text(city)

    def find_flights(self):
        self.driver.find_element(*self.FIND_FLIGHTS).click()
