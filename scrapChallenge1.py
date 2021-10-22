import requests
from bs4 import BeautifulSoup
import os
url = "https://www.gov.br/ans/pt-br/assuntos/prestadores/padrao-para-troca-de-informacao-de-saude-suplementar-2013-tiss/"
page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")
link = soup.find("a", class_="alert-link internal-link").get("href")
barra = link.split("/")[8]
new_link = url + barra

page = requests.get(new_link)
soup = BeautifulSoup(page.content, "html.parser")
pdf_name = soup.find("a", class_="btn btn-primary btn-sm center-block internal-link").get("href")
pdf = requests.get(pdf_name, stream=True)
try:
    with open(pdf_name.split("/")[10], "wb") as file:
        file.write(pdf.content)
    file.close()
    print("PDF {} baixado com sucesso em {}".format(pdf_name.split("/")[10],os.getcwd()))
except:
    print("Algo deu errado.")