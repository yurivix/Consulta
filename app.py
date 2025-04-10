from flask import Flask, render_template

app = Flask(__name__)

@app.route('/resumo')
def resumo():
    autora = {
        'Nome': 'Graziela Ortega Marinho',
        'CPF': '071.767.097-00',
        'Nascimento': '06/03/1976',
        'Sexo': 'Feminino',
        'Mãe': 'Noemi Regina Mendonça Ortega',
        'Endereço': 'Rua Desembargador Augusto Botelho, nº 830 – Praia da Costa, Vila Velha/ES – CEP: 29101-110',
        'Advogado': 'Yuri Iglezias Viana – OAB/ES 22668A – CPF: 104.888.067-20'
    }

    reus = [
        {
            'nome': 'Unimed Vitória',
            'dados': {
                'CNPJ': '27.578.434/0001-20',
                'Fundação': '11/04/1980',
                'Endereço': 'Av. Cezar Hilal, nº 700 – Bento Ferreira, Vitória/ES – CEP: 29050-903'
            }
        },
        {
            'nome': 'AllCare',
            'dados': {
                'CNPJ': '07.674.593/0001-10',
                'Endereço': 'Alameda Santos, 1357, 7º andar – São Paulo/SP – CEP: 01419-001',
                'Advogado': '''Luiz Guilherme Mendes Barreto – OAB/SP 200863A – CPF: 250.298.778-43<br>
                               Endereço: Rua Ricardo Avenarius, 1021, Casa 6 – São Paulo/SP – CEP: 05665-020'''
            }
        },
        # ...adicione os outros réus aqui no mesmo formato...
    ]

    return render_template('resumo.html', autora=autora, reus=reus)

