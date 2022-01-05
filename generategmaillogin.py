from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome()
driver.maximize_window()
driver.delete_all_cookies()
driver.get("http://www.gmail.com")
driver. find_element_by_id("Ident ifierId" ).send_keys( "++++++++++++++++@GMAIL.COM")
time.sleep(2)
driver.find_element_by_xpath('//*[@id=".identifyifierNext"]/div/button/div[2 1').click()
time.sleep(3)
driver.find_element_by_name("password").send_keys("+++++++++")
time.sleep(3)
driver.find_element_by_xpath('//*[ @id="passwordNext" ]/div/button/div [2]').click()
time.sleep(3)
driver.close()
print("Gmail login has been successfully completed")