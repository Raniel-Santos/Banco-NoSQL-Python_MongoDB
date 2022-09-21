def deleteUser(mydb,ObjectId):
    #Delete    
    _id =  input(str('Id do Usuario:'))
    mycol = mydb.Usuario
    print("\n####DELETADO####") 
    filter = { "_id":ObjectId (_id) }
    mycol.delete_one(filter)
    for x in mycol.find():
        print(x) 



