""" Tests for app.py """
import pytest

from app import checkin
from app import checkout
from app import cleaned
from app import repair


def test_checkin():
    """ Tests the checkin function """
    assert "Checkin Successfull" == checkin(1,1)

def test_checkout():
    """ Tests the checkout function """
    assert "Checkout Successfull" == checkout(1,1)

def test_cleaned():
    """ Tests the cleaned function """
    assert "Cleaned Successfull" == cleaned(1,1)

def test_repair():
    """ Tests the repair function """
    assert "Repair Successfull" == repair(1,1)
