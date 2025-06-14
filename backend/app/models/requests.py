from pydantic import BaseModel

class AgentSimulateRequest(BaseModel):
    goal: str
    agent_type: str
    tools: list
    memory: dict
    retry: dict
    verbose: bool


