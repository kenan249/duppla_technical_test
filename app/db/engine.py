import os
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
from urllib.parse import quote_plus

load_dotenv()

HOST = os.getenv("APP_HOST_DB")
USER = os.getenv("APP_USER_DB")
PASSWORD = os.getenv("APP_PASSWORD_DB")
DBNAME = os.getenv("APP_NAME_DB")
PORT = os.getenv("APP_PORT_DB", "5432")
# Valida que la variable de host se haya cargado
if not HOST:
    raise ValueError("La variable de entorno DREAM_TEAM_HOST_DB no está definida.")

# Codifica la contraseña para que sea segura en la URL
password_encoded = quote_plus(PASSWORD) if PASSWORD else ""

# Construye la URL de conexión usando el driver asíncrono
DATABASE_URL = (
    f"postgresql+asyncpg://{USER}:{password_encoded}@{HOST}:{PORT}/{DBNAME}"
)

print(f"Attempting to connect to: {HOST}")

# Para asyncpg, el SSL se configura a través de connect_args
engine = create_async_engine(
    DATABASE_URL,
    pool_pre_ping=True
)

AsyncSessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
)

async def get_db():
    async with AsyncSessionLocal() as session:
        yield session
