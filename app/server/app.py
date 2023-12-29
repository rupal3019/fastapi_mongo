from fastapi import FastAPI

from app.server.routes.student import router as StudentRouter

app = FastAPI()

app.include_router(StudentRouter, tags=["Student"],prefix="/student")

#Tags are identifiers used to group routes
@app.get("/",tags=["Root"])
async def read_root():
    return {"message": "welcome to your project"}
