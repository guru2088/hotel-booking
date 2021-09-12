from flask_restx import Resource, fields
from flask import request

import flask
import os
from flask import request
from flask import send_file
import requests
import io
import os
import json
import uuid

from main.booking import ns


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


@ns.route('/checkin/<int:floor>/<int:room>', methods=['POST'])
class Checkin(Resource):
    # @ns.marshal_with(booking, envelope='booking')
    def post(self, floor,room):
        try:
            if(any(int(x["floor"]) == int(floor) and int(x["room"]) == int(room)  for x in roomUpdates)):
                return {
                    'statusCode': 200,
                    'desc': "Room not Available",
                    'bookingStatus': 0
                }
            else:
                if(len([x for i,x in enumerate(roomInfo) if int(x["floor"]) == int(floor)]) and int(room) <= 5):
                    roomUpdates.append({"id": uuid.uuid4(), "floor": int(floor), "room": int(room), "status": 2})
                    return {
                        'statusCode': 200,
                        'desc': "Occupied = Floor : " + str(floor) + ", Room : " + str(room),
                        'bookingStatus': 1
                    }
                else:
                    return {
                        'statusCode': 200,
                        'desc': "Invalid Floor and Room Number",
                        'bookingStatus': 2
                    }
        except ValueError:
            return {
                'statusCode': 500,
                'desc': "Error in Checkin. Pleaes try again after some time...",
                'bookingStatus': -1
            }





@ns.route('/checkout/<int:floor>/<int:room>', methods=['POST'])
class Checkout(Resource):
    # @ns.marshal_with(booking, envelope='booking')
    def post(self, floor,room):
        try:
            if(any(x["floor"] == floor and x["room"] == room and x["status"] == 2 for x in roomUpdates)):
                indexes = [i for i,x in enumerate(roomUpdates) if x["floor"] == floor and x["room"] == room]
                del roomUpdates[indexes[0]]
                roomUpdates.append({"floor": int(floor), "room": int(room), "status": 3})
                return {
                    'statusCode': 200,
                    'desc': "Vacant",
                    'bookingStatus': 1
                }
            else:
                return {
                    'statusCode': 200,
                    'desc': "Cannot checkout. Because Room is not occupied",
                    'bookingStatus': 0
                }
        except ValueError:
            return {
                'statusCode': 500,
                'desc': "Error in Checkin. Pleaes try again after some time...",
                'bookingStatus': -1
            }


@ns.route('/cleaned/<int:floor>/<int:room>', methods=['POST'])
class Cleaned(Resource):
    # @ns.marshal_with(booking, envelope='booking')
    def post(self, floor,room):
        try:
            if(any(x["floor"] == floor and x["room"] == room and x["status"] == 3 for x in roomUpdates)):
                indexes = [i for i,x in enumerate(roomUpdates) if x["floor"] == floor and x["room"] == room]
                del roomUpdates[indexes[0]]
                return {
                    'statusCode': 200,
                    'desc': "Available",
                    'bookingStatus': 1
                }
            else:
                return {
                    'statusCode': 200,
                    'desc': "Cannot clean. Because Room is not vacant",
                    'bookingStatus': 1
                }
        except ValueError:
            return {
                'statusCode': 500,
                'desc': "Error in Checkin. Pleaes try again after some time...",
                'bookingStatus': -1
            }


@ns.route('/mark-repair/<int:floor>/<int:room>', methods=['POST'])
class Markrepair(Resource):
    # @ns.marshal_with(booking, envelope='booking')
    def post(self, floor,room):
        try:
            if(any(x["floor"] == floor and x["room"] == room and x["status"] == 3 for x in roomUpdates)):
                indexes = [i for i,x in enumerate(roomUpdates) if x["floor"] == floor and x["room"] == room]
                del roomUpdates[indexes[0]]
                roomUpdates.append({"floor": int(floor), "room": int(room), "status": 4})
                return {
                    'statusCode': 200,
                    'desc': "Taken for Repair",
                    'bookingStatus': 1
                }
            else:
                return {
                    'statusCode': 200,
                    'desc': "Cannot take for repair. Because Room is not vacant",
                    'bookingStatus': 1
                }
        except ValueError:
            return {
                'statusCode': 500,
                'desc': "Error in Checkin. Pleaes try again after some time...",
                'bookingStatus': -1
            }

@ns.route('/completed-repair/<int:floor>/<int:room>', methods=['POST'])
class Completedrepair(Resource):
    # @ns.marshal_with(booking, envelope='booking')
    def post(self, floor,room):
        try:
            if(any(x["floor"] == floor and x["room"] == room and x["status"] == 4 for x in roomUpdates)):
                indexes = [i for i,x in enumerate(roomUpdates) if x["floor"] == floor and x["room"] == room]
                del roomUpdates[indexes[0]]
                roomUpdates.append({"floor": int(floor), "room": int(room) ,"status": 3})
                return {
                    'statusCode': 200,
                    'desc': "Repair Completed",
                    'bookingStatus': 1
                }
            else:
                return {
                    'statusCode': 200,
                    'desc': "Cannot mark repair completed. Because Room is not taken for repair",
                    'bookingStatus': 1
                }
        except ValueError:
            return {
                'statusCode': 500,
                'desc': "Error in Checkin. Pleaes try again after some time...",
                'bookingStatus': -1
            }



@ns.route('/available/', methods=['GET'])
class RoomsAvailable(Resource):
    # @ns.marshal_with(booking, envelope='booking')
    def get(self):
        try:
            availabile = []
            for idxFloor,floor in enumerate(roomInfo):
                for idxRoom,room in enumerate(floor["rooms"]):
                    if(any(int(x["floor"]) == floor["floor"] and int(x["room"]) == room["id"] for x in roomUpdates) == False):
                        availabile.append(str(floor["floor"]) +  "-" + str(room["id"]))
                    if(idxFloor == len(roomInfo) - 1 and idxRoom == len(floor["rooms"]) - 1):
                        response = dict();
                        response['availabile'] = availabile
                        return {
                            'statusCode': 200,
                            'desc': "Available Rooms",
                            'response': response
                        }
        except ValueError:
            return {
                'statusCode': 500,
                'desc': "Error in Checkin. Pleaes try again after some time...",
                'bookingStatus': -1
            }
