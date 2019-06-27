from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from Block import *

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        lender = request.form['lender']
        amount = request.form['amount']
        borrower = request.form['borrower']

        write_block(name=lender, amount=amount, to_whom=borrower)
        return redirect(url_for('index'))
    return render_template('index.html')


@app.route('/checking', methods=['GET'])
def check():
    results = checkIntegrity()
    return render_template('index.html', results=results)


@app.route('/shows', methods=['GET'])
def show():
    return redirect(url_for('index'))



if __name__ == '__main__':
    app.run(debug=True)