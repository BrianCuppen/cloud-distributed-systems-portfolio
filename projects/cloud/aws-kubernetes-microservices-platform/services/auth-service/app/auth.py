from fastapi import HTTPException
from app.security import create_access_token


FAKE_USER = {
    "username": "admin",
    "password": "password123"
}


def authenticate_user(username: str, password: str):
    if (
        username != FAKE_USER["username"]
        or password != FAKE_USER["password"]
    ):
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )

    token = create_access_token(
        data={"sub": username}
    )

    return token