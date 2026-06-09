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

command = "AUTO"

@app.route("/command", methods=["GET"])
def get_command():

    return command

@app.route("/set_command/<cmd>")
def set_command(cmd):

    global command

    command = cmd.upper()

    return jsonify({
        "status": "success",
        "command": command
    })

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
