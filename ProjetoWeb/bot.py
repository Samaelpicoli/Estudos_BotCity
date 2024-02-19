# Import for the Web Bot
from botcity.web import WebBot, Browser, By, element_as_select
from webdriver_manager.chrome import ChromeDriverManager
import requests
import pandas as pd

url = 'https://aai-devportal-media.s3.us-west-2.amazonaws.com/challenges/customer-onboarding-challenge.csv'
arquivo = requests.get(url, allow_redirects=True)
open('MissingCustomers.csv', 'wb').write(arquivo.content)

dados = pd.read_csv('MissingCustomers.csv', sep = ',')
print(dados)

bot = WebBot()
bot.headless = False
bot.browser = Browser.CHROME
bot.driver_path = ChromeDriverManager().install()
bot.browse("https://developer.automationanywhere.com/challenges/automationanywherelabs-customeronboarding.html")
bot.wait(1000)
bot.maximize_window()


for coluna in dados.itertuples():
    bot.find_element('customerName', By.ID, waiting_time=40000, ensure_clickable=True).send_keys(coluna[1])
    bot.find_element('customerID', By.ID).send_keys(coluna[2])
    bot.find_element('primaryContact', By.ID).send_keys(coluna[3])
    bot.find_element('street', By.ID).send_keys(coluna[4])
    bot.find_element('city', By.ID).send_keys(coluna[5])
    estado = bot.find_element('state', By.ID)
    element_as_select(estado).select_by_value(coluna[6])
    bot.find_element('zip', By.ID).send_keys(coluna[7])
    bot.find_element('email', By.ID).send_keys(coluna[8])
    if coluna[9] == 'YES':
        bot.find_element('activeDiscountYes', By.ID).click()
    else:
        bot.find_element('activeDiscountNo', By.ID).click()
    
    if coluna[10] == 'NO':
        bot.find_element('NDA', By.ID).click()

    bot.find_element('submit_button', By.ID).click()

bot.find_element('btn-modal', By.ID, waiting_time=30000, ensure_clickable=True)
bot.screenshot('Acuracia.png')
bot.stop_browser()





