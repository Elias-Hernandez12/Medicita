import sqlite3

class ConexionDB:
    def __init__(self):
        self.conexion = sqlite3.connect("database/medicita.db")
        self.cursor = self.conexion.cursor()
        self.crear_tabla_pacientes()

    def crear_tabla_pacientes(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS pacientes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                correo TEXT UNIQUE NOT NULL,
                telefono TEXT,
                fecha_nacimiento TEXT,
                creado_en TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        self.conexion.commit()

    def insertar_paciente(self, nombre, correo, telefono, fecha_nacimiento):
        self.cursor.execute('''
            INSERT INTO pacientes (nombre, correo, telefono, fecha_nacimiento) 
            VALUES (?, ?, ?, ?)
        ''', (nombre, correo, telefono, fecha_nacimiento))
        self.conexion.commit()
