from flask import Flask
from flask import abort, redirect, url_for
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login')
def login():
    abort(401)
    #this_is_never_executed()

@app.route('/test')
def test():
    return

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404

if __name__ == '__main__':
    app.run(debug=True)