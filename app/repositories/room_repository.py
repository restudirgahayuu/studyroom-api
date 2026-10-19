
from app.schemas.room import RoomResponse


# Penyimpanan data sementara
_rooms: list[RoomResponse] = []
_next_room_id = 1


def get_all() -> list[RoomResponse]:
    return _rooms


def save(room: RoomResponse) -> RoomResponse:
    global _next_room_id

    new_room = RoomResponse(
        id=_next_room_id,
        nama_ruangan=room.nama_ruangan,
        kapasitas=room.kapasitas,
        lokasi=room.lokasi,
    )

    _rooms.append(new_room)
    _next_room_id += 1

    return new_room


def get_by_id(room_id: int) -> RoomResponse | None:
    for room in _rooms:
        if room.id == room_id:
            return room

    return None
