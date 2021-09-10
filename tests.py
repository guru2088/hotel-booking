""" Tests for app.py """
import pytest
from mock import patch
from app import checkin,checkout, cleaned,markrepair, completedrepair,roomsAvailable

def test_checkin():
    """ Tests the checkin function for success """
    assert "Occupied , Floor : " + str(1) + ", Room : " + str(1) == checkin(1,1)


def test_checkin():
    """ Tests the checkin function for error """
    assert "error" == checkin("asdfasd",1)

def test_checkin():
    """ Tests the checkin function for invalid floor number """
    assert "Invalid Floor and Room Number" == checkin(7,1)


def test_checkin():
    """ Tests the checkin function for invalid floor number """
    assert "Invalid Floor and Room Number" == checkin(1,6)


def test_checkin():
    """ Tests the checkin function for invalid floor number """
    assert "Invalid Floor and Room Number" == checkin(10,20)

def test_roomsAvailable():
    """ Tests the available function """
    assert True == isinstance(roomsAvailable(),dict)

def test_roomsAvailable():
    """ Tests the available error function """
    assert True == isinstance(roomsAvailable(),dict)

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
