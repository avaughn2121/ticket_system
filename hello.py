from flask import Flask, render_template
from gevent.pywsgi import WSGIServer

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/add_ticket')
def add_ticket():
    return render_template('add_ticket.html')

if __name__ == '__main__':
    # Debug/Development
    # app.run(debug=True, host="0.0.0.0", port="5000")
    # Production
    http_server = WSGIServer(('', 5000), app)
    http_server.serve_forever()