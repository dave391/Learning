from fastapi import FastAPI, Depends
import uvicorn
from pydantic import BaseModel 

app = FastAPI(title="API-somma",description="using FastAPI",version="1.0")

@app.get("/")
def hello():
    return {"--> http://127.0.0.1:8000/docs <--"}

class Numbers (BaseModel):
    num1 : float = 5
    num2 : float = 4
    num3 : float = 3

@app.get("/sum")
async def get_sumnumbers(numbers:Numbers= Depends()):
    try:
        res=numbers.num1 + numbers.num2 + numbers.num3
        return {"result":res}
    except:
        return {"result":"error"}


@app.post("/sum")
async def post_sumnumbers(numbers:Numbers):
    try:
        res= numbers.num1 + numbers.num2 + numbers.num3
        return {"result":res}
    except:
        return {"result":"error"}
    

@app.get("/mult")
async def get_sumnumbers(numbers:Numbers= Depends()):
    try:
        res=numbers.num1 * numbers.num2 * numbers.num3
        return {"result":res}
    except:
        return {"result":"error"}
    

@app.post("/mult")
async def post_sumnumbers(numbers:Numbers):
    try:
        res= numbers.num1 * numbers.num2 * numbers.num3
        return {"result":res}
    except:
        return {"result":"error"}
    


if __name__=="__main__":
    uvicorn.run("main:app",host="127.0.0.1",port=8000,reload=True)