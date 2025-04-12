from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("file:///C:/Users/pedro/AppData/Local/Microsoft/Windows/INetCache/IE/F5ZYLZBC/index[2].html")  

driver.find_element(By.ID, "email").send_keys("admin")
driver.find_element(By.ID, "senha").send_keys("@ASD_921@#a231")

for tentativa in range(3):
    captcha = driver.find_element(By.ID, "captcha-text").text
    driver.find_element(By.ID, "captcha").clear()
    driver.find_element(By.ID, "captcha").send_keys(captcha)
    driver.find_element(By.TAG_NAME, "button").click()
    input("Enter para continuar")
    
    if "sucesso" in driver.page_source.lower():
        print(f"tentativa: {tentativa+1} \nCAPTCHA: {captcha}")
        break
else:
    print("deu ruim")

time.sleep(5)
driver.quit()