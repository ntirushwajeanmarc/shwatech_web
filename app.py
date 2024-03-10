from flask import Flask, request,render_template,url_for,jsonify

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

#api request

data = {
    'phosphorus':4.6,
    'calicium':5.6,
    'potassium': 7.8,
    'ph':5.4,
    'result':'rice'
}
@app.route('/marcapi', methods=['GET','POST'])
def getapi():
    if request.method == 'GET':
        return jsonify(data)
    if request.method == 'POST':
        return jsonify(data)

#end of api request

#arduino part
@app.route('/arduino-gsm')
def gsm():
    return render_template('arduino/gsm.html')
@app.route('/arduino-sensors')
def arduinoSensors():
    return render_template('arduino/sensors.html')

@app.route('/arduino-introduction')
def arduino_intro():
    return render_template('arduino/introduction.html')
@app.route('/arduino-basics')
def arduino_basics():
    return render_template('arduino/basics.html')

@app.route('/arduino-ide')
def arduino_ide():
    return render_template('arduino/ide.html')

@app.route('/arduino-syntax')
def syntax():
    return render_template('arduino/syntax.html')

@app.route('/arduino-variables')
def arduino_variable():
    return render_template('arduino/variiable.html')

@app.route('/arduino-digital-io')
def arduino_digital():
    return render_template('arduino/digital.html')

@app.route('/arduino-analog-io')
def arduino_analog():
    return render_template('arduino/analog.html')

@app.route('/arduino-control')
def arduino_controller():
    return render_template('arduino/control.html')

@app.route('/arduino-functions')
def arduino_functions():
    return render_template('arduino/functions.html')

@app.route('/arduino-libraries')
def arduino_libraries():
    return render_template('arduino/library.html')

@app.route('/arduino-communication')
def arduino_communication():
    return render_template('/arduino/communication.html')

@app.route('/arduino-projects')
def arduino_project():
    return render_template('arduino/projects.html')
#arduino end

#Python
@app.route('/python-comments')
def py_comments():
    return render_template('python/comment.html')
@app.route('/python-variable')
def py_variables():
    return render_template('python/variable.html')
@app.route('/python-data-type')
def py_data_type():
    return render_template('python/datatype.html')
#End of python
content_data = [
    {"title": "Introduction to Python", "url": "/python-intro"},
    {"title": "Getting Started with Arduino", "url": "/arduino-start"},
    {"title": "C++ Basics", "url": "/cpp-basics"},
    {"title": "gsm", "url": "/arduino-gsm"},
    {"title": "sensors", "url": "/arduino-sensors"},
    # Add more content data as needed
]

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('q', '').lower()
    results = [content for content in content_data if query in content['title'].lower()]
    return jsonify(results)

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)