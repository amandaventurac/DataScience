import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb

def ler_dados_csv():
	global dados_principais
	dados_principais = pd.read_csv("dados_preventivo_sus.csv", header = 0)
	return dados_principais

ler_dados_csv()

def ler_dados_estados():
	global lista_estado, lista_municipio
	#a primeira coluna deste dataframe apresenta uma concatenação dentre estado e municipio
	#preciso dividir em duas colunas para ler corretamente
	dados_estados = open("lista_Municípios_com_IBGE_Brasil_Versao_CSV.csv", "r", encoding = "cp1252")
	lista_estado = []
	lista_municipio = []
	for line in dados_estados:
		primeira_coluna = line.split(';')[0]
		estado_com_espaco  = primeira_coluna[:2]
		estado_sem_espaco = estado_com_espaco.split(" ")[0]
		lista_estado.append(estado_sem_espaco)
		lista_municipio.append(primeira_coluna[2:].lower())
	dados_estados.close()
	dados_estados_adicionais = open('municipios_adicionais.txt', 'r')
	for line in dados_estados_adicionais:
		lista_municipio.append((line.split(';')[0]).lower())
		estado_com_skipline  = (line.split(';')[1])
		estado_sem_skipline = estado_com_skipline.split("\n")[0]
		estado_sem_skipline_sem_espaço = estado_sem_skipline.split(" ")[0]
		lista_estado.append(estado_sem_skipline_sem_espaço)
	dados_estados_adicionais.close()
	return lista_estado, lista_municipio

ler_dados_estados()


def classificar_estados(dados_principais, lista_municipio, lista_estado):
	global estado_segundo_municipio, estado_encontrado
	estado_segundo_municipio = []
	for i in range (0,len(dados_principais['no_cidade'])):
		municipio = dados_principais['no_cidade'][i]
		estado_encontrado = 0
		busca_estado_segundo_municipio(municipio,lista_municipio, lista_estado, estado_encontrado, estado_segundo_municipio)
	dados_principais['estado_segundo_municipio'] = np.asarray(estado_segundo_municipio)
	return dados_principais

def busca_estado_segundo_municipio(municipio, lista_municipio, lista_estado, estado_encontrado, estado_segundo_municipio):
	for a in range (0, len(lista_municipio)): 
		if lista_municipio[a] == municipio.lower():
			estado_encontrado = lista_estado[a]
	estado_segundo_municipio.append(estado_encontrado)
	return estado_encontrado, estado_segundo_municipio
	
classificar_estados(dados_principais, lista_municipio, lista_estado)


def plota_media_estados(dados_principais, estado_segundo_municipio):
	media_por_estados = dados_principais.groupby(['estado_segundo_municipio']).mean()
	print(media_por_estados)
	plt.xlabel('Estados')
	plt.ylabel("Número de exames de exames \n sobre a população de interesse")
	plt.title("Razão entre exames citopatológicos \n de colo do útero em mulheres de 25 a 59 anos \n de 12/2008 a 12/2011")
	plt.savefig('result.png', dpi = 300)
plota_media_estados(dados_principais, estado_segundo_municipio)