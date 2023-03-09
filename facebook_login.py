from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

try:
    # Launch a new instance of the browser
    driver = webdriver.Chrome()

    # Navigate to the Facebook login page
    driver.get('https://www.facebook.com/')

    # Locate the email and password input fields and enter the login information
    email_field = driver.find_element(By.ID, 'email')
    password_field = driver.find_element(By.ID, 'pass')

    email_field.send_keys('inspiration9595@gmail.com')
    password_field.send_keys('Mercedec-benc!')
    password_field.submit()

    # Wait for the login process to complete
    wait = WebDriverWait(driver, 100)
    wait.until(EC.url_changes('https://www.facebook.com/'))

except Exception as e:
    print('An error occurred:', e)
finally:
    # Close the browser
    driver.quit()
