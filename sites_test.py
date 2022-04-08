import datetime as dt
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from telegram_pack.send_telegram import send_to_telegram
from telegram_pack.config import TOKEN


chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(chrome_options=chrome_options, executable_path='/home/butovich_v/workspace/sitetest/drivers/chromedriver_lnx')



def site_chek(browser):
    dictionary = {
        "https://kupiperevozki.ru/": ("//div[@id='wb_element_instance121']", "22.07.2021", "25.07.2021"),
        "https://topphp.ru/": ("//div[@id='top_menu_wrapper']", "06.06.2021", "23.07.2021"),
        "https://it.bir.ru/": ("//div[@class='component-logo-img']", "08.06.2021", "31.07.2021"),
        "https://soft-pro.pro/": ("//nav[@id='nav_menu']", "03.07.2021", "24.08.2021"),
        # "https://expedition-pro.ru/": ("//section[@id='section0']", "06.06.2021", "12.05.2022"), вернуть через неделю
        "https://gruzland.ru/": ("//nav[@id='top-nav']", "06.06.2021", "27.08.2021"),
        "https://mirpolygraphy.ru/": ("//div/nav[@class='tm-navbar uk-navbar']", "06.06.2021", "23.07.2021"),
        "https://ruitpro.ru/": ("//div[@id='nav30920090']", "06.06.2021", "23.07.2021"),
        "https://soft.msk.ru/": ("//div/div[@id='section14f64406ccc3815']", "14.08.2021", "14.08.2021"),
        "https://bezlimit.market": ("", "08.10.2021", ""),
        "https://promis.su": ("", "08.10.2021", ""),
        "https://profi-telecom.ru": ("", "08.10.2021", ""),
        "https://kvatro-telecom.ru": ("", "29.01.2022", ""),
        "http://altair-telecom.ru": ("", "29.01.2022", ""),
        "http://dual-com.ru": ("", "29.01.2022", ""),
        "http://vmg-konsalting.ru": ("", "29.01.2022", ""),
        "https://telecom-alfa.ru/": ("//div[@id='header']", "17.03.2022", ""),
        "https://braitele.com/": ("//div[@id='customizr-slider-main_slider']", "17.03.2022", ""),
    }

    for item in dictionary:

        if dictionary[item][1]:
            now = dt.datetime.date(dt.datetime.now())
            date = dictionary[item][1].split('.')
            date = dt.datetime.date(dt.datetime(int(date[2]), int(date[1]), int(date[0])))
            zero = dt.timedelta(days=0)
            while date - now <= zero:
                date += dt.timedelta(days=365)
            for i in (1, 7, 30, 60, 90):
                delta = dt.timedelta(days=i)
                if date - now == delta:
                    send_to_telegram(f"Внимание! Для сайта {item} "
                                    f"заканчивается срок владения доменом {dictionary[item][1]}",
                                    TOKEN, -1001197336253)

        if dictionary[item][2]:
            now = dt.datetime.date(dt.datetime.now())
            date = dictionary[item][2].split('.')
            date = dt.datetime.date(dt.datetime(int(date[2]), int(date[1]), int(date[0])))
            zero = dt.timedelta(days=0)
            while date - now <= zero:
                date += dt.timedelta(days=365)
            for i in (1, 7, 30, 60, 90):
                delta = dt.timedelta(days=i)
                if date - now == delta:
                    send_to_telegram(f"Внимание! Для сайта {item} "
                                    f"заканчивается срок владения хостингом {dictionary[item][2]}", TOKEN, -1001197336253)

        if dictionary[item][0]:
            try:
                driver.get(item)
                driver.find_element(By.XPATH, dictionary[item][0])
            except Exception:
                send_to_telegram(f"Сайт не доступен:{item}", TOKEN, -1001197336253)

    time.sleep(5)


site_chek(driver)
