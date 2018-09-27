#-*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.touch_actions import TouchActions
from selenium.webdriver.common.action_chains import ActionChains
import myreal as myreal
import waug as waug
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

#transaction mode (구매 횟수를 정해주는 기능)은 차후에 추가하기로
# ch_trans_mode = input("choose trans mode ; 1 = normal , 2 = except")

if __name__ == "__main__":

    ch_company = input("which company do you want to buy? \n "
                       "if you want to buy something from MYREAL = input =>'myreal' \n"
                       " if you want to buy something from WAUG = input =>'waug' \n"
                       ": ")
    ch_item_region = input("choose region  \n"
                           " HONGKONG = 'hk' \n"
                           " SINGAPORE = 'sin'\n"
                           ":")

    driver = webdriver.Firefox()
    driver.wait = WebDriverWait(driver, 2)


    if ch_company == 1:
        driver.get(myreal_HOMEPAGE)
        myreal.login(driver)
        if ch_item_region == 1:
            driver.get(myreal_ITEMURL[ch_item_region])
        elif ch_item_region == 2:
            driver.get(myreal_ITEMURL[ch_item_region])
        else:
            print ("No such items")
        myreal.checkOpt(driver)
        myreal.order(driver)
        myreal.ticket(driver)
    elif ch_company == 2:
        driver.get(waug_HOMEPAGE)
        waug.login(driver)
        if ch_item_region == 1:
            driver.get(waug_ITEMURL[ch_item_region])
        elif ch_item_region == 2:
            driver.get(waug_ITEMURL[ch_item_region])
        else:
            print ("No such items")

        waug.checkOpt(driver)
        waug.order(driver)
        waug.payment(driver)
        waug.eticket(driver)
    else :
        print ("We don't have data about that company")