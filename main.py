from fastapi import FastAPI

app = FastAPI()


@app.get("/name/{my_name}")
def read_item(my_name: str):
    return {"name": my_name}


@app.get("/")
async def root():
    return {"message": "zd kowik"}
