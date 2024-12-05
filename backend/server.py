from fastapi import FastAPI
from routes import stream_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(stream_router)

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}
