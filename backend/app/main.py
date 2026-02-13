from fastapi import FastAPI
from app.db.session import engine, Base
from app.api.user import router as user_router
from app.api.auth import router as auth_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Aviation Tech Records")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)   
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
app.include_router(auth_router)

@app.get("/health", tags=["System"])
def health_check():
    return {"status": "OK"}

@app.get("/profile")
def read_profile():
    return {
        "name": "Aviation Tech Records API",
        "health": "Running",
        "version": "1.0.0"
    }
