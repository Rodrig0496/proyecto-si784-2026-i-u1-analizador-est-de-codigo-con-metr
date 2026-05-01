from fastapi import FastAPI

from app.persistencia.database.database import Base, engine
from app.persistencia.models.models import User, AnalysisReport
from app.presentacion.routers.analysis_router import router as analysis_router
from app.presentacion.routers.auth_router import router as auth_router

app = FastAPI(title="Analizador Estático de Código")

# Crear las tablas en la base de datos al iniciar
Base.metadata.create_all(bind=engine)

app.include_router(analysis_router)
app.include_router(auth_router)


@app.get("/")
async def root() -> dict[str, str]:
    return {"message": "Analizador Estático de Código"}
