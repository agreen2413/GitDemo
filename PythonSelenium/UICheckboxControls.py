

#Chrome Browser
import time
from select import select

from selenium import webdriver
from selenium.webdriver.support.select import Select

#For testing purposes swap between Chrome and Firefox
driver = webdriver.Chrome(executable_path="C:\\PythonSelenium\\chromedriver_win32\\chromedriver.exe")  #We need to pass the chrome ,exe so it knows whhere it is to execute it.
#driver = webdriver.Firefox(executable_path="C:\\PythonSelenium\\geckodriver.exe")  #We need to pass the chrome ,exe so it knows whhere it is to execute it.

driver.maximize_window()

#Uncomment this code to see how to do autosuggest dropdown
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
checkboxList = driver.find_elements_by_xpath("//input[@type='checkbox']")                 #Give you the list of all the checkboxes

print(len(checkboxList))                                                                  #len will giove me the total count of the checkbox

for checkbox in checkboxList:                                                             #Click all the checkboxes. For radio button you cant loop as you cant select all radio buttons
    #print(checkbox.get_attribute("value"))                                               #print what the attrtbute value looks like

    if checkbox.get_attribute("value") == "option2":
        checkbox.click()
        assert checkbox.is_selected()                                                     #asset will add validation whether checkbox is selected or not. if not it will throw assertion error


radioButtons = driver.find_elements_by_name("radioButton")

print(len(radioButtons))

radioButtons[2].click()
assert radioButtons[2].is_selected()                                                      #We do the radio buttons this way as we cant use for loop as we cant check all radio buttons
                                                                                          #Will check the 3rd radio button as index starts at 0


#Code below is to show how to validate whether a text box that shows a message or has a message is visible or not
#Note: assert always return or expect to return "true"
assert driver.find_element_by_id("displayed-text").is_displayed()                        #if its displayed returns true, if not returns false. By default its there

driver.find_element_by_id("hide-textbox").click()                                         #Hide the textbox that display the message.

#Note: Use assert not if you expect it to return false, otherwise test case will fail
assert not driver.find_element_by_id("displayed-text").is_displayed()                     #This will return false cause the textbox that has message is not displayed