from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from datetime import date
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Configure Chrome options for headless mode
chrome_options = Options()
# chrome_options.add_argument("--headless")  # Run in headless mode
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
    if day != "Saturday" and day != "Sunday":
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
                print("Punch-in pop up not detected!")
        except:
            try:
            
                punchInPopup1 =driver.find_element("xpath", "//button[contains(text(), 'Start')]")
            
                # Navigate to the punch-in page
                if punchInPopup1:  # Replace with the actual ID or selector
                    print("Punch-in btn detected",punchInPopup1)
                    punchInPopup1.click()
                    print("Punch-in successful in x optimis!!")  
                    print("X optimis logged in")
                else:
                    print("Punch-in pop btn not detected!")

            except:
                try:
                    print("No punch-in pop up detected in optimis trying to relogin")
                    dropdown_button = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.ID, "dropdownMenuButton1"))
                    )
                    dropdown_button.click()
                    logout_span = driver.find_element(By.XPATH, "//span[normalize-space(text())='Logout']")

                    print("logoutBtn detected",logout_span)   

                    logout_span.click()

                    time.sleep(5)
                    
                    # # Re login again and repeat the process
                    driver.get('https://x.optimis.in/login')

                    # Log in
                    username = driver.find_element(By.ID, 'usrname')  # Replace with the actual ID or selector
                    password = driver.find_element(By.ID, 'passwd')  # Replace with the actual ID or selector
                    username.send_keys('sagar@savitriya.com')
                    password.send_keys('Sagar@12345')
                    password.send_keys(Keys.RETURN)

                    # Wait for the page to load
                    time.sleep(5)
                    try:
                            punchInPopup1 =driver.find_element("xpath", "//button[contains(text(), 'Start')]")
                        
                            # Navigate to the punch-in page
                            if punchInPopup1:  # Replace with the actual ID or selector
                                print("Punch-in btn detected",punchInPopup1)
                                punchInPopup1.click()
                                print("Punch-in successful in x optimis!!")  
                                print("X optimis logged in")
                            else:
                                print("Punch-in pop btn not detected!")
                    except:
                            print("Punch-in pop btn not detected!")
                            
                            # Close the browser
                            driver.quit()
                except Exception as e:
                    print("logout failed",e)
           

       
    else:
        
        print("Today is weekend!!")   



except:
    # Close the browser
    driver.quit()
