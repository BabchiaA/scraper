from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from database import create_db
import chromedriver_autoinstaller

def scraper(email, password, url_page, max_scrolls = 5):
    chrome_options = webdriver.ChromeOptions() 
    driver = webdriver.Chrome(options=chrome_options)
    driver.get('https://www.facebook.com/') 
    print ("Opened facebook") 
    sleep(2) 

    email_input = driver.find_element('xpath', '//*[@id="email"]')
    email_input.send_keys(email) 
    
    password_input = driver.find_element('xpath', '//*[@id="pass"]')
    password_input.send_keys(password) 
    
    login = driver.find_element('xpath', '/html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[2]/button')
    login.click()
    sleep(3) 
    print('Connected')

    driver.get(url_page)
    sleep(5)

    scroll_count = 0
    while scroll_count < max_scrolls:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        sleep(2)  # give some time for new results to load
        scroll_count += 1

    print('done')

    posts = driver.find_elements(By.XPATH, "//div[contains(@class, 'x1iorvi4 x1pi30zi x1l90r2v x1swvt13')]")
    reacts = driver.find_elements(By.XPATH, "//div[contains(@class, 'x1i10hfl x1qjc9v5 xjqpnuy xa49m3k xqeqjp1 x2hbi6w x1ypdohk xdl72j9 x2lah0s xe8uvvx x2lwn1j xeuugli xggy1nq x1t137rt x1o1ewxj x3x9cwd x1e5q0jg x13rtm0m x3nfvp2 x1q0g3np x87ps6o x1lku1pv x1a2a7pz xjyslct xjbqb8w x13fuv20 xu3j5b3 x1q0q8m5 x26u7qi x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x1heor9g xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x1n2onr6 x16tdsg8 xt0b8zv x1hl2dhg x1ja2u2z')]")

    data = list()
    for i in range(len(posts)):
        data.append({'post' : posts[i].text, 'comments' : reacts[2*i].text, 'shares' : reacts[2*i+1].text})

    create_db(data)

