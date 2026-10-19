
# StudyRoom API

REST API untuk mengelola ruang belajar menggunakan FastAPI dan Python.

## Fitur

- Endpoint Home dan Health Check.
- Melihat daftar ruangan.
- Menambahkan ruangan.
- Melihat detail ruangan berdasarkan ID.
- Validasi data menggunakan Pydantic.
- Pengujian otomatis menggunakan Pytest.

## Teknologi

- Python 3.11
- FastAPI
- Uvicorn
- Pydantic
- Pytest
- HTTPX

## Instalasi

Buat virtual environment:

```bash
python -m venv .venv
```

Aktifkan virtual environment di Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Instal dependensi:

```bash
python -m pip install -r requirements.txt
```

## Menjalankan API

```bash
python -m uvicorn app.main:app --reload
```

Buka dokumentasi Swagger:

http://127.0.0.1:8000/docs

## Daftar Endpoint

| Method | Endpoint | Fungsi |
|---|---|---|
| GET | `/` | Halaman utama |
| GET | `/api/v1/health` | Health check |
| GET | `/api/v1/rooms/` | Melihat semua ruangan |
| POST | `/api/v1/rooms/` | Membuat ruangan |
| GET | `/api/v1/rooms/{room_id}` | Melihat detail ruangan |

## Menjalankan Pengujian

```bash
python -m pytest -v
```

Hasil pengujian awal: 15 test berhasil.

## Catatan

Data ruangan masih disimpan dalam memori sementara dan
akan hilang ketika server dimulai ulang.
