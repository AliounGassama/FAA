# Main application file for FastAPI backend

from fastapi import FastAPI, Depends
from sqlmodel import select
from contextlib import asynccontextmanager
from db.session import get_session
from db.model import Transaction
from db.init_db import init_db
from typing import List

# use lifespan as on_startup is deprecated
@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield

app = FastAPI(title="FAA", lifespan=lifespan)

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/")
def endpoint():
    return {"name": "FAA","status": "running"}

@app.get("/transactions", response_model=List[Transaction])
def transactions(*, session=Depends(get_session), ):
    return session.exec(select(Transaction)).all()

@app.get("/version")
def version():
    return {"version": "0.1.0"}