from fastapi import FastAPI
import socket

app = FastAPI()

@app.get("/")
def home():
    return {
        "message": "Welcome to Python API",
        "server": socket.gethostname()
    }

@app.get("/health")
def health():
    return {"status": "healthy"}
