from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

data_sensor = {
    "suhu": 0,
    "cahaya": 0,
    "kondisi": "-",
    "waktu": "-",
    "lampu": "OFF"
}

@app.route("/")
def home():

    return render_template(
        "index.html",
        data=data_sensor
    )

@app.route("/data", methods=["POST"])
def receive_data():

    global data_sensor

    data_sensor = request.json

    return jsonify({
        "status": "success"
    })

if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )