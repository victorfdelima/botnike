from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.expected_conditions import presence_of_element_located
import time

#ABRE O FIREFOX E ENTRA NO SITE DA NIKE

botName = 'Maxmilliam Bot'
driver = webdriver.Firefox();
driver.maximize_window()
driver.get("https://unite.nike.com.br/oauth.html?client_id=QLegGiUU042XMAUWE4qWL3fPUIrpQTnq&redirect_uri=https%3A%2F%2Fwww.nike.com.br%2Fapi%2Fv2%2Fauth%2Fnike-unite%2Fset&response_type=code&locale=pt_BR&state=%2F");
time.sleep(1);
print(f"{botName} Diz: Entrei no site..!")

#INPUTA OS DADOS, EMAIL E SENHA
time.sleep(1);
driver.find_element_by_name('emailAddress').click();
time.sleep(0.7);
driver.find_element_by_name('emailAddress').send_keys('lucasjefferson00@gmail.com', Keys.TAB);
time.sleep(0.5);
driver.find_element_by_name('password');
time.sleep(0.5);
driver.find_element_by_name('password').send_keys('Saw50812@');
time.sleep(0.8);

#CLICA NO BOTÃO DE LOGIN
driver.find_element_by_xpath('/html/body/div[7]/form/div[6]/input').click();
print(f"{botName} Diz: Consegui fazer login!");
time.sleep(3);

#Coloca um produto qualquer no carrinho
time.sleep(3);
driver.get('https://www.nike.com.br/chuteira-nike-tiempo-legend-9-academy-infantil-67-80-83-337420?gridPosition=A4');
time.sleep(1);
print(f"{botName} Diz: Colocando Produto fake");
#Ignora os demais popups
driver.find_element_by_xpath('/html/body/div[4]/div/a').click();
time.sleep(1);
driver.execute_script("window.scrollTo(0, 200)");
time.sleep(1);
driver.find_element_by_css_selector('#variacoesTamanhos > ul > li:nth-child(2) > label').click();
time.sleep(2);
driver.find_element_by_css_selector('#btn-comprar').click();
time.sleep(2);
driver.find_element_by_xpath('/html/body/header[1]/div[1]/div/div/div[2]/span[3]/div[2]/div/div[2]/div[2]/a[2]').click();
time.sleep(1);
print(f"{botName} Diz: Ignorando Popups");

#Abre uma nova aba com o produto SNKRS
driver.execute_script("window.open('');")
time.sleep(1)
driver.switch_to.window(driver.window_handles[1])
driver.get('https://www.nike.com.br/dunk-low-153-169-211-345295');
time.sleep(2);
print(f"{botName} Diz: Abri uma nova aba e adicionarei o produto ao carrinho")
#Aceita os coockies do site. (Só é possível clicar no botão de compra com os coockies aceitos)
#driver.find_element_by_xpath('/html/body/div[4]/div/a').click()
#time.sleep(2);

#Rola até o meio da página
driver.execute_script("window.scrollTo(0, 500)")
time.sleep(2);
driver.find_element_by_css_selector('#variacoes > div > ul > li:nth-child(6) > label').click();
time.sleep(2);
driver.find_element_by_css_selector('#btn-comprar').click()
time.sleep(1);
print(f"{botName} Diz:  Pronto! Agora irei autenticar via SMS..")
# Adiciona humanamente um numero de celular para receber SMS
driver.find_element_by_name('CelularCliente').send_keys('3')
time.sleep(2)
driver.find_element_by_name('CelularCliente').send_keys('1')
time.sleep(0.3)
driver.find_element_by_name('CelularCliente').send_keys('9')
time.sleep(0.3)
driver.find_element_by_name('CelularCliente').send_keys('9')
time.sleep(0.3)
driver.find_element_by_name('CelularCliente').send_keys('3')
time.sleep(0.3)
driver.find_element_by_name('CelularCliente').send_keys('6')
time.sleep(0.3)
driver.find_element_by_name('CelularCliente').send_keys('7')
time.sleep(0.3)
driver.find_element_by_name('CelularCliente').send_keys('8')
time.sleep(0.3)
driver.find_element_by_name('CelularCliente').send_keys('6')
time.sleep(0.3)
driver.find_element_by_name('CelularCliente').send_keys('9')
driver.find_element_by_name('CelularCliente').send_keys('1', Keys.RETURN)
time.sleep(0.2)
print(f"{botName} Diz: Autenticando..")
time.sleep(0.2)
print(f"{botName} Diz: Quase la..")
time.sleep(20)
# Método para realizar contagem em segundos para inputar código enviado para o celular
for c in range(20, -1, -1):
    c = c - 0
    time.sleep(1)
    print("Você tem {} segundos para inputar o código..".format(c))


