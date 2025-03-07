from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('highlight_region')
def handle_highlight(data):
    """
    Receives a region to highlight and broadcasts to all clients.
    Example message: {"region": "toes"}
    """
    socketio.emit('update_highlight', data)

if __name__ == '__main__':
    socketio.run(app, debug=True)

