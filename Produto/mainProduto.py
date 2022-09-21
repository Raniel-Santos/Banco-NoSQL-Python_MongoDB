import Produto.insert as insert
import Produto.search as search
import Produto.update as update
import Produto.delete as delete
from bson.objectid import ObjectId

def produtoOptions(mydb):

    selecionarOpçoes = True

    while selecionarOpçoes:

        print('''Escolha uma Opção abaixo: \n
            [1] Adicionar Produto
            [2] Buscar todos os produtos
            [3] Buscar produto por ID
            [4] Atualizar produto
            [5] Deletar produto
            [6] Voltar ao menu 
            [0] Sair
        ''')

        Opcoes = input(str("Opção: "))

        match Opcoes:
            case "1":
                insert.inserirProduto(mydb)
            case "2":
                search.allProdutos(mydb)
            case "3":
                search.produtoByID(mydb,ObjectId)    
            case "4":
                update.updateProduto(mydb,ObjectId)
            case "5":
                delete.deleteProduto(mydb,ObjectId)
            case "6":
                return
            case "0":
                selecionarOpçoes = False
                print("\n Até a próxima ! \n")
                break;