# Assignment 5 (PyTest, Python) – BlazeDemo UI Automation

**System under test:** https://blazedemo.com (Approved list: Booking/Reservation)

## Requirements Coverage
1) **Test lifecycle management**: setup/teardown implemented with PyTest fixture (`tests/conftest.py`)
2) **Logging**: Python `logging` with file output (`logs/automation.log`)
3) **HTML report**: `pytest-html` (`reports/report.html`)
4) **Screenshots on failure**: automatic capture + attach to HTML report (`reports/screenshots/`)
5) **Minimum 3 test cases**: 3 automated test cases included

## Project Structure
```
Assignment_5_PyTest_BlazeDemo/
├── requirements.txt
├── pytest.ini
├── README.md
├── logs/                 (generated)
├── reports/              (generated)
├── pages/
│   ├── __init__.py
│   ├── home_page.py
│   ├── reserve_page.py
│   └── purchase_page.py
└── tests/
    ├── __init__.py
    ├── conftest.py
    └── test_blazedemo.py
```

## Install
```bash
python -m pip install -r requirements.txt
```

## Run tests + generate HTML report
```bash
python -m pytest
```

## Outputs
- HTML report: `reports/report.html`
- Screenshots on failure: `reports/screenshots/`
- Log file: `logs/automation.log`
