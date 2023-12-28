from fastapi import FastAPI

app = FastAPI()


#Tags are identifiers used to group routes
@app.get("/",tags=["Root"])
async def read_root():
    return {"message": "welcome to your project"}