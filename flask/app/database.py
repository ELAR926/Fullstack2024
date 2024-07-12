# database.py

import os
import psycopg2
from dotenv import load_dotenv
from flask import g

load_dotenv()

DATABASE_CONFIG = {
    'user': os.getenv('PGSQL_USER'),
    'password': os.getenv('PGSQL_PASSWORD'),
    'host': os.getenv('PGSQL_HOST'),
    'database': os.getenv('PGSQL_DATABASE'),
    'port': os.getenv('PGSQL_PORT', '5432')
}


def get_db():
    if 'db' not in g:
        g.db = psycopg2.connect(**DATABASE_CONFIG)
    return g.db


def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()


def init_app(app):
    # Cerrar la conexión a la base de datos cuando finaliza la solicitud
    app.teardown_appcontext(close_db)


def test_connection():
    conn = None
    try:
        # Conectar a la base de datos y verificar la conexión
        conn = psycopg2.connect(**DATABASE_CONFIG)
        cur = conn.cursor()
        cur.execute("SELECT version();")
        db_version = cur.fetchone()
        print(f"Conexión exitosa a PostgreSQL! Versión del servidor: {
              db_version[0]}")
    except Exception as e:
        print(f"Error de conexión: {str(e)}")
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()
