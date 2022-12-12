import Compra.insertCompra as insert
import Compra.findCompra as search
def compraOptions(mydb):
    selecionarOpçoes = True

    while selecionarOpçoes:

        print('''Escolha uma Opção abaixo: \n
            [1] Adicionar compra
            [2] Buscar todas as compras
            [3] Buscar compras por ID            
            [4] Voltar ao menu 
            [0] Sair
        ''')

        Opcoes = input(str("Opção: "))

        match Opcoes:
            case "1":
                insert.inserir_compra(mydb)
            case "2":
                search.findAll(mydb)
            case "3":
                search.findById(mydb)    
            case "4":
                return
            case "0":
                selecionarOpçoes = False
                print("\n Até a próxima ! \n")
                break;