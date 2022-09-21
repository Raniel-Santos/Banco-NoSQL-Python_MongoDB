import Vendedor.insert as insert
import Vendedor.delete as delete
import Vendedor.search as search
from bson.objectid import ObjectId



def vendedorOptions(mydb):
    
    selecionarOpçoes = True

    while selecionarOpçoes:

        print('''Escolha uma Opção abaixo: \n
            [1] Adicionar Vendedor
            [2] Buscar todos os Vendedores
            [3] Buscar Vendedor por ID
            [4] Deletar Vendedor
            [5] Voltar ao menu 
            [0] Sair
        ''')

        Opcoes = input(str("Opção: "))

        match Opcoes:
            case "1":
                insert.inserirVendedor(mydb)
            case "2":
                search.allVendedores(mydb)
            case "3":
                search.vendedorByID(mydb,ObjectId)    
            case "4":
                delete.deleteVendedor(mydb,ObjectId)
            case "5":
                return
            case "0":
                selecionarOpçoes = False
                print("\n Até a próxima ! \n")
                break;
