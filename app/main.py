
from fastapi import FastAPI

from app.exceptions import register_exception_handlers
from app.routers.health import router as health_router
from app.routers.rooms import router as rooms_router

app = FastAPI(
    title="StudyRoom API",
    description=(
        "REST API untuk mengelola ruang belajar "
        "dan pemesanan ruangan."
    ),
    version="1.0.0",
)

# Mengaktifkan penanganan error terpusat
register_exception_handlers(app)


@app.get("/", tags=["Home"])
def home():
    return {
        "message": "Selamat datang di StudyRoom API",
        "status": "success",
    }


app.include_router(
    health_router,
    prefix="/api/v1",
)

app.include_router(
    rooms_router,
    prefix="/api/v1/rooms",
    tags=["Rooms"],
)
