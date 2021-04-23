from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

app = FastAPI()


origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/chat/{my_name}/{text}")
def read_item(my_name: str, text: str):
    a[my_name] = text

    return a


@app.get("/name/{my_name}")
def read_item(my_name: str):
    return {"name": my_name}


@app.get("/")
async def root():
    return {"message": "zd kowik"}
