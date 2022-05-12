from stations import *
from working_datas import *
from helper_weather import *
import schedule
import time

def everything():
    all_stations = [dhk_urlz, ctg_urlz, syl_url, mymensingh_url, raj_url, rang_url, khul_url, bar_url]
    draco = get_data(all_stations, driver_path)
    full_send(draco)

schedule.every().day.at(e_time).do(everything)

#while True: 
#    schedule.run_pending()
#    time.sleep(1)