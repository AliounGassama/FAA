from fastapi import FastAPI

app = FastAPI(title="FAA")

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/")
def endpoint():
    return {"name": "FAA","status": "running"}

transaction = {"date": "08/31", "amount": 1000, "description": "rent"}
@app.get("/transactions")
def transactions():
    return transaction

@app.get("/version")
def version():
    return {"version": "0.1.0"}
