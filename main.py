import uvicorn
from fastapi import FastAPI
from models import User

app = FastAPI()



@app.get("/users")
def user():
    second_user_data = {
        "id": 1,
        "name": "John Doe"
    }
    my_second_user: User = User(**second_user_data)
    return my_second_user

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)