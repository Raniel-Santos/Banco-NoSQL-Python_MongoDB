import Usuario.insert as insert
import Usuario.delete as delete
import Usuario.update as update
import Usuario.search as search
from bson.objectid import ObjectId

def userOptions(mydb):

    selecionarOpçoes = True

    while selecionarOpçoes:

        print('''Escolha uma Opção abaixo: \n
            [1] Adicionar Usuário
            [2] Buscar todos os Usuários
            [3] Buscar Usuário por ID
            [4] Atualizar Usuário
            [5] Deletar Usuário
            [6] Voltar ao menu 
            [0] Sair
        ''')

        Opcoes = input(str("Opção: "))

        match Opcoes:
            case "1":
                insert.inserirUsuário(mydb)
            case "2":
                search.allUsers(mydb)
            case "3":
                search.userByID(mydb,ObjectId)    
            case "4":
                update.updateUser(mydb,ObjectId)
            case "5":
                delete.deleteUser(mydb,ObjectId)
            case "6":
                return
            case "0":
                selecionarOpçoes = False
                print("\n Até a próxima ! \n")
                break;












