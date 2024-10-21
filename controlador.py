import tkinter as tk
from Pantallas.inicio import InicioApp
from Pantallas.iniciar_sesion import IniciarSesionApp
from Pantallas.registrarse import RegistrarseApp
from Pantallas.perfil import PerfilApp
from Pantallas.menu import MenuApp
from Pantallas.recuperar_contraseña import RecuperarPasswordApp
from Pantallas.registrar_cita import RegistrarCitaApp
from Pantallas.historial import HistorialApp
from Pantallas.agenda import AgendaApp



class Controlador:
    def __init__(self, master):
        self.master = master
        self.current_app = None
        self.mostrar_inicio()  # Mostrar la pantalla de inicio al inicio

    def mostrar_inicio(self):
        self.cerrar_pantalla_actual()
        self.current_app = InicioApp(master=self.master, controlador=self)
        self.current_app.pack(fill=tk.BOTH, expand=True)

    def mostrar_iniciar_sesion(self):
        self.cerrar_pantalla_actual()
        self.current_app = IniciarSesionApp(master=self.master, controlador=self)
        self.current_app.pack(fill=tk.BOTH, expand=True)
        
    def mostrar_registrarse(self):
        self.cerrar_pantalla_actual()
        self.current_app = RegistrarseApp(master=self.master, controlador=self)
        self.current_app.pack(fill=tk.BOTH, expand=True)
        
    def mostrar_menu(self):
        self.cerrar_pantalla_actual()
        self.current_app = MenuApp(master=self.master, controlador=self)  # Asegúrate de pasar el controlador
        self.current_app.pack(fill=tk.BOTH, expand=True)
        
    def mostrar_recuperar_contraseña(self):
        self.cerrar_pantalla_actual()
        self.current_app = RecuperarPasswordApp(master=self.master, controlador=self)
        self.current_app.pack(fill=tk.BOTH, expand=True)

    def mostrar_perfil(self):
        self.cerrar_pantalla_actual()
        self.current_app = PerfilApp(master=self.master, controlador=self)  # Asegúrate de pasar el controlador
        self.current_app.pack(fill=tk.BOTH, expand=True)
    
    def mostrar_registrar_cita(self):
        self.cerrar_pantalla_actual()
        self.current_app = RegistrarCitaApp(master=self.master, controlador=self)  # Asegúrate de pasar el controlador
        self.current_app.pack(fill=tk.BOTH, expand=True)
        
    def mostrar_historial(self):
        self.cerrar_pantalla_actual()
        self.current_app = HistorialApp(master=self.master, controlador=self)  # Asegúrate de pasar el controlador
        self.current_app.pack(fill=tk.BOTH, expand=True)
        
    def mostrar_agenda(self):
        self.cerrar_pantalla_actual()
        self.current_app = AgendaApp(master=self.master, controlador=self)  # Asegúrate de pasar el controlador
        self.current_app.pack(fill=tk.BOTH, expand=True)
         
    def cerrar_pantalla_actual(self):
        if self.current_app is not None:
            self.current_app.pack_forget()  # Oculta la pantalla actual

