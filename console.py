import psycopg2
from settings import DATABASE, USER
from flask import Flask

from backend.api.main import *
from settings import DATABASE, USER

app = create_app(DATABASE, USER)

app.run(debug = True)