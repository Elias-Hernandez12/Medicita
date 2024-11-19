import tkinter as tk
from Pantallas.inicio import InicioApp
from Pantallas.iniciar_sesion import IniciarSesionApp
from Pantallas.perfil import PerfilApp
from Pantallas.menu import MenuApp
from Pantallas.recuperar_contraseña import RecuperarPasswordApp
from Pantallas.registrar_cita import RegistrarCitaApp
from Pantallas.historial import HistorialApp
from Pantallas.agenda import AgendaApp
from Pantallas.rol import RolApp 
from Pantallas.registro_paciente import RegistroPacienteApp
from Pantallas.registro_doctor import RegistroDoctorApp

class Controlador:
    def __init__(self, master):
        self.master = master
        self.current_app = None
        self.mostrar_inicio()

    def mostrar_inicio(self):
        self.cerrar_pantalla_actual()
        self.current_app = InicioApp(master=self.master, controlador=self)
        self.current_app.pack(fill=tk.BOTH, expand=True)

    def mostrar_iniciar_sesion(self):
        self.cerrar_pantalla_actual()
        self.current_app = IniciarSesionApp(master=self.master, controlador=self)
        self.current_app.pack(fill=tk.BOTH, expand=True)

    def mostrar_rol(self):
        self.cerrar_pantalla_actual()
        self.current_app = RolApp(master=self.master, controlador=self)
        self.current_app.pack(fill=tk.BOTH, expand=True)

    def mostrar_registrar_paciente(self):
        self.cerrar_pantalla_actual()
        self.current_app = RegistroPacienteApp(master=self.master, controlador=self)  # Asegúrate de que esta clase existe
        self.current_app.pack(fill=tk.BOTH, expand=True)

    def mostrar_registrar_doctor(self):
        self.cerrar_pantalla_actual()
        self.current_app = RegistroDoctorApp(master=self.master, controlador=self)  
        self.current_app.pack(fill=tk.BOTH, expand=True)

    def mostrar_menu(self):
        self.cerrar_pantalla_actual()
        self.current_app = MenuApp(master=self.master, controlador=self)
        self.current_app.pack(fill=tk.BOTH, expand=True)

    def mostrar_recuperar_contraseña(self):
        self.cerrar_pantalla_actual()
        self.current_app = RecuperarPasswordApp(master=self.master, controlador=self)
        self.current_app.pack(fill=tk.BOTH, expand=True)

    def mostrar_perfil(self):
        self.cerrar_pantalla_actual()
        self.current_app = PerfilApp(master=self.master, controlador=self)
        self.current_app.pack(fill=tk.BOTH, expand=True)

    def mostrar_registrar_cita(self):
        self.cerrar_pantalla_actual()
        self.current_app = RegistrarCitaApp(master=self.master, controlador=self)
        self.current_app.pack(fill=tk.BOTH, expand=True)

    def mostrar_historial(self):
        self.cerrar_pantalla_actual()
        self.current_app = HistorialApp(master=self.master, controlador=self)
        self.current_app.pack(fill=tk.BOTH, expand=True)

    def mostrar_agenda(self):
        self.cerrar_pantalla_actual()
        self.current_app = AgendaApp(master=self.master, controlador=self)
        self.current_app.pack(fill=tk.BOTH, expand=True)

    def cerrar_pantalla_actual(self):
        if self.current_app is not None:
            self.current_app.pack_forget() 

