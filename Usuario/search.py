def allUsers(mydb):
    mycol = mydb.Usuario
    mydoc = mycol.find()
    print('\n Lista de todos os Usuários \n')
    for x in mydoc:
        print(f'id: {x["_id"]}')
        print(f'Nome: {x["nome"]}')
        print(f'Email: {x["email"]}')
        print ('\n ---------- \n')


def userByID(mydb,ObjectId):
    allUsers(mydb)
    userID = input(str('\n Escolha um Usuário pelo seu ID: '))    
    mycol = mydb.Usuario
    myquery = {"_id":ObjectId(userID)}
    mydoc = mycol.find_one(myquery)   
    print(f'id: {mydoc["_id"]}')
    print(f'Nome: {mydoc["nome"]}')
    print(f'Email: {mydoc["email"]}')
    print('\n ---------- \n')
    return mydoc
