import psycopg2
from flask import Flask
from backend.api.main import *
from settings import DATABASE, USER
from backend.tests import *

app = create_app(DATABASE, USER)

app.run(debug = True)