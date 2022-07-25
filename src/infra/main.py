from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from fastapi import FastAPI
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
@app.get("/get_record_cam_stream/")
def get_record_cam_stream(device_id, cam, subtype, start_time, end_time, company_id=1):




if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=HTTP_PORT, access_log=False)