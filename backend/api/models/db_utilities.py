import psycopg2
# from settings import DATABASE, USER

conn = psycopg2.connect(database='olympics', user='austinburdette')
cursor = conn.cursor()

