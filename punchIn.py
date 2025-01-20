from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from datetime import date
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

# Configure Chrome options for headless mode
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in headless mode
chrome_options.add_argument("--disable-gpu")  # Disable GPU usage
chrome_options.add_argument("--no-sandbox")  # Bypass OS security model
chrome_options.add_argument("--disable-dev-shm-usage")  # Overcome limited resources

# Create a Chrome WebDriver
driver = webdriver.Chrome(options=chrome_options)



try:

    #Check date if today is saturday or sunday
    today = date.today()
    day = today.strftime("%A")
    print("Today is: ",day)
    if day != "Saturday" or day != "Sunday":
            # # Open the HR management system
        driver.get('https://x.optimis.in/login')

        # Log in
        username = driver.find_element(By.ID, 'usrname')  # Replace with the actual ID or selector
        password = driver.find_element(By.ID, 'passwd')  # Replace with the actual ID or selector
        username.send_keys('sagar@savitriya.com')
        password.send_keys('Sagar@12345')
        password.send_keys(Keys.RETURN)

        # Wait for the page to load
        time.sleep(5)
        print("X optimis logged in")

        try:
            birthdayPopup =driver.find_element("xpath", "//h2[contains(text(), 'Today's Birthdays')]")
            if birthdayPopup:  # Replace with the actual ID or selector
                print("Birthday pop up detected")
                birthdayBtn =driver.find_element("xpath", "//*[@id='birthday-quotes-modal']//*[@aria-label='Close']")
                birthdayBtn.click()
                print("Birthday pop up closed!!")
        except:
            print("No birthday pop up detected")
        
        try:
            punchInPopup =driver.find_element("xpath", "//h2[contains(text(), 'Would you like to start your day')]")
        
            # Navigate to the punch-in page
            if punchInPopup:  # Replace with the actual ID or selector
                print("Punch-in pop up detected")
                punchInBtn1 =driver.find_element("xpath", "//button[contains(text(), 'Yes')]")
                punchInBtn1.click()
                print("Punch-in successful in x optimis!!")


            else:
                print("Punch-in failed!")
        except:
            print("No punch-in pop up detected in optimis")

            # Open the HR management system
        driver.get('https://hr.azminds.com/login')

        # Log in
        username = driver.find_element(By.ID, ':r0:')  # Replace with the actual ID or selector
        password = driver.find_element(By.ID, ':r1:')  # Replace with the actual ID or selector
        username.send_keys('sagar.azminds@gmail.com')
        password.send_keys('azminds12345')
        password.send_keys(Keys.RETURN)

        # Wait for the page to load
        time.sleep(5)
        try:
            azPunchInBtn =driver.find_element("xpath", "//button[contains(text(), 'Punch In')]")
        
            # Navigate to the punch-in page
            if azPunchInBtn:  # Replace with the actual ID or selector
                azPunchInBtn.click()
                print("Punch-in completed successfully!",azPunchInBtn)
                
            else:
                print("Punch-in failed!")
        except:
            print("No punch-in pop up detected")
    else:
        
        print("Today is weekend!!")   



except:
    # Close the browser
    driver.quit()
