from flask import Flask, request,render_template,url_for
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/GSM')
def gsm():
    return render_template('gsm.html')
@app.route('/arduino-sensors')
def arduinoSensors():
    return render_template('sensors.html')
if __name__ == '__main__':
    app.run(debug=True, port=5000)