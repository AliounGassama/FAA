from fastapi import FastAPI

app = FastAPI(title="FAA")

@app.get("/health")
def health():
    return {"status": "ok"}
