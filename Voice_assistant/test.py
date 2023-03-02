import pyowm
from textblob import TextBlob

token = "384b9846cf4c17ec74e5b1334bc9ca02"

owm = pyowm.OWM(token)
manager = owm.weather_manager()

final_ru_str = "Альметьевск"
blob = TextBlob(final_ru_str)
final_en_str = str(blob.translate(to="en"))

observation = manager.weather_at_place(final_en_str)

weather = observation.weather

ost = {"first": [2, 3, 4], "second": [1], "not": [11, 12, 13, 14]}
temp_city = round(weather.temperature('celsius')['temp'])
temp = abs(temp_city) % 10


if temp in ost["first"] and temp not in ost["not"]:
    cels = "градуса"
elif temp in ost["second"] and temp not in ost["not"]:
    cels = "градус"
else:
    cels = "градусов"

speed_city = round(weather.wind()['speed'], 1)
print(
    f"На улице города {final_ru_str} сейчас {temp_city} {cels}, ветер {speed_city} метра в секунду.")
