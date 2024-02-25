from flask import Flask, render_template, request, jsonify

app = Flask(__name__, static_url_path='/static')


@app.route('/')
def index():
    return render_template('logIn.html')

@app.route('/submit')
def submit():
    return render_template('submit.html')

@app.route('/overview')
def overview():
    return render_template('overview.html')

@app.route('/creators')
def creators():
    return render_template('creators.html')

@app.route('/output')
def output():
    return render_template('output.html')

@app.route('/faq')
def faq():
    return render_template('faq.html')

@app.route('/evaluate', methods=['POST'])
def evaluate():
    return render_template('output.html')

if __name__ == '__main__':
    app.run(debug=True)
