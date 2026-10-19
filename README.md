# StudyRoom API

REST API untuk mengelola data ruang belajar menggunakan FastAPI dan Python.

## Fitur

- Endpoint Home dan Health Check.
- Melihat daftar ruangan.
- Menambahkan ruangan.
- Melihat detail ruangan berdasarkan ID.
- Validasi data menggunakan Pydantic v2.
- Autentikasi menggunakan API Key.
- Pembatasan akses berdasarkan role admin dan user.
- Penanganan error terpusat.
- Dokumentasi API melalui Swagger UI.
- Pengujian otomatis menggunakan Pytest.

## Teknologi

- Python 3.11
- FastAPI
- Pydantic v2
- Uvicorn
- Pytest
- HTTPX

## Instalasi

Buat virtual environment:

```powershell
python -m venv .venv
```

Aktifkan virtual environment di Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Instal dependensi:

```powershell
python -m pip install -r requirements.txt
```

## Menjalankan API

```powershell
python -m uvicorn app.main:app --reload
```

Dokumentasi Swagger dapat dibuka melalui:

http://127.0.0.1:8000/docs

## Daftar Endpoint

| Method | Endpoint | Fungsi |
|---|---|---|
| GET | `/` | Halaman utama |
| GET | `/api/v1/health` | Health check |
| GET | `/api/v1/rooms/` | Melihat semua ruangan |
| POST | `/api/v1/rooms/` | Menambahkan ruangan |
| GET | `/api/v1/rooms/{room_id}` | Melihat detail ruangan |

## Autentikasi

Endpoint untuk menambahkan ruangan membutuhkan header `X-API-Key`.

API Key latihan:

- Admin: `studyroom-admin-key-2026`
- User: `studyroom-user-key-2026`

Role admin dapat menambahkan ruangan. Role user tidak memiliki izin untuk melakukan operasi tersebut.

**Catatan:** API Key di atas hanya untuk latihan. Jangan gunakan API Key hardcoded seperti ini untuk aplikasi produksi.

## Menjalankan Pengujian

Jalankan perintah berikut:

```powershell
python -m pytest -v
```

Hasil pengujian terakhir: **21 passed**.

## Catatan

Data ruangan masih disimpan dalam memori sementara. Data akan hilang ketika server dimulai ulang.
