from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware
from config import llm_init

# Import the routes
from routes.system import router as system_router
from routes.user import router as user_router
from routes.agents import router as agents_router

app = FastAPI()

# Configure the router to include the prefix /api/v1
router = APIRouter(prefix="/api/v1")

# Add the configurations on the app when it starts
@app.on_event("startup")
def startup_event():
    print("Starting up...")
    llm_init()

# Wrap the router with the app to include the prefix /api/v1
router.include_router(system_router)
router.include_router(user_router)
router.include_router(agents_router)

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