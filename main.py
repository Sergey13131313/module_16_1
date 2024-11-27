from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    return "Главная"

@app.get('/user/admin')
async def admin_page() -> str:
    return 'Вы вошли как администратор'


@app.get('/user/{user_id}')
async def id_page(user_id: str) -> str:
    return f'Вы вошли как пользователь № {user_id}'


@app.get('/user')
async def user(user_name:str, age:int)->str:
    return f'Информация о пользователе. Имя: {user_name}, Возраст: {age}'


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.2", port=8000)