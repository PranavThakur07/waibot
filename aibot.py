from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time




chrome_options = Options()
prefs = {
    "profile.default_content_setting_values.media_stream": 1,  
    "profile.default_content_setting_values.notifications": 2,  
}
chrome_options.add_experimental_option("prefs", prefs)
chrome_options.add_argument("--use-fake-ui-for-media-stream")
#chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1920,1080")  


service = Service('E:\Python\driver\chromedriver.exe')


driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    driver.get("https://vapi.ai")
    
    mic_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, 'circle'))
    )
    
    
    mic_button.click()
    print("Microphone button clicked successfully!")
    time.sleep(100)


    
finally:
    driver.quit()
