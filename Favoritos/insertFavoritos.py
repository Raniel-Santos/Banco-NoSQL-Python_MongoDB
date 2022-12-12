import Usuario.search as searchUser
import Produto.search as searchProduto
from bson.objectid import ObjectId

def adicionar_fav(mydb):
    user = mydb.Usuario

    usuarios = searchUser.userByID(mydb,ObjectId)
    execucao = True

    while execucao:            
        opcao = input(str("Deseja adicionar um produto aos favoritos ? "))
        
        if opcao.lower() == 'sim':
            produto = searchProduto.produtoByID(mydb,ObjectId)
            user.update_one({"_id":ObjectId(usuarios["_id"])},{ "$push":{ "lista_favoritos":produto } })
        else:
            execucao = False
    
    print("\nProduto adicionado aos favoritos.\n")