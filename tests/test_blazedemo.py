import logging
import pytest
from selenium.webdriver.common.by import By

from pages.home_page import HomePage
from pages.reserve_page import ReservePage
from pages.purchase_page import PurchasePage

LOGGER = logging.getLogger("automation")

@pytest.mark.smoke
def test_tc01_search_flights(driver):
    """TC-01: Search flights should open reserve page with results"""
    LOGGER.info("TC-01 START: search flights")
    home = HomePage(driver)
    home.open()

    LOGGER.info("Step: select departure and destination")
    home.select_departure("Boston")
    home.select_destination("London")
    home.find_flights()

    reserve = ReservePage(driver)
    LOGGER.info("Checkpoint: header contains selected cities")
    assert "Boston" in reserve.header_text()
    assert "London" in reserve.header_text()
    assert reserve.flights_count() > 0
    LOGGER.info("TC-01 END: pass")


def test_tc02_choose_flight_opens_purchase_page(driver):
    """TC-02: Choosing a flight should open purchase page"""
    LOGGER.info("TC-02 START: choose flight")
    home = HomePage(driver)
    home.open()
    home.select_departure("Paris")
    home.select_destination("Rome")
    home.find_flights()

    reserve = ReservePage(driver)
    assert reserve.flights_count() > 0

    LOGGER.info("Step: choose first available flight")
    reserve.choose_first_flight()

    purchase = PurchasePage(driver)
    LOGGER.info("Checkpoint: purchase page header is displayed")
    assert "reserved" in purchase.header_text().lower()
    LOGGER.info("TC-02 END: pass")


def test_tc03_complete_purchase_shows_confirmation(driver):
    """TC-03: Completing purchase should show confirmation page"""
    LOGGER.info("TC-03 START: complete purchase")
    home = HomePage(driver)
    home.open()
    home.select_departure("San Diego")
    home.select_destination("New York")
    home.find_flights()

    reserve = ReservePage(driver)
    reserve.choose_first_flight()

    purchase = PurchasePage(driver)
    LOGGER.info("Step: fill passenger details and purchase")
    purchase.fill_form(name="Student A", address="Street 1", city="Astana", state="KZ", zip_code="010000", card="4111111111111111")
    purchase.purchase()

    LOGGER.info("Checkpoint: confirmation header appears")
    # Confirmation page has <h1>Thank you for your purchase today!</h1>
    h1 = driver.find_element(By.TAG_NAME, "h1").text.lower()
    assert "thank you" in h1
    LOGGER.info("TC-03 END: pass")
