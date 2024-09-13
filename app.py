from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def hello():
    data = None
    if request.method == "POST":
        city = request.form.get('city')
        response = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={city},india&units=imperial&appid=d2a02760d2ef58d25d2c6e3f0fb2c70e")
    
        data = response.json()
    
    return render_template("weather.html", data=data)


if(__name__=="__main__"):
    app.run(debug=True)
