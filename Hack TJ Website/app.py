import os
from flask import Flask, render_template, request, jsonify, redirect, url_for
import openai

app = Flask(__name__)
openai.api_key = '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'

def index():
    return render_template('logIn.html')

# Update the route to handle the form submission and redirect to /overview
@app.route('/overview', methods=['POST'])
def handle_login():

    return redirect(url_for('overview'))

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
    try:
        # Assuming successful login, redirect to the overview page
        return redirect(url_for('overview'))

        # The following code is not needed as we are redirecting
        # code = request.form['code']
        # completion = openai.chat.completions.create(
        #     messages=[
        #         {'role': 'system', 'content': '...'},  
        #         {'role': 'user', 'content': f'User input: {code}'}
        #     ],
        #     model="gpt-3.5-turbo"
        # )
        # result = completion.choices[0].message.content

        # Log the result to the terminal
        # print(result)

        # return render_template('output.html', code=code, result=result)
    except Exception as e:
        print('Error:', str(e))
        return jsonify({'error': 'Internal Server Error'}), 500

if __name__ == '__main__':
    app.run(debug=True)
