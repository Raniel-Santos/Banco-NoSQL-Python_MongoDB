def inserirProduto(mydb):
    print("Inicializado Cadastro de Produtos do Mercado Livre\n")
    nome_produto = input(str('Nome do Produto: '))
    descricao = input(str('Descrição (tipo) do produto: '))
    preco = input(str('Preço: R$ '))
    qtd_estoque = input (str('Quantidade em estoque: '))
   

    mycol = mydb.Produto
    print('\n Produto inserido com Sucesso!!!\n')
    mydict = {
        "nome_produto": nome_produto,
        "descricao": descricao,
        "preco": preco,
        "qtd_estoque": qtd_estoque,
        "vendedor":[]
    }
    
    x = mycol.insert_one(mydict)
    print(x.inserted_id)