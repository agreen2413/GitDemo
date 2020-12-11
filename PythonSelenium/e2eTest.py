

#Chrome Browser
from selenium import webdriver

#For testing purposes swap between Chrome and Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(executable_path="C:\\PythonSelenium\\chromedriver_win32\\chromedriver.exe")  #We need to pass the chrome ,exe so it knows whhere it is to execute it.

driver.maximize_window()
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element_by_css_selector("a[href*='shop']").click()

products = driver.find_elements_by_xpath("//div[@class='card h-100']") #highlight all the cards in the page that has diff phones on sale

for product in products:
    #print(product.find_element_by_xpath("div/h4/a").text)
    productName = product.find_element_by_xpath("div/h4/a").text       #This will give you the text like "Blackberry", Nokia" etc


    if productName  == "Blackberry":
        #Then we add this item into the cart by clicking the Add button
        product.find_element_by_xpath("div/button").click()

driver.find_element_by_css_selector("a[class*='btn-primary']").click()   #class* means more than one class but we choose the btn-primary one
driver.find_element_by_xpath("//button[@class='btn btn-success']").click()
driver.find_element_by_id("country").send_keys("United")

#add explicit wait. Explicit wait target only the specific element until it comes up.
wait = WebDriverWait(driver, 7)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "United States of America")))


driver.find_element_by_link_text("United States of America").click()
driver.find_element_by_xpath("//div[@class='checkbox checkbox-primary']").click()
driver.find_element_by_css_selector("[type='submit']").click()

#print(driver.find_element_by_class_name("alert-success").text)
successText = driver.find_element_by_class_name("alert-success").text  #If there is "more than one class name", you can select which class name you want to use. This case i used alert-success
assert "Success! Thank you!" in successText
driver.get_screenshot_as_file("Screenshot.png")

print(driver.title)
print(driver.current_url)                    #Use current_url to ensure your on the correct site. This will validate the site is correct and youll know if it gets hack if it print other than what you expected.

#driver.back()
#driver.refresh()
#driver.close()