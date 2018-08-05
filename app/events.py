from flask import session, request
from flask_socketio import emit, join_room, leave_room
from app import socketio


@socketio.on('joined')
def joined(message):
    room = session.get('username')
    join_room(room)
    print('join')
    print(room)
    # emit('status', {'msg': session.get('username') + str(' has entered the room.')}, room=room)


@socketio.on('text')
def text(message):
    room = session.get('username')
    emit('message', {'msg': session.get('username') + ':' + message['msg']}, room=room)


@socketio.on('left')
def left(message):
    room = session.get('username')
    leave_room(room)
    emit('status', {'msg': session.get('username') + ' has left the room.'}, room=room)
