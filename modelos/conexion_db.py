import sqlite3

class ConexionDB:
    def __init__(self):
        self.conexion = sqlite3.connect("database/medicita.db")
        self.cursor = self.conexion.cursor()
        self.crear_tabla_pacientes()  
        self.crear_tabla_doctores()   

    def crear_tabla_pacientes(self):
        self.cursor.execute(""" 
            CREATE TABLE IF NOT EXISTS pacientes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                correo TEXT UNIQUE NOT NULL,
                telefono TEXT,
                fecha_nacimiento DATE,
                contrasena TEXT NOT NULL,
                creado_en TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        self.conexion.commit()

    def crear_tabla_doctores(self):
        self.cursor.execute(""" 
            CREATE TABLE IF NOT EXISTS doctores (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                correo TEXT UNIQUE NOT NULL,
                telefono TEXT,
                especialidad TEXT,
                contrasena TEXT NOT NULL,
                creado_en TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        self.conexion.commit()
        
    def insertar_paciente(self, nombre, correo, telefono, fecha_nacimiento, contrasena):
        try:
            self.cursor.execute(""" 
                INSERT INTO pacientes (nombre, correo, telefono, fecha_nacimiento, contrasena) 
                VALUES (?, ?, ?, ?, ?)
            """, (nombre, correo, telefono, fecha_nacimiento, contrasena))
            self.conexion.commit()  
            print("Paciente registrado correctamente.")
        except sqlite3.IntegrityError:
            print("Error: El correo ya está registrado.")
        except sqlite3.Error as e:
            print(f"Error al registrar el paciente: {e}")

    def insertar_doctor(self, nombre, correo, telefono, especialidad, contrasena):
        try:
            self.cursor.execute(""" 
                INSERT INTO doctores (nombre, correo, telefono, especialidad, contrasena) 
                VALUES (?, ?, ?, ?, ?)
            """, (nombre, correo, telefono, especialidad, contrasena))
            self.conexion.commit()  
            print("Doctor registrado correctamente.")
        except sqlite3.IntegrityError:
            print("Error: El correo ya está registrado.")
        except sqlite3.Error as e:
            print(f"Error al registrar el doctor: {e}")

    def obtener_pacientes(self):
        self.cursor.execute("SELECT * FROM pacientes")
        return self.cursor.fetchall()

    def obtener_doctores(self):
        self.cursor.execute("SELECT * FROM doctores")
        return self.cursor.fetchall()

    def cerrar_conexion(self):
        self.conexion.close()