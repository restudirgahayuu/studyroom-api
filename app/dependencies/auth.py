
import secrets

from fastapi import Header, HTTPException, status


# API key untuk latihan
API_KEYS = {
    "studyroom-admin-key-2026": "admin",
    "studyroom-user-key-2026": "user",
}


def verify_api_key(
    x_api_key: str = Header(default=""),
) -> str:
    for api_key, role in API_KEYS.items():
        if secrets.compare_digest(x_api_key, api_key):
            return role

    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="API key tidak valid atau tidak ditemukan",
    )


def require_admin(role: str) -> None:
    if role != "admin":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Akses ditolak. Role admin diperlukan.",
        )
