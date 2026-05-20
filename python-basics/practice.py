cities = [
    {'name': 'Thorsby', 'temp': 80},
    {'name': 'Clanton', 'temp': 90},
    {'name': 'Birmingham', 'temp': 60},
    {'name': 'Bessemer', 'temp': 34},
    {'name': 'Alabaster', 'temp': 12},
    ]

def city_temp():
    cold_temp = 0
    hot_temp = 0
    for city in cities:
        if city['temp'] >= 80:
            print(f"Stay cool, it's {city['temp']}")
            hot_temp += 1
        else:
            print(f"Not too hot, it's only {city['temp']}")
            cold_temp += 1
    summary(cold_temp,hot_temp)


def summary(cold_temp,hot_temp):
    print(f"There are {hot_temp} hot cities and {cold_temp} cold cities. Plan accordingly")

city_temp()
