import datetime
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
import uvicorn


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.options("/opt")
def opt():
    return(
        FastAPI.options( )
    )
@app.get("/home")
def home():
    return(
       datetime.datetime(2005, 7, 14, 12, 30)
    )

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=80, access_log=False)