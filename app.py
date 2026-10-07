from fastapi import FastAPI
from fastapi.responses import Response
import json

# Инициализация FastAPI приложения
app = FastAPI()

with open('meetings.json', 'r', encoding="utf-8") as f:
    meetings = json.load(f)

# делаем тестовый endpoint
@app.get("/health")
async def health_check():
    return Response(content="OK", media_type="text/plain")

# делаем endpoint для поиска животного по имени
@app.get("/meetings/name/{name}")
async def find_animal_by_name(name: str):
    for animal in meetings:
            if animal['name'] == name:
               return animal 
    return Response(content="Животное не найдено", media_type="text/plain")

# делаем endpoint для поиска животного по типу
@app.get("/meetings/type/{animal_type}")
async def find_animal_by_type(animal_type: str):
    find_animal = []
    for animal in meetings:
        if animal['type'] == animal_type:
            find_animal.append(animal)
    return find_animal
