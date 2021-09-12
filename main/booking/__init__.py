from flask_restx import Namespace

ns = Namespace('Booking', path='/')

from main.booking.v1 import views  # noqa
