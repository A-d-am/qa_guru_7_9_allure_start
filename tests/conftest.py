import pytest
from selene import browser


@pytest.fixture(autouse=True)
def driver_management():
    browser.config.base_url = 'https://github.com'
    browser.config.window_height = 1080
    browser.config.window_width = 1920

    yield

    browser.quit()