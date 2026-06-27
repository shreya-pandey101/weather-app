from flask import Flask, render_template, request
import requests
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("API_KEY")

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/weather",methods=["post"])
def weather():
    city_name = request.form["city"]
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()
    if data['cod']==200:
        description = data['weather'][0]['description']
        temp = data['main']['temp']
        return render_template("index.html",weather_data=f"The weather in city {city_name} is {description} with a temperature of {temp}°C")
    else:
        return "City not found. Please try again."
if __name__ == "__main__":
    app.run(debug=True)