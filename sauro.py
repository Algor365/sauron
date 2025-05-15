from pymongo import MongoClient

# Cole sua string aqui, que está no formato mongodb+srv://...
uri = "mongodb+srv://carlosdenobrega9988:huSYKtnGRLp3CG7H@sauron.qpue9bn.mongodb.net/?retryWrites=true&w=majority&appName=sauron"

client = MongoClient(uri)

# Exemplo: acessa o banco padrão
db = client.sauron  # ou o nome do seu banco

# Exemplo: acessar coleção e inserir documento
colecao = db.minha_colecao
resultado=colecao.find({},{'nome':0,'_id':0})
doc=list(resultado)
print(doc)
