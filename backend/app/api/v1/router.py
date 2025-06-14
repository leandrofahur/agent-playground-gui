from fastapi import APIRouter
from api.v1.endpoints import agents, system

api_router = APIRouter(prefix="/api/v1")

# Include all routes:
api_router.include_router(agents.router, prefix="/agents", tags=["agents"])
api_router.include_router(system.router, prefix="/system", tags=["system"])




