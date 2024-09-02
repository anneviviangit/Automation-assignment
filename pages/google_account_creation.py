from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def setup_driver():
    """Set up the Chrome WebDriver."""
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    return driver

def navigate_to_signup(driver):
    """Navigate to the Google sign-up page."""
    driver.get("https://accounts.google.com/signup")

def fill_signup_form(driver, first_name, last_name, month, day, year, gender_value):
    """Fill out the Google account creation form."""
    wait = WebDriverWait(driver, 10)

    # Fill first name and last name
    first_name_field = wait.until(EC.presence_of_element_located((By.ID, "firstName")))
    first_name_field.send_keys(first_name)

    last_name_field = driver.find_element(By.ID, "lastName")
    last_name_field.send_keys(last_name)

    click_next_button(driver)

    # Fill in the date of birth
    month_field = driver.find_element(By.ID, "month")
    month_field.send_keys(month)

    day_field = driver.find_element(By.ID, "day")
    day_field.send_keys(str(day))

    year_field = driver.find_element(By.ID, "year")
    year_field.send_keys(str(year))

    # Select gender
    gender_field = driver.find_element(By.ID, "gender")
    gender_field.send_keys(gender_value)

    click_next_button(driver)

def use_existing_email(driver, existing_email):
    """Select the option to use an existing email and input the email address."""
    wait = WebDriverWait(driver, 10)
    try:
        # Click the link or button to use an existing email address
        use_existing_email_radio = wait.until(
            EC.presence_of_element_located((By.XPATH, "(//div[@role='radio'])[2]"))
        )
        use_existing_email_radio.click()
        email_field = wait.until(EC.presence_of_element_located((By.ID, "username")))
        email_field.send_keys(existing_email)
        click_next_button(driver)
    except Exception as e:
        print(f"An error occurred while using the existing email: {e}")

def click_next_button(driver):
    """Click the 'Next' button."""
    next_button = driver.find_element(By.XPATH, "//button[@jsname='LgbsSe']")
    next_button.click()
    time.sleep(2)
def fill_password(driver, password):
    """Fill in the password and confirm the password."""
    wait = WebDriverWait(driver, 10)

    # Locate the Password field and input the password
    password_field = wait.until(EC.presence_of_element_located((By.NAME, "Passwd")))
    password_field.send_keys(password)

    # Locate the Confirm Password field and input the same password
    confirm_password_field = wait.until(EC.presence_of_element_located((By.NAME, "ConfirmPasswd")))
    confirm_password_field.send_keys(password)

    click_next_button(driver)

def enter_phone_number(driver, phone_number):
    """Enter the phone number where the verification code will be sent."""
    wait = WebDriverWait(driver, 10)

    # Wait for the phone number field to be present and input the phone number
    phone_number_field = wait.until(EC.presence_of_element_located((By.ID, "phoneNumberId")))
    phone_number_field.send_keys(phone_number)

    click_next_button(driver)

def click_next_button(driver):
    """Click the 'Next' button."""
    next_button = driver.find_element(By.XPATH, "//button[@jsname='LgbsSe']")
    next_button.click()
    time.sleep(2)

def main():
    """Main function to run the script."""
    driver = None
    try:
        driver = setup_driver()
        navigate_to_signup(driver)
        fill_signup_form(driver, "Anne", "Vivian", "August", 25, 2000, "FEMALE")
        use_existing_email(driver, "existing.email@example.com")  
        fill_password(driver, "YourPassword123") 
        enter_phone_number(driver, "717174114")  
        submit_form(driver)
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        if driver:
            driver.quit()

if __name__ == "__main__":
    main()
