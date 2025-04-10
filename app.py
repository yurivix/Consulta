from flask import Flask, render_template, request
from zeep import Client
import os

app = Flask(__name__)

# Substitua por seu caminho local ao certificado se necessário
WSDL_URL = "https://pje.tjes.jus.br/pje/intercomunicacao?wsdl"
client = Client(WSDL_URL)

@app.route("/", methods=["GET", "POST"])
def index():
    processo_data = None
    if request.method == "POST":
        numero_processo = request.form["numero_processo"]
        try:
            # Aqui você precisa substituir pela chamada correta ao método do serviço do TJES
            # Abaixo é um exemplo genérico e pode variar dependendo do WSDL
            response = client.service.consultarProcesso(numero_processo)

            processo_data = {
                "numero": response.numeroProcesso,
                "classe": response.classe,
                "assunto": response.assunto,
                "partes": response.partes,
                "movimentacoes": response.movimentacoes
            }

        except Exception as e:
            processo_data = {"erro": str(e)}

    return render_template("index.html", processo=processo_data)

if __name__ == "__main__":
    app.run(debug=True)
