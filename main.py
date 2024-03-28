import uvicorn
from fastapi import FastAPI
from starlette.staticfiles import StaticFiles

from ToDoApp.database import engine
from ToDoApp.models import Base
from ToDoApp.routers import auth, todos

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.mount("/static", StaticFiles(directory="ToDoApp/static"), name="static")


@app.get("/healthy")
async def health_check():
    return {"status": "Healthy"}

app.include_router(auth.router)
app.include_router(todos.router)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
