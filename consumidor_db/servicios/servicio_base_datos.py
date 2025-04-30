import pyodbc
from modelos.usuario import Usuario

class ServicioBaseDatos:
    @staticmethod
    def obtener_conexion():
        # Cambia estos datos según tu configuración de SSMS
        servidor = 'DESKTOP-NLNB3B0\\SQLEXPRESS'  # o el nombre de tu servidor
        base_datos = 'PreRegistroDB'
        usuario = 'sa'
        contraseña = '123'

        conexion = pyodbc.connect(
            f'DRIVER={{ODBC Driver 17 for SQL Server}};'
            f'SERVER={servidor};DATABASE={base_datos};UID={usuario};PWD={contraseña}'
        )
        return conexion

    @staticmethod
    def inicializar_bd():
        conexion = ServicioBaseDatos.obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute('''
            IF NOT EXISTS (
                SELECT * FROM sysobjects WHERE name='Usuarios' AND xtype='U'
            )
            CREATE TABLE Usuarios (
                id INT IDENTITY(1,1) PRIMARY KEY,
                nombre NVARCHAR(100),
                apellido NVARCHAR(100),
                correo NVARCHAR(100),
                programa NVARCHAR(100),
                telefono NVARCHAR(50)
            )
        ''')
        conexion.commit()
        conexion.close()

    @staticmethod
    def guardar_usuario(usuario: Usuario):
        conexion = ServicioBaseDatos.obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute('''
            INSERT INTO Usuarios (nombre, apellido, correo, programa, telefono)
            VALUES (?, ?, ?, ?, ?)
        ''', (usuario.nombre, usuario.apellido, usuario.correo, usuario.programa, usuario.telefono))
        conexion.commit()
        conexion.close()
