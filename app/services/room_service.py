
from fastapi import HTTPException, status

from app.repositories import room_repository
from app.schemas.room import RoomCreate, RoomResponse


def get_all_rooms() -> list[RoomResponse]:
    return room_repository.get_all()


def create_new_room(room: RoomCreate) -> RoomResponse:
    new_room = RoomResponse(
        id=0,
        **room.model_dump(),
    )

    return room_repository.save(new_room)


def get_room_by_id(room_id: int) -> RoomResponse:
    room = room_repository.get_by_id(room_id)

    if room is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Ruangan tidak ditemukan",
        )

    return room
