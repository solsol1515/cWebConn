
from selenium import webdriver

usr = ''
pwd = ''

# 1. webdriver 객체 생성
driver = webdriver.Chrome('./webdriver/chromedriver.exe')
driver.implicitly_wait(3)

driver.get("http://www.facebook.com")

email = driver.find_element_by_id('email')
pwd = driver.find_element_by_id('pass')

email.send_keys(usr)        # 아이디
pwd.send_keys(pwd)          # 비밀번호

btn = driver.find_element_by_name('login')
btn.click()
driver.implicitly_wait(2)