from flask import Flask, request, render_template
from zeep import Client
from zeep.transports import Transport
from requests.auth import HTTPBasicAuth
import requests
import os

app = Flask(__name__)

# Pegando usuário e senha das variáveis de ambiente
PJE_USER = os.getenv('PJE_USER')
PJE_PASS = os.getenv('PJE_PASS')

# URL do WSDL do PJe/TJES
WSDL_URL = 'https://pje.tjes.jus.br/pje/intercomunicacao?wsdl'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        numero_processo = request.form['numero_processo']

        try:
            # Autenticação via HTTP Basic
            session = requests.Session()
            session.auth = HTTPBasicAuth(PJE_USER, PJE_PASS)
            transport = Transport(session=session)

            # Cria o cliente com autenticação
            client = Client(wsdl=WSDL_URL, transport=transport)

            # Chama o método correto com os parâmetros necessários
            response = client.service.consultarProcesso(numeroProcesso=numero_processo)

            return render_template('resultado.html', processo=response)

        except Exception as e:
            return f"Erro ao consultar o processo: {e}"

    return render_template('index.html')
