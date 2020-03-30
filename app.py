from flask import Flask, render_template
import requests

app = Flask(__name__)
{'date': '2020-3-27', 'confirmed': 54, 'deaths': 0, 'recovered': 0}


@app.route('/')
def home():
    req_data = requests.get(
        "https://pomber.github.io/covid19/timeseries.json").json()
    print(req_data["Rwanda"])
    Bdata = {'date': req_data["Rwanda"][-1]["date"],
             'confirmed': 0, 'deaths': 0, 'recovered': 0}

    SSdata = {'date': req_data["Rwanda"][-1]["date"],
              'confirmed': 0, 'deaths': 0, 'recovered': 0}

    return render_template("index.html",
                           Rdata=req_data["Rwanda"][-1],
                           Kdata=req_data["Kenya"][-1],
                           Ugdata=req_data["Uganda"][-1],
                           Tzdata=req_data["Tanzania"][-1],
                           Bdata=Bdata,
                           SSdata=SSdata
                           )
