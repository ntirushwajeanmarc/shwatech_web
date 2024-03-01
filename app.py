from flask import Flask, request,render_template,url_for,jsonify

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
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
    app.run(debug=True, port=5000)