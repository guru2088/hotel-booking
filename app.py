import flask
import os
from flask import request
from flask import send_file
import requests
import io
import os
import json
import uuid


app = flask.Flask(__name__)
app.config["DEBUG"] = True

roomInfo = [
    {
        "floor": 1,
        "rooms" : [
            {"id": 1, "name" : "A"},
            {"id": 2, "name" : "B"},
            {"id": 3, "name" : "C"},
            {"id": 4, "name" : "D"},
            {"id": 5, "name" : "E"}
        ]
    },
    {
        "floor": 2,
        "rooms" : [
            {"id": 1, "name" : "A"},
            {"id": 2, "name" : "B"},
            {"id": 3, "name" : "C"},
            {"id": 4, "name" : "D"},
            {"id": 5, "name" : "E"}
        ]
    },
    {
        "floor": 3,
        "rooms" : [
            {"id": 1, "name" : "A"},
            {"id": 2, "name" : "B"},
            {"id": 3, "name" : "C"},
            {"id": 4, "name" : "D"},
            {"id": 5, "name" : "E"}
        ]
    },
    {
        "floor": 4,
        "rooms" : [
            {"id": 1, "name" : "A"},
            {"id": 2, "name" : "B"},
            {"id": 3, "name" : "C"},
            {"id": 4, "name" : "D"},
            {"id": 5, "name" : "E"}
        ]
    },
]



roomStatus  = [
    {"id" : 1, "status" : "Available", "color": "Green"},
    {"id" : 2, "status" : "Occupied", "color": "Red"},
    {"id" : 3, "status" : "Vacant", "color": "Orange"},
    {"id" : 4, "status" : "Repair", "color": "Gray"}
]


# Above Master JSONs roomInfo and roomStatus can also be stored in any databases or External Data soruces,
# For ease of view i have placed here

roomUpdates = []

# For this program i am updating all the values in local array. We can also do CRUD operations in database. Please
# maintain the server running during all testing cycles. If server restarted all the testing operations needs to be done
# from start

@app.route('/', methods=['GET'])
def main():
    return "Welcome to Boutique Hotel Reservation System"

@app.route('/checkin/<floor>/<room>', methods=['POST'])
def checkin(floor,room):
    try:
        if(any(int(x["floor"]) == int(floor) and int(x["room"]) == int(room)  for x in roomUpdates)):
            return "Room not Available"
        else:
            if(len([x for i,x in enumerate(roomInfo) if int(x["floor"]) == int(floor)]) and int(room) <= 5):
                roomUpdates.append({"id": uuid.uuid4(), "floor": int(floor), "room": int(room), "status": 2})
                return "Occupied = Floor : " + str(floor) + ", Room : " + str(room)
            else:
                return "Invalid Floor and Room Number"
    except ValueError:
        return "error"


@app.route('/checkout/<floor>/<room>', methods=['POST'])
def checkout(floor,room):
    try:
        if(any(x["floor"] == floor and x["room"] == room and x["status"] == 2 for x in roomUpdates)):
            indexes = [i for i,x in enumerate(roomUpdates) if x["floor"] == floor and x["room"] == room]
            del roomUpdates[indexes[0]]
            roomUpdates.append({"floor": int(floor), "room": int(room), "status": 3})
            return "Vacant"
        else:
            return "Cannot checkout. Because Room is not occupied"
    except ValueError:
        return "error"



@app.route('/cleaned/<floor>/<room>', methods=['POST'])
def cleaned(floor,room):
    try:
        if(any(x["floor"] == floor and x["room"] == room and x["status"] == 3 for x in roomUpdates)):
            indexes = [i for i,x in enumerate(roomUpdates) if x["floor"] == floor and x["room"] == room]
            del roomUpdates[indexes[0]]
            return "Available"
        else:
            return "Cannot clean. Because Room is not vacant"
    except ValueError:
        return "error"

@app.route('/mark-repair/<floor>/<room>', methods=['POST'])
def markrepair(floor,room):
    try:
        if(any(x["floor"] == floor and x["room"] == room and x["status"] == 3 for x in roomUpdates)):
            indexes = [i for i,x in enumerate(roomUpdates) if x["floor"] == floor and x["room"] == room]
            del roomUpdates[indexes[0]]
            roomUpdates.append({"floor": int(floor), "room": int(room), "status": 4})
            return "Taken for Repair"
        else:
            return "Cannot take for repair. Because Room is not vacant"
    except ValueError:
        return "error"

@app.route('/completed-repair/<floor>/<room>', methods=['POST'])
def completedrepair(floor,room):
    try:
        if(any(x["floor"] == floor and x["room"] == room and x["status"] == 4 for x in roomUpdates)):
            indexes = [i for i,x in enumerate(roomUpdates) if x["floor"] == floor and x["room"] == room]
            del roomUpdates[indexes[0]]
            roomUpdates.append({"floor": int(floor), "room": int(room) ,"status": 3})
            return "Repair Completed"
        else:
            return "Cannot mark repair completed. Because Room is not taken for repair"
    except ValueError:
        return "error"

@app.route('/available', methods=['GET'])
def roomsAvailable():
    try:
        availabile = []
        for idxFloor,floor in enumerate(roomInfo):
            for idxRoom,room in enumerate(floor["rooms"]):
                if(any(int(x["floor"]) == floor["floor"] and int(x["room"]) == room["id"] for x in roomUpdates) == False):
                    availabile.append(str(floor["floor"]) +  "-" + str(room["id"]))
                if(idxFloor == len(roomInfo) - 1 and idxRoom == len(floor["rooms"]) - 1):
                    response = dict();
                    response['availabile'] = availabile
                    return response
    except ValueError:
        return "error"

app.run(host='0.0.0.0', port=8002)
