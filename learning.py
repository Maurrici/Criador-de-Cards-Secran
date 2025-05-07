from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd
from datetime import datetime


def setup():
    driver = webdriver.Chrome()
    driver.get("https://secran.digital/admin/cards/add")
    driver.maximize_window()
    return driver

def get_wait(driver):
    return WebDriverWait(driver, 20)    

def login(driver):
    email_field = driver.find_element(by=By.ID, value="login_email")
    password_field = driver.find_element(by=By.ID, value="login_password")
    login_btn = driver.find_element(By.CSS_SELECTOR, "button.ant-btn.ant-btn-primary.ant-btn-lg.ant-btn-block")

    email_field.send_keys("evelyn.mendonca@secran.com.br")
    password_field.send_keys("#Ufcinfo_12")
    login_btn.click()
    time.sleep(5)

def redirect_to_add_page(driver):
    time.sleep(5)
    driver.get("https://secran.digital/admin/cards/add")

def create_card(model, title, date, signed, tag): 
    def select_model():
        # Localiza botão de importar modelo
        links = driver.find_elements(by=By.CSS_SELECTOR, value=".ant-card-extra a")
        link_modelo = None
        for link in links:
            if link.text == "Importar de Modelos de Cards":
                link_modelo = link
                break
        
        if link_modelo:
            link_modelo.click()
        else:
            print("Botão 'Importar Modelo' não encontrado.")
            return
        
        time.sleep(3)

        # Busca o modelo
        search_field = driver.find_element(by=By.CSS_SELECTOR, value=".ant-modal-body span.ant-input-affix-wrapper input")
        search_field.send_keys(model)

        time.sleep(3)

        # Escolhe o modelo
        links = driver.find_elements(by=By.CSS_SELECTOR, value=".ant-table-cell.ant-table-cell-ellipsis a")
        link_modelo_arte = None
        for link in links:
            if link.text == model:
                link_modelo_arte = link
                break
        
        if link_modelo_arte:
            link_modelo_arte.click()
        else:
            print(f"Botão '{model}' não encontrado.")
            return
        
        time.sleep(5)
    
    def set_title():
        title_field = driver.find_element(by=By.ID, value="card_name")
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'})", title_field)

        wait = get_wait(driver)
        wait.until(EC.element_to_be_clickable)

        title_field.send_keys(f" - {title}")

    def select_tag():
        tag_field = driver.find_element(by=By.ID, value="card_tags")
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'})", tag_field)
        
        wait = get_wait(driver)
        wait.until(EC.element_to_be_clickable)

        tag_field.click()
        tag_field.send_keys(tag)
        time.sleep(1)
        options = driver.find_elements(by=By.CLASS_NAME, value="ant-select-item-option-content")

        option_correct = None
        for option in options:
            if option.text == tag:
                option_correct = option
                break
        
        if option_correct:
            option_correct.click()
        else:
            print("Botão 'Tag' não encontrado.")
            return

    def select_signed():
        signed_field = driver.find_element(by=By.ID, value="card_users")
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'})", signed_field)
        
        wait = get_wait(driver)
        wait.until(EC.element_to_be_clickable)

        signed_field.send_keys(signed)
        time.sleep(3)
        options = driver.find_elements(by=By.CLASS_NAME, value="ant-select-item-option-content")

        option_correct = None
        for option in options:
            if option.text.upper() == signed:
                option_correct = option
                break
        
        if option_correct:
            option_correct.click()
        else:
            print("Botão 'Responsável' não encontrado.")
            return

    def set_date():
        date_field = driver.find_element(by=By.ID, value="card_due_date")
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'})", date_field)

        wait = get_wait(driver)
        wait.until(EC.element_to_be_clickable)

        btns_clear = driver.find_elements(by=By.CSS_SELECTOR, value=".ant-picker-clear .anticon.anticon-close-circle")
        btns_clear[1].click()
        date_field.send_keys(date, Keys.ENTER)

    select_model()
    set_title()
    select_tag()
    select_signed()
    set_date()

    btn_save = driver.find_element(By.CSS_SELECTOR, ".ant-btn.ant-btn-primary.sc-eqIVtm.gSDvSK")
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'})", btn_save)
    wait = get_wait(driver)
    wait.until(EC.element_to_be_clickable)
    btn_save.click()

def teardown(driver):
    driver.quit()

df = pd.read_excel("planilha_cards.xlsx", dtype={'Data': str})
driver = setup()
login(driver)

for _, row in df.iterrows():
    modelo = row['Modelo']
    titulo = row['Título']
    data = row['Data']
    responsavel = row['Responsável']
    tag = row['Tag']

    data_obj = datetime.strptime(data, "%Y-%m-%d %H:%M:%S")
    data_formatada = data_obj.strftime("%d/%m/%Y")

    print(modelo, titulo, data_formatada, responsavel, tag)
    redirect_to_add_page(driver)
    time.sleep(5)
    create_card(modelo, titulo, data, responsavel, tag)
    time.sleep(20)

teardown(driver)