from fastapi import FastAPI
import uvicorn

app=FastAPI()

@app.get("/comesonobravo") #decoratore per definire l'url delle nostre API
def home():
    return{"Hello" : "World!"}

@app.get("/docs") 
def docs():
    return{"https://localhost:8000/docs"}

@app.get("/inserisci/{stringa}")
def string(stringa):
    return {f"la stringa inderita è : {stringa}"}
    


if __name__=="__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)



