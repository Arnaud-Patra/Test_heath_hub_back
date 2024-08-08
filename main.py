from fastapi import FastAPI, HTTPException
import uvicorn
from models.usermodel import UserModel
from services.userservice import UserService


app = FastAPI()


@app.get("/")
async def root():
    return {"message": ""}


@app.get("/users/{user_id}")
async def get_user(user_id: int):

    user_service = UserService()
    user = user_service.get_user(user_id)

    # TODO : handle internal error : try catch

    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    return user


@app.post("/create_user")
async def create_user(user_data: UserModel):
    user_service = UserService()

    status = user_service.create_user(user_data)

    return status

if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0', port=8000)
