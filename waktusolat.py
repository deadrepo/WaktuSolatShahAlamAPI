from flask import Flask
from flask import jsonify
import requests

app = Flask(__name__)

@app.route('/waktusolat/')
def waktusolat():

    #Shah Alam API Endpoint
    URL = "https://www.e-solat.gov.my/index.php?r=esolatApi/takwimsolat&period=today&zone=sgr01"

    # A GET request to the API
    response = requests.get(URL)

    # Print the response
    response_json = response.json()
    print(response_json)
    print()
    return(response_json)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=105)

