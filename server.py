from flask import Flask, render_template, session, redirect, request

app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe' # set a secret key for security purposes
import random # import the random module


@app.route('/')
def home():
    if 'num' not in session:
        session['num'] = random.randint(1, 100) # random number between 1-100
    return render_template('index.html')

@app.route('/test_num', methods = ['POST'])
def test_num():
    session['guessed_number'] = request.form['guessed_number']
    if int(session['guessed_number']) > int(session['num']):
        session['status'] = 'Too High'
    elif int(session['guessed_number']) < int(session['num']):
        session['status'] = 'Too Low'
    else:
        session['status'] = 'Equal'
    return redirect('/')

@app.route('/clear')
def clear():
    session.clear()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)