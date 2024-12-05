from fastapi import FastAPI

app = FastAPI()


@app.get('/')
async def main():
    return 'Главная страница'


@app.get('/user/admin')
async def admin():
    return 'Вы вошли как администратор'


@app.get('/user/{user_id}')
async def user_page(user_id):
    return f'Вы вошли как пользователь № {user_id}'


@app.get('/user')
async def user_info(user_name: str, age: int):
    return f'Информация о пользователе. Имя: {user_name}, Возраст: {age}.'
