Tarea 3: Sistema experto de ciberseguridad para Pymes

La aplicación es un prototipo desarrollado en python y flask. La aplicación aplica la metodología CommonKADS para diagnosticar riesgos en la seguridad
de PYMES y recomienda estrategias para mejorar la seguridad de estas.

- La aplicación cuenta con una interfaz web simple hecha con Flask.
- Las preguntas y reglas se encuentran en la clase "base_conocimiento.py".
- Cuenta con un motor de encadenamiento hacia adelante implementado en "base_conocimiento.py". 
- El sistema explica porqué recomienda cada estrategia.
- Los diagnosticos se guardan en la base de datos "diagnosticos.db".

Como ejecutarlo:
- Solo se requiere tener Python 3 y la libreria Flask (pip install Flask).

    1. Primero debe clonar el repositorio desde github a visual Studio code
    2. Ejecutar la aplicación con el botón de ejecutar de visual Studio code
    3. Abrir en el navegador "http://127.0.0.1:5000/", puede escribirlo manualmente o hacer Ctrl + clic al link que aparece en la terminal

Estructura del proyecto:
- app.py: Servidor web principal de Flask, maneja las rutas y la conexión a la Base de datos.
- base_conocimiento: Contiene las preguntas y las reglas del sistema experto.
- diagnosticos.db: Base de datos SQLite donde se guardan los resultados.
- templates/: Carpeta que contiene el formulario HTML (index.html y resultados.html), donde index muestra las preguntas, y resultados entrega las 
recomendaciones que el sistema le da al usuario.
