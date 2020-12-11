#Implicit, Explicit and Pause

#Chrome Browser
import time
from select import select

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select

#For testing purposes swap between Chrome and Firefox
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(executable_path="C:\\PythonSelenium\\chromedriver_win32\\chromedriver.exe")  #We need to pass the chrome ,exe so it knows whhere it is to execute it.
#driver = webdriver.Firefox(executable_path="C:\\PythonSelenium\\geckodriver.exe")  #We need to pass the chrome ,exe so it knows whhere it is to execute it.

#This code below is how to handle first window tab and click another link that opens another child tab. How selenium knows.
driver.maximize_window()

#Uncomment this code to see how to do autosuggest dropdown
driver.get("https://rahulshettyacademy.com/AutomationPractice")

actionChains = ActionChains(driver)                    #pass the driver as an argument so the driver can see all the methods in ActionChains

menu = driver.find_element_by_id("mousehover")
actionChains.move_to_element(menu).perform()            #So it will hover to "Mouse Hover",without "perform" it will not hover or execute

childMenu = driver.find_element_by_link_text("Reload")    #This is the sub menu of the parent menu "Mouse Hover"
actionChains.move_to_element(childMenu).click().perform()  #Without "perform" method it will not click

print(driver.title)
print(driver.current_url)                    #Use current_url to ensure your on the correct site. This will validate the site is correct and youll know if it gets hack if it print other than what you expected.
#driver.close()



