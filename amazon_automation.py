from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

options = webdriver.ChromeOptions() 
options.add_experimental_option("detach",True)
driver = webdriver.Chrome(options)
driver.maximize_window()

# open Amazon
driver.get("https://www.amazon.in/")
time.sleep(3)

# login
sign_in = driver.find_element(By.ID,"nav-link-accountList") 
sign_in.click()
time.sleep(2)

# enter email /phoneno.
driver.find_element(By.ID,"ap_email").send_keys("your_email_here")
driver.find_elements(By.ID,"continue").click()
time.sleep(2)

# password
driver.find_element(By.ID,"ap_password").send_keys("your_password_here")
driver.find_element(By.ID,"signInSubmit").click()
time.sleep(3)

# search product
search_box = driver.find_element(By.ID,"twotabsearchtextbox")
search_box.send_keys("laptop")
search_box.send_keys(Keys.RETURN)
time.sleep(3)

first_product = driver.find_element(By.XPATH,"//span[@class='a-size-medium a-color-base a-text-normal']")
first_product.click()
time.xleep(3)
driver.switch_to.windoow(driver.window_handles[1])

# add to cart
driver.find_element(By.ID,"add-to-cart-button").click()
time.sleep(3)

# checkout
try:
    checkout_buton =driver.find_element(By.NAME,"proceedToRetailCheckout")
except:
    try:
        checkout_button = driver.find_element(By.ID,"sc-buy-box-ptc-button")
    except:
        print("Checkout button not found")
        print("Maybe Amazon is asking for OTP, address,or payment")
        print("Script will wait until you fix it manuallyin browser")
        input("Press ENTER here in the terminal after completing OTP/address/payment")
        checkout_button = driver.find_element(By.NAME,"proceedToRetailCheckout")
checkout_button.click()
time.sleep(5)
print("reached paymentpage(simulation only, no payment made)")        

        
