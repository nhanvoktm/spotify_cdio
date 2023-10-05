from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import csv
import logging
import os
import glob
import shutil
import pandas as pd
option = Options()
option.add_experimental_option("detach",True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=option)

driver.maximize_window()
website = 'https://spotifydown.com/vi'
driver.get(website)

#source : Thư mục download mặc định
source = r"C:\Users\ACER\Downloads"

#destination : Thư mục mình cần lưu
destination = "D:\music_data_all\audio"

data = list(pd.read_csv("id_track.csv").values)

logging.basicConfig(filename="process.log",
                    format='%(asctime)s %(message)s',
                    filemode='a')

for url in data:
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    try:
        time.sleep(3)
        button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/div/div[1]/input')))
        button.send_keys(str(url[0]))
        time.sleep(2)
        button.send_keys(Keys.ENTER)
        time.sleep(3)
        driver.find_element((By.XPATH, '//*[@id="__next"]/div/div[2]/div[1]/div/div[2]/button')).click()
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/div/div[2]/div[1]/a[1]')))
        time.sleep(2)
        driver.find_element((By.XPATH, '//*[@id="__next"]/div/div[2]/div[1]/a[1]')).click()
        time.sleep(3)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/div[2]/div/div[2]'))).click()
        time.sleep(3)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/div/div[2]/div[1]/a[2]'))).click()
        time.sleep(2)
        # Đoạn dưới đây lấy tất cả file có đuôi .mp3 chuyển tới thư mục đích

        # file_path = glob.glob(os.path.join(source, '*.mp3'), recursive=True)[0]
        #
        # dst_path = os.path.join(destination, os.path.basename(file_path))
        #
        # shutil.move(file_path, dst_path)

        logger.info(f"success fully download : {url}")

    except:
        logger.error(f"failed at : {url}")
        driver.refresh()







