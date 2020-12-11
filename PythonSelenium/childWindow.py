#Implicit, Explicit and Pause

#Chrome Browser
import time
from select import select

from selenium import webdriver
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
driver.get("https://the-internet.herokuapp.com/windows")
driver.find_element_by_link_text("Click Here").click()

#("parentid, childid")
#The code below is to handle when there is another tab or windows open.

childWindow = driver.window_handles[1]             #child window, how you handle when you click a link and open another tab
driver.switch_to.window(childWindow)
print(driver.find_element_by_tag_name("h3").text)  #child window
driver.close()                                     #close the child window

driver.switch_to.window(driver.window_handles[0])  #parent window. go back to first tab again.
assert "Opening a new window" == driver.find_element_by_tag_name("h3").text         #parent window

print(driver.title)
print(driver.current_url)                    #Use current_url to ensure your on the correct site. This will validate the site is correct and youll know if it gets hack if it print other than what you expected.
#driver.close()



