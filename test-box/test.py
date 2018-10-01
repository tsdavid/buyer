#-*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import requests
from bs4 import BeautifulSoup

from selenium.webdriver.support.select import Select
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.touch_actions import TouchActions
from selenium.webdriver.common.action_chains import ActionChains
import accounts_vars as ac_var
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

#could not be scrolled into view
#url : https://stackoverflow.com/questions/41744368/scrolling-to-element-using-webdriver/41744591


#ipacktour : http://ipacktour.com
myreal_HOMEPAGE = "https://www.myrealtrip.com/users/sign_in"
myreal_ITEMURL = ["https://www.myrealtrip.com/offers/15441","https://www.myrealtrip.com/offers/21988"]


def login(driver):
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*/input[@name='user[email]']"))).send_keys(
        USERID)
    driver.find_element_by_xpath( "//*/input[@name='user[password]']").send_keys(PASSWORD)
    #driver.execute_script( "//*/input[@name='btn btn-default']")
    login_but = driver.find_element_by_xpath("/html/body/main/div/div/div[3]/form/div/div[4]/button")
    login_but.click()#로그인 버튼 클릭학
    #WebDriverWait(driver, WAITTIME).until(
     #   EC.presence_of_element_located((By.XPATH, "//a[@href='http://ipacktour.com/user/logout']")))



#상품 날짜 옵션 넣기
def checkOpt_date(driver):
    #상품날짜 설정 버튼 클릭
    WebDriverWait(driver, 100).until(EC.presence_of_element_located(
        (By.XPATH, "//*[@id='calendarBtn']"))).click()
    #driver.find_element_by_xpath("//*[@id='calendarBtn']").click()
    #상품날짜 선택
    WebDriverWait(driver, 100).until(EC.presence_of_element_located(
        (By.LINK_TEXT, str(30)))).click()

    #옵션선택 클릭

    driver.set_script_timeout(70)

    # 상품옵션 설정 버튼 클릭
    # driver.implicitly_wait(1000)
    WebDriverWait(driver, 100).until(EC.presence_of_element_located(
        (By.XPATH,
         "/html/body/main/section/div[2]/div[1]/div[2]/div[3]/div/div[1]/div/div[2]/div/div[3]/div[1]"))).click()
    # driver.find_element_by_class_name("peoplepicker-container").click()


    # driver.implicitly_wait(1000)
    # 상품 수량 체크하기

    ########테스트 함수 성공성공성공성공성공성공
def test_info(driver):

    driver.implicitly_wait(1000)
    driver.set_script_timeout(50)



    felement = driver.find_element_by_xpath(
        "//*[@id='optionBtn']/div[3]"
    )

    actions = ActionChains(driver)
    actions.move_to_element(felement).perform()




    driver.implicitly_wait(1000)
    driver.set_script_timeout(50)

    element = driver.find_element_by_xpath(
        "//*[@id='optionBtn']/div[4]/div/div/div[2]/div/div/div/span[4]/button"
    )

    actions = ActionChains(driver).click()
    actions.move_to_element(element).perform()

    i = 0
    while i < 4:
        element.click()
        i += 1
    #driver.execute_script("arguments[0].scrollIntoView();", element)




    #driver.set_script_timeout(2)
    WebDriverWait(driver, 100).until(EC.presence_of_element_located((
        By.XPATH, "//*[@id='checkPriceBtn']/button"
    ))).click()




    #driver.implicitly_wait(1000)
    #driver.set_script_timeout(50)
    time.sleep(1)
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH,
         "/html/body/main/section/div[2]/div[1]/div[2]/div[3]/div/div[2]/form/div[2]/div/div[2]/button"
                                                                                ))).click()
    ########테스트 함수 성공성공성공성공성공성공

#뷰티플수프로 마이페이지에 있는 html 데이터를 가지고와
#그래서 그거로 싱가폴인지 홍콩인지 구분해
#그리고 이용일로 구분을 해
#두 조건에 맞는 걸로 셀리옴으로 클릭해서 들어가든 , bs4로 href 따서 들어가든 // 그냥 selenium으로 들어가야
#로그인 정보가 유지될듯
#거기에서 티켓 함수로 가는거지
#오키?
#내일 할수 있게씾?
#내일의 너를 믿는다 새꺄
#일단 현재 url을 가지고온다
#bs4로 url의 html을 파싱한다
#파싱한 html에서 지역 , 날짜를 분류한다
#해당하는 기준에 부합하는 url로 넘어간다

def test_ticket(driver):
    web_url = driver.current_url
    print(web_url)

    req = requests.get(web_url)
    html = req.text
    
    soup = BeautifulSoup(html, 'html.parser')
    #print soup.find({"div":"info"})



if __name__ == "__main__":
    number = input("what account do you want to buy : ")
    USER = ac_var.myreal_users[number]
    USER_DM = ac_var.myreal_user_domain[number]
    USERID = USER + USER_DM
    PASSWORD = "tongsung8116!"



    #구매 과정 시작
    driver = webdriver.Firefox()
    driver.wait = WebDriverWait(driver, 2)
        #기다림
    driver.implicitly_wait(10)
        #메인 홈페이지
    driver.get(myreal_HOMEPAGE)
    login(driver)
    driver.get("https://www.myrealtrip.com/traveler/reservations/ongoing")
    test_ticket(driver)


        #상품 URL
    #driver.get(myreal_ITEMURL[1])
        #상품 날짜 정보
    #checkOpt_date(driver)
        #상품 나이 정보
    #driver.set_script_timeout(10)
    #test_info(driver)