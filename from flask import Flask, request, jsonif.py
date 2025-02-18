from flask import Flask, request, jsonify
import jwt
import sqlite3
import os
from datetime import datetime, timedelta

app = Flask(__name__)
SECRET_KEY = "supersecretkey"
FLAG = "FLAG{Blind_SQLi_JWT}"  # Флаг, который игрок должен найти

# Инициализация базы данных
def init_db():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)''')
    c.execute("INSERT OR IGNORE INTO users (id, username, password) VALUES (1, 'admin', 'supersecure')")
    c.execute('''CREATE TABLE IF NOT EXISTS flags (id INTEGER PRIMARY KEY, secret TEXT)''')
    c.execute("INSERT OR IGNORE INTO flags (id, secret) VALUES (1, ?)" , (FLAG,))
    conn.commit()
    conn.close()

init_db()

# Функция для генерации токена
def generate_token(username):
    payload = {
        'username': username,
        'exp': datetime.utcnow() + timedelta(minutes=10)
    }
    return jwt.encode(payload, SECRET_KEY, algorithm='HS256')

@app.route('/')
def home():
    return "<h1>Welcome to the CTF Challenge</h1><p>Login via /login</p>"

# Эндпоинт для входа
def authenticate():
    username = request.json.get('username')
    password = request.json.get('password')
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    user = c.fetchone()
    conn.close()
    if user:
        return jsonify({'token': generate_token(username)})
    return jsonify({'error': 'Invalid credentials'}), 401

app.route('/login', methods=['POST'])(authenticate)

# Уязвимый эндпоинт с Blind SQL Injection
@app.route('/flag', methods=['POST'])
def get_flag():
    token = request.json.get('token')
    try:
        decoded = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        username = decoded['username']
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        c.execute(f"SELECT secret FROM flags WHERE id={request.json.get('id')}")
        flag = c.fetchone()
        conn.close()
        if flag:
            return jsonify({'flag': flag[0]})
    except Exception as e:
        return jsonify({'error': 'Unauthorized'}), 403

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
