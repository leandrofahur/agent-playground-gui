from pydantic import BaseModel

class AgentSimulateRequest(BaseModel):
    goal: str = ""
    agent_type: str = "langchain"
    tools: list[str] = []
    memory: dict = {}
    retry: dict = {}
    verbose: bool = True
