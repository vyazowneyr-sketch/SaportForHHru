from fastapi import FastAPI
from app.api import api_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title = "HHru Sapport",
    description = "Service for parsing and delivering vacancies from HH API",
    version = "0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
    )
