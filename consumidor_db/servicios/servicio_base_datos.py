import sqlite3
from modelos.usuario import Usuario

class ServicioBaseDatos:
    @staticmethod
    def inicializar_bd():
        conexion = sqlite3.connect('pre_registro.db')
        cursor = conexion.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                apellido TEXT NOT NULL,
                correo TEXT NOT NULL,
                programa TEXT NOT NULL,
                telefono TEXT NOT NULL
            )
        ''')
        conexion.commit()
        conexion.close()

    @staticmethod
    def guardar_usuario(usuario: Usuario):
        conexion = sqlite3.connect('pre_registro.db')
        cursor = conexion.cursor()
        cursor.execute('''
            INSERT INTO usuarios (nombre, apellido, correo, programa, telefono)
            VALUES (?, ?, ?, ?, ?)
        ''', (usuario.nombre, usuario.apellido, usuario.correo, usuario.programa, usuario.telefono))
        conexion.commit()
        conexion.close()