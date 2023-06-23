from fastapi import FastAPI, Depends
import uvicorn
from pydantic import BaseModel 

app = FastAPI()

@app.get("/")
def hello():
    return {"--> http://127.0.0.1:8000/docs <--"}

class Numbers (BaseModel):
    num1 : int = 5
    num2 : int = 4

@app.get("/sum")
def get_sumnumbers(numbers:Numbers= Depends()):
    res=numbers.num1 + numbers.num2
    return {"result":res}

@app.post("/sum")
def get_sumnumbers(numbers:Numbers):
    res=numbers.num1 + numbers.num2
    return {"result":res}

    


if __name__=="__main__":
    uvicorn.run("main:app",host="127.0.0.1",port=8000,reload=True)