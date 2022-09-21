def deleteVendedor(mydb,ObjectId):
    #Delete    
    _id =  input(str('Id do Vendedor:'))
    mycol = mydb.Vendedor
    print("\n####DELETADO####") 
    filter = { "_id":ObjectId (_id) }
    mycol.delete_one(filter)
    for x in mycol.find():
        print(x) 