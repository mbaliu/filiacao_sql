#-*-coding: utf8-*-

import bs4
from selenium import webdriver
#import pandas as pd


# Carrega e abre uma aplicação do chrome
def load_chrome():
	global driver
	driver = webdriver.Chrome(r'..\\chromedriver.exe')
	#driver2 = webdriver.Ie(r'..\\IEDriverServer.exe')
	


# Carrega a página desejada (Geo Sampa)
def load_page(site=''):
	# Escolha entre o site da prodam ou o do cidadão
	if site == 'prodam':
		site = 'http://mapas.geosampa.prodam/PaginasPublicas/_SBC.aspx'
	else:
		site = 'http://geosampa.prefeitura.sp.gov.br/PaginasPublicas/_SBC.aspx'

	# Carrega o site
	driver.get(site)

def botao_pesquisar():
	# FEcha a janela de boas-vindas
	driver.find_element_by_xpath("//div[@class='close']").click()
	
	# Clica no botão PESQUISAR
	driver.find_element_by_xpath("//*[@class='ctlBtnPesquisaLogradouroItemInactive olButton']").click()
	
	# Seleciona a ABA desejada - Integração
	aba = 'Integração'
	driver.find_element_by_xpath("//area[@alt='{}']".format(aba)).click()

	# Seleciona a OPÇÃO desejada - filiação
	opcao = 'Filiação de Lotes'
	driver.find_element_by_xpath("//select[@id='cboSerieIntegracao']/option[text()='{}']".format(opcao)).click()

	
	
	'''
	Códigos de referencia - obsoletos
	driver.find_element_by_xpath("//select[@id='cboTipoMapaArticulado']/option[text()='Ortofotos 2004']").click()
	driver.find_element_by_class_name('ctlBtnPesquisaLogradouroItemInactive olButton')
	"//div[@id='OpenLayers_Control_Panel_535'][@title='Pesquisar']"
	'''

def set_input(sql='1112223333'):
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
	# CASO 1 - Não há registros
	# Identifica que não há resposta
	element = driver.find_element_by_xpath("//div[@id='popup_message']")
	if element:
		driver.find_element_by_xpath("//div[@id='popup_panel']/input[@type='button']").click()
		continue
		
	# Identifica se tem resposta
	element = driver.find_element_by_xpath("//div[@id='divDadosIntegracao']")
	if element:
		pass
	
	# Identifica os dados de PAI
	####### id='gbox_T_02824' não funciona - talvez class='ui-jqgrid-btable'
	#//td[@id='gridDadosIntegracaoB']//table[@class="ui-jqgrid-btable"] PAI
	#//td[@id='gridDadosIntegracaoC']//table[@class="ui-jqgrid-btable"] FILHO
	element = driver.find_element_by_xpath("//div[@id='gbox_T_02824']") #funciona??? Verifica se existe a tabela de pai
	if element:
		# TABELA DE PAI
		driver.find_element_by_xpath("//table[@id='T_02824']")
		# Linha
		("//table[@id='T_02824']/tbody/tr[@class='ui-widget-content jqgrow ui-row-ltr']")
		# Encontra os campos da tabela
		rows = driver.find_elements_by_xpath("//table[@id='T_02824']/tbody/tr[@class='ui-widget-content jqgrow ui-row-ltr']")
		for r in rows: # Seleciona todas as linhas menos a primeira que é desnecessária
			# Encontrará todas as células ==========================
			cells = driver.find_elements_by_xpath("//table[@id='T_02824']/tbody/tr[@class='ui-widget-content jqgrow ui-row-ltr']/td")
			for c in cells:
				valor = c.text
				
	else:
		# Não possui PAI
		pass

	# Identifica os dados de FILHO


def save_data():
	pass


'''
range_v = valor.text.split(' ao ')
lotes_range = [v for v in range(range_v[0], range_v[1]+1)]
'''
