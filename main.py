from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Create a Service object pointing to the path of your ChromeDriver
s = Service('/usr/local/bin/chromedriver')

# Pass the Service object to the WebDriver
driver = webdriver.Chrome(service=s)

# Open a website (change the URL to your desired website)
driver.get('https://www.trusteddocks.com/catalog/managers/225-united-arab-emirates')

# Get cookies
cookies = driver.get_cookies()
print(cookies)

# Cleanup
driver.quit()
