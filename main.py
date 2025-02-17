from fastapi import FastAPI
from fastapi.responses import FileResponse
import uvicorn

app = FastAPI()


@app.get("/")
async def root():
    return FileResponse("public/index.html")


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)