from bson import ObjectId
import Usuario.search as buscarUsuario
import Produto.search as buscarProduto
from datetime import date

def inserir_compra(mydb):
    compra = mydb.Compra
    usuario = mydb.Usuario

    lista_produtos = []
    usuarios = buscarUsuario.userByID(mydb,ObjectId)

    data_atual = date.today()
    data_formatada = data_atual.strftime('%d/%m/%Y')    

    
    execucao = True
    while execucao:
        
        opcao = input(str("Deseja comprar um produto ? "))
        
        if opcao.lower() == "sim":
            produto = buscarProduto.produtoByID(mydb,ObjectId)
            lista_produtos.append(produto)
           
        else:
            execucao = False
    
    mydict = {
        "data_compra":data_formatada,
        'usuario':usuarios,
        "produtos":lista_produtos
    }
    print(type(usuarios))

    compra_id = compra.insert_one(mydict)

    compra_realizada = compra.find_one({"_id":ObjectId(compra_id.inserted_id)})
    usuario.update_one({"_id":ObjectId(usuarios["_id"])},{ "$push": { "compras":compra_realizada }})
    
    print("\nCompra realizada com sucesso")
    print(f'Id da compra {compra_id.inserted_id}')