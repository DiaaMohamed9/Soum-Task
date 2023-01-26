import pytest
from  pages.mainPage import *
from  pages.categoryProductsPage import *
from  pages.categoryProductsCardsPage import *
from  pages.productdetialsPage import *
import time

def test_soum_mobile_category(appium_driver):
    #test the flow if you want bay device from the mobile category at Soum
    mainPageObj=mainPage(appium_driver)
    categoryProductsPageObj=categoryProductsPage(appium_driver)
    categoryProductsCardsPageObj=categoryProductsCardsPage(appium_driver)
    productdetialsPageObj=productdetialsPage(appium_driver)
    mainPageObj.skip_the_onBoarding()
    mainPageObj.cancel_referral()
    mainPageObj.choose_mobile_category()
    categoryProductsPageObj.choose_product_from_the_page()
    categoryProductsCardsPageObj.choose_product_card_from_the_page()
    oldPriceFromCardsListPage=categoryProductsCardsPageObj.get_the_chose_product_old_price()
    newPriceFromCardsListPage=categoryProductsCardsPageObj.get_the_chose_product_new_price()
    theDiscountFromCardsListPage=categoryProductsCardsPageObj.get_the_chose_product_discount_amount()
    categoryProductsCardsPageObj.click_on_the_chose_product_card()
    # assert oldPriceFromCardsListPage-newPriceFromCardsListPage==theDiscountFromCardsListPage #make sure the disount that appear is correct 
    productdetialsPageObj.wait_the_product_detials_load_page()
    oldPriceFromProductDetialsPage=productdetialsPageObj.get_the_product_old_price()
    newPriceFromProductDetialsPage=productdetialsPageObj.get_the_product_new_price()
    theDiscountFromProductDetialsPage=productdetialsPageObj.get_the_product_discount_amount()
    finalPriceFromProductDetialsPage=productdetialsPageObj.get_the_product_final_price()
    assert oldPriceFromCardsListPage==oldPriceFromProductDetialsPage
    assert newPriceFromProductDetialsPage==newPriceFromCardsListPage
    assert theDiscountFromProductDetialsPage==theDiscountFromCardsListPage
    assert finalPriceFromProductDetialsPage==newPriceFromProductDetialsPage
    time.sleep(1)
