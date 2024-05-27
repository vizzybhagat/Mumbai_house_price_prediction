from flask import Flask, request, jsonify
import util

app= Flask(__name__)

#Simple routing function
@app.route('/get_location_names')
def get_location_names():
    response = jsonify({
        'locations': util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin','*')
    return response


@app.route('/predict_home_price', methods=['POST'])
def predict_home_price():
    total_sqft = int(request.form['total_sqft'])
    bhk = int(request.form['bhk'])
    location = request.form['location']

    response = jsonify({
        'estimated_price': util.get_estimated_price(location, total_sqft,bhk)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


if __name__=='__main__':
    print("Starting Python flask server for home price prediction..")
    util.load_saved_artifacts()
    app.run()