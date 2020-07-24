from unittest import TestCase
from boggle import Boggle
from app import app
from flask import session

class FlaskTests(TestCase):
    def setUp(self):
        """ Stuff to do before every test. """
        
        with app.test_client() as client:
            res = client.get("/")
            html = res.get.data(as_text=True)
            
            self.assertEqual(res.status_code, 200)
            self.assertIn("<button>Enter</button>", html)