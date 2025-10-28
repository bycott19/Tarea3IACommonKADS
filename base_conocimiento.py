"""
Base de conocimiento del sistema experto
Preguntas y reglas para ciberseguridad en PYMES
"""

def obtener_preguntas():
    """Retorna la lista de preguntas del cuestionario"""
    return [
        {
            'id': 'frecuencia_backups',
            'texto': '¿Con qué frecuencia realiza backups de su información?',
            'opciones': [
                {'valor': 'nunca', 'texto': 'Nunca'},
                {'valor': 'mensual', 'texto': 'Mensualmente'},
                {'valor': 'semanal', 'texto': 'Semanalmente'},
                {'valor': 'diario', 'texto': 'Diariamente'}
            ]
        },
        {
            'id': 'ubicacion_backups',
            'texto': '¿Dónde almacena los backups?',
            'opciones': [
                {'valor': 'no_realiza', 'texto': 'No realiza backups'},
                {'valor': 'solo_local', 'texto': 'Solo localmente'},
                {'valor': 'local_nube', 'texto': 'Local y en la nube'},
                {'valor': 'solo_nube', 'texto': 'Solo en la nube'}
            ]
        },
        {
            'id': 'uso_2fa',
            'texto': '¿Usa Doble Factor de Autenticación (2FA) en cuentas importantes?',
            'opciones': [
                {'valor': 'no', 'texto': 'No'},
                {'valor': 'si', 'texto': 'Sí'}
            ]
        },
        {
            'id': 'politica_contraseñas',
            'texto': '¿Tiene política de contraseñas?',
            'opciones': [
                {'valor': 'no', 'texto': 'No'},
                {'valor': 'si', 'texto': 'Sí'}
            ]
        },
        {
            'id': 'datos_sensibles',
            'texto': '¿Maneja datos sensibles de clientes?',
            'opciones': [
                {'valor': 'no', 'texto': 'No'},
                {'valor': 'si', 'texto': 'Sí'}
            ]
        },
        {
            'id': 'antivirus',
            'texto': '¿Tiene antivirus actualizado en todos los equipos?',
            'opciones': [
                {'valor': 'no', 'texto': 'No'},
                {'valor': 'si', 'texto': 'Sí'}
            ]
        },
        {
            'id': 'firewall',
            'texto': '¿Usa firewall?',
            'opciones': [
                {'valor': 'no', 'texto': 'No'},
                {'valor': 'si', 'texto': 'Sí'}
            ]
        },
        {
            'id': 'formacion_empleados',
            'texto': '¿Da formación en ciberseguridad a empleados?',
            'opciones': [
                {'valor': 'no', 'texto': 'No'},
                {'valor': 'si', 'texto': 'Sí'}
            ]
        },
        {
            'id': 'politicas_documentadas',
            'texto': '¿Tiene políticas de seguridad documentadas?',
            'opciones': [
                {'valor': 'no', 'texto': 'No'},
                {'valor': 'si', 'texto': 'Sí'}
            ]
        },
        {
            'id': 'plan_incidentes',
            'texto': '¿Tiene plan para responder a incidentes?',
            'opciones': [
                {'valor': 'no', 'texto': 'No'},
                {'valor': 'si', 'texto': 'Sí'}
            ]
        },
        {
            'id': 'teletrabajo',
            'texto': '¿Permite teletrabajo?',
            'opciones': [
                {'valor': 'no', 'texto': 'No'},
                {'valor': 'si', 'texto': 'Sí'}
            ]
        },
        {
            'id': 'cumplimiento_legal',
            'texto': '¿Cumple con normativas de protección de datos?',
            'opciones': [
                {'valor': 'no', 'texto': 'No'},
                {'valor': 'si', 'texto': 'Sí'}
            ]
        }
    ]