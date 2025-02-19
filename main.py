import uvicorn
from fastapi import FastAPI
from models import UserAge

app = FastAPI()


@app.post('/user')
async def show_user(user: UserAge):
    return {"name": user.name,
            "age": user.age,
            "is_adult": user.age >= 18}


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
