from flask import Flask, request, jsonify
from pymongo import MongoClient
import re
import os

app = Flask(__name__)

# Conexão com o MongoDB Atlas
mongo_uri = os.getenv('MONGO_URI')
if not mongo_uri:
    raise Exception("Variável MONGO_URI não configurada")

client = MongoClient(mongo_uri)
db = client.sauron
colecao = db.minha_colecao

# Rota para inserir dados
@app.route('/inserir', methods=['POST'])
def inserir():
    data = request.get_json()
    nome = data.get('nome')
    idade = data.get('idade')

    if not nome or not isinstance(idade, int):
        return jsonify({'erro': 'Dados inválidos'}), 400

    colecao.insert_one({'nome': nome, 'idade': idade})
    return jsonify({'mensagem': 'Dados inseridos com sucesso'}), 201

# Rota de teste (GET)
@app.route('/')
def home():
    doc=list(colecao.find({},{'_id':0}))
    return doc



@app.route('/deletar/<nome>', methods=['DELETE'])
def deletar(nome):
    # Cria regex que remove espaços/tabs em volta e ignora case
    nome_regex = re.compile(f'^{re.escape(nome.strip())}$', re.IGNORECASE)
    
    resultado = colecao.delete_many({'nome': nome_regex})
    
    if resultado.deleted_count > 0:
        return jsonify({'mensagem': f'{resultado.deleted_count} documento(s) deletado(s) com sucesso.'})
    else:
        return jsonify({'erro': 'Nome não encontrado.'}), 404



if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
