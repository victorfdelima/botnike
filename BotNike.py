#!/usr/bin/env python
# coding: utf-8

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
driver.find_element_by_name('emailAddress').send_keys('vittinferreira@gmail.com', Keys.TAB);
time.sleep(0.5);
driver.find_element_by_name('password');
time.sleep(0.5);
driver.find_element_by_name('password').send_keys('82384580vV!');
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
time.sleep(2)
driver.find_element_by_id('ccard-number').click()
time.sleep(2)
driver.find_element_by_id('ccard-number').send_keys('4716 6217 2264 7088', Keys.TAB)
time.sleep(2)
driver.find_element_by_id('ccard-owner').click()
time.sleep(1)
driver.find_element_by_id('ccard-owner').send_keys('Jefferson Lucas Gomes', Keys.TAB)
time.sleep(1)
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


#Inputa o numero do telefone e aguarda 4 segundos para clicar



#driver.find_element_by_xpath('/html/body/main/div[1]/div[8]/div[2]/div[5]/a').click()
#time.sleep(1)

#bot da nike entra no site (done)
#faz login (done)
#coloca um produto no carrinho (done)
#Deixa o checkout pronto com o produto()
#Na aba nova retira o produto antigo()
#Pede SMS, autentica o SMS()
#coloca no carrinho o tenis
#Faz o checkout do SKU adicionado no Config.json no checkout da aba anterior.
