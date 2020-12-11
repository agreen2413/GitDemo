

#Chrome Browser
import time
from select import select

from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="C:\\PythonSelenium\\chromedriver_win32\\chromedriver.exe")  #We need to pass the chrome ,exe so it knows whhere it is to execute it.

driver.maximize_window()

#Uncomment this code to see how to do autosuggest dropdown
# driver.get("https://rahulshettyacademy.com/dropdownspractise/")
#
# driver.find_element_by_id("autosuggest").send_keys("ind")
# time.sleep(2)
# countries = driver.find_elements_by_css_selector("li[class='ui-menu-item'] a") #This css syntax will give all the list base on what you type.
#
# print(len(countries))                                                          #len will give me all the list of the countries
#
# for country in countries:
#     if country.text == "India":
#         country.click()
#         break
#
# assert driver.find_element_by_id("autosuggest").get_attribute('value') == 'India'
# #

driver.get("https://www.makemytrip.com/")

driver.find_element_by_css_selector("label[for='fromCity']").click()
time.sleep(2)
driver.find_element_by_css_selector("input[placeholder='From']").send_keys("del")

cities = driver.find_elements_by_css_selector("p[class*='blackText']") #class* means there is more than one class but choose 'blackText' class. Will give you the list of all cities in blackText color

print(len(cities))                                                     #len will give me all the list of the countries

for city in cities:
    if city.text == "Del Rio, United States":
        city.click()
        break

driver.find_element_by_xpath("//p[text()='Delhi, 'India']").click()




message = driver.find_element_by_class_name("alert-success").text                #This is to find the element by class name. The Success text above after clicking the Submit button
assert "success" in message

print(driver.title)
print(driver.current_url)                    #Use current_url to ensure your on the correct site. This will validate the site is correct and youll know if it gets hack if it print other than what you expected.

#driver.back()
#driver.refresh()
#driver.close()