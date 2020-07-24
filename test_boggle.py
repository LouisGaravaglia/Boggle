from unittest import TestCase
from boggle import Boggle
from app import app
from flask import session


class FlaskTests(TestCase):
    
    def setUp(self):
        """ Stuff to do before every test. """

        app.config['TESTING'] = True
        self.client = app.test_client()

    def test_home_page(self):
        """ Make sure all elements are appearing in the home page """
        
        with app.test_client() as client:
           res = client.get("/")
           html = res.get_data(as_text=True)
           
           self.assertEqual(res.status_code, 200)
           self.assertIn("<button>Enter</button>", html)
           self.assertIn("board", session)
           self.assertIsNone(session.get('highscore'))
           self.assertIsNone(session.get('nplays'))
           self.assertIn(b'<p>High Score:', res.data)
           self.assertIn(b'Score:', res.data)
           self.assertIn(b'Seconds Left:', res.data)

    def test_word(self):
        """ Make sure board is loading correctly and words are being counted correctly"""
        
        with app.test_client() as client:
            with client.session_transaction() as change_session:
                change_session["board"] = [["B", "O", "Y", "T", "D"],
                                           ["A", "A", "E", "F", "G"],
                                           ["D", "F", "T", "D", "E"],
                                           ["B", "O", "Y", "T", "D"],
                                           ["A", "A", "E", "F", "G"]]
           
            res = client.get("/check-word?word=boy")
            self.assertEqual(res.json["result"], "ok")
            res2 = client.get("/check-word?word=bad")
            self.assertEqual(res.json["result"], "ok")
            res3 = client.get("/check-word?word=bat")
            self.assertEqual(res.json["result"], "ok")
            import pdb
            pdb.set_trace()
            # res4 = client.get("/check-word?word=tttt")
            # self.assertEqual(res.json["result"], 'not-word')
            # res5 = client.get("/check-word?word=tummy")
            # self.assertEqual(res.json["result"], 'not-on-board')
    
    def test_invalid_word(self):
        """Test if word is in the dictionary"""

        self.client.get('/')
        response = self.client.get('/check-word?word=impossible')
        self.assertEqual(response.json['result'], 'not-on-board')
        res = self.client.get("/check-word?word=tttt")
        self.assertEqual(res.json["result"], 'not-word')
        res2 = self.client.get("/check-word?word=tummy")
        self.assertEqual(res2.json["result"], 'not-on-board')