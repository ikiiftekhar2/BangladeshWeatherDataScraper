import string
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from datetime import datetime
import re

options = Options()
options.headless = True

def fetch_data(url: str, driver_path : str) -> str:
    try:
        driver = webdriver.Chrome(driver_path)
        driver.get(url)
        curr_data = driver.find_elements_by_class_name("forecastbox")
        raw_dat = []
        for v in curr_data:
            raw_dat.append(v.text)
        t_text = ''
        for z in raw_dat:
            if len(z) > 0:
                t_text = z
        return t_text
    except:
        print("Failed on fetching forecast")


def process_text(text: str, curr_list : list, c_url : str) -> dict:
    try:
        curr_url = c_url
        divi = curr_list[1]
        definer = curr_url.split('#')
        stio = ''
        if len(curr_url.split('#')) > 1:
            t_string = definer[1]
            res = re.sub(r'[^a-zA-Z]', ' ', t_string)
            res = re.sub(' +', ' ', res)
            stio = res
        else:
            stio = divi

        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y")
        pre_ev = re.findall("[-+]?(?:\d*\.\d+|\d+)", text)
        packaged_data = {
        "Date" : dt_string ,
        "Station" : stio,
        "TempMax" : pre_ev[0],
        "TempMin" : pre_ev[1],
        "RainMM" : pre_ev[6], 
        "HUmidMorn" : pre_ev[12],
        "HUmidEve" : pre_ev[13], 
        "SurfPressure" : pre_ev[14],
        "Wind" : pre_ev[7],
        "Sunrise" : pre_ev[2] + ":" + pre_ev[3],
        "Sundown" : str((int(pre_ev[4]) + 12)) + ":" + pre_ev[5]}
        return packaged_data
    except:
        print("Failed to process data")


def get_data(st_data : list, driver_path : string) -> list:
    
    f_pckg = []
    for v in st_data:
        urlz = v[0]
        for b in urlz:
            f_pckg = f_pckg + [
                process_text(fetch_data(b, driver_path),v, b)
            ]
