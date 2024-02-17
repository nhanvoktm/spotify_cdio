from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import logging
import os
import glob
import shutil
import pandas as pd
#source : Thư mục download mặc định
source = r"C:\Users\ACER\Downloads"

#destination : Thư mục mình cần lưu
destination = "D:\music_data_all\audio"

data = list(pd.read_csv("download_audio.csv").values)

logging.basicConfig(filename="process.log",
                    format='%(asctime)s %(message)s',
                    filemode='a')

option = Options()
option.add_experimental_option("detach",True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=option)

#Cấu hình thời gian chờ
data_sync_duration = 3
init_page_duration = 5
driver.get('https://spotifydown.com')

driver.maximize_window()
for url in data:

    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    try:

        time.sleep(init_page_duration)

        driver.find_element(By.CSS_SELECTOR, 'input.searchInput').send_keys(url[0])

        time.sleep(2)

        driver.find_element(By.XPATH, '//button[text()="Download"]').click()

        time.sleep(data_sync_duration)

        driver.find_element(By.XPATH, '//button[text()="Download"]').click()

        WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[download]')))
        time.sleep(data_sync_duration)
        driver.find_element(By.CSS_SELECTOR, 'a[download]').click()

        time.sleep(data_sync_duration)

        # Đoạn dưới đây lấy tất cả file có đuôi .mp3 chuyển tới thư mục đích

        # file_path = glob.glob(os.path.join(source, '*.mp3'), recursive=True)[0]
        #
        # dst_path = os.path.join(destination, os.path.basename(file_path))
        #
        # shutil.move(file_path, dst_path)

        logger.info(f"success fully download : {url}")

    except:

        logger.error(f"failed at : {url}")

    finally:
        driver.refresh()
