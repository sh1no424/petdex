from fastapi import FastAPI
from fastapi.responses import Response
from pydantic import BaseModel, Field
from typing import Literal
from datetime import date
import json

# Инициализация FastAPI приложения
app = FastAPI()

with open('meetings.json', 'r', encoding="utf-8") as f:
    meetings = json.load(f)

class Geo(BaseModel):
        lat: float=Field(ge=-90, le=90)
        lon: float=Field(ge=-180, le=180)
        
class MeetingCreate(BaseModel):
    name: str
    type: Literal["cat", "dog"]
    geo: Geo
    date: date

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

@app.post("/meetings/create/", status_code=201 )
async def create_meeting(meeting: MeetingCreate):
    meetings.append(meeting.model_dump())
    return Response(content="Добавлена встреча с животным", media_type="text/plain")
