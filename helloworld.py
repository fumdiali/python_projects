from bottle import Bottle, run

app = Bottle()

@app.route('/hello')
def hi():
    return "Hello,There.."

run(app,host='localhost',port=8000, debug=True)
