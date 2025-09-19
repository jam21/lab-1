from app import app
import psycopg2
import os

def test_postgres_connection():
    conn = psycopg2.connect(
        host=os.getenv("DB_HOST", "localhost"),
        port=os.getenv("DB_PORT", 5432),
        user=os.getenv("DB_USER", "user"),
        password=os.getenv("DB_PASSWORD", "password"),
        dbname=os.getenv("DB_NAME", "mydb"),
    )
    cur = conn.cursor()
    cur.execute("SELECT 1;")
    result = cur.fetchone()
    assert result[0] == 1
    conn.close()

def test_app():
    assert app is not None
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200
    assert b'Hello DevOps' in response.data

def test_demo():
    assert app is not None
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200
    assert b'Demo was good' in response.data