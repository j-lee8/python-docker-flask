import requests
# import pandas as pd
from flask import Flask, render_template
app = Flask(__name__)

query = """query {
    launches {
        rocket {
            rocket_name
        }
        mission_name
        id
    }
}"""

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/ships")
def get_ships():
    url = 'https://api.spacex.land/graphql/'
    r = requests.post(url, json={'query': query})
    print(r.status_code)
    print(r.text)

    return render_template('ships.html', data=r.text) 

if __name__ == "__main__":
  app.run(debug=True)