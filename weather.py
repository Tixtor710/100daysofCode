import requests

API_KEY= "ce72769ab24a414498e4adaa20de63a7"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

city= input("Enter a City Name: ")
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"

response= requests.get(request_url)

if response.status_code == "200":
    data= response.json()
    weather = data["weather"][0]["description"]
    print(weather)
    temperature =round(data ["main"]["temp"] - 273.15, 2)
    print("weather:",weather)
    print("temperature:", temperature)

else:
    print("error occured.")
