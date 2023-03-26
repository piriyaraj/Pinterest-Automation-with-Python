"""
This module provides a Browser class that can be used to automate pin creation on Pinterest. 

It requires the selenium package and a ChromeDriverManager to be installed.

Example usage:

    browser = Browser(username='myusername', password='mypassword')
    browser.start()
    browser.createPin(image='path/to/image.jpg', title='My Pin', 
    description='A description of my pin', destinationLink='https://example.com')
"""

import json
import os
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


pinterest_home = "https://www.pinterest.com/"
pre_login_button = '/html/body/div[1]/div[1]/div/div/div/div/div/div[1]/div/div/div[1]/div/div[2]/div[2]/button/div/div'
login_button = "//button[@type='submit']"
pin_builder = "https://www.pinterest.com/pin-builder/"
pin_name = "//*[starts-with(@id, 'pin-draft-title-')]"
pin_description = "//*[starts-with(@id, 'pin-draft-description-')]/div/div/div/div/div/div/div"
image_input = "//*[starts-with(@id, 'media-upload-input-')]"
pin_link = "//*[starts-with(@id, 'pin-draft-link-')]"
drop_down_menu = "//button[@data-test-id='board-dropdown-select-button']"
publish_button = "//button[@data-test-id='board-dropdown-save-button']"


class Browser:
    """
    A class that provides methods for automating pin creation on Pinterest.
    """
    def __init__(self, username: str, password: str) -> None:
        """
        Constructor for Browser class.

        Args:
            username (str): The Pinterest username to use for login.
            password (str): The Pinterest password to use for login.
        """
        self.username = username
        self.password = password
        
    def __login(self):
        """
        Private method to perform login.
        """
        # Open Pinterest on Chrome Driver
        self.driver.get(pinterest_home)
        time.sleep(3)

        # Click log in link
        self.driver.find_element(By.XPATH, pre_login_button).click()
        time.sleep(3)

        # Log in
        user = self.driver.find_element(By.NAME, "id")
        user.send_keys(self.username)
        time.sleep(3)
        pas = self.driver.find_element(By.NAME, "password")
        pas.send_keys(self.password)
        time.sleep(3)
        self.driver.find_element(By.XPATH, login_button).click()
        time.sleep(3)
    
    def start(self):
        """
        Method to start the ChromeDriver and perform login.
        """
        options = webdriver.ChromeOptions() 
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        self.__login()
        
    def createPin(self, image:str, title:str, description:str, destinationLink:str,imageAlt:str,boardName:str):
        """
        Creates a new pin on Pinterest using the provided image, title, description, destination link,
        image alt text, and board name.
        
        Args:
            image (str): The file path to the image to use for the pin.
            title (str): The title to use for the pin.
            description (str): The description to use for the pin.
            destinationLink (str): The destination link to use for the pin.
            imageAlt (str): The alt text to use for the pin image.
            boardName (str): The name of the board to save the pin to.
            
        Returns:
            None: This method does not return anything, but creates a new pin on the Pinterest account.
        """
        # Navigate to the pin builder page
        self.driver.get(pin_builder)
        time.sleep(10)
        # Upload the image
        imgUpload=self.driver.find_element(By.XPATH, '//input[@type="file"]')
        time.sleep(1)
        imgUpload.send_keys(image)
        time.sleep(10)
        print("=====> image uploaded")
        # Enter the pin title
        pinTitleTag=self.driver.find_element(By.XPATH, pin_name)
        pinTitleTag.send_keys(title)
        time.sleep(10)
        print("=====> title posted")

        # Enter the pin description
        pinDescriptionTag=self.driver.find_element(By.XPATH, pin_description)
        print(pinDescriptionTag.get_attribute('data-offset-key'))
        pinDescriptionTag.send_keys(description)
        print("=====> description posted")
        
        # Add alt
        pinAltTag=self.driver.find_element(By.XPATH, "//*[@id='__PWS_ROOT__']/div[1]/div/div[2]/div/div/div/div[2]/div[2]/div/div/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[1]/div[4]/div/button/div/div")
        print(pinAltTag.get_attribute('class'))
        pinAltTag.click()
        time.sleep(10)
        pinAltTag1=self.driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div/div[2]/div/div/div/div[2]/div[2]/div/div/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[1]/div[4]/div/div[2]/div[1]/textarea')
        print(pinAltTag1.get_attribute('placeholder'))
        pinAltTag1.send_keys(imageAlt)
        time.sleep(10)
        
        # Select a board to save the pin to
        dropdown_menu = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div/div[2]/div/div/div/div[2]/div[2]/div/div/div/div/div/div/div/div/div/div[1]/div/div[2]/div/div/div/button[1]')
        dropdown_menu.click()
        print("=====> Dropdown clicked")
        time.sleep(10)
        option = self.driver.find_element(By.XPATH, '//div[contains(text(), "'+boardName+'")]')
        option.click()
        print("=====> Board selected")
        
        time.sleep(10)

        # Enter the pin destination link
        pinLinkTag=self.driver.find_element(By.XPATH, pin_link)
        pinLinkTag.send_keys(destinationLink)
        time.sleep(10)
        print("=====> Link posted")


        # Publish the pin
        pinPublishTag=self.driver.find_element(By.XPATH, publish_button)
        print(pinPublishTag.get_attribute('class'))
        pinPublishTag.click()