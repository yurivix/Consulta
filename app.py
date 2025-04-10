from flask import Flask, render_template, request, redirect, url_for
import uuid

app = Flask(__name__)
processos = {}  # Armazena os processos em memória temporariamente

@app.route('/')
def index():
    return '''
        <h2>Enviar Novo Processo</h2>
        <form method="post" action="/novo">
            <textarea name="dados" rows="20" cols="100" placeholder='Cole os dados em JSON aqui'></textarea><br>
            <input type="submit" value="Enviar">
        </form>
    '''

@app.route('/novo', methods=['POST'])
def novo_processo():
    import json

    try:
        dados = json.loads(request.form['dados'])
    except Exception as e:
        return f'<p>Erro ao interpretar os dados: {e}</p><a href="/">Voltar</a>'

    processo_id = str(uuid.uuid4())  # gera ID único
    processos[processo_id] = dados
    return redirect(url_for('resumo_processo', processo_id=processo_id))

@app.route('/resumo/<processo_id>')
def resumo_processo(processo_id):
    dados = processos.get(processo_id)
    if not dados:
        return "<p>Processo não encontrado</p>"

    return render_template('resumo.html',
                           autora=dados.get('autora'),
                           reus=dados.get('reus'),
                           processo_id=processo_id)
