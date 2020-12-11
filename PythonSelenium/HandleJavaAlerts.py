

#Chrome Browser
import time
from select import select

from selenium import webdriver
from selenium.webdriver.support.select import Select

validateText = "Option3"
#For testing purposes swap between Chrome and Firefox
driver = webdriver.Chrome(executable_path="C:\\PythonSelenium\\chromedriver_win32\\chromedriver.exe")  #We need to pass the chrome ,exe so it knows whhere it is to execute it.
#driver = webdriver.Firefox(executable_path="C:\\PythonSelenium\\geckodriver.exe")  #We need to pass the chrome ,exe so it knows whhere it is to execute it.

driver.maximize_window()

#Uncomment this code to see how to do autosuggest dropdown
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

driver.find_element_by_css_selector("#name").send_keys("Option3")                 #If it has an id, you can use # in CSS only
driver.find_element_by_id("alertbtn").click()                                     #click the alert button

# #The selenium driver only works for html but not in javascript to handle alert messages in web applications that have Java alert messages. Below code is how to grab alerts
alert = driver.switch_to.alert
#print(alert.text)                          #print the text in the alert message box

alertText = alert.text                      #print the text in the alert message box
assert validateText in alertText            #validate to make sure that the word "Option3" exist in the pop up message box
alert.accept()                              #click th OK button to close the message box


