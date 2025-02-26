import pymongo, os
from dotenv import load_dotenv
load_dotenv()
MongoDb_Connection_str = os.environ['MONGODB_STR']

client = pymongo.MongoClient(MongoDb_Connection_str)
db = client['LinkRefine']
UserProfile_Suggestion_collection = db['UserProfile_Sug']
conv_collection = db['Conv']
UserData_collection = db['UserData']