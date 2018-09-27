#-*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.alert import Alert
import os
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

USER_CON = ["North","Parkes","Humphries","Mellor","Carey","Ingram","Summers","Leonard","Young","Griffiths"]
USER = USER_CON[8]
USERID = USER + "@poongsung.me"
PASSWORD = "tongsung8116!"

F_NAME = USER
L_NAME = USER[0]
MD_PHONE = "7251"
LT_PHONE = "8121"


driver = webdriver.Chrome('\Users\owner\macro\chromedriver')
driver.implicitly_wait(3)
driver.get('https://www.waug.com/main')

driver.fullscreen_window()
login_btn = driver.find_element_by_xpath("//*[@id='navbar']/div/a[1]")
login_btn.click()
driver.find_element_by_xpath("//*[@id='mem_id']").send_keys(USERID)
driver.find_element_by_xpath("//*[@id='mem_pwd']").send_keys(PASSWORD)
    #click the login button
driver.find_element_by_xpath("//*[@id='frm-login']/button").click()
WebDriverWait(driver, 1000000).until(EC.presence_of_element_located((By.XPATH, "//*[@id='content']/div/div/div/div[3]/div[1]/div[1]"))).click()
    #이티켓 클릭 커멘드
WebDriverWait(driver, 0.5).until(EC.presence_of_element_located((By.XPATH, "//*[@id='content']/div[1]/div/div/div[3]/div/div[11]/div[1]"))).click()
driver.find_element_by_xpath("//*[@id='content']/div[1]/div/div/div[3]/div/div[11]/div[2]").click()
driver.find_element_by_xpath("//*[@id='content']/div[1]/div/div/div[3]/div/div[11]/div[3]").click()
driver.find_element_by_xpath("//*[@id='content']/div[1]/div/div/div[3]/div/div[11]/div[4]").click()
driver.find_element_by_xpath("//*[@id='content']/div[1]/div/div/div[3]/div/div[11]/div[5]").click()
driver.find_element_by_xpath("//*[@id='content']/div[1]/div/div/div[3]/div/div[11]/div[6]").click()
driver.find_element_by_xpath("//*[@id='content']/div[1]/div/div/div[3]/div/div[11]/div[7]").click()
driver.find_element_by_xpath("//*[@id='content']/div[1]/div/div/div[3]/div/div[11]/div[8]").click()
driver.find_element_by_xpath("//*[@id='content']/div[1]/div/div/div[3]/div/div[11]/div[9]").click()
driver.find_element_by_xpath("//*[@id='content']/div[1]/div/div/div[3]/div/div[11]/div[1]").click()

os.system('dir')
#WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.XPATH, "//*[@id='content']/div[1]/div/div/div[3]/div/div[11]/div[1]"))).click()
#WebDriverWait(driver, 0.1).until(EC.presence_of_element_located((By.XPATH, "//*[@id='content']/div[1]/div/div/div[3]/div/div[11]/div[2]"))).click()
#WebDriverWait(driver, 0.1).until(EC.presence_of_element_located((By.XPATH, "//*[@id='content']/div[1]/div/div/div[3]/div/div[11]/div[3]"))).click()
#WebDriverWait(driver, 0.1).until(EC.presence_of_element_located((By.XPATH, "//*[@id='content']/div[1]/div/div/div[3]/div/div[11]/div[4]"))).click()
#WebDriverWait(driver, 0.1).until(EC.presence_of_element_located((By.XPATH, "//*[@id='content']/div[1]/div/div/div[3]/div/div[11]/div[5]"))).click()
#WebDriverWait(driver, 0.1).until(EC.presence_of_element_located((By.XPATH, "//*[@id='content']/div[1]/div/div/div[3]/div/div[11]/div[6]"))).click()
#WebDriverWait(driver, 0.1).until(EC.presence_of_element_located((By.XPATH, "//*[@id='content']/div[1]/div/div/div[3]/div/div[11]/div[7]"))).click()
#WebDriverWait(driver, 0.1).until(EC.presence_of_element_located((By.XPATH, "//*[@id='content']/div[1]/div/div/div[3]/div/div[11]/div[8]"))).click()
#WebDriverWait(driver, 0.1).until(EC.presence_of_element_located((By.XPATH, "//*[@id='content']/div[1]/div/div/div[3]/div/div[11]/div[9]"))).click()
#WebDriverWait(driver, 0.1).until(EC.presence_of_element_located((By.XPATH, "//*[@id='content']/div[1]/div/div/div[3]/div/div[11]/div[10]"))).click()


#파이썬으로 파일 다운로드
#url: https://kkamikoon.tistory.com/7
#원도우 cmd 명령어 목록
#url : https://zetawiki.com/wiki/%EC%9C%88%EB%8F%84%EC%9A%B0_CMD_%EB%AA%85%EB%A0%B9%EC%96%B4_%EB%AA%A9%EB%A1%9D
#파이썬으로 cmd 실행
#url : http://mwultong.blogspot.com/2007/01/python-system-exec.html