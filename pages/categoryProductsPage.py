from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from  selectors.categoryProductsPage import selectors
from appium.webdriver.common.appiumby import AppiumBy
import random

class categoryProductsPage:
    def __init__(self, driver):
        self.driver = driver
    def choose_product_from_the_page(self):
        #use random product that been chose  and use it to create Xpath selector to  click it
        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located(
                (AppiumBy.XPATH, selectors.productsAvailabeAtPage)))
        products=self.driver.find_elements(AppiumBy.XPATH,selectors.productsAvailabeAtPage)
        numberOfProducts=len(products)
        choseProduct= random.randint(2,numberOfProducts) 
        self.driver.find_element(AppiumBy.XPATH,selectors.choseProductIcon.format(choseProduct)).click()


