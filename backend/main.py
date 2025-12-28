from fastapi import FastAPI

app = FastAPI(title="FAA")

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/")
def endpoint():
    return {"name": "FAA","status": "running"}

transactions = {"date": "08/31", "amount": 1000, "name": "rent"}
@app.get("/transaction")
def transaction():
    return transactions

@app.get("/version")
def version():
    return {"version": "0.1.0"}
