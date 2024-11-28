from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given(u'Entro na Página de contato do Instituto Joga Junto')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://www.jogajuntoinstituto.org/#Contato")

@when(u'Insiro meus dados')
def stepInserirDados(context):
    context.driver.find_element(By.ID, "nome").send_keys("Marcio")
    context.driver.find_element(By.ID, "email").send_keys("marcio.techwork@gmail.com")
    context.driver.find_element(By.ID, "assunto").send_keys("Ser facilitador")
    context.driver.find_element(By.ID, "mensagem").send_keys("Quero ser facilitador!!")
    

@when(u'Envio a mensagem "Teste - Hello!"')
def stepEnvioMensagem(context):
    context.driver.find_element(By.ID, "mensagem").send_keys("Teste - Hello!", Keys.TAB, Keys.ENTER)



@then(u'Fecho o navegador')
def fecharNav(context):
    context.driver.quit()