
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

ADMIN_HEADERS = {
    "X-API-Key": "studyroom-admin-key-2026"
}

USER_HEADERS = {
    "X-API-Key": "studyroom-user-key-2026"
}


def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["status"] == "success"


def test_health():
    response = client.get("/api/v1/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


def test_get_rooms_initially_empty():
    response = client.get("/api/v1/rooms/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_create_room():
    response = client.post(
        "/api/v1/rooms/",
        json={
            "nama_ruangan": "Ruang Belajar B",
            "kapasitas": 20,
            "lokasi": "Lantai 2",
        },
        headers=ADMIN_HEADERS,
    )

    assert response.status_code == 201
    assert response.json()["nama_ruangan"] == "Ruang Belajar B"
    assert response.json()["kapasitas"] == 20


def test_create_room_invalid_capacity():
    response = client.post(
        "/api/v1/rooms/",
        json={
            "nama_ruangan": "Ruang Belajar C",
            "kapasitas": 0,
            "lokasi": "Lantai 1",
        },
        headers=ADMIN_HEADERS,
    )
    assert response.status_code == 422


def test_room_not_found():
    response = client.get("/api/v1/rooms/9999")
    assert response.status_code == 404


def test_get_rooms_after_creation():
    response = client.get("/api/v1/rooms/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_create_room_missing_field():
    response = client.post(
        "/api/v1/rooms/",
        json={
            "nama_ruangan": "Ruang Belajar D",
            "kapasitas": 15,
        },
        headers=ADMIN_HEADERS,
    )
    assert response.status_code == 422


def test_create_room_capacity_too_large():
    response = client.post(
        "/api/v1/rooms/",
        json={
            "nama_ruangan": "Ruang Belajar E",
            "kapasitas": 101,
            "lokasi": "Lantai 1",
        },
        headers=ADMIN_HEADERS,
    )
    assert response.status_code == 422


def test_create_room_name_too_short():
    response = client.post(
        "/api/v1/rooms/",
        json={
            "nama_ruangan": "AB",
            "kapasitas": 10,
            "lokasi": "Lantai 1",
        },
        headers=ADMIN_HEADERS,
    )
    assert response.status_code == 422


def test_create_room_location_too_short():
    response = client.post(
        "/api/v1/rooms/",
        json={
            "nama_ruangan": "Ruang Belajar F",
            "kapasitas": 10,
            "lokasi": "AB",
        },
        headers=ADMIN_HEADERS,
    )
    assert response.status_code == 422


def test_create_room_name_too_long():
    response = client.post(
        "/api/v1/rooms/",
        json={
            "nama_ruangan": "R" * 101,
            "kapasitas": 10,
            "lokasi": "Lantai 1",
        },
        headers=ADMIN_HEADERS,
    )
    assert response.status_code == 422


def test_create_room_capacity_negative():
    response = client.post(
        "/api/v1/rooms/",
        json={
            "nama_ruangan": "Ruang Belajar G",
            "kapasitas": -5,
            "lokasi": "Lantai 1",
        },
        headers=ADMIN_HEADERS,
    )
    assert response.status_code == 422


def test_get_existing_room():
    create_response = client.post(
        "/api/v1/rooms/",
        json={
            "nama_ruangan": "Ruang Belajar H",
            "kapasitas": 25,
            "lokasi": "Lantai 3",
        },
        headers=ADMIN_HEADERS,
    )

    assert create_response.status_code == 201
    room_id = create_response.json()["id"]

    response = client.get(f"/api/v1/rooms/{room_id}")
    assert response.status_code == 200
    assert response.json()["id"] == room_id


def test_create_room_location_too_long():
    response = client.post(
        "/api/v1/rooms/",
        json={
            "nama_ruangan": "Ruang Belajar I",
            "kapasitas": 10,
            "lokasi": "L" * 101,
        },
        headers=ADMIN_HEADERS,
    )
    assert response.status_code == 422


def test_create_room_without_api_key():
    response = client.post(
        "/api/v1/rooms/",
        json={
            "nama_ruangan": "Ruang Tanpa Key",
            "kapasitas": 10,
            "lokasi": "Lantai 1",
        },
    )
    assert response.status_code == 401


def test_create_room_with_invalid_api_key():
    response = client.post(
        "/api/v1/rooms/",
        json={
            "nama_ruangan": "Ruang Key Salah",
            "kapasitas": 10,
            "lokasi": "Lantai 1",
        },
        headers={"X-API-Key": "invalid-key"},
    )
    assert response.status_code == 401


def test_create_room_with_user_role():
    response = client.post(
        "/api/v1/rooms/",
        json={
            "nama_ruangan": "Ruang untuk User",
            "kapasitas": 10,
            "lokasi": "Lantai 1",
        },
        headers=USER_HEADERS,
    )
    assert response.status_code == 403


def test_create_room_with_admin_role():
    response = client.post(
        "/api/v1/rooms/",
        json={
            "nama_ruangan": "Ruang Admin",
            "kapasitas": 15,
            "lokasi": "Lantai 2",
        },
        headers=ADMIN_HEADERS,
    )
    assert response.status_code == 201

    
def test_error_response_format_room_not_found():
    response = client.get("/api/v1/rooms/9999")

    assert response.status_code == 404

    body = response.json()
    assert body["success"] is False
    assert body["error"]["code"] == 404
    assert body["error"]["message"] == "Ruangan tidak ditemukan"


def test_error_response_format_unauthorized():
    response = client.post(
        "/api/v1/rooms/",
        json={
            "nama_ruangan": "Ruang Uji",
            "kapasitas": 10,
            "lokasi": "Lantai 1",
        },
    )

    assert response.status_code == 401

    body = response.json()
    assert body["success"] is False
    assert body["error"]["code"] == 401
    assert body["error"]["message"] == (
        "API key tidak valid atau tidak ditemukan"
    )

