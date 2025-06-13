from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware

# Import the routes
from routes.system import router as system_router
from routes.user import router as user_router

app = FastAPI()
router = APIRouter(prefix="/api/v1")

# @router.get("/")
# def read_root():
#     return {"message": "Sanity Check!"}

# Wrap the router with the app to include the prefix /api/v1
router.include_router(system_router)
router.include_router(user_router)

# Add the router to the app
app.include_router(router)

# Enable communication between frontend and backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)