from fastapi import FastAPI
from routers.user_router import UserRouter
from sqlmodel import SQLModel, create_engine
from contextlib import asynccontextmanager
from repository.user_repository import UserRepository
from repository.base_repository import BaseRepository
from models.user_model import User

# Database setup
DATABASE_URL = "sqlite:///./app.db"
engine = create_engine(DATABASE_URL, echo=True, connect_args={"check_same_thread": False})

# Set engine for all repositories (BELANGRIJK: voor lifespan)
BaseRepository.set_engine(engine)

@asynccontextmanager
async def lifespan(app: FastAPI):
    """Startup/shutdown events"""
    # Maak tabellen aan bij startup
    SQLModel.metadata.create_all(engine)
    yield
    # Cleanup bij shutdown (optioneel)


app = FastAPI(lifespan=lifespan)

user_router_instance = UserRouter()
app.include_router(user_router_instance.router, prefix="/user", tags=["users"])


