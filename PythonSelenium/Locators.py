

#Chrome Browser
from select import select

from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="C:\\PythonSelenium\\chromedriver_win32\\chromedriver.exe")  #We need to pass the chrome ,exe so it knows whhere it is to execute it.

driver.maximize_window()
driver.get("https://rahulshettyacademy.com/angularpractice/")
#driver.find_element_by_name("name").send_keys("Rahul")                           #This is to find the element by name locator
driver.find_element_by_css_selector("input[name='name']").send_keys(("Rahul"))    #This is to find the element by css locator
driver.find_element_by_id("exampleCheck1").click()                                #This is to find the element by id locator. This is the checkbox

dropdown = Select(driver.find_element_by_id("exampleFormControlSelect1"))         #Use Select class for static dropdown. Import Select package
dropdown.select_by_visible_text("Female")
dropdown.select_by_index(0)

driver.find_element_by_xpath("//input[@type='submit']").click()                   #This is to find the element by xpath locator. The Submit button

message = driver.find_element_by_class_name("alert-success").text                #This is to find the element by class name. The Success text above after clicking the Submit button
assert "success" in message

print(driver.title)
print(driver.current_url)                    #Use current_url to ensure your on the correct site. This will validate the site is correct and youll know if it gets hack if it print other than what you expected.

#driver.back()
#driver.refresh()
#driver.close()