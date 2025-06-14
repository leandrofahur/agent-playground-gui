from pydantic import BaseModel

class AgentSimulateResponse(BaseModel):
    status: str = "failed"
    steps: list[dict] = [{"tool": "", "input": "", "output": "", "success": False}]
    final_output: str = ""

class AgentToolResponse(BaseModel):
    name: str
    description: str
    params: list = []