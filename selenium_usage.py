from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# 2. Launch a new instance of the browser:
driver = webdriver.Chrome()

# 3.Navigate to the Facebook login page:
driver.get('https://www.facebook.com/')

# 4.Locate the email and password input fields and enter the login information:
email_field = driver.find_element(By.ID, 'email')
# email_field = driver.find_element_by_id('email')
# password_field = driver.find_element_by_id('pass')
password_field = driver.find_element(By.ID, 'pass')

email_field.send_keys('your_email')
password_field.send_keys('your_password')

# 5. Submit the login form:
password_field.send_keys(Keys.RETURN)

# 6.Wait for the login process to complete (for example, by waiting for a specific element on the next page to load):
driver.implicitly_wait(10000)  # wait up to 10 seconds for an element to appear