import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
import math
import datetime

html = requests.get('https://www.linkedin.com.br/jobs/search/?currentJobId=3509470930&f_E=1&f_JT=F&geoId=106057199&keywords=Marketing%20E%20Publicidade&location=Brasil').content

soup = BeautifulSoup(html, 'html.parser')
nome = soup.find(class_="base-search-card__title").get_text().strip()
quantidade_vagas = soup.find(class_="results-context-header__job-count").get_text().strip()

print(quantidade_vagas)
print(nome)

dic_vagas = {'Vaga':[], 'Empresa':[], 'Local':[], 'Tipo de contratação':[], 'Nível de experiência':[], 'Data da postagem':[], 'Horário':[]}

for i in range(1, int(quantidade_vagas)+1):
    url_pag = f'https://www.linkedin.com.br/jobs/search/?currentJobId=3509470930&f_E=1&f_JT=F&geoId=106057199&keywords=Marketing%20E%20Publicidade&location=Brasil'
    soup = BeautifulSoup(html, 'html.parser')
    vagas = soup.find_all(class_=re.compile("base-search-card__info"))
    
    for info in vagas:
        vaga = info.find(class_=re.compile("base-search-card__title")).get_text().strip()
        empresa = info.find(class_=re.compile("base-search-card__subtitle")).get_text().strip()
        local = info.find(class_=re.compile("job-search-card__location")).get_text().strip()
        Tipo_contratação = "Tempo integral"
        Nível_experiência = "Estágio"
        Data_postagem = info.find(class_=re.compile("job-search-card__listdate")).get_text().strip()
        horas = datetime.datetime.now()


        print(vaga ,empresa, local, Tipo_contratação, Nível_experiência, Data_postagem, horas)

        dic_vagas['Vaga'].append(vaga)
        dic_vagas['Empresa'].append(empresa)
        dic_vagas['Local'].append(local)
        dic_vagas['Tipo de contratação'].append(Tipo_contratação)
        dic_vagas['Nível de experiência'].append(Nível_experiência)
        dic_vagas['Data da postagem'].append(Data_postagem)
        dic_vagas['Horário'].append(horas)

df = pd.DataFrame(dic_vagas)
df.to_csv('C:/Users/adm/Desktop/Nova pasta/vagas.csv', encoding='ISO-8859-1', sep=';')
      

