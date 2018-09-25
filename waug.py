#-*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.alert import Alert

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

WAITTIME = 500
SLEEPSEC = 5
LOOP = 3 # -1 for infinite

#ipacktour : http://ipacktour.com
#ipack_HOMEPAGE = "http://ipacktour.com/user/login"
#ipack_ITEMURL = "http://ipacktour.com/product/detail/view/2018042600002"

outof_stock_URL = "http://www.ipacktour.com"

waug_HOMEPAGE = "https://www.waug.com/main"
waug_hk_dl_ITEMURL = "https://www.waug.com/good/?idx=104500"
waug_sin_uss_ITEMURL = "https://www.waug.com/good/?idx=105851"

USER_CON = ["","Brown","Robinson","Thompson","Wright","Walker","White","Davies","Edwards"]
USER = USER_CON[7]
USERID = USER + "@poongsung.me"
PASSWORD = "tongsung8116!"
USE_DATE = str(int(time.strftime("%d"))+2)
F_NAME = USER
L_NAME = USER[0]
MD_PHONE = "7251"
LT_PHONE = "8121"




def login(driver):
    #push the "login button" at main page
    login_btn = driver.find_element_by_link_text("로그인")
    login_btn.click()
    #send ID information at ID space
    driver.find_element_by_xpath("//*[@id='mem_id']").send_keys(USERID)
    driver.find_element_by_xpath("//*[@id='mem_pwd']").send_keys(PASSWORD)
    #click the login button
    driver.find_element_by_xpath("//*[@id='frm-login']/button").click()

    #now we can next stage, product page

def coupon_check(driver):
    coupon_btn = driver.find_element_by_xpath("//*[@id='download-coupon']/div/div[2]")
    if coupon_btn is None:
        print "No Coupon"
    else:
        coupon_btn.click()
        Alert(driver).accept()
        print "Coupon is saved"



def checkStock(driver):
    stock_check = driver.find_element_by_css_selector(".goodtitle-direct-imgsize img")
    if stock_check is None:
        print "there is out of stock"
        driver.get(outof_stock_URL)
    else:
        #True
        print "wow good job"
        coupon_check(driver)




def checkOpt(driver):
    #print '날짜 설정'
    #WebDriverWait(driver, 10).until(
     #   EC.presence_of_element_located((By.XPATH, "/html/body/div[9]/div[1]/table/tbody/tr[4]/td[4]"))).click()
    driver.find_element_by_xpath("//*[@id='s_date']").click()
    WebDriverWait(driver , 2)
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "td.today"))).click()
    #driver.find_element_by_xpath("//table/tbody/tr/td[@name='today']").click()
    #driver.find_element_by_tag_name('td').find_element_by_class_name('today').click()

    #상품 설정
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='select2-parent_option-container']"))).click()
    #driver.find_element_by_xpath("//*[@id='select2-parent_option-container']").click()
    driver.find_element_by_css_selector("li.select2-results__option:last-child").click()

    #수량설정 1클릭
    driver.find_element_by_css_selector("button.btn.count-up").click()
    driver.find_element_by_css_selector("button.btn.count-up").click()
    driver.find_element_by_css_selector("button.btn.count-up").click()
    driver.find_element_by_css_selector("button.btn.count-up").click()
    driver.find_element_by_css_selector("button.btn.count-up").click()
    driver.find_element_by_css_selector("button.btn.count-up").click()
    driver.find_element_by_css_selector("button.btn.count-up").click()
    driver.find_element_by_css_selector("button.btn.count-up").click()
    driver.find_element_by_css_selector("button.btn.count-up").click()
    driver.find_element_by_css_selector("button.btn.count-up").click()


    #예약하기 버튼 클릭
    driver.find_element_by_xpath("//*[@id='btn-order']").click()

def checkout(driver):
    driver.find_element_by_xpath("//*[@id='sec_option_box']/div[5]/div[1]").click()

def order(driver):
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='frm-order-info']/div/div[2]/div[1]/input"))).send_keys(
        F_NAME)
    driver.find_element_by_css_selector("input.widthauto.user-tel-mobile-number").send_keys(MD_PHONE)
    driver.find_element_by_css_selector("input.widthauto.user-tel-mobile-number:last-child").send_keys(LT_PHONE)
    driver.find_element_by_css_selector("input.widthauto.first.order-info-eng-name").send_keys(F_NAME)
    driver.find_element_by_xpath("//*[@id='frm-order-info']/div/div[2]/div[3]/input[2]").send_keys(L_NAME)

    #입력완료 버튼 클릭
    driver.find_element_by_css_selector("button#btn-info-write").click()

