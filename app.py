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
@app.route('/')
def index():
    """Página principal con el cuestionario"""
    preguntas = obtener_preguntas()
    return render_template('index.html', preguntas=preguntas)

@app.route('/diagnosticar', methods=['POST'])
def diagnosticar():
    """Procesa el diagnóstico y muestra resultados"""
    # Obtener respuestas del formulario
    respuestas = {}
    for key, value in request.form.items():
        if key.startswith('pregunta_'):
            respuestas[key.replace('pregunta_', '')] = value
    
    # Evaluar reglas
    recomendaciones = evaluar_reglas(respuestas)
    
    # Guardar en base de datos
    guardar_diagnostico(respuestas, recomendaciones)
    
    return render_template('resultados.html', 
                         respuestas=respuestas, 
                         recomendaciones=recomendaciones,
                         total_recomendaciones=len(recomendaciones))

@app.route('/reiniciar')
def reiniciar():
    """Reinicia el diagnóstico"""
    return render_template('index.html', preguntas=obtener_preguntas())

if __name__ == '__main__':
    init_db()
    app.run(debug=True, port=5000)