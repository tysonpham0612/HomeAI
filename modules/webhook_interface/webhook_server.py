from fastapi import FastAPI, Request
import uvicorn

app = FastAPI()
@app.post("/webhook/motion")
async def motion_event(request: Request):
    data = await request.json()
    print("Motion detected",data)
    return {"status": "received"}

def start_webhook_server():
    uvicorn.run("modules.webhook_interface.webhook_server:app", host="0.0.0.0", port=8000)