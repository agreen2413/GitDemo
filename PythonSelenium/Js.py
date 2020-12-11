
#Chrome Browser
import time
from select import select

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="C:\\PythonSelenium\\chromedriver_win32\\chromedriver.exe")  #We need to pass the chrome ,exe so it knows whhere it is to execute it.
#driver = webdriver.Firefox(executable_path="C:\\PythonSelenium\\geckodriver.exe")  #We need to pass the chrome ,exe so it knows whhere it is to execute it.

#This code below is how to handle first window tab and click another link that opens another child tab. How selenium knows.
driver.maximize_window()

#Js DOM can access and objects / elements in the html web page just like selenium.
#Selenium has a method to execute javascript code in it.
#Note In selenium you can not use ex. print(driver.find_element_by_name("name").text to print the text whatever you pass on the send_key.
#So if you want to see the text entered on the text box by using send_keys use the "get_attribute("value")" coming from javascript DOM family

driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element_by_name("name").send_keys("Hello")

print(driver.find_element_by_name("name").get_attribute("value"))                   #print hello by using get_attribute("value") to see whet you pass one send_keys using "selenium"
print(driver.execute_script('return document.getElementsByName("name")[0].value'))  #print hello using pure javascript DOM.

shopButton = driver.find_element_by_css_selector("a[href*='shop']")                 #click the shop button on top of the page
driver.execute_script('arguments[0].click();', shopButton)                          #arguments[0] is the shopButton, if more than one arguments then arguments[1] so on
driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")              #using javascript and DOM to scroll, 0 representing top of page

assert "Hello" == driver.find_element_by_name("name").get_attribute("value")

print(driver.title)
print(driver.current_url)                    #Use current_url to ensure your on the correct site. This will validate the site is correct and youll know if it gets hack if it print other than what you expected.
#driver.close()