def payment(driver):
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='content']/form/div/div[2]/div/div[2]/div[1]/div/div/div/div/div[3]/div/label/p"))).click()
    WebDriverWait(driver, 2)
    driver.find_element_by_xpath("//*[@id='chk-order-agree']").click()
   # driver.find_element_by_xpath("//*[@id='btn-modal-coupon']").click()
    #포인트 사용
    WebDriverWait(driver, 2)
    driver.find_element_by_xpath("/html/body/div[1]/div[4]/form/div/div[2]/div/div[2]/div[2]/div/div/div/div[2]/div[2]/button").click()
   #구매버튼
    WebDriverWait(driver, 2)
    driver.find_element_by_xpath("//*[@id='btn-order-pay']").click()
    #chk_coupon = driver.find_element_by_partial_link_text('USS')
    #chk_coupon = WebDriverWait(driver, 10).until(
    #    EC.presence_of_element_located((By.XPATH,"//div[@data-idx = '143056']//span"))).text()
    #chk_coupon = driver.find_element_by_xpath("//div[@data-idx = '143056']//span").text()
    #if chk_coupon == "USS7000":
    #    print "fuck no uss700 coupon"
 #   else:
   #     get_coupon.click()
    #    driver.find_element_by_xpath("//*[@id='btn-apply-coupon']").click()

def eticket(driver):
    WebDriverWait(driver, 10000).until(
        EC.presence_of_element_located((By.XPATH,
                                        "/html/body/div[1]/div[4]/div/div[2]/div[3]/div[2]/a"))).click()
    WebDriverWait(driver, 100).until(
        EC.presence_of_element_located((By.XPATH,
                                        "/html/body/div[1]/div[4]/div/div/div/div[3]/div[1]/div[1]/div[2]"))).click()

    #티켓클릭
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH,
                                        "/html/body/div[1]/div[4]/div[1]/div/div/div[3]/div/div[11]/div[1]/a/div"))).click()
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH,
                                        "/html/body/div[1]/div[4]/div[1]/div/div/div[3]/div/div[11]/div[2]/a/div"))).click()
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH,
                                        "/html/body/div[1]/div[4]/div[1]/div/div/div[3]/div/div[11]/div[3]/a/div"))).click()
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH,
                                        "/html/body/div[1]/div[4]/div[1]/div/div/div[3]/div/div[11]/div[4]/a/div"))).click()
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH,
                                        "/html/body/div[1]/div[4]/div[1]/div/div/div[3]/div/div[11]/div[5]/a/div"))).click()
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH,
                                        "/html/body/div[1]/div[4]/div[1]/div/div/div[3]/div/div[11]/div[6]/a/div"))).click()
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH,
                                        "/html/body/div[1]/div[4]/div[1]/div/div/div[3]/div/div[11]/div[7]/a/div"))).click()
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH,
                                        "/html/body/div[1]/div[4]/div[1]/div/div/div[3]/div/div[11]/div[8]/a/div"))).click()
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH,
                                        "/html/body/div[1]/div[4]/div[1]/div/div/div[3]/div/div[11]/div[9]/a/div"))).click()
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH,
                                        "/html/body/div[1]/div[4]/div[1]/div/div/div[3]/div/div[11]/div[10]/a/div"))).click()



if __name__ == "__main__":
    driver = webdriver.Firefox()
    driver.wait = WebDriverWait(driver, 2)

    driver.get(waug_HOMEPAGE)

    login(driver)
    driver.get(waug_sin_uss_ITEMURL)
  #  checkStock(driver)
    #coupon_check(driver)
    #driver.wait
    checkOpt(driver)
    order(driver)
    payment(driver)
    eticket(driver)
    #i = 1
    #while(checkStock(driver, i)):
    #    i += 1
     #   time.sleep(SLEEPSEC)
      #  if (i > LOOP and LOOP != -1):
       #     break
        #driver.get(ITEMURL)

    #checkout(driver)

   # order(driver)