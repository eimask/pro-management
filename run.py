from app import app, socketio


# app.run(host='0.0.0.0', port=8000, debug=True)

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000)

