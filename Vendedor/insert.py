def inserirVendedor(mydb):
    print("Inicializado Cadastro de Vendedores do Mercado Livre\n")
    vendedor = input(str("Nome do vendedor: "))
    cnpj = input (str('CNPJ (se houver):'))
    cpf_vendedor = input (str('CPF: '))
    email_vendedor = input (str('email: '))

    mycol = mydb.Vendedor
    print('\n Vendedor cadastrado com Sucesso!\n')
    mydict ={
        "vendedor": vendedor,
        "cnpj": cnpj,
        "cpf_vendedor": cpf_vendedor,
        "email_vendedor": email_vendedor,
        "produtos":[]
    }

    x = mycol.insert_one(mydict)
    print(x.inserted_id)