from botcity.web import WebBot, Browser, By
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager

def inicializa_navegador(bot):

    bot.headless = False
    bot.browser = Browser.CHROME
    bot.driver_path = ChromeDriverManager().install()
    bot.browse("https://docs.google.com/forms/d/e/1FAIpQLSfWBhBnzkAfK3UCrHVG3mCud9e0L4ILu3DCScGLxMjpiP5_xQ/viewform?pli=1")
    bot.maximize_window() 

def leitura_arquivo():

    df = pd.read_excel('Data.xlsx')
    return df

def inserindo_dados(bot, dados):
    
    for index, linha in dados.iterrows():

        input_nome = bot.find_element("//div[contains(@data-params, 'Name')]//input", By.XPATH, waiting_time=30000, ensure_clickable=True)
        input_nome.send_keys(linha['Name'])

        input_idade = bot.find_element("//div[contains(@data-params, 'Age')]//input", By.XPATH, waiting_time=30000, ensure_clickable=True)
        input_idade.send_keys(linha['Age'])

        input_cidade = bot.find_element("//div[contains(@data-params, 'City')]//input", By.XPATH, waiting_time=30000, ensure_clickable=True)
        input_cidade.send_keys(linha['City'])

        botao_submit = bot.find_element("//span[text()='Enviar']", By.XPATH)
        botao_submit.click()

        outra_resposta = bot.find_element("//a[text()='Enviar outra resposta']", By.XPATH, waiting_time=50000, ensure_clickable=True)
        outra_resposta.click()

        

def encerrar_navegador(bot):
    
    bot.wait(3000)
    bot.stop_browser()


if __name__ == '__main__':

    bot = WebBot()

    inicializa_navegador(bot)

    dados = leitura_arquivo()

    inserindo_dados(bot, dados)

    encerrar_navegador(bot)

