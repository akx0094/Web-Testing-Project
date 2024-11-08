from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize the Chrome WebDriver
driver = webdriver.Chrome()

# Load the webpage
driver.get("http://localhost/Final/projsamp.html")  # replace with the actual URL

# Maximize the browser window
driver.maximize_window()

# List of expected card titles and their associated data
card_data = [
    {"title": "Shaniwar Wada", "modal_id": "shaniwarWadaModal", "map_link": "https://www.google.com/maps?q=Shaniwar+Wada,Pune"},
    {"title": "Aga Khan Palace", "modal_id": "agaKhanPalaceModal", "map_link": "https://www.google.com/maps?q=Aga+Khan+Palace,Pune"},
    {"title": "Lal Mahal", "modal_id": "lalMahalModal", "map_link": "https://www.google.com/maps?q=Lal+Mahal,Pune"},
    {"title": "Sinhagad Fort", "modal_id": "sinhagadhModal", "map_link": "https://maps.app.goo.gl/sJibJghcbBSeoFcr8"},
    {"title": "Pataleshwar Cave", "modal_id": "pataleshwarModal", "map_link": "https://maps.app.goo.gl/fiMKi29LP71SwB36A"},
    {"title": "Vishrambaug Wada", "modal_id": "vishrambaugModal", "map_link": "https://maps.app.goo.gl/wvvLJLfsFCZiMocN6"}
]

try:
    for index, card in enumerate(card_data):
        # Find each card container by index
        card_container = WebDriverWait(driver, 10).until(
            EC.visibility_of_all_elements_located((By.CLASS_NAME, "card"))
        )[index]

        # Check the title of each card
        card_title = card_container.find_element(By.CLASS_NAME, "card-title")
        print(f"Captured card title text: {card_title.text}")
        assert card["title"] in card_title.text.strip(), f"Card title does not match for {card['title']}"

        # Test 'Read More' Button to Open Modal
        read_more_button = card_container.find_element(By.LINK_TEXT, "Read More")
        read_more_button.click()

        # Wait for the modal to appear
        modal = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, card["modal_id"])))
        assert modal.is_displayed(), f"Modal did not open for {card['title']}"

        # Close the modal
        close_button = modal.find_element(By.CLASS_NAME, "close")
        close_button.click()

        # Test Google Maps Link
        google_maps_button = card_container.find_element(By.CSS_SELECTOR, ".btn-success")
        google_maps_link = google_maps_button.get_attribute("href")
        assert google_maps_link == card["map_link"], f"Google Maps link is incorrect for {card['title']}"

        # Click the Google Maps link to ensure it opens in a new tab
        google_maps_button.click()

        # Switch to the new tab and verify URL
        WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))
        driver.switch_to.window(driver.window_handles[1])
        assert card["map_link"] in driver.current_url, f"Google Maps link did not open correctly for {card['title']}"

        # Close the Google Maps tab and switch back to the original tab
        driver.close()
        driver.switch_to.window(driver.window_handles[0])

        print(f"All tests passed for {card['title']}.")


    

finally:
    # Close the browser
    driver.quit()
