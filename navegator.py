from selenium import webdriver
import pyautogui

pyautogui.PAUSE = 1


browser = webdriver.Chrome()
browser.get("https://www.google.com/")
preco = browser.find_element(
        'xpath', '/html/body/div[5]/div[1]/div/div/input[2]').get_attribute('value')


browser.quit()
