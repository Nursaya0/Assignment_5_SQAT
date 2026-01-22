import os
import logging
import pytest
from datetime import datetime

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# ---------- Logging (file) ----------
def _configure_logger():
    os.makedirs("logs", exist_ok=True)
    logger = logging.getLogger("automation")
    logger.setLevel(logging.INFO)

    if logger.handlers:
        return logger

    fmt = logging.Formatter("%(asctime)s [%(levelname)s] %(name)s - %(message)s")

    fh = logging.FileHandler("logs/automation.log", encoding="utf-8")
    fh.setLevel(logging.INFO)
    fh.setFormatter(fmt)

    sh = logging.StreamHandler()
    sh.setLevel(logging.INFO)
    sh.setFormatter(fmt)

    logger.addHandler(fh)
    logger.addHandler(sh)
    return logger

LOGGER = _configure_logger()


# ---------- PyTest lifecycle management ----------
@pytest.fixture
def driver():
    LOGGER.info("SETUP: start browser")
    os.makedirs("reports/screenshots", exist_ok=True)

    headless = os.environ.get("HEADLESS", "false").lower() == "true"
    options = Options()
    if headless:
        options.add_argument("--headless=new")
    options.add_argument("--window-size=1400,900")

    d = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    d.implicitly_wait(5)
    d.maximize_window()

    yield d

    LOGGER.info("TEARDOWN: quit browser")
    d.quit()


# ---- Store test reports so we can access them later ----
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)


# ---------- Screenshots on failure + attach to pytest-html ----------
def pytest_runtest_teardown(item, nextitem):
    rep = getattr(item, "rep_call", None)
    if rep is not None and rep.failed:
        drv = item.funcargs.get("driver", None)
        if drv is None:
            return

        ts = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
        name = f"{item.name}_{ts}.png"
        path = os.path.join("reports", "screenshots", name)

        try:
            drv.save_screenshot(path)
            LOGGER.error("FAILURE: screenshot saved to %s", path)

            # attach to pytest-html if available
            try:
                import pytest_html
                extra = getattr(rep, "extra", [])
                extra.append(pytest_html.extras.png(path))
                rep.extra = extra
            except Exception:
                pass
        except Exception as e:
            LOGGER.error("Could not take screenshot: %s", e)


def pytest_configure(config):
    # optional metadata for pytest-html (safe)
    if not hasattr(config, "_metadata") or config._metadata is None:
        config._metadata = {}
    config._metadata["System Under Test"] = "BlazeDemo (https://blazedemo.com)"
    config._metadata["Framework"] = "PyTest + Selenium"
    config._metadata["Logs"] = "logs/automation.log"
