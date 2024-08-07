from flask import jsonify, request, redirect, url_for
from app.models import Reserva

# Ruta para mostrar el formulario (GET)


def mostrar_formulario():
    Reservas = Reserva.GET_mostrar_formulario()
    serialized_Reservas = [Reserva.serialize(Reserva) for Reserva in Reservas]
    return jsonify(serialized_Reservas)

# Ruta para procesar el formulario (POST)


def procesar_formulario():
    # Aquí procesas los datos enviados desde el formulario
    nombre = request.form.get('nombre')
    apellido = request.form.get('apellido')
    email = request.form.get('email')
    fecha_entrada = request.form.get('fecha_entrada')
    fecha_salida = request.form.get('fecha_salida')

    # Por ahora, simplemente imprime los datos recibidos
    print(f"Datos recibidos: Nombre: {nombre}, Apellido: {apellido}, Email: {email}, "
          f"Fecha de Entrada: {fecha_entrada}, Fecha de Salida: {fecha_salida}")

    # Procesar y guardar los datos en la base de datos usando Task.POST_procesar_formulario
    inserted_id = Reserva.POST_procesar_formulario(
        nombre, apellido, email, fecha_entrada, fecha_salida)

    # Redirigir al usuario a una nueva página usando URL_FOR
    return redirect(url_for('mostrar_formulario'))
