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
myreal_ITEMURL = ["https://www.myrealtrip.com/offers/15441","https://www.myrealtrip.com/offers/15441"]

#waug : https://www.waug.com/main/
#ipack_HOMEPAGE = "http://ipacktour.com/user/login"
#ipack_ITEMURL = "http://ipacktour.com/product/detail/view/2018042600002"

number = 3
USER_LIST = ['esther_01','Collins','Bell','Shaw','Patel']
USER = USER_LIST[number]
USERID = USER+"@poongsung.me"
PASSWORD = "tongsung8116!"

#reserve user info
F_NAME = USER
L_NAME = USER[0]
FULL_NAME = F_NAME + "." +L_NAME
BIRTH_DATE = "881225"
PHONE_NB = "01072518121"


def login(driver):
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*/input[@name='user[email]']"))).send_keys(
        USERID)
    driver.find_element_by_xpath( "//*/input[@name='user[password]']").send_keys(PASSWORD)
    #driver.execute_script( "//*/input[@name='btn btn-default']")
    login_but = driver.find_element_by_xpath("/html/body/main/div/div/div[3]/form/div/div[4]/button")
    login_but.click()#로그인 버튼 클릭학
    #WebDriverWait(driver, WAITTIME).until(
     #   EC.presence_of_element_located((By.XPATH, "//a[@href='http://ipacktour.com/user/logout']")))


def checkOpt(driver):
    #상품날짜 설정 버튼 클릭
    WebDriverWait(driver, 1000).until(EC.presence_of_element_located(
        (By.XPATH, "//*[@id='calendarBtn']"))).click()
    #driver.find_element_by_xpath("//*[@id='calendarBtn']").click()
    #상품날짜 선택
    WebDriverWait(driver, 1000).until(EC.presence_of_element_located(
        (By.LINK_TEXT, "24"))).click()



    # 상품옵션 설정 버튼 클릭
   #driver.implicitly_wait(1000)
    WebDriverWait(driver, 100000).until(EC.presence_of_element_located(
        (By.XPATH, "/html/body/main/section/div[2]/div[1]/div[2]/div[3]/div/div[1]/div/div[2]/div/div[3]/div[1]"))).click()
    #driver.find_element_by_class_name("peoplepicker-container").click()



    # 상품 수량 체크하기
    WebDriverWait(driver, 10000).until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, ".option-box:nth-child(2) .btn.bootstrap-touchspin-up"))).click()
    driver.find_element_by_css_selector(".option-box:nth-child(2) .btn.bootstrap-touchspin-up").click()
    driver.find_element_by_css_selector(".option-box:nth-child(2) .btn.bootstrap-touchspin-up").click()
    driver.find_element_by_css_selector(".option-box:nth-child(2) .btn.bootstrap-touchspin-up").click()


    #driver.find_element_by_css_selector(".input-group-btn:last-child").click()
    #driver.find_element_by_xpath("//span[@name='.bootstrap-touchspin-up']").click()


    #driver.find_element_by_css_selector(".ui-datepicker-current-day").click()


    #금액 조회하기
    WebDriverWait(driver, 200000).until(EC.presence_of_element_located((
        By.XPATH, "//*[@id='checkPriceBtn']/button"
    ))).click()
    #driver.find_element_by_xpath("//*[@id='checkPriceBtn']/button").click()



    #구매하기 버튼
    driver.implicitly_wait(100000000)
    WebDriverWait(driver, 3000000000).until(EC.presence_of_element_located(
        (By.XPATH, "/html/body/main/section/div[2]/div[1]/div[2]/div[3]/div/div[2]/form/div[2]/div/div[2]/button"))).click()


def checkout(driver):
    #update the prices
    driver.find_element_by_xpath("//*[@id='checkPriceBtn']/button").click()
    #purchase btn
    #WebDriverWait(driver, 2)
    driver.implicitly_wait(10)
    driver.execute_script("window.scrollTo(0, 500)")
    buy_btn = driver.find_element_by_xpath("/html/body/main/section/div[2]/div[1]/div[2]/div[3]/div/div[2]/form/div[2]/div/div[2]/button")
    actions = ActionChains(driver)
    actions.move_to_element(buy_btn).click()
    #WebDriverWait(driver, 20).until(
    #    EC.presence_of_element_located((By.XPATH, "/html/body/main/section/div[2]/div[1]/div[2]/div[3]/div/div[2]/form/div[2]/div/div[2]/button/span/img"))).click()
    #WebDriverWait(driver, 0).until(
     #EC.presence_of_element_located((By.LINK_TEXT, "구매하기"))).click()
    #driver.find_element_by_css_selector(".reserve-btn .button:nth-child(1)").click()

