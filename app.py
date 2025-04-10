from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

# Simulando uma base de dados de processos
DADOS_PROCESSOS = {
    "0000001-00.2020.8.26.0000": {
        "autor": "João da Silva",
        "réu": "Empresa XYZ Ltda",
        "vara": "1ª Vara Cível",
        "data_distribuicao": "15/03/2020",
        "assunto": "Cobrança"
    },
    "0000002-00.2020.8.26.0000": {
        "autor": "Maria Oliveira",
        "réu": "Banco ABC S.A.",
        "vara": "2ª Vara Cível",
        "data_distribuicao": "10/05/2020",
        "assunto": "Empréstimo"
    }
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/buscar_processo', methods=['POST'])
def buscar_processo():
    numero = request.json.get('numero')
    dados = DADOS_PROCESSOS.get(numero)
    if dados:
        return jsonify(dados)
    else:
        return jsonify({"erro": "Processo não encontrado."}), 404

if __name__ == '__main__':
    app.run(debug=True)
