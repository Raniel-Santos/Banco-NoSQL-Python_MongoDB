import Favoritos.insertFavoritos as insert

def case_favoritos(mydb):
    
    execucao = True
    while execucao:
        print('''Opções
        [1] Adicionar produto a favoritos
        [0] Voltar
            ''')
        
        opcao = input(str("Escolha uma das opções: "))
        
        match opcao:
            case "1":
                insert.adicionar_fav(mydb)
            case "0":
                return