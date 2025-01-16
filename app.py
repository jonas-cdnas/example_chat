from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit
import logging

# Configuración del servidor Flask y SocketIO
app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecretkey'
socketio = SocketIO(app)

# Configuración de logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

@app.route('/')
def index():
    logging.info("Route '/' accessed")
    return render_template('index.html')

@socketio.on('connect')
def handle_connect():
    user_ip = request.remote_addr or '127.0.0.1'
    logging.info(f"Client connected: {user_ip}")
    emit('message', {'type': 'status', 'sender': user_ip, 'data': 'Connected successfully'}, broadcast=True)

@socketio.on('disconnect')
def handle_disconnect():
    user_ip = request.remote_addr or '127.0.0.1'
    logging.info(f"Client disconnected: {user_ip}")
    emit('message', {'type': 'status', 'sender': user_ip, 'data': 'Disconnected'}, broadcast=True)

@socketio.on('message')
def handle_message(message):
    user_ip = request.remote_addr or '127.0.0.1'
    logging.info(f"Message received from {user_ip}: {message}")
    emit('message', {'type': 'chat', 'sender': user_ip, 'data': message}, broadcast=True)

if __name__ == '__main__':
    logging.info("Starting Flask-SocketIO server on 0.0.0.0:9000")
    socketio.run(app, host='0.0.0.0', port=9000, debug=True)