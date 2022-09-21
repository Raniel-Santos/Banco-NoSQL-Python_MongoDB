def allProdutos(mydb):
    mycol = mydb.Produto
    mydoc = mycol.find()
    print('\n Lista de todos os Produtos \n')
    for x in mydoc:
        print(f'id: {x["_id"]}')
        print(f'nome_produto: {x["nome_produto"]}')
        print(f'preco: {x["preco"]}')
        print(f'qtd_estoque: {x["qtd_estoque"]}')
        print ('\n ---------- \n')



def produtoByID(mydb,ObjectId):
    allProdutos(mydb)
    produtoID = input(str('\n Escolha um Produto pelo seu ID: '))    
    mycol = mydb.Produto
    myquery = {"_id":ObjectId(produtoID)}
    mydoc = mycol.find(myquery)
    for x in mydoc:
        print(f'id: {x["_id"]}')
        print(f'nome_produto: {x["nome_produto"]}')
        print(f'preco: {x["preco"]}')
        print(f'qtd_estoque: {x["qtd_estoque"]}')
        print ('\n ---------- \n')