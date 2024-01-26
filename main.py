from geopy.geocoders import Nominatim
import json
from req import make_post_request

from OrderGenerator import OrderGenerator, random_string


with open("data/config.json", 'r', encoding="utf-8") as file:
    data = json.load(file)


K = 10 ** data["accuracy"]
COUNT = data["count"]
URL = data["url"]


def parse_towns():
    # Открываем файл
    with open('data/citys.json', 'r') as f:
        # Считываем содержимое файла в переменную data
        data = f.read()

    # Преобразуем содержимое файла из JSON в словарь
    towns = json.loads(data)
    data = []
    for v in towns.values():
        data.extend(v)

    result = []

    for i in range(len(data)):
        geolocator = Nominatim(user_agent=random_string(3))
        town = data[i]
        location = geolocator.geocode(town)

        if location:
            result.append ({
                "name": town,
                "latitude": location.latitude,
                "longitude": location.longitude
            })
        else:
            print("invalid location for", town)

    with open("data/res1.json", 'w', encoding="utf-8") as file:
        json.dump(result, file)
    return result


def read_json():
    data = None
    with open('data/data.json', 'r') as f:
        # Считываем содержимое файла в переменную data
        data = f.read()
    return eval(data)


def main():
    towns = read_json()
    if not towns:
        return
    for i in range(COUNT):
        generator = OrderGenerator(towns)
        print(make_post_request(URL, generator.get_request_body()).text)



if __name__ == "__main__":
    main()
