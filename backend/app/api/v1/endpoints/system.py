from fastapi import APIRouter

router = APIRouter()

@router.get("/health", tags=["system"])
def health_check():
    '''
    @param: None
    @return: JSON response with status "ok!"
    @description: This endpoint is used to check if the backend is running.
    '''
    return {"status": "ok!"}

