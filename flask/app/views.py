# views.py

from flask import jsonify, request
from app.models import Task

def mostrar_formulario():
    try:
        # Obtener las tareas activas y no completadas
        tasks = Task.GET_mostrar_formulario()
        return jsonify([Task.serialize(task) for task in tasks])
    except Exception as e:
        return jsonify({'error': f'Error al obtener las tareas: {str(e)}'}), 500

def procesar_formulario():
    # Obtener datos del formulario enviado
    datos = request.json
    nombre = datos.get('nombre')
    apellido = datos.get('apellido')
    email = datos.get('email')
    fecha_entrada = datos.get('fecha_entrada')
    fecha_salida = datos.get('fecha_salida')

    # Validar datos recibidos (opcional)
    if not nombre or not apellido or not email or not fecha_entrada or not fecha_salida:
        return jsonify({'error': 'Todos los campos son obligatorios'}), 400

    try:
        # Procesar el formulario y guardar la tarea
        inserted_id = Task.POST_procesar_formulario(
            nombre, apellido, email, fecha_entrada, fecha_salida)
        return jsonify({'message': 'Tarea creada correctamente', 'id': inserted_id}), 201
    except Exception as e:
        return jsonify({'error': f'Error al crear la tarea: {str(e)}'}), 500
