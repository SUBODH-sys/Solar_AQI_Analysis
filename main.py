from flask import Flask, render_template, request
from aqi_api import fetch_aqi, estimate_solar_generation

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get_aqi", methods=["POST"])
def get_aqi():
    city = request.form.get("city")
    aqi_data = fetch_aqi(city)
    
    aqi_json = json.loads(aqi_data)
    if aqi_json.get("message") == "success" and aqi_json.get("stations"):
        station = aqi_json["stations"][0]  
        context = {
            "city": station.get("city"),
            "state": station.get("state"),
            "AQI": station.get("AQI"),
            "category": station.get("aqiInfo", {}).get("category"),
            "CO": station.get("CO"),
            "NO2": station.get("NO2"),
            "OZONE": station.get("OZONE"),
            "PM10": station.get("PM10"),
            "PM25": station.get("PM25"),
            "SO2": station.get("SO2"),
            "updated_at": station.get("updatedAt")
        }

        context["solar_generation"] = estimate_solar_generation(context)
    else:
        context = {
            "error": "Unable to fetch AQI data for the specified city."
        }

    return render_template("result.html", context=context)

if __name__ == "__main__":
    app.run(debug=True)
