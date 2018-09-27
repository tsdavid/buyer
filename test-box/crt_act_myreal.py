#-*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.touch_actions import TouchActions
from selenium.webdriver.common.action_chains import ActionChains
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

#could not be scrolled into view
#url : https://stackoverflow.com/questions/41744368/scrolling-to-element-using-webdriver/41744591
WAITTIME = 500
SLEEPSEC = 5
LOOP = 3 # -1 for infinite

#ipacktour : http://ipacktour.com
myreal_HOMEPAGE = "https://www.myrealtrip.com/users/sign_in"
myreal_sigup = "https://www.myrealtrip.com/users/sign_up"
myreal_ITEMURL = ["https://www.myrealtrip.com/offers/15441","https://www.myrealtrip.com/offers/15441"]

crt_user = []

number = 0
USER_LIST = ["Brown","Robinson","Thompson","Wright","Walker","White","Davies","Edwards","Hughes","Green","Hall","Lewis","esther_01","Collins",
                    "Bell","Shaw","Murphy","Miller","evans","Harris","Clarke","Patel","Jackson","Wood","Johnson","Turner","Martin","Cooper","Hill",
                    "Ward","jones","Morris","Moore","Clark","Lee","King","taylor","Baker","Harrison","Morgan","Allen","James","thomas",
                "Scott","Phillips","Watson","Davis","Parker","williams","Price","Bennett","Young","Griffiths", "Mtchell", "wilson",
                "Kelly","Cook","Carter","Richardson","Bailey"

             ]
USER = crt_user[number]
USERID = USER+"@poongsung.me"
PASSWORD = "tongsung8116!"

#reserve user info
F_NAME = USER
L_NAME = USER[0]
FULL_NAME = F_NAME + "." +L_NAME
BIRTH_DATE = "881225"
PHONE_NB = "01072518121"


def singup(driver):
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "/html/body/main/div/form/div/div[3]/div/div[1]/div/div[2]/div/input"))).send_keys(USER)
    driver.find_element_by_xpath("/html/body/main/div/form/div/div[3]/div/div[2]/div/div[2]/div/input").send_keys(USERID)
    driver.find_element_by_xpath("/html/body/main/div/form/div/div[3]/div/div[3]/div/div[2]/div/input").send_keys(PASSWORD)
    driver.find_element_by_xpath("/html/body/main/div/form/div/div[3]/div/div[4]/div/div[2]/div/input").send_keys(PASSWORD)

    #약관동의
    driver.find_element_by_xpath("//*[@id='checkAll']").click()
    driver.find_element_by_xpath("//*[@id='checkLocation']").click()
    #driver.find_element_by_xpath("//*[@id='checkMarketingAll']").click()

    #회원가입 버튼
    WebDriverWait(driver, 5).until(EC.presence_of_element_located(
        (By.XPATH, "/html/body/main/div/form/div/div[3]/div/div[6]/button"))).click()


    #팝업 버튼
    WebDriverWait(driver, 15).until(EC.presence_of_element_located(
        (By.XPATH, "/html/body/div[13]/div[7]/button"))).click()

    # 이메일 인증 버튼
    WebDriverWait(driver, 1500).until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, "div.tab:nth-child(2)"))).click()
    WebDriverWait(driver, 1500).until(EC.presence_of_element_located(
        (By.XPATH, "//*[@id='send-verify-email-btn']"))).click()



if __name__ == "__main__":
    driver = webdriver.Firefox()
    driver.wait = WebDriverWait(driver, 2)
    driver.implicitly_wait(10)
    #driver.fullscreen_window()
    driver.get(myreal_sigup)

    singup(driver)

