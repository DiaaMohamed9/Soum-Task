from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from  selectors.mainPage import selectors
from appium.webdriver.common.appiumby import AppiumBy

class mainPage:
    def __init__(self, driver):
        self.driver = driver
    def skip_the_onBoarding(self):
        # 
        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located(
                (AppiumBy.XPATH, selectors.skipAtTheOnBoarding))).click()
    def cancel_referral(self):
        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located(
                (AppiumBy.XPATH, selectors.calcelTheReferral))).click()
    def choose_mobile_category(self):
        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located(
                (AppiumBy.XPATH, selectors.mobileCategoryMainPage))).click()