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
#iframe, frameset, frame     These are the three diff types of frames

driver.get("https://the-internet.herokuapp.com/iframe")

#The following code below are part of the frame
#We have to switch to frame in order to clear the text "Your content goes here." Because this message is "inside the frame." before we can clear it.
driver.switch_to.frame("mce_0_ifr")        #pass either frameid, framename or index value. This case passing the "id"
driver.find_element_by_css_selector("#tinymce").clear()
driver.find_element_by_css_selector("#tinymce").send_keys("I got in and i am able to automate!")

#Now lets print this "An iFrame containing the TinyMCE WYSIWYG Editor" but get out of the frame. This text is not part of the frame
driver.switch_to.default_content()   #This is the method that will bring you back to your normal html browser
print(driver.find_element_by_tag_name("h3").text)

print(driver.title)
print(driver.current_url)                    #Use current_url to ensure your on the correct site. This will validate the site is correct and youll know if it gets hack if it print other than what you expected.
#driver.close()



