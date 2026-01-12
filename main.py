from fastapi import FastAPI
from routers.user_router import UserRouter
from sqlmodel import create_engine
from contextlib import asynccontextmanager
from sqlmodel import SQLModel
from repositories.user_repositories import UserRepository

# Database setup
DATABASE_URL = "sqlite:///./app.db"
engine = create_engine(DATABASE_URL, echo=True)

# Set engine voor repositories (BELANGRIJK: voor lifespan)
UserRepository.set_engine(engine)

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


