from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from time import sleep
import gspread
from oauth2client.service_account import ServiceAccountCredentials

options = Options()
options.headless = False #Visivel ou Oculto

navegador = webdriver.Firefox(options=options)

link = "XXXXXXXXXX"

navegador.get(url=link)
sleep(1)

inputUsuario = navegador.find_element(by=By.ID,value="email")
inputUsuario.send_keys("XXXXXXXXXX")
sleep(1)

submitBotao = navegador.find_element(by=By.CSS_SELECTOR,value=".btn").click()
sleep(1)

inputSenha = navegador.find_element(by=By.ID,value="current-password")
inputSenha.send_keys("XXXXXXXXXXXXXXX")
sleep(1)

submitBotao = navegador.find_element(by=By.CSS_SELECTOR,value=".btn").click()
sleep(5)

estatisticasHover = navegador.find_element(by=By.ID,value="menu-estatisticas").click()
sleep(0.6)

feedback = navegador.find_element(by=By.LINK_TEXT,value='Feedback de Oportunidade').click()
sleep(2)

filtros = navegador.find_element(by=By.ID,value="filter-button").click()
sleep(1)

filtrosData = navegador.find_element(by=By.NAME,value="date").click()
sleep(1)

filtrosDataMes = navegador.find_element(by=By.CSS_SELECTOR, value=".ranges > ul:nth-child(1) > li:nth-child(3)").click()
sleep(3)

feedRespondido = navegador.find_element(by=By.CSS_SELECTOR,value="text:nth-child(1)")

acontecidas = navegador.find_element(by=By.CSS_SELECTOR,value="text:nth-child(2)")

acontecidasValor = acontecidas.text
feedRespondidoValor = feedRespondido.text

# Autenticação com o Google Sheets
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX', scopes=scope)
client = gspread.authorize(creds)

# Abra a planilha desejada
planilha = client.open_by_key('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')

# Selecione a folha desejada
folha = planilha.worksheet('XXXXXXXXXXXXXXXXXXXXX')  # Ou use o método get_worksheet(index) para selecionar uma folha por índice
# por exemplo: folha = planilha.get_worksheet(0)

# Escreva o conteúdo na célula específica (C17)
folha.update(range_name='C17', values=[[str(feedRespondidoValor)]])
folha.update(range_name='D17',values=[[str(acontecidasValor)]])




