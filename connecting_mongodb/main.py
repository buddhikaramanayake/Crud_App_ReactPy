from pymongo import MongoClient

# Replace <uri> with your MongoDB Atlas connection string
uri="mongodb+srv://buddhika:shadowrex@cluster0.afn1jxe.mongodb.net/"
client=MongoClient(uri)

# Replace <database-name> with the name of your database
db= client["Sample_database"]

# Replace <collection-name> with the name of your collection
collection= db["buddhi"]

# chaeck the connection
try:
    client.admin.command("ping")
    print ("Pinged your deployment, You successfully connected to MongoDB!")
except Exception as e:
    print(e)

document = {"name": "Danial","age": 36 }

#Insert the document into the collection
insert_result = collection.insert_one(document)

#Print the ID of the inserted document
print("Insert Document ID:", insert_result.inserted_id)

client.close()