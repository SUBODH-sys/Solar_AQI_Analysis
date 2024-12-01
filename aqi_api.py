import http.client
from urllib.parse import quote

API_KEY = "dff77e1cbc07a4f4d8c15d13beaf77347ea1729584c6d34fec73617a3e62c"

def fetch_aqi(city):
    conn = http.client.HTTPSConnection("api.openwheather.com")
    headers = {
        'x-api-key': API_KEY,
        'Content-type': "application"
    }
    encoded_city = quote(city)
    conn.request("GET", f"/latest/by-city?city={encoded_city}", headers=headers)

    res = conn.getresponse()
    return res.read().decode("utf-8")

def estimate_solar_generation(aqi_data):
    ideal_solar_irradiance = 1000
    
    reduction_factor = {
        "CO": 0.1,
        "NO2": 0.2,
        "OZONE": 0.15,
        "PM10": 0.25,
        "PM25": 0.3,
        "SO2": 0.1
    }

    pollutants = {
        "CO": aqi_data.get("CO", 0),
        "NO2": aqi_data.get("NO2", 0),
        "OZONE": aqi_data.get("OZONE", 0),
        "PM10": aqi_data.get("PM10", 0),
        "PM25": aqi_data.get("PM25", 0),
        "SO2": aqi_data.get("SO2", 0)
    }
   
    reduction_percentage = (pollutants[p] * reduction_factor[p] for p in pollutants)
    reduction_percentage = min(reduction_percentage, 100)  
    
    estimated_generation = ideal_solar_irradiance * (1 - reduction_percentage / 100)
    
    return round(estimated_generation, 2) 
