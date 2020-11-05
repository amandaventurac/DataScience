import pandas as pd 


def relacionar_siglas_com_nomes_estados(camiho_arquivo_siglas_estados):
	global estados_siglas, estados_nomes
	input_siglas_nomes = open(camiho_arquivo_siglas_estados, "r")
	estados_siglas = []
	estados_nomes = []
	for line in input_siglas_nomes:
		line = line.split("\n")[0]
		if len(line) == 2:
			estados_siglas.append(line)
		if len(line) >2:
			estados_nomes.append(line)
	return estados_siglas, estados_nomes

relacionar_siglas_com_nomes_estados("estados_e_siglas.txt")

def importar_df_densidade_populacional_com_siglas(estados_siglas, estados_nomes, arquivo_densidade_populacional):
	global dados_densidade_populacional
	dados_densidade_populacional = pd.read_csv(arquivo_densidade_populacional, header = 4, )
	dados_densidade_populacional.columns = ['estado', '1872','1890','1900','1920','1940','1950','1960','1970','1980','1991','2000','2010']
	coluna_sigla_estados = []
	for element in range(0, len(dados_densidade_populacional['estado'])):
		coluna_sigla_estados.append('0')
	for element in range (0,len(dados_densidade_populacional['estado'])):
		for i in range (0, len (estados_nomes)):
			try:
				if estados_nomes[i].upper() == dados_densidade_populacional['estado'][element].upper():
					coluna_sigla_estados[element] = estados_siglas[i]
		
			except:
				pass
	dados_densidade_populacional['sigla estado'] = coluna_sigla_estados
	return dados_densidade_populacional

importar_df_densidade_populacional_com_siglas(estados_siglas, estados_nomes, "densidade_demografica_estados.csv")

def adicionar_densidade_populacional_arquivo_exames(dados_densidade_populacional, arquivo_exames_caminho, arquivo_output_caminho):
	arquivo_exames = open(arquivo_exames_caminho, "r")
	lista_densidade_populacional = []
	for line in arquivo_exames:
		sigla_arquivo_exames =  line.split(',')[0]
		for i in range (0,len(dados_densidade_populacional['sigla estado'])):
			sigla_df_densidade_populacional = dados_densidade_populacional['sigla estado'][i]
			if sigla_arquivo_exames == sigla_df_densidade_populacional:
				densidade_string_virgula = dados_densidade_populacional['2010'][i]
				densidade_string_ponto = densidade_string_virgula.split()[0] .replace(',','.')
				lista_densidade_populacional.append(densidade_string_ponto)
	arquivo_exames.close()
	arquivo_exames = open(arquivo_exames_caminho, "r")
	arquivo_output = open(arquivo_output_caminho, 'w+')
	indice_lista_densidade_populacional = 0
	for line in arquivo_exames:
		arquivo_output.write(line.split('\n')[0] + ',' + lista_densidade_populacional[indice_lista_densidade_populacional])
		arquivo_output.write('\n')
		indice_lista_densidade_populacional += 1
		print('1')
	arquivo_output.close()
	arquivo_exames.close()


adicionar_densidade_populacional_arquivo_exames(dados_densidade_populacional, "media_exames_por_estado.txt", 'media_exames_por_estado_com_densidade_demografica.txt')
