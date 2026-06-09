from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

data_sensor = {
"suhu": 0,
"cahaya": 0,
"kondisi": "-",
"waktu": "-",
"lampu": "OFF"
}

command = "AUTO"

@app.route("/")
def home():

```
return render_template(
    "index.html",
    data=data_sensor
)
```

@app.route("/data", methods=["POST"])
def receive_data():

```
global data_sensor

data_sensor = request.json

return jsonify({
    "status": "success"
})
```

@app.route("/sensor")
def sensor():

```
return jsonify(data_sensor)
```

@app.route("/command")
def get_command():

```
return command
```

@app.route("/set_command/<cmd>")
def set_command(cmd):

```
global command

command = cmd.upper()

return jsonify({
    "status": "success",
    "command": command
})
```

if **name** == "**main**":

```
app.run(
    host="0.0.0.0",
    port=5000,
    debug=True
)
```
