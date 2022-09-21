import Produto.search
from bson.objectid import ObjectId

def deleteProduto(mydb,ObjectId):
    Produto.search.allProdutos(mydb)
    _id = input(str('Insira o Id do Produto:'))
    mycol = mydb.Produto
    print("\n#### Produto Deletado ####") 
    filter = { "_id":ObjectId (_id) }
    mycol.delete_one(filter)
    for x in mycol.find():
        print(x)  