def order(driver):
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,"/html/body/main/section/div/form/div[2]/div[1]/div[2]/div/div[2]/div[2]/input"))).send_keys(L_NAME)
    driver.find_element_by_xpath("/html/body/main/section/div/form/div[2]/div[1]/div[2]/div/div[3]/div[2]/input").send_keys(F_NAME)
    driver.find_element_by_xpath("/html/body/main/section/div/form/div[2]/div[1]/div[2]/div/div[4]/div[2]/input").send_keys(FULL_NAME)
    driver.find_element_by_xpath("//*[@id='input-icc']").click()
    driver.find_element_by_xpath("/html/body/main/section/div/form/div[2]/div[1]/div[2]/div/div[5]/div[2]/select/option[2]").click()
    driver.find_element_by_xpath("/html/body/main/section/div/form/div[2]/div[1]/div[2]/div/div[6]/div[2]/input").send_keys(BIRTH_DATE)
    driver.find_element_by_xpath("/html/body/main/section/div/form/div[2]/div[2]/div[2]/div/div[1]/div[2]/div[2]/input").send_keys(PHONE_NB)
    driver.find_element_by_xpath("/html/body/main/section/div/form/div[2]/div[2]/div[2]/div/div[2]/div[2]/div/select").click()
    driver.find_element_by_xpath("/html/body/main/section/div/form/div[2]/div[2]/div[2]/div/div[2]/div[2]/div/select/option[5]").click()
    driver.find_element_by_xpath("/html/body/main/section/div/form/div[2]/div[2]/div[2]/div/div[2]/div[3]/div/select").click()
    driver.find_element_by_xpath("/html/body/main/section/div/form/div[2]/div[2]/div[2]/div/div[2]/div[3]/div/select/option[4]").click()

    driver.find_element_by_xpath("//*[@id='type-wcard']").click()
    driver.find_element_by_xpath("//*[@id='checkbox_terms_traveler']").click()
    driver.find_element_by_xpath("//*[@id='reservation-btn']").click()


    #티켓 받는 곳까지 가는 기다림
    #마이페이지 클릭
    WebDriverWait(driver, 1000).until(EC.presence_of_element_located(
        (By.XPATH,
         "/html/body/div[3]/header/nav/div[1]/div[3]/ul/li[4]/a/img"))).click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.XPATH,
         "/html/body/div[3]/header/nav/div[1]/div[3]/div/ul/li[2]/div[2]"))).click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.XPATH,
         "/html/body/main/div/div[4]/div[2]/div[2]/div/a"))).click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.XPATH,
         "//*[@id='vouchersBtn']"))).click()

def ticket(driver):
    #티켓정보로 넘어가기
    WebDriverWait(driver, 100).until(EC.presence_of_element_located(
        (By.XPATH,
         "/html/body/main/div/div[4]/div/div[2]/div/a"))).click()

    #티켓 클릭
    WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.XPATH,
         "/html/body/main/div/div[4]/div[3]/div/div[1]/div[3]/div[1]/a"))).click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.XPATH,
         "/html/body/main/div/div[4]/div[3]/div/div[1]/div[3]/div[2]/a"))).click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.XPATH,
         "/html/body/main/div/div[4]/div[3]/div/div[1]/div[3]/div[3]/a"))).click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.XPATH,
         "/html/body/main/div/div[4]/div[3]/div/div[1]/div[3]/div[4]/a"))).click()


if __name__ == "__main__":
    #driver = webdriver.Chrome('\Users\owner\macro\chromedriver')
    driver = webdriver.Firefox()
    driver.wait = WebDriverWait(driver, 2)
    driver.implicitly_wait(10)
    #driver.fullscreen_window()
    driver.get(myreal_HOMEPAGE)


    login(driver)
    driver.get(myreal_ITEMURL[0])
    checkOpt(driver)
    #driver.wait
    #checkout(driver)
    order(driver)
    ticket(driver)
    #i = 1
    #while(checkStock(driver, i)):
    #    i += 1
     #   time.sleep(SLEEPSEC)
      #  if (i > LOOP and LOOP != -1):
       #     break
        #driver.get(ITEMURL)



   # order(driver)