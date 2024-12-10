import tkinter as tk
from tkinter import PhotoImage, messagebox
from modelos.conexion_db import ConexionDB
import re

class IniciarSesionApp(tk.Frame):
    def __init__(self, master=None,  controlador=None):
        super().__init__(master)
        master.geometry("1420x800")
        master.minsize(1420, 800)
        self.controlador = controlador
        self.conexion = ConexionDB()
        self.master = master
        self.configure(bg="#E0F7FA")  # Establecer el color de fondo
        self.create_widgets()
        
    def create_widgets(self):
        # Frame para el header
        self.header_frame = tk.Frame(self, bg="#E0F7FA")
        self.header_frame.pack(padx=20, pady=10, fill=tk.X)

        # Título del programa
        self.label_titulo = tk.Label(self.header_frame, text="Medicita", font=("Helvetica", 28, "bold"), bg="#E0F7FA", fg="#007FFF")
        self.label_titulo.pack(side=tk.LEFT)

        # Frame principal para el contenido
        self.main_frame = tk.Frame(self, bg="#E0F7FA")
        self.main_frame.pack(padx=20, pady=20, fill=tk.BOTH, expand=True)

        # Crear el formulario de inicio de sesión dentro de un frame
        self.crear_frame_iniciar_sesion()
        
        # Cargar la imagen (asegúrate de que la ruta sea correcta)
        self.imagen = PhotoImage(file=r"imagenes\regresar.png")
        
        # Botón de imagen
        self.boton_imagen = tk.Button(self.main_frame, image=self.imagen, command=self.controlador.mostrar_inicio, borderwidth=0, bg="#E0F7FA", activebackground="#E0F7FA")
        self.boton_imagen.place(x=80, y=30)  # Ajusta la posición como desees
        
    def crear_frame_iniciar_sesion(self):
        # Frame para el formulario de inicio de sesión con dimensiones fijas
        self.form_frame = tk.Frame(self.main_frame, bg="#ffffff", relief=tk.GROOVE, borderwidth=2)
        self.form_frame.place(relx=0.5, rely=0.5, anchor="center", width=800, height=680)  # Establecer tamaño y centrar

        # Label de bienvenida
        self.label_bienvenida = tk.Label(self.form_frame, text="Iniciar Sesión", font=("Helvetica", 26, "bold"), bg="#ffffff", fg="black")
        self.label_bienvenida.grid(row=0, column=0, columnspan=5, padx=(70, 50) ,pady=(30, 0), sticky="w")

        # Label de instrucciones
        self.label_gestor = tk.Label(self.form_frame, text="Ingresa tus credenciales para acceder al sistema de citas", font=("Helvetica", 18, "bold"), bg="#ffffff", fg="#8a8d8e")
        self.label_gestor.grid(row=1, column=0, columnspan=2, padx=(70, 0) ,pady=(20, 30), sticky="w")

        # Label y entrada para el correo electrónico
        self.label_correo = tk.Label(self.form_frame, text="Nombre/Correo Electrónico/telefono", font=("Helvetica", 18), bg="#ffffff")
        self.label_correo.grid(row=2, column=0, padx=(70, 10), pady=(10, 10), sticky="w")
        self.entry_correo = tk.Entry(self.form_frame, font=("Helvetica", 18), relief= tk.SUNKEN, borderwidth=2)
        self.entry_correo.grid(row=3, column=0, columnspan=4, padx=(70, 0), pady=(10, 10), sticky="we", ipady=5)
        self.set_placeholder(self.entry_correo, "usuario@example.com")

        # Label y entrada para la contraseña
        self.label_contrasena = tk.Label(self.form_frame, text="Contraseña:", font=("Helvetica", 18), bg="#ffffff")
        self.label_contrasena.grid(row=4, column=0, padx=(70, 10), pady=(10, 10), sticky="w")
        self.entry_contrasena = tk.Entry(self.form_frame, font=("Helvetica", 18), show='*', relief= tk.SUNKEN, borderwidth=2)
        self.entry_contrasena.grid(row=5, column=0, columnspan=4, padx=(70, 0), pady=(10, 10), sticky="we", ipady=5)
        self.set_placeholder(self.entry_contrasena, "************")

        # Botón para iniciar sesión
        self.boton_iniciar_sesion = tk.Button(self.form_frame, text="Iniciar Sesión", font=("Helvetica", 18, "bold"), command=self.iniciar_sesion, bg="#332a2a", fg="white", cursor="hand2")
        self.boton_iniciar_sesion.grid(row=6, column=0, columnspan=4, padx=(70, 0), pady=(20, 10), sticky="we")
        
        # boton de recuperar contraseña
        self.boton_recuperar_contraseña = tk.Button(self.form_frame, text="¿Recuperar contraseña?", font=("Helvetica", 18, "bold"), command=self.controlador.mostrar_recuperar_contraseña, bg="#ffffff", fg="#007FFF", cursor="hand2", borderwidth=0, activebackground="#ffffff")
        self.boton_recuperar_contraseña.grid(row=7, column=0, columnspan=4, padx=(70, 0), pady=(10, 10), sticky="we")
        
        # Label pregunta y Boton registarse
        self.label_pregunta = tk.Label(self.form_frame, text="¿No tienes una cuenta?", font=("Helvetica", 18), bg="#ffffff", fg="black")
        self.label_pregunta.grid(row=8, column=0, columnspan=1, padx=(70, 10), pady=(10, 10), sticky="we")
        self.boton_registrarse = tk.Button(self.form_frame, text="Registrarse", font=("Helvetica", 18, "bold"), command=self.controlador.mostrar_rol, bg="#ffffff", fg="#007FFF", cursor="hand2", borderwidth=0, activebackground="#ffffff")
        self.boton_registrarse.grid(row=8, column=1, padx=(10, 50), pady=(10, 10), sticky="we")
    
    def set_placeholder(self, entry, placeholder_text):
        # Función que gestiona el placeholder
        def placeholder_behavior(event):
            if event.type == tk.EventType.FocusIn and entry.get() == placeholder_text:
                entry.delete(0, tk.END)
                entry.config(fg="black")
            elif event.type == tk.EventType.FocusOut and entry.get() == "":
                entry.insert(0, placeholder_text)
                entry.config(fg="#A9A9A9")
                
        entry.insert(0, placeholder_text)
        entry.config(fg="#A9A9A9")
        
        entry.bind("<FocusIn>", placeholder_behavior)
        entry.bind("<FocusOut>", placeholder_behavior)

    def iniciar_sesion(self):
        identificador = self.entry_correo.get().strip()  # Campo que combina nombre/correo/teléfono
        contrasena = self.entry_contrasena.get().strip()

        rol = self.conexion.verificar_iniciar_sesion(identificador, contrasena)

        if rol == "paciente":
            messagebox.showinfo("Éxito", "Inicio de sesión exitoso como paciente.")
            self.controlador.mostrar_menu_paciente()
        elif rol == "doctor":
            messagebox.showinfo("Éxito", "Inicio de sesión exitoso como doctor.")
            self.controlador.mostrar_menu()
        else:
            messagebox.showerror("Error", "Identificador o contraseña incorrectos.")