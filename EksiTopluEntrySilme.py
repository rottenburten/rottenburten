from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
import time

PATH = "C:\\Program Files (x86)\\chromedriver.exe"

driver = webdriver.Chrome(PATH)

driver.get("https://eksisozluk.com/giris?returnUrl=https%3A%2F%2Feksisozluk.com%2F")


link = driver.find_element_by_link_text("giriş")
link.click()

driver.implicitly_wait(5)

username =driver.find_element_by_name("UserName")
password =driver.find_element_by_name("Password")
#??? yerine eksi kullanıcı adını gir
username.send_keys("???")
#??? yerine eksi sifreni gir. 
password.send_keys("???")
time.sleep(10)

password.send_keys(Keys.ENTER)

#??? yerine kullanıcı adını yaz
driver.get("https://eksisozluk.com/biri/???")

time.sleep(10)


contentblock = driver.find_elements_by_class_name("topic-item")
time.sleep(10)

for content in contentblock:
    svgObj = content.find_element_by_id("svg-dots")
    actionBuilder = ActionChains(driver)
    actionBuilder.click(svgObj).perform()
    time.sleep(42)

    sil = content.find_element_by_link_text("sil")
    actionBuilder = ActionChains(driver)
    actionBuilder.click(sil).perform()
    time.sleep(42)

    silform =driver.find_element_by_css_selector("body.light-theme.theme-disabled:nth-child(2) div.instapaper_body:nth-child(2) section:nth-child(1) form.entry-menu-form.modal:nth-child(1) fieldset.vertical:nth-child(2) > div.actions:nth-child(4)")
    time.sleep(42)
    kesin = silform.find_element_by_class_name("primary")
    actionBuilder = ActionChains(driver)
    actionBuilder.click(kesin).perform()
    time.sleep(40)
