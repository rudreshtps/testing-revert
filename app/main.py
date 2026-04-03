from fastapi import FastAPI

from app.routers import health, items

app = FastAPI(
    title="Sample API",
    description="Sample FastAPI backend",
    version="0.1.0",
)

app.include_router(health.router, tags=["health"])
app.include_router(items.router, prefix="/items", tags=["items"])


@app.get("/")
def root() -> dict[str, str]:
    return {"message": "Sample FastAPI backend", "docs": "/docs"}
