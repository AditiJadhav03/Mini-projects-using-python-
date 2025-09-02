'''import requests
city = input("Enter city: ")
api_key = "caab03e4d4a7d4b1e9ccc4f06d4a8cb4" 
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

res = requests.get(url).json()
print(f"Weather in {city}: {res['weather'][0]['description']}, Temp: {res['main']['temp']}°C")'''

import requests

city = input("Enter city: ")
api_key = "5b629a736ec9517a3d7b5ea2d0478e6e" 
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

res = requests.get(url).json()

# Debug: Print raw response
print(res)

if res.get("cod") != 200:  # if API returns an error code
    print("Error:", res.get("message", "Something went wrong"))
else:
    weather = res["weather"][0]["description"]
    temp = res["main"]["temp"]
    print(f"Weather in {city}: {weather}, Temp: {temp}°C")
