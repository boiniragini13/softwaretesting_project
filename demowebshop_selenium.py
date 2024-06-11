import time

from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=opts)

driver.get("https://demowebshop.tricentis.com/")
time.sleep(2)


driver.find_element('xpath', '//a[text() ="Register"]').click()
time.sleep(1)
driver.find_element('xpath', '//input[@id="gender-female"]').click()
driver.find_element('xpath', '//input[@id="FirstName"]').send_keys('ragini')
driver.find_element('xpath', '//input[@id="LastName"]').send_keys('boini')
driver.find_element('xpath', '//input[@id ="Email"]').send_keys('raginiboini01@gmail.com')
driver.find_element('xpath', '//input[@id ="Password"]').send_keys('passWord123')
driver.find_element('xpath', '//input[@id="ConfirmPassword"]').send_keys('passWord123')
driver.find_element('xpath', '//input[@id="register-button"]').click()
time.sleep(2)
driver.find_element('xpath', '//a[text()="Log out"]').click()



driver.find_element('xpath', '//a[text()="Log in"]').click()
time.sleep(2)
driver.find_element('xpath', '//input[@id="Email"]').send_keys('raginiboini01@gmail.com')
driver.find_element('xpath', '//input[@id="Password"]').send_keys('passWord123')
driver.find_element('xpath', '//input[@value="Log in"]').click()
time.sleep(2)



driver.find_element('xpath', '//input[@id="small-searchterms"]').send_keys('gift card')
time.sleep(1)
driver.find_element('xpath', '//input[@class="button-1 search-box-button"]').click()
time.sleep(1)
driver.find_element('xpath', '(//input[@value="Add to cart"])[1]').click()
time.sleep(1)


driver.find_element('xpath', '//input[@class="recipient-name"]').send_keys('lilly')
time.sleep(1)
driver.find_element('xpath', '//input[@class="button-1 add-to-cart-button"]').click()
time.sleep(1)
driver.find_element('xpath', '//a[text()="Shopping cart"]').click()
time.sleep(1)
driver.find_element('xpath', '//select[@id="CountryId"]').click()
time.sleep(2)
driver.find_element('xpath', '//option[text()="Canada"]').click()
time.sleep(2)
driver.find_element('xpath', '//input[@id="termsofservice"]').click()
time.sleep(1)
driver.find_element('xpath', '//button[@id="checkout"]').click()
time.sleep(1)


driver.find_element('xpath', '//select[@id="BillingNewAddress_CountryId"]').click()
time.sleep(1)
driver.find_element('xpath', '//option[text()="Canada"]').click()
time.sleep(1)
driver.find_element('xpath', '//input[@id="BillingNewAddress_City"]').send_keys('pune')
time.sleep(1)
driver.find_element('xpath', '//input[@id="BillingNewAddress_Address1"]').send_keys('laxmi')
time.sleep(1)
driver.find_element('xpath', '//input[@id="BillingNewAddress_ZipPostalCode"]').send_keys('500321')
time.sleep(1)
driver.find_element('xpath', '//input[@id="BillingNewAddress_PhoneNumber"]').send_keys('963258741')
time.sleep(1)
driver.find_element('xpath', '//input[@onclick="Billing.save()"]').click()
time.sleep(2)
driver.find_element('xpath', '(//input[@class="button-1 new-address-next-step-button"])[2]').click()
time.sleep(1)
driver.find_element('xpath', '//input[@class="button-1 shipping-method-next-step-button"]').click()
time.sleep(1)
driver.find_element('xpath', '//input[@class="button-1 payment-method-next-step-button"]').click()
time.sleep(1)
driver.find_element('xpath', '//input[@class="button-1 payment-info-next-step-button"]').click()
time.sleep(1)
driver.find_element('xpath', '//input[@class="button-1 confirm-order-next-step-button"]').click()


















