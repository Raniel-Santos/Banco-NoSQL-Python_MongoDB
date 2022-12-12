from bson.objectid import ObjectId

def findAll(mydb):
    compras = mydb.Compra
    for compra in compras.find():
        print("--  Lista de compras  --\n")
        print(f'id: {compra["_id"]}')
        print(f'Data da compra: {compra["data_compra"]}')
        print("\n----------------------------------------\n")

def findById(mydb):
    compras = mydb.Compra
    findAll(mydb)
    compra_id = input(str("Digite o id da compra que deseja cancelar: "))
    compra = compras.find_one({"_id":ObjectId(compra_id)})
    print(f'\n--  Compra de id {compra["_id"]}  --\n')
    print(f'Data da compra: {compra["data_compra"]}')
    print("\n----------------------------------------\n")
    return compra

