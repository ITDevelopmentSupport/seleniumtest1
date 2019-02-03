from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(r"C:\Users\cquevedo\PycharmProjects\FirstSeleiumTest\drivers\chromedriver.exe")
driver.set_page_load_timeout(10)
driver.get("http://google.com")
driver.find_element_by_name("q").send_keys("IT Development & Support Inc", Keys.ENTER)
#driver.find_element_by_name("btnK").send_keys(Keys.ENTER)
time.sleep(4)
driver.quit()

