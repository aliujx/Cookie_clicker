from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

chrome_driver_path = "/home/julia/Programs/Chrome-driver/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("http://orteil.dashnet.org/experiments/cookie/")
cookie_click = driver.find_element_by_id("cookie")

money = int(driver.find_element_by_id("money").text)
coockies_second = driver.f


#five_sec = time.time() + 5
#while five_sec:
    #cookie_click.click()

# 5 minutes from now
#while True:
    #test = 0
   # if test == 5 or time.time() > timeout:
      #  break
   # test = test - 1
