from fastapi import FastAPI
import uvicorn

app = FastAPI()
@app.get("/health")
def health():
    return "server is running"


if __name__=="__main__":
    uvicorn.run(app="health:app",reload=True)