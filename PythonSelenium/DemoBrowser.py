from selenium import webdriver

#Every browswer has an executable file.
#Through Selenium test, we need to invoke that executable file that will invoke the right browser we want.

#Chrome Browser
driver = webdriver.Chrome(executable_path="C:\\PythonSelenium\\chromedriver_win32\\chromedriver.exe")  #We need to pass the chrome ,exe so it knows whhere it is to execute it.

#Firefox Browser
#driver = webdriver.Firefox(executable_path="C:\\PythonSelenium\\geckodriver.exe")  #We need to pass the chr

#IE Browser
#driver = webdriver.Ie(executable_path="C:\\PythonSelenium\\IEDriverServer.exe")  #We need to pass the chr

driver.maximize_window()
driver.get("https://rahulshettyacademy.com/")

print(driver.title)
print(driver.current_url)                    #Use current_url to ensure your on the correct site. This will validate the site is correct and youll know if it gets hack if it print other than what you expected.

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
print(driver.current_url)

driver.back()
driver.refresh()
driver.close()