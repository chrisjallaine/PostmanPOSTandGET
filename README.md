# FastAPI User Management API

This is a simple FastAPI project that allows users to be created and stored in a CSV file. The API supports adding multiple users at once and retrieving stored users.

## 🚀 Features
- Create multiple users in a single request  
- Store user data in `users_data.csv`  
- Retrieve stored users via a GET request  
- Data persists even after restarting the server  

## 📌 Requirements
- Python 3.8+  
- FastAPI  
- Uvicorn  
- Pandas  

## 🛠 Installation
1. Clone this repository:  
   ```sh
   git clone https://github.com/yourusername/your-repo-name.git
   cd your-repo-name
   ```

2. Create a virtual environment (optional but recommended):  
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows, use 'venv\Scripts\activate'
   ```

3. Install dependencies:  
   ```sh
   pip install fastapi uvicorn pandas
   ```

## 🚀 Running the API
Start the FastAPI server with:  
```sh
uvicorn main:app --host 127.0.0.1 --port 8000
```
The API will be available at: [http://127.0.0.1:8000](http://127.0.0.1:8000)

## 📖 API Endpoints

### ➕ Create Users (POST `/user/`)
Creates one or more users and stores them in `users_data.csv`.

#### **Request Body (JSON)**
```json
[
    {"user_id": 1, "username": "chrisjallaine"},
    {"user_id": 2, "username": "anotheruser"}
]
```

#### **Response**
```json
{
    "msg": "Users created and stored successfully",
    "users": [
        {"user_id": 1, "username": "chrisjallaine"},
        {"user_id": 2, "username": "anotheruser"}
    ]
}
```

### 📜 Get Users (GET `/users/`)
Retrieves all stored users from `users_data.csv`.

#### **Response Example**
```json
{
    "users": [
        {"user_id": 1, "username": "chrisjallaine"},
        {"user_id": 2, "username": "anotheruser"}
    ]
}
```

### 📂 Export Users (GET `/export_users/`)
Checks if `users_data.csv` exists and confirms storage.

#### **Response Example**
```json
{
    "msg": "Users are stored in 'users_data.csv'"
}
```

## 📂 Where is `users_data.csv` Stored?
The CSV file is saved in the same directory as the script.  
You can check its location by running:  
```sh
ls users_data.csv  # On Windows, use 'dir users_data.csv'
```

## 💡 Notes
- Ensure FastAPI and dependencies are installed before running.  
- If port 8000 is already in use, run FastAPI on another port:  
  ```sh
  uvicorn main:app --host 127.0.0.1 --port 8080
  ```

## 📝 License
This project is licensed under the MIT License.
