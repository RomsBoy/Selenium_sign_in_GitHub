import time
import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome('../chromedriver.exe')  #choose your path
driver.get("https://github.com/")

assert "GitHub" in driver.title
elem = driver.find_element_by_xpath("/html/body/div[1]/header/div/div[2]/div[2]/a[1]")
elem.click()

assert "Sign in" in driver.title

login=driver.find_element_by_id("login_field")
login.send_keys(sys.argv[1])

password=driver.find_element_by_id("password")
password.send_keys(sys.argv[2])


driver.find_element_by_name("commit").click()


time.sleep(10)

driver.close()


