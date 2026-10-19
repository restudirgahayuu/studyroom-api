
from pydantic import BaseModel, Field


class RoomCreate(BaseModel):
    nama_ruangan: str = Field(
        min_length=3,
        max_length=100,
        description="Nama ruang belajar",
    )
    kapasitas: int = Field(
        gt=0,
        le=100,
        description="Kapasitas maksimal ruangan",
    )
    lokasi: str = Field(
        min_length=3,
        max_length=100,
        description="Lokasi ruang belajar",
    )


class RoomResponse(RoomCreate):
    id: int