driver.find_element_by_xpath('/html/body/div[19]/div/div/div[2]/form[2]/div[2]/button[1]').click()
time.sleep(3)
driver.find_element_by_css_selector('div.ckt__linha-produto:nth-child(2) > div:nth-child(5) > a:nth-child(1)').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/main/div[4]/div/div[4]/a').click()
time.sleep(1.5)
driver.find_element_by_id('seguir-pagamento').click()
time.sleep(2)
driver.find_element_by_css_selector('button.undefined:nth-child(1)').click()
print(f"{botName} Diz:  Addicionando dados do cartão agora...")
time.sleep(2)

# Inputa os dados do cartão para pagamento

driver.find_element_by_id('ccard-number').click()
time.sleep(2)
driver.find_element_by_id('ccard-number').send_keys('4716 6217 2264 7088', Keys.TAB)
time.sleep(2)
driver.find_element_by_id('ccard-owner').click()
time.sleep(1)
driver.find_element_by_id('ccard-owner').send_keys('Jefferson Lucas Gomes', Keys.TAB)
time.sleep(1)
# Adiciona o CPF
driver.find_element_by_id('ccard-document').send_keys('5', Keys.TAB)
time.sleep(0.3)
driver.find_element_by_id('ccard-document').send_keys('5', Keys.TAB)
time.sleep(0.3)
driver.find_element_by_id('ccard-document').send_keys('5', Keys.TAB)
time.sleep(0.3)
driver.find_element_by_id('ccard-document').send_keys('5', Keys.TAB)
time.sleep(0.3)
driver.find_element_by_id('ccard-document').send_keys('5', Keys.TAB)
time.sleep(0.3)
driver.find_element_by_id('ccard-document').send_keys('5', Keys.TAB)
time.sleep(0.3)
driver.find_element_by_id('ccard-document').send_keys('5', Keys.TAB)
time.sleep(0.3)
driver.find_element_by_id('ccard-document').send_keys('5', Keys.TAB)
time.sleep(0.3)
driver.find_element_by_id('ccard-document').send_keys('5', Keys.TAB)
time.sleep(0.3)
driver.find_element_by_id('ccard-document').send_keys('5', Keys.TAB)
time.sleep(0.3)
driver.find_element_by_id('ccard-document').send_keys('5', Keys.TAB)
time.sleep(0.5)
# Coloca a data de validade do cartão
print(f"{botName} Diz:  Escolhendo a data exata do cartão")
driver.find_element_by_css_selector('#exp-month').click()
time.sleep(0.5)
driver.find_element_by_css_selector('#exp-month > option:nth-child(4)').click()
time.sleep(0.5)
driver.find_element_by_css_selector('#exp-year').click()
time.sleep(0.5)
driver.find_element_by_css_selector('#exp-year > option:nth-child(9)').click()
time.sleep(1)
# Aceita política de privacidade
print(f"{botName} Diz:  Pronto, agora aceitando os termos e políticas...")
driver.find_element_by_css_selector('#security-code').send_keys('892')
time.sleep(0.6)
driver.find_element_by_css_selector('#linkTrocasCancelamentos').click()
time.sleep(1)
driver.find_element_by_css_selector('.false > button:nth-child(1)').click()
time.sleep(1)
print(f"{botName} Diz:  Confirmando o pagamento...")
# Clica no botão de pagar
driver.find_element_by_css_selector('#confirmar-pagamento').click()