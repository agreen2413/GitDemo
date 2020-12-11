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
driver.get("https://chercher.tech/practice/practice-pop-ups-selenium-webdriver")

actionChains = ActionChains(driver)     #pass the driver as an argument so the driver can see all the methods in ActionChains

#actionChains.context_click(driver.find_element_by_id("double-click")).perform()  #This will right click
actionChains.double_click(driver.find_element_by_id("double-click")).perform()  #This will double click.

# #The selenium driver only works for "html" but not in javascript to handle alert messages in web applications that have Java alert messages. Below code is how to grab alerts
alert = driver.switch_to.alert
#print(alert.text)                          #print the text in the alert message box

alertText = alert.text                      #print the text in the alert message box
assert "You double clicked me!!!, You got to be kidding me" == alertText
alert.accept()                              #click th OK button to close the message box

print(driver.title)
print(driver.current_url)                    #Use current_url to ensure your on the correct site. This will validate the site is correct and youll know if it gets hack if it print other than what you expected.
#driver.close()




