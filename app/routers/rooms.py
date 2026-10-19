
from fastapi import APIRouter, HTTPException, status
from app.schemas.room import RoomCreate, RoomResponse

router = APIRouter()

# Penyimpanan sementara untuk latihan
rooms: list[RoomResponse] = []
next_room_id = 1


@router.get("/", response_model=list[RoomResponse])
def get_rooms():
    return rooms


@router.post(
    "/",
    response_model=RoomResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_room(room: RoomCreate):
    global next_room_id

    # Membuat ID otomatis
    new_room = RoomResponse(
        id=next_room_id,
        **room.model_dump(),
    )

    rooms.append(new_room)
    next_room_id += 1

    return new_room


@router.get("/{room_id}", response_model=RoomResponse)
def get_room(room_id: int):
    for room in rooms:
        if room.id == room_id:
            return room

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Ruangan tidak ditemukan",
    )
