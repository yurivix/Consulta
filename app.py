from flask import Flask, request, render_template
from zeep import Client
from zeep.transports import Transport
import os

app = Flask(__name__)

# Variáveis de ambiente
ID_CONSULTANTE = os.getenv('ID_CONSULTANTE')
SENHA_CONSULTANTE = os.getenv('SENHA_CONSULTANTE')

# WSDL do serviço
WSDL_URL = 'https://pje.tjes.jus.br/pje/intercomunicacao?wsdl'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        numero_processo = request.form['numero_processo']

        try:
            client = Client(wsdl=WSDL_URL)

            # Chamada com todos os parâmetros obrigatórios
            response = client.service.consultarProcesso(
                idConsultante=ID_CONSULTANTE,
                senhaConsultante=SENHA_CONSULTANTE,
                numeroProcesso=numero_processo
            )

            return render_template('resultado.html', processo=response)

        except Exception as e:
            return f"Erro ao consultar o processo: {e}"

    return render_template('index.html')
