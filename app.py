from flask import Flask, render_template, request
from zeep import Client
from zeep.transports import Transport
from zeep.exceptions import Fault
import requests

app = Flask(__name__)

# URL do WSDL do TJES
WSDL_URL = 'https://pje.tjes.jus.br/pje/intercomunicacao?wsdl'

# Consulta os dados do processo no WSDL do TJES
def consultar_processo(numero_processo):
    try:
        session = requests.Session()
        transport = Transport(session=session)
        client = Client(WSDL_URL, transport=transport)

        response = client.service.consultarProcesso(numeroProcesso=numero_processo)
        
        return response
    except Fault as e:
        print(f"Erro na consulta ao WSDL: {e}")
        return None
    except Exception as e:
        print(f"Erro geral: {e}")
        return None

@app.route('/', methods=['GET', 'POST'])
def index():
    processo_info = None
    if request.method == 'POST':
        numero_processo = request.form['numero_processo']
        processo_info = consultar_processo(numero_processo)

    return render_template('index.html', processo_info=processo_info)

if __name__ == '__main__':
    app.run(debug=True)
