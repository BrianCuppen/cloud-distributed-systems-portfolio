from fastapi import FastAPI
from app.models import LoginRequest, TokenResponse
from app.auth import authenticate_user

app = FastAPI(
    title="Auth Service",
    version="1.0.0"
)


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }


@app.post(
    "/login",
    response_model=TokenResponse
)
def login(request: LoginRequest):

    token = authenticate_user(
        request.username,
        request.password
    )

    return {
        "access_token": token,
        "token_type": "bearer"
    }