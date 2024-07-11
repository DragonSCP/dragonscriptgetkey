from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def extrair_key_executor_delta(link):
    try:
        # Configuração do navegador
        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--ignore-ssl-errors')

        # Inicialização do WebDriver do Chrome
        driver = webdriver.Chrome(options=options)
        driver.maximize_window()

        # Abrir a página do link fornecido
        driver.get(link)

        # Esperar até que o botão 'Continuar' seja clicável
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'recaptcha-anchor'))).click()

        # Esperar até que o botão 'Watch Video' apareça e clicar nele
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, 'Watch Video'))).click()

        # Esperar 5 segundos após clicar em 'Watch Video'
        time.sleep(5)

        # Clicar em 'Continue' após esperar 5 segundos
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, 'Continue'))).click()

        # Esperar até que a Key seja visível e extrair o texto dela
        key_element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, 'key')))
        key = key_element.text.strip()

        return key

    except Exception as e:
        print(f"Ocorreu um erro: {str(e)}")
        return None

    finally:
        driver.quit()

# URL do link fornecido
link = "https://gateway.platoboost.com/a/8?id=6182101796"

# Extrair a chave executor delta
key_executor_delta = extrair_key_executor_delta(link)

if key_executor_delta:
    print(f"A chave executor delta é: {key_executor_delta}")
else:
    print("Não foi possível extrair a chave executor delta do link fornecido.")
