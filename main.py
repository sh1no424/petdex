import json

with open('meetings.json', 'r', encoding='utf-8') as f:
    meetings = json.load(f)

def find_animal_by_name(name):
    for animal in meetings:
        if animal['name'] == name:
            return f"Имя: {animal['name']}, Тип: {animal['type']}, Координаты: {animal['geo']['lat']}, {animal['geo']['lon']}"
    return None

def find_animal_by_geo(lat, lon):
    count_animal = 0
    for animal in meetings:
        if animal['geo']['lat'] > lat and animal['geo']['lon'] > lon:
            count_animal += 1
    return count_animal

def find_animal_by_type(animal_type):
    find_animal = []
    for animal in meetings:
        if animal['type'] == animal_type:
            find_animal.append(f"Имя: {animal['name']}, Тип: {animal['type']}, Координаты: {animal['geo']['lat']}, {animal['geo']['lon']}")
    return find_animal

#search_name = input("Введите имя животного для поиска:")
#print(find_animal_by_name(search_name))
#search_lat = float(input("Введите широту для поиска:"))
#search_lon = float(input("Введите долготу для поиска:"))
#print(find_animal_by_geo(search_lat, search_lon))
search_type = input("Введите тип животного для поиска:")
print("\n".join(find_animal_by_type(search_type)))