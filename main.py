from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

file = open("log.txt","w")

driver = webdriver.Chrome()

driver.get('https://www.saucedemo.com')
driver.maximize_window()

def login():
    user_name = driver.find_element(By.XPATH,'//input[@id="user-name"]')
    login="standard_user"
    user_name.send_keys(login)
    file.write("Success write login\n")

    user_pass = driver.find_element(By.XPATH, '//input[@id="password"]')
    password="secret_sauce"
    user_pass.send_keys(password)
    file.write("Success write password\n")

    sleep(2)

    login_button = driver.find_element(By.XPATH, '//input [@id="login-button"]')
    login_button.click()
    file.write("Success click login\n")

login()
file.close()

sleep(5)
