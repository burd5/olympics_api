import psycopg2
# from settings import DATABASE, USER

conn = psycopg2.connect(database='olympics', user='austinburdette')
cursor = conn.cursor()

test_conn = psycopg2.connect(database='test_olympics', user='austinburdette')
test_cursor = conn.cursor()

def drop_records(cursor, conn, table_name):
    cursor.execute(f"TRUNCATE {table_name} RESTART IDENTITY;")
    conn.commit()

def drop_tables(table_names, cursor, conn):
    for table_name in table_names:
        drop_records(cursor, conn, table_name)

def drop_all_tables(conn, cursor):
    table_names = ['games', 'events', 'results', 'athletes', 'teams']
    drop_tables(table_names, cursor, conn)

