from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from src.core.config import settings
from sqlmodel import Session
from pydantic import BaseModel, ConfigDict

Base = declarative_base()


# Базовый класс для SQLAlchemy и Pydantic
class BaseModelMixin(BaseModel):
    model_config = ConfigDict(from_attributes=True)


DATABASE_URL = (
    f"postgresql://{settings.PG_USERNAME}:{settings.PG_PASSWORD}@"
    f"{settings.PG_HOST}:{settings.PG_PORT}/{settings.PG_DATABASE}"
)

engine = create_engine(DATABASE_URL)
metadata = MetaData()
metadata.reflect(bind=engine)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)


def get_db_session() -> Session:
    with Session(engine) as session:
        yield session
