from flask import Flask, render_template, request, session
from base_conocimiento import obtener_preguntas, evaluar_reglas
import sqlite3
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'clave_secreta_ciberseguridad_2025'

def init_db():
    """Inicializa la base de datos SQLite"""
    conn = sqlite3.connect('diagnosticos.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS diagnosticos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            fecha TEXT NOT NULL,
            respuestas TEXT NOT NULL,
            recomendaciones TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def guardar_diagnostico(respuestas, recomendaciones):
    """Guarda el diagnóstico en la base de datos"""
    try:
        conn = sqlite3.connect('diagnosticos.db')
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO diagnosticos (fecha, respuestas, recomendaciones)
            VALUES (?, ?, ?)
        ''', (datetime.now().isoformat(), str(respuestas), str(recomendaciones)))
        conn.commit()
        conn.close()
        return True
    except Exception as e:
        print(f"Error al guardar diagnóstico: {e}")
        return False