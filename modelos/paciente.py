import sqlite3

class PacienteRegistrarCita:
    def __init__(self):
        self.conexion = sqlite3.connect("database/medicita.db")
        self.cursor = self.conexion.cursor()
        
    def cerrar_conexion(self):
        self.conexion.close()
        
    def registrar_cita(self):
        