from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/ai/{voice}")
async def say_hello(voice: str):
    return {"message": f"Hello {name}"}
