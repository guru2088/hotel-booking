import flask
import os
from flask import request
from flask import send_file
import requests
import io
import os
import json


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


# Above Master JSONs can also be stored in any database or constant files , For ease of view i have placed here

roomUpdates = []

@app.route('/', methods=['GET'])
def main():
    return "Welcome to Boutique Hotel Reservation System"

@app.route('/checkin/<floor>/<room>', methods=['POST'])
def checkin(floor,room):
    roomUpdates.append({"floor": floor, "room": room, "status": 2})
    return "Checkin Successfull"

@app.route('/checkout/<floor>/<room>', methods=['POST'])
def checkout(floor,room):
    roomUpdates.append({"floor": floor, "room": room, "status": 3})
    return "Checkout Successfull"

@app.route('/cleaned/<floor>/<room>', methods=['POST'])
def cleaned(floor,room):
    roomUpdates.append({"floor": floor, "room": room, "status": 1})
    return "Cleaned Successfull"

@app.route('/repair/<floor>/<room>', methods=['POST'])
def repair(floor,room):
    roomUpdates.append({"floor": floor, "room": room, "status": 4})
    # checkout(floor,room)
    return "Repair Successfull"

@app.route('/available/', methods=['GET'])
def roomsAvailable():
    availability = []
    for floor in roomInfo:
        for room in floor["rooms"]:
            if(roomUpdates and [x for x in roomUpdates if int(x["floor"]) == int(floor["floor"]) and int(x["room"]) == int(room["id"])]):
                availability.append("Occupied " + str(floor["floor"]) + " -" + str(room["id"]))
            else:
                availability.append("Vacant "+  str(floor["floor"]) + " - " + str(room["id"]))
    return availability



app.run(host='0.0.0.0', port=8000)
