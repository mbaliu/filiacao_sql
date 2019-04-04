#-*-coding: utf8-*-

#import bs4
from selenium import webdriver
#import pandas as pd


# Carrega e abre uma aplicação do chrome
def load_chrome():
	global driver
	driver = webdriver.Chrome(r'..\\chromedriver.exe')
	#driver = webdriver.Chrome(r'C:\Users\x417028\Desktop\Arq\chromedriver.exe')
	


# Carrega a página desejada (Geo Sampa)
def load_page(site='prodam'):
	# Escolha entre o site da prodam ou o do cidadão
	if site == 'prodam':
		site = 'http://mapas.geosampa.prodam/PaginasPublicas/_SBC.aspx'
	else:
		site = 'http://geosampa.prefeitura.sp.gov.br/PaginasPublicas/_SBC.aspx'

	# Carrega o site
	driver.get(site)

def botao_pesquisar():
	#Remove a janela de boas-vindas
	driver.find_element_by_xpath("//div[@class='close']").click()
	
	# Clica no botão PESQUISAR
	driver.find_element_by_xpath("//*[@class='ctlBtnPesquisaLogradouroItemInactive olButton']").click()
	
	# Seleciona a ABA desejada - Integração
	aba = 'IPTU'
	aba = 'Integração'
	driver.find_element_by_xpath("//area[@alt='{}']".format(aba)).click()

	# Seleciona a OPÇÃO desejada - filiação
	opcao = 'Filiação de Lotes'
	driver.find_element_by_xpath("//select[@id='cboSerieIntegracao']/option[text()='{}']".format(opcao)).click()

	'''
	driver.find_element_by_xpath("//select[@id='cboTipoMapaArticulado']/option[text()='Ortofotos 2004']").click()
	driver.find_element_by_class_name('ctlBtnPesquisaLogradouroItemInactive olButton')
	"//div[@id='OpenLayers_Control_Panel_535'][@title='Pesquisar']"
	'''

def set_input(sql='0011112222'):
	# Completa com o SQL
	

	setor =  sql[:3]
	quadra = sql[3:6]
	lote =   sql[6:10]
	cond =   sql[10:]


	element = driver.find_element_by_xpath("//input[@name='TxtIntSetor']")
	element.send_keys(setor)
	
	element = driver.find_element_by_xpath("//input[@name='TxtIntQuadra']")
	element.send_keys(quadra)

	element = driver.find_element_by_xpath("//input[@name='TxtIntLote']")
	element.send_keys(lote)

	# Solicita a procura do SQL
	driver.find_element_by_xpath("//input[@id='BtnIntegracao']").click()

def get_data():
	# Identifica os dados de PAI


	# Identifica os dados de FILHO


def save_data():
	
