from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Path to your chromedriver.exe
chrome_driver_path = r"C:\Users\91969\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe"
service = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=service)

wait = WebDriverWait(driver, 10)

# ----------------------
# Open the login page
# ----------------------
driver.get("https://practicetestautomation.com/practice-test-login/")
driver.maximize_window()

# ----------------------
# Test Case 1: Positive Login
# ----------------------
driver.find_element(By.ID, "username").send_keys("student")
driver.find_element(By.ID, "password").send_keys("Password123")
driver.find_element(By.ID, "submit").click()

# Wait for the success page to load
wait.until(EC.url_contains("logged-in-successfully"))
heading = wait.until(EC.presence_of_element_located((By.TAG_NAME, "h1")))
heading_text = heading.text
print("🔍 Heading found:", heading_text)

assert "Logged In Successfully" in heading_text, "❌ Success message not found"

assert driver.find_element(By.LINK_TEXT, "Log out").is_displayed(), "❌ Logout button not visible"

print("✅ Positive Login Test Passed")

# Go back to login page
driver.get("https://practicetestautomation.com/practice-test-login/")
time.sleep(2)

# ----------------------
# Test Case 2: Invalid Username
# ----------------------
driver.find_element(By.ID, "username").clear()
driver.find_element(By.ID, "password").clear()

driver.find_element(By.ID, "username").send_keys("incorrectUser")
driver.find_element(By.ID, "password").send_keys("Password123")
driver.find_element(By.ID, "submit").click()

# Wait for error message
error_msg = wait.until(EC.visibility_of_element_located((By.ID, "error"))).text
assert "Your username is invalid!" in error_msg, "❌ Error message mismatch for invalid username"
print("✅ Negative Username Test Passed")

# ----------------------
# Test Case 3: Invalid Password
# ----------------------
driver.find_element(By.ID, "username").clear()
driver.find_element(By.ID, "password").clear()

driver.find_element(By.ID, "username").send_keys("student")
driver.find_element(By.ID, "password").send_keys("incorrectPassword")
driver.find_element(By.ID, "submit").click()

error_msg = wait.until(EC.visibility_of_element_located((By.ID, "error"))).text
assert "Your password is invalid!" in error_msg, "❌ Error message mismatch for invalid password"
print("✅ Negative Password Test Passed")

# ----------------------
# Close browser
# ----------------------
driver.quit()
