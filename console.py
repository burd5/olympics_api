import psycopg2
from flask import Flask
from backend.api.main import *
from settings import DATABASE, USER, PASSWORD
from backend.tests import *
from backend.api.models import *

app = create_app(DATABASE, USER, PASSWORD)

app.run(debug = True)