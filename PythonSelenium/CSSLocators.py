#Chrome Browser
from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\PythonSelenium\\chromedriver_win32\\chromedriver.exe")  #We need to pass the chrome ,exe so it knows whhere it is to execute it.

driver.maximize_window()
driver.get("https://login.salesforce.com/")

driver.find_element_by_css_selector("#username").send_keys("agreen")      #The '#' is use only for css. CSS fastest locators in selenium
driver.find_element_by_css_selector(".password").send_keys("Hammer12!")   # The "." is only use in css for "classname" attribute when there is multiple class.
driver.find_element_by_css_selector(".password").clear()
driver.find_element_by_link_text("Forgot Your Password?").click()        #To know that it is a "link text" in the html it has the anchor "a"
driver.find_element_by_xpath("//a[text()='Cancel']").click()

print(driver.find_element_by_xpath("//form[@name='login']/div[1]/label").text)  #/div[1] means the first div on the list, could be three div
print(driver.find_element_by_css_selector("form[name='login'] label:nth-child(3)").text)
print(driver.title)
print(driver.current_url)                    #Use current_url to ensure your on the correct site. This will validate the site is correct and youll know if it gets hack if it print other than what you expected.

#driver.back()
#driver.refresh()
driver.close()