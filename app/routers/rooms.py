
from fastapi import APIRouter, Depends, status

from app.dependencies.auth import require_admin, verify_api_key
from app.schemas.room import RoomCreate, RoomResponse
from app.services.room_service import (
    create_new_room,
    get_all_rooms,
    get_room_by_id,
)

router = APIRouter()


@router.get("/", response_model=list[RoomResponse])
def get_rooms():
    return get_all_rooms()


@router.post(
    "/",
    response_model=RoomResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_room(
    room: RoomCreate,
    role: str = Depends(verify_api_key),
):
    require_admin(role)
    return create_new_room(room)


@router.get("/{room_id}", response_model=RoomResponse)
def get_room(room_id: int):
    return get_room_by_id(room_id)
