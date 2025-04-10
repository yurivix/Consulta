from flask import Flask, request, render_template
from zeep import Client

app = Flask(__name__)

# URL do WSDL do TJES
WSDL_URL = 'https://pje.tjes.jus.br/pje/ConsultaPJe?wsdl'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        numero_processo = request.form['numero_processo']
        try:
            client = Client(WSDL_URL)
            # Substitua 'consultarProcesso' pelo método correto do serviço
            response = client.service.consultarProcesso(numeroProcesso=numero_processo)
            return render_template('resultado.html', processo=response)
        except Exception as e:
            return f"Erro ao consultar o processo: {e}"
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
