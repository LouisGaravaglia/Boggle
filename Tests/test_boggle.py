from unittest import TestCase
from boggle import Boggle
from app import app
from flask import session

class FlaskTests(TestCase):
    def setUp(self):
        """ Stuff to do before every test. """