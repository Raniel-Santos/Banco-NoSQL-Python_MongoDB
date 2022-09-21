def allVendedores(mydb):
    mycol = mydb.Vendedor
    mydoc = mycol.find()
    print('\n Lista de todos os Vendedores \n')
    for x in mydoc:
        print(f'id: {x["_id"]}')
        print(f'Nome Vendedor: {x["vendedor"]}')
        print(f'Email Vendedor: {x["email_vendedor"]}')
        print(f'cpf Vendedor: {x["cpf_vendedor"]}')
        print(f'cnpj Vendedor: {x["cnpj"]}')
        print ('\n ---------- \n')


def vendedorByID(mydb,ObjectId):
    allVendedores(mydb)
    userID = input(str('\n Escolha um Vendedor pelo seu ID: '))    
    mycol = mydb.Vendedor
    myquery = {"_id":ObjectId(userID)}
    mydoc = mycol.find(myquery)
    for x in mydoc:
        print(f'id: {x["_id"]}')
        print(f'Nome Vendedor: {x["vendedor"]}')
        print(f'Email Vendedor: {x["email_vendedor"]}')
        print(f'cpf Vendedor: {x["cpf_vendedor"]}')
        print(f'cnpj Vendedor: {x["cnpj"]}')
        print ('\n ---------- \n')

