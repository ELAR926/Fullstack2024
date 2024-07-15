# models.py

from app.database import get_db


class Reserva:
    def __init__(self, id=None, nombre=None, apellido=None, email=None, fecha_entrada=None, fecha_salida=None, completada=None, activa=None):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.fecha_entrada = fecha_entrada
        self.fecha_salida = fecha_salida
        self.completada = completada
        self.activa = activa

    @staticmethod
    def __get_Reserva_by_query(query):
        db = get_db()
        cursor = db.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()

        Reservas = []
        for row in rows:
            Reservas.append(
                Reserva(
                    id=row[0],
                    nombre=row[1],
                    apellido=row[2],
                    email=row[3],
                    fecha_entrada=row[4],
                    fecha_salida=row[5],
                    completada=row[6],
                    activa=row[7]
                )
            )
        cursor.close()
        return Reservas

    @staticmethod
    def GET_mostrar_formulario():
        return Reserva.__get_Reserva_by_query(
            """
            SELECT id, nombre, apellido, email, fecha_entrada, fecha_salida, completada, activa
            FROM reserva
            WHERE activa = true AND completada = false
            ORDER BY fecha_salida
            """
        )

    @staticmethod
    def POST_procesar_formulario(nombre, apellido, email, fecha_entrada, fecha_salida):
        query = """
            INSERT INTO reserva (nombre, apellido, email, fecha_entrada, fecha_salida, completada, activa)
            VALUES (%s, %s, %s, %s, %s, false, true)
            RETURNING id
            """
        db = get_db()
        cursor = db.cursor()
        cursor.execute(query, (nombre, apellido, email,
                       fecha_entrada, fecha_salida))
        db.commit()
        inserted_id = cursor.fetchone()[0]
        return inserted_id

    @staticmethod
    def get_by_id(id):
        db = get_db()
        cursor = db.cursor()
        query = "SELECT * FROM reserva WHERE id = %s"
        cursor.execute(query, (id,))
        row = cursor.fetchone()
        cursor.close()

        if row:
            return Reserva(
                id=row[0],
                nombre=row[1],
                apellido=row[2],
                email=row[3],
                fecha_entrada=row[4],
                fecha_salida=row[5],
                completada=row[6],
                activa=row[7]
            )
        return None

    def save(self):
        db = get_db()
        cursor = db.cursor()
        if self.id:
            cursor.execute(
                """ UPDATE reserva 
                SET nombre = %s, apellido = %s, email = %s, fecha_entrada = %s, fecha_salida = %s, completada = %s, activa = %s
                WHERE id = %s
                """,
                (self.nombre, self.apellido, self.email, self.fecha_entrada,
                 self.fecha_salida, self.completada, self.activa, self.id)
            )
        else:
            cursor.execute(
                """ INSERT INTO reserva (nombre, apellido, email, fecha_entrada, fecha_salida, completada, activa)
                VALUES(%s, %s, %s, %s, %s, %s, %s)
                """,
                (self.nombre, self.apellido, self.email, self.fecha_entrada, self.fecha_salida, self.completada, self.activa))
            self.id = cursor.lastrowid
        db.commit()
        cursor.close()

    def delete(self):
        db = get_db()
        cursor = db.cursor()
        query = "UPDATE reserva SET activa = false WHERE id = %s"
        cursor.execute(query, (self.id,))
        db.commit()
        cursor.close()

    @staticmethod
    def serialize(Reserva):
        return {
            'id': Reserva.id,
            'nombre': Reserva.nombre,
            'apellido': Reserva.apellido,
            'email': Reserva.email,
            'fecha_entrada': Reserva.fecha_entrada.strftime('%Y-%m-%d %H:%M:%S'),
            'fecha_salida': Reserva.fecha_salida.strftime('%Y-%m-%d %H:%M:%S'),
            'completada': Reserva.completada,
            'activa': Reserva.activa
        }
