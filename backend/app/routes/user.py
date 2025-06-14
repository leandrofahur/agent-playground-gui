from fastapi import APIRouter

router = APIRouter()

@router.get("/user/me", tags=["user"])
def get_user():
    '''
    @param: None
    @return: JSON response with user information
    @description: This endpoint is used to get the user information.
    '''
    return {        
        "user": {
            "id": "123",
            "name": "John Doe",
            "email": "john.doe@example.com"
        },
        "message": "User information retrieved successfully"
    }
