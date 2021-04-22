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


@app.get("/name/{my_name}")
def read_item(my_name: str, my_surname: str):
    return {"name": my_name}


@app.get("/")
async def root():
    return {"message": "zd kowik"}
