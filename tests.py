""" Tests for main.booking.v1.views """
import pytest
import json
from mock import patch
from main.booking.v1.views import Checkin,RoomsAvailable


# def test_create_user(self):
#     resp = self.client.post(
#         self.url,
#         data=json.dumps({
#             'name': 'John Doe',
#             'email': 'john.doe@example.com'
#         }), content_type='application/json')
#     self.assertEqual(resp.status_code, 201)

def test_checkin_success():
    """ Tests the checkin function for success """
    assert {'statusCode': 200, 'desc': 'Occupied = Floor : 1, Room : 1', 'bookingStatus': 1} == Checkin.post(0,1,1)


# def test_checkin():
#     """ Tests the checkin function for error """
#     assert { "message": "The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again. You have requested this URI [/main/api/checkin/asdfasd/1] but did you mean /main/api//checkin/<int:floor>/<int:room> or /main/api//checkout/<int:floor>/<int:room> or /main/api//doc/ ?" } == Checkin("asdfasd",1)

def test_checkin_invalid_floor_number():
    """ Tests the checkin function for invalid floor number """
    assert { "statusCode": 200, "desc": "Invalid Floor and Room Number", "bookingStatus": 2 }  == Checkin.post(0,7,1)


def test_checkin_invalid_room_number():
    """ Tests the checkin function for invalid floor number """
    assert { "statusCode": 200, "desc": "Invalid Floor and Room Number", "bookingStatus": 2 }  == Checkin.post(0,1,6)


def test_checkin_invalid_floorroom_number():
    """ Tests the checkin function for invalid floor number """
    assert { "statusCode": 200, "desc": "Invalid Floor and Room Number", "bookingStatus": 2 }  == Checkin.post(0,10,20)


def test_roomsAvailable():
    """ Tests the available function """
    assert True == isinstance(RoomsAvailable().get(),dict)


# Above are some of the test cases to prove the ability of writing test cases. In real project we can achieve 100% in code coverage

# def test_checkout():
#     """ Tests the checkout function """
#     assert "Checkout Successfull" == checkout(1,1)
#
# def test_cleaned():
#     """ Tests the cleaned function """
#     assert "Cleaned Successfull" == cleaned(1,1)
#
# def test_markrepair():
#     """ Tests the repair function """
#     assert "Repair Successfull" == markrepair(1,1)
#
# def test_completedrepair():
#     """ Tests the repair function """
#     assert "Repair Successfull" == completedrepair(1,1)
#
