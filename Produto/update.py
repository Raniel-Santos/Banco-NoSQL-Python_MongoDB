import Produto.search
from bson.objectid import ObjectId

def updateProduto(mydb,ObjectId):
    _id = input(str('Insira o ID do Produto: '))
    mycol = mydb.Produto
    nome_produto = input(str('Nome do Produto: '))
    descricao = input(str('Descrição (tipo) do produto: '))
    preco = input(str('Preço: R$'))
    qtd_estoque = (str('Quantidade em estoque: '))

    print("\n Produto Atualizado com Sucesso!\n")

    newvalues = {"$set": {
        "nome_produto": nome_produto,
        "descricao": descricao,
        "preco": preco,
        "qtd_estoque": qtd_estoque
    }}

    filter = {"_id": ObjectId (_id)}
    mycol.update_one(filter,newvalues)

    for x in mycol.find():
        print(x)  