def inserirUsuário(mydb):
    print("Inicializado Cadastro de Usuário do Mercado Livre\n")
    nome = input(str("Nome: "))
    email = input(str("Email: "))
    telefone = input(str("Telefone: "))
    cpf = input(str("CPF: "))
    print('\n')

    enderecos = cadastroEnd()

    mycol = mydb.Usuario
    mydict ={
        "nome": nome,
        "email": email,
        "telefone": telefone,
        "cpf": cpf,
        "enderecos":enderecos,
        "lista_favoritos":[],
        "compras":[]
    }

    x = mycol.insert_one(mydict)
    print("\n Usuário Cadastrado com Sucesso, Bem-vindo ao Mercado Livre")
    print (f'ID do Usuario: {x.inserted_id}')

def cadastroEnd():

    execucao = True
    enderecos = []
    print("Cadastro de endereço\n")

    while execucao:
            
        opcao = input(str("Deseja cadastrar um endereco ? Digite 'sim' para cadastrar "))
        if opcao.lower() == 'sim':
            estado = input(str("Digite o Estado: "))
            cep = input(str("Digite o CEP: "))
            cidade = input(str("Digite a Cidade: "))
            bairro = input(str("Digite o Bairro: "))
            rua = input(str("Digite a Rua: "))
            numero  = input(str("Digite o Número: "))
            print('\n')
            enderecos.append({"estado":estado,"cep":cep,"cidade":cidade,"bairro":bairro,"rua":rua,"numero":numero})
        
        else:
            execucao = False

    return enderecos
