import Usuario.search
from bson.objectid import ObjectId

def updateUser(mydb,ObjectId):
    _id = input(str('Insira o ID do Usuário: '))
    mycol = mydb.Usuario
    nome = input(str("Nome: "))
    email = input(str("Email: "))
    telefone = input(str("Telefone: "))

    print("\n Usuário Atualizado com Sucesso!\n")

    
    newvalues = {"$set": {
        "nome": nome,
        "email": email,
        "telefone": telefone    
    }}
    
    filter = {"_id": ObjectId (_id)}
    mycol.update_one(filter,newvalues)
    
    for x in mycol.find():
        print(x)