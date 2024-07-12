# models.py

from app.database import get_db

class Task:
    @staticmethod
    def _get_tasks_by_query(query, params=None):
        db = get_db()
        cursor = db.cursor()
        cursor.execute(query, params)
        rows = cursor.fetchall()
        tasks = []
        for row in rows:
            task = {
                'id': row[0],
                'nombre': row[1],
                'apellido': row[2],
                'email': row[3],
                'fecha_entrada': row[4],
                'fecha_salida': row[5],
                'completada': row[6],
                'activa': row[7]
            }
            tasks.append(task)
        return tasks

    @staticmethod
    def GET_mostrar_formulario():
        query = """
            SELECT id, nombre, apellido, email, fecha_entrada, fecha_salida, completada, activa
            FROM reserva
            WHERE activa = true AND completada = false
            ORDER BY fecha_salida
            """
        return Task._get_tasks_by_query(query)

    @staticmethod
    def POST_procesar_formulario(nombre, apellido, email, fecha_entrada, fecha_salida):
        query = """
            INSERT INTO reserva (nombre, apellido, email, fecha_entrada, fecha_salida, completada, activa)
            VALUES (%s, %s, %s, %s, %s, false, true)
            RETURNING id
            """
        db = get_db()
        cursor = db.cursor()
        cursor.execute(query, (nombre, apellido, email, fecha_entrada, fecha_salida))
        db.commit()
        inserted_id = cursor.fetchone()[0]
        return inserted_id

    @staticmethod
    def get_by_id(id):
        query = "SELECT * FROM reserva WHERE id = %s"
        db = get_db()
        cursor = db.cursor()
        cursor.execute(query, (id,))
        row = cursor.fetchone()
        task = {
            'id': row[0],
            'nombre': row[1],
            'apellido': row[2],
            'email': row[3],
            'fecha_entrada': row[4],
            'fecha_salida': row[5],
            'completada': row[6],
            'activa': row[7]
        } if row else None
        return task

    @staticmethod
    def marcar_completada(id):
        query = "UPDATE reserva SET completada = true WHERE id = %s"
        db = get_db()
        cursor = db.cursor()
        cursor.execute(query, (id,))
        db.commit()

    @staticmethod
    def delete(id):
        query = "UPDATE reserva SET activa = false WHERE id = %s"
        db = get_db()
        cursor = db.cursor()
        cursor.execute(query, (id,))
        db.commit()

    @staticmethod
    def serialize(task):
        return {
            'id': task['id'],
            'nombre': task['nombre'],
            'apellido': task['apellido'],
            'email': task['email'],
            'fecha_entrada': task['fecha_entrada'].isoformat(),  # Formato ISO 8601 para fechas
            'fecha_salida': task['fecha_salida'].isoformat(),    # Formato ISO 8601 para fechas
            'completada': task['completada'],
            'activa': task['activa']
        }
