from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from  selectors.productdetialsPage import selectors
from appium.webdriver.common.appiumby import AppiumBy
import random,re

class productdetialsPage:
    def __init__(self, driver):
        self.driver = driver
    def wait_the_product_detials_load_page(self):
        # self.driver.find_element(AppiumBy.XPATH,selectors.enterAsGuest)
        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located(
                (AppiumBy.XPATH, selectors.detailsPageLoadListner)))

    def get_the_product_old_price(self):
        return  int(re.findall("\d+",self.driver.find_element(AppiumBy.XPATH,selectors.theProductOldPriceAtProductPage).text)[0])
    def get_the_product_new_price(self):
        return  int(re.findall("\d+",self.driver.find_element(AppiumBy.XPATH,selectors.theProductNewPriceAtProductPage).text)[0])
    def get_the_product_discount_amount(self):
        return  int(re.findall("\d+",self.driver.find_element(AppiumBy.XPATH,selectors.discountAmountAtProductPage).text)[0])
    def get_the_product_final_price(self):
        return  int(re.findall("\d+",self.driver.find_element(AppiumBy.XPATH,selectors.theFinalPriceAtProductPage).text)[0])