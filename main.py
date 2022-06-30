from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import pyautogui


def special_wait(by,value,browser,wait_time=600):
    counter = 0
    wait_time*=10
    while True:
        counter+=1
        try:
            element = browser.find_element(by,value)
            break
        except Exception as e:
            time.sleep(0.1)
        if counter==wait_time:
            break


def pyautogui_wait(wait_time=20):
    counter = 0
    wait_time*=10
    while True:
        counter+=1
        try:
            pyautogui.getWindowsWithTitle("Select Folder to Upload")[0]
            break
        except IndexError:
            time.sleep(0.1)
        if counter==wait_time:
            break

#SABİTLER
FILE = open("options.txt","r")
EMAIL = FILE.readline().strip()
PASSWORD = FILE.readline().strip()
PATH = FILE.readline().strip()
BASE_URL="https://onedrive.live.com/about/tr-tr/signin/"


#Driver setup
options = Options()
# options.headless = True
browser = webdriver.Chrome(options=options)
browser.get(BASE_URL)

#Giriş yap ekranına girilmesi
special_wait(By.XPATH,'//*[@id="mainContent"]/iframe',browser)
iframe_element = browser.find_element(By.XPATH,'//*[@id="mainContent"]/iframe')
browser.switch_to.frame(iframe_element)


#E-mailin girlmesi ve ileri butonuna tıklanması
special_wait(By.XPATH,'//*[@id="placeholder"]/div[2]/div/input',browser)
email_input_element= browser.find_element(By.XPATH,'//*[@id="placeholder"]/div[2]/div/input')
email_input_element.send_keys(EMAIL)

next_to_password_element=browser.find_element(By.XPATH,'//*[@id="placeholder"]/div[4]/input')
next_to_password_element.click()


#Şifrenin girilmesi ve giriş yap butonuna tıklanması
special_wait(By.ID,'i0118',browser)
password_input_element = browser.find_element(By.ID,'i0118')
password_input_element.send_keys(PASSWORD)

signIn_element = browser.find_element(By.ID,'idSIButton9')
signIn_element.click()


#Oturumun açık kalmaması sağlanıyor
special_wait(By.CSS_SELECTOR,'input[value="Hayır"]',browser)
no_session_element = browser.find_element(By.CSS_SELECTOR,'input[value="Hayır"]')
no_session_element.click()


#Pop-up'ların engellenmesi
try:
    pop_up1_element1 = browser.find_element(By.XPATH,'//*[@id="appRoot"]/div/div[3]/div[4]/div/div/div[2]/div[3]/div/div[1]/button/i')
    pop_up1_element1.click()
except:
    pass


#upload butonuna tıklanıyor
special_wait(By.NAME,'Karşıya Yükle',browser)
upload_element = browser.find_element(By.NAME,'Karşıya Yükle')
upload_element.click()

open_folder_element = browser.find_element(By.NAME,'Klasör')
open_folder_element.click()


#Dosya yolu seçiliyor
pyautogui_wait()
pyautogui.write(PATH)
pyautogui.press('enter')
pyautogui.press('enter')
pyautogui.press('left')
pyautogui.press('enter')

#Tekrarlanan dosyaların her ikisi de saklanıyor
special_wait(By.NAME,'Her ikisini de sakla',browser)
keep_both_element = browser.find_element(By.NAME,'Her ikisini de sakla')
keep_both_element.click()


#Dosyanın yüklenmesi bekleniyor
special_wait(By.CSS_SELECTOR,'i[data-icon-name="CheckMark"]',browser)
browser.quit()













