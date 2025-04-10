from flask import Flask, request, render_template
from zeep import Client
from zeep.transports import Transport
from requests.auth import HTTPBasicAuth
import requests
import os

app = Flask(__name__)

# Pegando usuário, senha e idConsultante das variáveis de ambiente
PJE_USER = os.getenv('PJE_USER')
PJE_PASS = os.getenv('PJE_PASS')
ID_CONSULTANTE = os.getenv('ID_CONSULTANTE')  # <-- adicione isso no Render também

# WSDL do serviço de intercomunicação
WSDL_URL = 'https://pje.tjes.jus.br/pje/intercomunicacao?wsdl'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        numero_processo = request.form['numero_processo']

        try:
            # Sessão autenticada
            session = requests.Session()
            session.auth = HTTPBasicAuth(PJE_USER, PJE_PASS)
            transport = Transport(session=session)

            # Cliente SOAP com autenticação
            client = Client(wsdl=WSDL_URL, transport=transport)

            # Consulta ao processo com os dois parâmetros
            response = client.service.consultarProcesso(
                idConsultante=ID_CONSULTANTE,
                numeroProcesso=numero_processo
            )

            return render_template('resultado.html', processo=response)

        except Exception as e:
            return f"Erro ao consultar o processo: {e}"

    return render_template('index.html')
