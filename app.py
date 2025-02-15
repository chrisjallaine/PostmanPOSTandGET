from fastapi import FastAPI
from pydantic import BaseModel, Field
import pandas as pd
import os

app = FastAPI()

CSV_FILE = "users_data.csv"

# Ensure CSV file exists with proper headers
if not os.path.exists(CSV_FILE):
    pd.DataFrame(columns=["user_id", "username"]).to_csv(CSV_FILE, index=False)

class UserCreate(BaseModel):
    user_id: int = Field(..., gt=0, description="Unique identifier for the user")
    username: str = Field(..., min_length=3, max_length=50, description="User's unique name")

@app.post("/user/")
async def create_user(user_data: list[UserCreate]):
    """
    API endpoint to create multiple users and store them in a CSV file.
    """
    new_users = [{"user_id": user.user_id, "username": user.username} for user in user_data]

    # Append new users to the CSV file
    df = pd.DataFrame(new_users)
    df.to_csv(CSV_FILE, mode="a", header=False, index=False)

    return {"msg": "Users created and stored successfully", "users": new_users}

@app.get("/users/")
async def get_users():
    """
    API endpoint to retrieve users from the CSV file.
    """
    try:
        df = pd.read_csv(CSV_FILE)
        users_list = df.to_dict(orient="records")
        return {"users": users_list}
    except Exception as e:
        return {"error": str(e)}

@app.get("/export_users/")
async def export_users():
    """
    API endpoint to confirm that users have been stored in the CSV file.
    """
    if os.path.exists(CSV_FILE):
        return {"msg": f"Users are stored in '{CSV_FILE}'"}
    return {"msg": "No users found in CSV file"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
