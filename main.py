import uvicorn
from req import app

if __name__ == "__main__":
    uvicorn_process = uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8022,
        reload=True,
        workers=2,
    )
