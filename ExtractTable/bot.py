from botcity.web import WebBot, Browser, By
from botcity.web.parsers import table_to_dict
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

def main():

    bot = WebBot()

    bot.headless = False

    bot.browser = Browser.CHROME

    bot.driver_path = ChromeDriverManager().install()

    bot.browse("https://www.w3schools.com/html/html_tables.asp")

    bot.maximize_window()

    #extraindo uma tabela e salvando em um csv
    tabela = bot.find_element('customers', By.ID, waiting_time=40000, ensure_visible=True)

    dados = table_to_dict(tabela)

    print(dados)

    bot.stop_browser()

    df = pd.DataFrame(dados)
    
    df.to_csv('Customers.csv', sep=',', index=False)

if __name__ == '__main__':
    main()
