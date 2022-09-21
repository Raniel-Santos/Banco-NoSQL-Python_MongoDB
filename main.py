import pymongo
from pymongo.server_api import ServerApi
import Produto.mainProduto as mainProduto
import Vendedor.mainVendedor as mainVendedor
import Usuario.mainUsuario as mainUsuario

client = pymongo.MongoClient("mongodb+srv://Raniel:pjfUjNlp3PdH3Yh8@raniel-fatec.og59z6w.mongodb.net/?retryWrites=true&w=majority", server_api=ServerApi('1'))

## global mydb
mydb = client.mercado_livre

selecionarOpçoes = True

while selecionarOpçoes:

    print('''Escolha uma Opção abaixo: \n
        [1] Usuário
        [2] Produto
        [3] Vendedores
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
        case "0":
            selecionarOpçoes = False
            print("\n Até a próxima ! \n")
            break;











