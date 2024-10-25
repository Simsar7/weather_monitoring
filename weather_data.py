import requests

def get_weather_data(city):
    api_key = "d10ab055b94792fbf691a747368d0b85"  # Your API key
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    complete_url = f"{base_url}?q={city}&appid={api_key}&units=metric"
    
    response = requests.get(complete_url)
    weather_data = response.json()
    
    print(weather_data)  # Print the raw response for debugging
    
    return weather_data
