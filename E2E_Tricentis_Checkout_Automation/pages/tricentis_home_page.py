from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomePage:
    '''
    Objective : 
        Page Object Model (POM) for the Home and Product Selection Page.
        This module contains the 'HomePage' class, which manages initial user interactions
        such as Selecting an item from the product listing, handling scroll actions
        and entering recipient information.
    Args : 
        driver (WebDriver): The Selenium WebDriver instance used to interact with the web page.
        recipient_name (str): The name of the gift card recipient.
        recipient_email (str): The email address of the gift card recipient.
    '''
    def __init__(self, driver):
        self.driver = driver
        self.item_to_select = (By.XPATH, "(//input[@value='Add to cart'])[1]") 
        self.add_to_cart_button = (By.ID, "add-to-cart-button-2")
        self.cart_success_banner = (By.XPATH, "//p[@class='content']")

    def scroll_to_item(self):
        item = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.item_to_select))
        ActionChains(self.driver).move_to_element(item).perform()

    def choose_item(self):
        self.driver.find_element(*self.item_to_select).click()
    
    def enter_recipent_information(self, recipient_name, recipient_email):
        name_field = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "giftcard_2_RecipientName")))
        email_field = self.driver.find_element(By.ID, "giftcard_2_RecipientEmail")
        name_field.clear()
        name_field.send_keys(recipient_name)        
        email_field.clear()
        email_field.send_keys(recipient_email)
    
    def add_to_cart(self):
        self.driver.find_element(*self.add_to_cart_button).click()
        
    def item_is_added_to_cart(self): 
        return self.driver.find_element(*self.cart_success_banner).is_displayed() 