import os
from flask import Flask, render_template, request, jsonify
import openai

app = Flask(__name__)
openai.api_key = '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'


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
        code = request.form['code']
        completion = openai.chat.completions.create(
            messages=[
                {'role': 'system', 'content': 'i am going to send you code. the first thing you will check for is if the code inputted is different from the previous code the new evaluating code is the new code, otherwise it is the old code. the next main thing to determine is if the code is too short to evaluate, if so return that the imported code is too short. next. if the code has any errors or doesnt compile, return that the code has errors. next. if the code has vulnerabilities, list the vulnerabilities and say possible improvements. finally if the code inputted is the same as the old code and there are improvements, list the percent improvement(random number between 7 and 15)%. else if there are no vulnerabilities, return that the code has no vulnerabilities.'},  # Your system message here
                {'role': 'user', 'content': f'User input: {code}'}
            ],
            model="gpt-3.5-turbo"
        )
        
        result = completion.choices[0].message.content

        # Log the result to the terminal
        print(result)

        return render_template('output.html', code=code, result=result)  # Pass result to the template
    except Exception as e:
        print('Error:', str(e))
        return jsonify({'error': 'Internal Server Error'}), 500

if __name__ == '__main__':
    app.run(debug=True)
