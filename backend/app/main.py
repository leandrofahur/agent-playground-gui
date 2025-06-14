from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware
from core.config import llm_init, swagger_metadata_config
from api.v1.router import api_router

app = FastAPI(
    title="Agent Simulation API",
    description="This is the API for the Agent Simulation project.",
    version="1.0.0",
    contact={
        "name": "Agent Simulation API",
        "url": "https://github.com/leandrofahur/agent-playground-gui",                        
    },
    openapi_tags=swagger_metadata_config()
)

# Add the configurations on the app when it starts
@app.on_event("startup")
def startup_event():
    print("\n\nStarting up...")
    print("Config initialized")
    llm_init()    
    print("LLM initialized")
    print("Starting up... done\n\n")

# Add the router to the app
app.include_router(api_router)

# Enable communication between frontend and backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)