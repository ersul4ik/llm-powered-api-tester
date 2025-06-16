from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def read_message(msg: str):
    # Read message from the UI and pass it to OpenAI
    return {"message": f"Hello World {msg}"}


