import os , sys
import time
import xlrd
from lib2to3.pgen2 import driver
from xml.dom.minidom import Element
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.keys import Keys

EXTENSION_PATH = os.getcwd() + '/file/metamask.crx'
DRIVER_PATH = os.getcwd() + '/file/chromedriver'
PHRASE_PATH = os.getcwd() + '/file/phrase.xlsx'

def installExtension():
    print('path', EXTENSION_PATH)

    #use global variable for options
    global chrome_options
    chrome_options = ChromeOptions()
    chrome_options.add_extension(EXTENSION_PATH)

#call function
installExtension()

#creating an instane of our webdriver and appl;yinh chromeoptions
def WebDriver():
    print("Launch selenium web driver")

    #use global variable for driver
    global driver
    driver = webdriver.Chrome(DRIVER_PATH, options=chrome_options)
    driver.maximize_window()

#call function
WebDriver()

def setupMetamask():
    print("Set up Metamask")
    driver.implicitly_wait(20)

    #load metamask html page
    driver.get('chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/home.html#initialize/create-password/import-with-seed-phrase')

    #get pharse.xlsx
    wb = xlrd.open_workbook(PHRASE_PATH)
    sheet = wb.sheet_by_index(0)

    #input phrase on metamask
    driver.switch_to.window(driver.window_handles[-1])
    driver.implicitly_wait(5)
    driver.find_element(By.ID,'import-srp__srp-word-0').send_keys(sheet.cell_value(0,0))
    driver.find_element(By.ID,'import-srp__srp-word-1').send_keys(sheet.cell_value(1,0))
    driver.find_element(By.ID,'import-srp__srp-word-2').send_keys(sheet.cell_value(2,0))
    driver.find_element(By.ID,'import-srp__srp-word-3').send_keys(sheet.cell_value(3,0))
    driver.find_element(By.ID,'import-srp__srp-word-4').send_keys(sheet.cell_value(4,0))
    driver.find_element(By.ID,'import-srp__srp-word-5').send_keys(sheet.cell_value(5,0))
    driver.find_element(By.ID,'import-srp__srp-word-6').send_keys(sheet.cell_value(6,0))
    driver.find_element(By.ID,'import-srp__srp-word-7').send_keys(sheet.cell_value(7,0))
    driver.find_element(By.ID,'import-srp__srp-word-8').send_keys(sheet.cell_value(8,0))
    driver.find_element(By.ID,'import-srp__srp-word-9').send_keys(sheet.cell_value(9,0))
    driver.find_element(By.ID,'import-srp__srp-word-10').send_keys(sheet.cell_value(10,0))
    driver.find_element(By.ID,'import-srp__srp-word-11').send_keys(sheet.cell_value(11,0))

    #input password
    driver.find_element(By.ID,'password').send_keys('password123')
    driver.find_element(By.ID,'confirm-password').send_keys('password123')
    driver.find_element(By.ID,'create-new-vault__terms-checkbox').click()
    driver.find_element(By.CSS_SELECTOR,'#app-content > div > div.main-container-wrapper > div > div > div.first-time-flow__import > form > button').click()
    driver.find_element(By.CSS_SELECTOR,'#app-content > div > div.main-container-wrapper > div > div > button').click()

#call function
setupMetamask()

def connectToWebsite():
    driver.implicitly_wait(10)
    driver.get('https://marketplace.devucc.name/')

    #Connect metamask
    driver.find_element(By.XPATH,'//*[@id="__next"]/div[1]/div/div[3]/div/button/span').click()
    window_before = driver.window_handles[0]
    print(driver.title)
    driver.find_element(By.XPATH,'/html/body/div[4]/div/div/div/button[1]').click()
    window_after = driver.window_handles[1]
    driver.switch_to.window(window_after)
    print(driver.title)
    time.sleep(5)
    driver.switch_to.window(driver.window_handles[2])
    print(driver.title)
    driver.find_element(By.XPATH,'//*[@id="app-content"]/div/div[2]/div/div[3]/div[2]/button[2]').click()
    driver.find_element(By.XPATH,'//*[@id="app-content"]/div/div[2]/div/div[2]/div[2]/div[2]/footer/button[2]').click()
    print("Wallet Connected")

connectToWebsite()