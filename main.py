import pandas
from flask import Flask, render_template, request, redirect, url_for
import data_functions
mypath = "data/"

if data_functions.check_db_present(mypath):
    pass
else:
    data_functions.extract_clean_data(mypath)

app = Flask(__name__)


@app.route("/")
def home():
    # Fetch data from your function
    stations_list = data_functions.get_stations(mypath)

    # PASS the data to the HTML template using a keyword argument
    return render_template("home.html", weather_data=stations_list)

@app.route("/api/v1/<station>/<date>")
def about(station, date):
    temperature = {
        "station": station,
        "date": date,
        "temperature": data_functions.fetch_temperature(mypath,station, date),
    }
    return temperature
if __name__ == "__main__":
    app.run(debug=True)