import strawberry
from typing import Optional,List, Dict

from datetime import date, datetime



from  ..database.mongodb import create_mongo_client
mydb = create_mongo_client()



@strawberry.type
class User:
   
    fullname: str
    username: str
    password: str
    created: Optional[datetime] = None
    status: Optional[str] = None
    role: Optional[str] = None




    
    

@strawberry.type
class Query:
    
   
    
    
    @strawberry.field
    def get_user(self, username: str) -> Optional[User]:
        user = mydb.login.find()
        if user:
            return User(
                fullname=user["fullname"],
                username=user["username"],
                status=user["status"],
                role=user["role"],
                created=str(user["created"])
            )
        return None
            
        





