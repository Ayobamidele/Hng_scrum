from sqlalchemy.orm import sessionmaker, scoped_session, declarative_base
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import create_engine
from api.utils.settings import settings, BASE_DIR

DB_HOST = settings.DB_HOST
DB_PORT = settings.DB_PORT
DB_USER = settings.DB_USER
DB_PASSWORD = settings.DB_PASSWORD
DB_NAME = settings.DB_NAME
DB_TYPE = settings.DB_TYPE


def get_db_engine(test_mode: bool = False):
    DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    print(DATABASE_URL, DB_TYPE)
    if DB_TYPE == "sqlite" or test_mode:
        BASE_PATH = f"sqlite:///{BASE_DIR}"
        DATABASE_URL = BASE_PATH + "/"

        if test_mode:
            DATABASE_URL = BASE_PATH + "test.db"

            return create_engine(
                DATABASE_URL, connect_args={"check_same_thread": False}
            )
    elif DB_TYPE == "postgresql":
        DATABASE_URL = (
            f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
        )

    return create_engine(DATABASE_URL)


engine = get_db_engine()

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)

db_session = scoped_session(SessionLocal)

Base = declarative_base()


def create_database():
    return Base.metadata.create_all(bind=engine)


def get_db():
    db = db_session()
    try:
        yield db
    finally:
        db.close()
