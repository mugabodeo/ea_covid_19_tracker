from flask import Flask, render_template
import requests
from flask_disqus import Disqus


app = Flask(__name__)
disq = Disqus(app)


@app.route('/')
def home():
    req_data = requests.get(
        "https://pomber.github.io/covid19/timeseries.json").json()
    print(req_data["Rwanda"])

    SSdata = {'date': req_data["Rwanda"][-1]["date"],
              'confirmed': 0, 'deaths': 0, 'recovered': 0}

    return render_template("index.html",
                           Rdata=req_data["Rwanda"][-1],
                           Kdata=req_data["Kenya"][-1],
                           Ugdata=req_data["Uganda"][-1],
                           Tzdata=req_data["Tanzania"][-1],
                           Bdata=req_data["Burundi"][-1],
                           SSdata=SSdata
                           )
