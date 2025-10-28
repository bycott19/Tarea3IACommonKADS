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

def evaluar_reglas(hechos):
    recomendaciones = []
    
    if hechos.get('frecuencia_backups') == 'nunca' and hechos.get('datos_sensibles') == 'si':
        recomendaciones.append({
            'titulo': 'IMPLEMENTAR SISTEMA DE BACKUP',
            'descripcion': 'Realice backups diarios automáticos y almacene una copia en la nube.',
            'justificacion': 'Se detectó que maneja datos sensibles ("si") pero nunca realiza backups ("nunca").'
        })
    
    if hechos.get('uso_2fa') == 'no' and hechos.get('datos_sensibles') == 'si':
        recomendaciones.append({
            'titulo': 'ACTIVAR DOBLE FACTOR DE AUTENTICACIÓN',
            'descripcion': 'Configure 2FA en email corporativo y sistemas críticos.',
            'justificacion': 'Se detectó que maneja datos sensibles ("si") pero no utiliza 2FA ("no").'
        })
    
    if hechos.get('antivirus') == 'no':
        recomendaciones.append({
            'titulo': 'INSTALAR ANTIVIRUS',
            'descripcion': 'Instale el antivirus empresarial en todos los equipos y manténgalo actualizado.',
            'justificacion': 'Se detectó que no tiene antivirus actualizado en todos los equipos ("no").'
        })
    
    if hechos.get('firewall') == 'no':
        recomendaciones.append({
            'titulo': 'CONFIGURAR FIREWALL',
            'descripcion': 'Implemente un firewall para proteger la red interna.',
            'justificacion': 'Se detectó que no usa un firewall de red ("no").'
        })
    
    if hechos.get('politica_contraseñas') == 'no':
        recomendaciones.append({
            'titulo': 'CREAR POLÍTICA DE CONTRASEÑAS',
            'descripcion': 'Establezca contraseñas de 12+ caracteres con mayúsculas, números y símbolos.',
            'justificacion': 'Se detectó que no existe una política de contraseñas formal ("no").'
        })
    
    if hechos.get('formacion_empleados') == 'no' and hechos.get('teletrabajo') == 'si':
        recomendaciones.append({
            'titulo': 'CAPACITAR EMPLEADOS (TELETRABAJO)',
            'descripcion': 'Realice formación trimestral sobre phishing y seguridad en teletrabajo.',
            'justificacion': 'Se detectó que permite el teletrabajo ("si") pero no da formación a empleados ("no").'
        })
    
    if hechos.get('politicas_documentadas') == 'no' and hechos.get('datos_sensibles') == 'si':
        recomendaciones.append({
            'titulo': 'DOCUMENTAR POLÍTICAS',
            'descripcion': 'Cree manual de políticas de seguridad y uso aceptable de recursos.',
            'justificacion': 'Se detectó que maneja datos sensibles ("si") pero no tiene políticas de seguridad documentadas ("no").'
        })
    
    if hechos.get('plan_incidentes') == 'no' and hechos.get('datos_sensibles') == 'si':
        recomendaciones.append({
            'titulo': 'DESARROLLAR PLAN DE INCIDENTES',
            'descripcion': 'Documente procedimientos para responder a brechas de seguridad.',
            'justificacion': 'Se detectó que maneja datos sensibles ("si") pero no tiene un plan de respuesta a incidentes ("no").'
        })
    
    if hechos.get('cumplimiento_legal') == 'no' and hechos.get('datos_sensibles') == 'si':
        recomendaciones.append({
            'titulo': 'CUMPLIR NORMATIVAS',
            'descripcion': 'Adeúese a LOPD/GDPR: registre tratamientos y nombre delegado de protección.',
            'justificacion': 'Se detectó que maneja datos sensibles ("si") pero no cumple con normativas de protección de datos ("no").'
        })
    
    if hechos.get('ubicacion_backups') == 'no_realiza':
        recomendaciones.append({
            'titulo': 'ALMACENAR BACKUPS SEGURO',
            'descripcion': 'Use estrategia 3-2-1: 3 copias, 2 medios, 1 externa.',
            'justificacion': 'Se detectó que no realiza backups ("no_realiza"). Esta es una falla crítica.'
        })
    
    if hechos.get('teletrabajo') == 'si' and hechos.get('firewall') == 'no':
        recomendaciones.append({
            'titulo': 'SEGURIDAD EN TELETRABAJO',
            'descripcion': 'Implemente VPN y políticas de seguridad para dispositivos remotos.',
            'justificacion': 'Se detectó que permite el teletrabajo ("si") pero no cuenta con un firewall de red ("no").'
        })
    
    if hechos.get('formacion_empleados') == 'no':
        recomendaciones.append({
            'titulo': 'CONCIENCIACIÓN CONTINUA',
            'descripcion': 'Realice simulaciones de phishing mensuales y formación básica.',
            'justificacion': 'Se detectó que no se da formación en ciberseguridad a los empleados ("no").'
        })
    
    return recomendaciones