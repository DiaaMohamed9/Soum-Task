import pytest
from appium import webdriver

@pytest.fixture(scope='session')
def appium_driver():
    desired_caps = {
            "platformName": "Android",
            "deviceName": "emulator-5554",
            "appPackage": "com.soum.sa",
            "newCommandTimeout":"60000",
            # "app": r"\build\VIP.apk",
            "appActivity": ".MainActivity",
            'autoGrantPermissions' :'true'
        }
    return webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
