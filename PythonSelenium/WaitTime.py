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

list = []
list2 = []

driver = webdriver.Chrome(executable_path="C:\\PythonSelenium\\chromedriver_win32\\chromedriver.exe")  #We need to pass the chrome ,exe so it knows whhere it is to execute it.
#driver = webdriver.Firefox(executable_path="C:\\PythonSelenium\\geckodriver.exe")  #We need to pass the chrome ,exe so it knows whhere it is to execute it.

driver.implicitly_wait(5)
# #implicit target the entire steps
# #Wait until 5 sec if object is not displayed
# #Global wait
# #If it takes 1.5 sec to display, it will not use the remaining 3.5 sec. execution will resume.

driver.maximize_window()

#Uncomment this code to see how to do autosuggest dropdown
driver.get("https://rahulshettyacademy.com/seleniumPractise/")

driver.find_element_by_css_selector("input.search-keyword").send_keys("ber")     #Will return the pictures that is type berries
time.sleep(4)                                                                    #time class belongs to Python and not selenium webdriver
driver.find_elements_by_xpath("//div[@class='products']/div")                    #Traverse from parent to child.. Parent = //div[@class='products'] child is /div
count = len(driver.find_elements_by_xpath("//div[@class='products']/div"))       #print the total counts of the items
assert count == 3                                                                #assert will pass if count is 3 if not it will fail

AddToCartButtons = driver.find_elements_by_xpath("//div[@class='product-action']/button")

for Button in AddToCartButtons:                                                   #iterate to all the AddToCart buttons using for loop
    list.append(Button.find_element_by_xpath("parent::div/parent::div/h4").text)  #traverse from parent to child so we can grab the text of the items. Only xpath can traverse
    Button.click()                                                                #Click ALL the AddToCart buttons
print(list)

driver.find_element_by_css_selector("img[alt='Cart']").click()                    #Click the bag icon or image
driver.find_element_by_xpath("//button[text()='PROCEED TO CHECKOUT']").click()    #Click the proceed to checkout button

#add explicit wait. Explicit wait target only the specific element until it comes up.
wait = WebDriverWait(driver, 6)
wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "promoCode")))                       #Wait till the promo code text box is present

items = driver.find_elements_by_css_selector("p.product-name")                                                  #get the list of the items

for item in items:                                                                                              #iterate through the items
    list2.append(item.text)

print(list2)
assert list == list2                                                                                            #Compare and validate that the text in list is the same and equal as in list2
originalDiscount = driver.find_element_by_css_selector(".discountAmt").text                                     #grab the discount text before applying the discount

driver.find_element_by_class_name("promoCode").send_keys("rahulshettyacademy")                                  #Enter your promo code
driver.find_element_by_css_selector(".promoBtn").click()                                                        #click promo button, it has a "class" of .promoBtn so we can use "."

wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "span.promoInfo")))

discountAmount = driver.find_element_by_css_selector(".discountAmt").text                                        #grab the discount text before applying the discount
assert float(discountAmount) < int(originalDiscount)                                                             #The discout is a floating number and original is an int

print(driver.find_element_by_css_selector("span.promoInfo").text)                                                #grab the text that you below after successfully applying the promoCode

amounts = driver.find_elements_by_xpath("//tr/td[5]/p")
discountAmount
sum = 0

for amount in amounts:
    sum = sum + int(amount.text)

print(sum)

totalAmount = int(driver.find_element_by_class_name("totAmt").text)
assert sum == totalAmount





