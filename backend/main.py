from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.auth import router as auth_router
from api.artifacts import router as artifact_router
from api.stripe import router as stripe_router
from database import init_db
app = FastAPI()
origins = ["http://localhost:5173"]  # frontend dev origin
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(auth_router, prefix="/api/auth")
app.include_router(artifact_router, prefix="/api/artifacts")
app.include_router(stripe_router, prefix="/api/stripe")
@app.on_event("startup")
async def startup():
    await init_db()

