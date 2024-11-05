from pymongo import MongoClient



def create_mongo_client():
	
    var_url = f"mongodb+srv://joeysabusido:genesis11@cluster0.bmdqy.mongodb.net/payroll?retryWrites=true&w=majority"
    client = MongoClient(var_url, maxPoolSize=None)
    conn = client['payroll']

	return conn




