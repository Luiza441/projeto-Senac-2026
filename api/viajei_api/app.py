from fastapi import FastAPI

app = FastAPI()

@app.get("/hello")
def ola_mundo():
    return{"Olá! Pessoal!"}