from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

# Set up WebDriver (make sure to have the appropriate WebDriver installed, e.g., ChromeDriver)
driver = webdriver.Chrome()

# Open chess.com
driver.get("https://www.chess.com/login")
time.sleep(2)  # Let the page load

# Log in to chess.com
username_input = driver.find_element(By.ID, "username")  # Modify the element locator as per the actual site structure
password_input = driver.find_element(By.ID, "password")
username_input.send_keys("your_username")
password_input.send_keys("your_password")
password_input.submit()
time.sleep(3)  # Wait for login to complete

# Define your moves sequence here
moves = [("e2", "e4"), ("g1", "f3")]  # Example moves list, replace with actual moves based on binary

# Navigate to a game (you may need to adjust this to find and start a game)
driver.get("https://www.chess.com/play/computer")
time.sleep(3)

# Play each move on the board
actions = ActionChains(driver)
for start, end in moves:
    # Locate the starting square and ending square elements
    start_square = driver.find_element(By.CSS_SELECTOR, f"[data-square='{start}']")
    end_square = driver.find_element(By.CSS_SELECTOR, f"[data-square='{end}']")

    # Execute the move
    actions.click(start_square).click(end_square).perform()
    time.sleep(2)  # Pause between moves for better visualization

# Close the browser once done
driver.quit()
