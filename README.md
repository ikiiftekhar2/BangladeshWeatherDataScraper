# BangladeshWeatherDataScraper
This repository scrapes and uploads daily at a given schedule to Google Sheets

STEP BY STEP instructions:

1) Download python any version will work => 3.6
2) Check your current version of Chrome. Use this link to download the required version https://chromedriver.chromium.org/downloads
3) After downloading chromedriver in a known location, copy the file path.
4) Open workin_datas.py as a text file using note pad and change the directory of the variable "driver_path" to your location (They should look similar)
5) Edit the e_time variable in the same file to your convinient time.
6) Open Command Prompt and type cd following by the filepath of the extracted folder
7) Run "pip install -r requirements.txt" inside command prompt
8) Run "python main.py" and it should work automatically.
9) The program will stay active 24/7 and will show a black screen which means its working. (If it fails on certain things it will automatically throw error)
10) In order to interact less with Command Prompt you may use this two step process from this link https://datatofish.com/batch-python-script/
11) ENJOY. P.S If you know the link you know ;-))


FOR CUSTOM Google Sheets Documents


1) Follow until Step 5
2) Go the keys.json file and copy the "client_email" variable's email and go to your Google Sheets and share to this email as editor.
3) YOU MAY BREAK THE FILE IN THE STEP BELOW
4) Edit the value for SAMPLE_SPREADSHEET_ID in line 94 of helper_weather.py with your spreadsheet. GUIDE: https://developers.google.com/sheets/api/guides/concepts
5) Continue from Step 6
