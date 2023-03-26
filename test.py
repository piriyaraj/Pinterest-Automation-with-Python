# Import the required modules
import time
from browser import Browser

# Set the login credentials
username = "your_username"
password = "your_password"

# Set the pin details
image_path = "path_to_image_file"
pin_title = "Your pin title"
pin_description = "Your pin description"
destination_link = "Your destination link"
board_name = "Your board name"
altName = "Alt for image"
# Create a new browser instance and start it
browser = Browser(username, password)
browser.start()

# Create a new pin
browser.createPin(image_path, pin_title, pin_description, destination_link,altName,board_name)

# Wait for the pin to be created
time.sleep(10)

# Close the browser
browser.driver.quit()
