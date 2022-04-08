from pymongo import MongoClient
import pymongo
CONNECTION_DATA = "mongodb+srv://ben6119070:BL246810@cluster0.qojmx.mongodb.net/OnABetterNote?retryWrites=true&w=majority"

client = MongoClient(CONNECTION_DATA)

col = client["Notes"]

x = col.find()

for i in x:
    print(i)



# db = client.database
# collections = db.Notes

# notes_to_add = {
#     "test": "tset"
# }

# collections.insert_one(notes_to_add)

# print((client["OnABetterNote"]["Notes"]))