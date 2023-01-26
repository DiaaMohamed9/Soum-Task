from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from  selectors.categoryProductsCardsPage import selectors
from appium.webdriver.common.appiumby import AppiumBy
import random,re

class categoryProductsCardsPage:
    def __init__(self, driver):
        self.driver = driver
        self.choseProductCard=0
    def choose_product_card_from_the_page(self):
        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located(
                (AppiumBy.XPATH, selectors.theProductCardsList)))
        products=self.driver.find_elements(AppiumBy.XPATH,selectors.theProductCardsList)
        numberOfProducts=len(products)
        self.choseProductCard= random.randint(1,numberOfProducts) 

    def get_the_chose_product_old_price(self):
        #use random product that been set by  choose_product_card_from_the_page and use it to create Xpath selector to get the old product price 
        return  int(re.findall("\d+",self.driver.find_element(AppiumBy.XPATH,selectors.theProductOldPrice.format(self.choseProductCard)).text)[0])
    def get_the_chose_product_new_price(self):
        #use random product that been set by  choose_product_card_from_the_page and use it to create Xpath selector to get the new product price 
        return  int(re.findall("\d+",self.driver.find_element(AppiumBy.XPATH,selectors.theProductNewPrice.format(self.choseProductCard)).text)[0])
    def get_the_chose_product_discount_amount(self):
        #use random product that been set by  choose_product_card_from_the_page and use it to create Xpath selector to get the discount  amount 
        return  int(re.findall("\d+",self.driver.find_element(AppiumBy.XPATH,selectors.discountAmount.format(self.choseProductCard)).text)[0])
    def click_on_the_chose_product_card(self):
        self.driver.find_element(AppiumBy.XPATH,selectors.theProductNewPrice.format(self.choseProductCard)).click()
