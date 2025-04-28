from appium import webdriver
from appium.options.android import UiAutomator2Options
import pytest


capabilities = dict(
    platformName='Android',
    automationName='uiautomator2',
    deviceName='988e5036485152374c',
    platformVersion = "9",
    appPackage='com.instagram.android',
)


capabilities_options = UiAutomator2Options().load_capabilities(capabilities)

appium_server_url = 'http://localhost:4723'


@pytest.fixture()
def driver():
    driver = webdriver.Remote(appium_server_url, options=capabilities_options)
    yield driver
    driver.terminate_app('com.instagram.android')
    driver.quit()