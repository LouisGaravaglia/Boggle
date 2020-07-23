from boggle import Boggle
from app import app
from flask import Flask, request, render_template, session, make_response, redirect, flash
from random import choice, randint
from unittest import TestCase
from flask_debugtoolbar import DebugToolbarExtension


app = Flask(__name__)

app.config["SECRET_KEY"] = "4534gdghjk5d#$RGR^HDG"
app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False 
app.config["TESTING"] = True
app.config["DEBUG_TB_HOSTS"] = ["dont-show-debug-toolbar"]

debug = DebugToolbarExtension(app)

boggle_game = Boggle()
