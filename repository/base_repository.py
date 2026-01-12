from sqlalchemy import Engine
from sqlmodel import Session


class BaseRepository:
    """Base repository class with engine management"""
    _engine: Engine | None = None

    @classmethod
    def set_engine(cls, engine: Engine) -> None:
        """Set the database engine for all repositories"""
        cls._engine = engine

    @classmethod
    def _get_session(cls) -> Session:
        """Get a database session"""
        if cls._engine is None:
            raise RuntimeError("Engine not set. Call set_engine() first.")
        return Session(cls._engine)

