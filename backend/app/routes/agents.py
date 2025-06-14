from fastapi import APIRouter
from models.requests import AgentSimulateRequest
from models.responses import AgentSimulateResponse, AgentToolResponse

router = APIRouter()

@router.post("/agents/simulate", tags=["agents"])
def simulate_agent(payload: AgentSimulateRequest) -> AgentSimulateResponse:
    '''
    This endpoint receives an agent configuration (goal, tools, memory, retry strategy, etc.), builds the agent, runs it, and returns the execution trace.
    '''
    # TODO: Implement the agent simulation
    print("Agent simulation started...")
    print(payload)

    return AgentSimulateResponse(
        status="success", 
        steps=[
            {"tool": "tool1", "input": "input1", "output": "output1", "success": True},
            {"tool": "tool2", "input": "input2", "output": "output2", "success": True},
            {"tool": "tool3", "input": "input3", "output": "output3", "success": True},
            {"tool": "tool4", "input": "input4", "output": "output4", "success": True},
            {"tool": "tool5", "input": "input5", "output": "output5", "success": True},
            {"tool": "tool6", "input": "input6", "output": "output6", "success": True},
            {"tool": "tool7", "input": "input7", "output": "output7", "success": True},            
        ], 
        final_output="final_output"
    )

@router.get("/agents/tools", tags=["agents"])
def get_tools() -> list[AgentToolResponse]:
    '''
    @param: None
    @return: list[str]
    @description: This endpoint is used to get the tools.
    '''    
    return [
        AgentToolResponse(name="tool1", description="tool1 description", params=["param1", "param2", "param3"]),
        AgentToolResponse(name="tool2", description="tool2 description", params=[]),
        AgentToolResponse(name="tool3", description="tool3 description", params=["param1"]),
    ]