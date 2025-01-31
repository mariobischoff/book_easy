from fastapi import APIRouter

router = APIRouter()

@router.get("/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id}

@router.put("/{user_id}")
def update_user(user_id: int):
    return {"message": f"User {user_id} updated!"}