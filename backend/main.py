from fastapi import FastAPI,Query
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from src.scrapper.profile import profile_optimizer
from src.Database.db import UserProfile_Suggestion_collection
from bson import ObjectId
import logging,uuid

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],  
)
class user_profile(BaseModel):
    url:str

@app.post("/linkrefine/upload")
def user_profile_optimizer(user_input:user_profile):
    try:

        user_url = user_input.url
        link_id = str(uuid.uuid4())
        # user_id = user_input.user_id
        response = profile_optimizer(user_url,link_id)
        response = True
        if response is None:
            return {"message":False} 
        elif response is True:
            return {"message":True,"link_id":link_id}
        else:
            return {"message":False}
            
    except:
        return  {"message":False}
    

def serialize_mongo_response(document):
    if isinstance(document, list):
        return [serialize_mongo_response(item) for item in document]
    elif isinstance(document, dict):
        new_document = {}
        for key, value in document.items():
            if isinstance(value, ObjectId):
                new_document[key] = str(value)
            elif isinstance(value, (dict, list)):
                new_document[key] = serialize_mongo_response(value)
            else:
                new_document[key] = value
        return new_document
    else:
        return document

@app.get("/linkrefine/review")
def profile_suggestion(link_id: str = Query(..., description="URL of the LinkedIn profile")):
    print(link_id)
    response = UserProfile_Suggestion_collection.find_one({"link_id": link_id})
    if response:
        serialized_response = serialize_mongo_response(response)
        return {"response": serialized_response}
    return {"response": "Upload a URL"}



if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

    