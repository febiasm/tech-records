from fastapi import FastAPI
from app.db.session import engine, Base
from app.api.user import router as user_router

app = FastAPI(title="Aviation Tech Records")

import time
from sqlalchemy.exc import OperationalError

@app.on_event("startup")
def startup():
    for i in range(10):
        try:
            print(" Waiting for database...")
            Base.metadata.create_all(bind=engine)
            print("Database connected.")
            break
        except OperationalError:
            time.sleep(2)
    else:
        print(" Database not reachable.")

app.include_router(user_router)

@app.get("/health", tags=["System"])
def health_check():
    return {"status": "OK"}
