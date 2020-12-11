

#Chrome Browser
from select import select

from selenium import webdriver
from selenium.webdriver.support.select import Select

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start_maximized")
chrome_options.add_argument("headless")                           #happening in the background and you wont see the browser comes up
chrome_options.add_argument("ignore-certificate-errors")

#driver = webdriver.Chrome(executable_path="C:\\PythonSelenium\\chromedriver_win32\\chromedriver.exe")  #We need to pass the chrome ,exe so it knows whhere it is to execute it.
driver = webdriver.Chrome(executable_path="C:\\PythonSelenium\\chromedriver_win32\\chromedriver.exe", options=chrome_options)

#driver.maximize_window()
driver.get("https://rahulshettyacademy.com/angularpractice/")

print(driver.title)
print(driver.current_url)                    #Use current_url to ensure your on the correct site. This will validate the site is correct and youll know if it gets hack if it print other than what you expected.

#driver.back()
#driver.refresh()
#driver.close()