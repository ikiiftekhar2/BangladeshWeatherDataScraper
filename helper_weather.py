from selenium import webdriver
from selenium.webdriver.chrome.options import Options

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
        print("OOpsie on fetching data")

def process_text(text: str) -> list:
    
