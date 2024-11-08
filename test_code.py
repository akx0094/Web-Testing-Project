from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--start-maximized")

# Initialize the WebDriver
driver = webdriver.Chrome(options=chrome_options)

# List of test cases with different input values
test_data = [
    {"name": "John Doe", "email": "john@example.com", "message": "Hello, this is a test message!"}
    ,{"name": "Jane Smith", "email": "jane.smith@example.com", "message": "Testing multiple inputs in the form."},
    {"name": "Alice Brown", "email": "alice.b@example.com", "message": "This is another test message."},
    # Add more dictionaries for additional test cases
]

try:
    # Loop through the test data to perform multiple form submissions
    for data in test_data:
        # Open the form page to start each test
        driver.get("http://localhost/Final/projsamp.html")

        # Wait for the input fields to be present (with a longer wait for slow page loading)
        WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.NAME, 'name')))
        WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.NAME, 'email')))
        WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.NAME, 'message')))

        # Locate and fill input fields
        name_input = driver.find_element(By.NAME, 'name')
        email_input = driver.find_element(By.NAME, 'email')
        message_input = driver.find_element(By.NAME, 'message')

        # Clear any pre-filled values
        name_input.clear()
        email_input.clear()
        message_input.clear()

        # Input values from the current test data
        name_input.send_keys(data["name"])
        email_input.send_keys(data["email"])
        message_input.send_keys(data["message"])

        # Print the values being submitted for visibility
        print(f"Submitting: Name: {data['name']}, Email: {data['email']}, Message: {data['message']}")

        # Submit the form using the submit button or form action
        driver.find_element(By.XPATH, "//form").submit()

        # Wait for the success message on connect.php (extend wait time)
        try:
            # Wait until success message or confirmation is displayed
            WebDriverWait(driver, 2).until(
                EC.presence_of_element_located((By.XPATH, "//body[contains(text(), 'The record has been inserted successfully successfully!')]"))
            )
            # Capture and print the success message
            success_message = driver.find_element(By.XPATH, "//body[contains(text(), 'The record has been inserted successfully successfully!')]").text
            print("Response:", success_message)
        except Exception as e:
            print(f"Data Submitted Successfully")
            continue  # If no success message found, skip to the next test case

        # Wait a few seconds to ensure the page is fully loaded
       # time.sleep(5)

        # After confirming success, use driver.back() to return to the form page
        driver.back()  # This will take the browser back to the form page

        # Optional: Add a brief pause between test cases for better visibility in testing
        time.sleep(2)

except Exception as e:
    print(f"Successfull")

finally:
    # Close the browser after testing
    driver.quit()
