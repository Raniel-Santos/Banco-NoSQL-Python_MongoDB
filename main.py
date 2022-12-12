import pymongo
from pymongo.server_api import ServerApi
import Compra.mainCompra as mainCompra
import Produto.mainProduto as mainProduto
import Vendedor.mainVendedor as mainVendedor
import Usuario.mainUsuario as mainUsuario
import Favoritos.mainFavoritos as mainFavorito

client = pymongo.MongoClient("mongodb+srv://Raniel2:Raninho93@raniel-fatec.og59z6w.mongodb.net/?retryWrites=true&w=majority", server_api=ServerApi('1'))

## global mydb
mydb = client.mercado_livre

selecionarOpçoes = True

while selecionarOpçoes:

    print('''Escolha uma Opção abaixo: \n
        [1] Usuário
        [2] Produto
        [3] Vendedores
        [4] Compras
        [5] Favoritos
        [0] Sair
    ''')

    Opcoes = input(str("Opção: "))

    match Opcoes:
        case "1":
            mainUsuario.userOptions(mydb)
        case "2":
            mainProduto.produtoOptions(mydb)
        case "3":
            mainVendedor.vendedorOptions(mydb)
        case "4":
            mainCompra.compraOptions(mydb)
        case "5":
            mainFavorito.case_favoritos(mydb)
        case "0":
            selecionarOpçoes = False
            print("\n Até a próxima ! \n")
            break;











