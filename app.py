import sqlite3
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('Projet_planetegeekdating.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')

def hello():
    return ("Hello there")