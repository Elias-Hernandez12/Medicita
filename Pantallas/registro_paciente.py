import tkinter as tk
from tkinter import PhotoImage, messagebox
from modelos.conexion_db import ConexionDB
import re

class RegistroPacienteApp(tk.Frame):
    def __init__(self, master=None, controlador=None):
        super().__init__(master)
        master.geometry("1420x800")
        self.controlador = controlador
        self.conexion = ConexionDB()
        self.master = master
        self.configure(bg="#E0F7FA")  # Establecer el color de fondo
        self.create_widgets()
        
    def create_widgets(self):
        # Frame para el header
        self.header_frame = tk.Frame(self, bg="#E0F7FA")
        self.header_frame.pack(padx=20, pady=(5,0), fill=tk.X)

        # Título del programa
        self.label_titulo = tk.Label(self.header_frame, text="Medicita", font=("Helvetica", 28, "bold"), bg="#E0F7FA", fg="#007FFF")
        self.label_titulo.pack(side=tk.LEFT)

        # Frame principal para el contenido
        self.main_frame = tk.Frame(self, bg="#E0F7FA")
        self.main_frame.pack(padx=20, pady=20, fill=tk.BOTH, expand=True)

        # Crear el formulario de registro
        self.crear_frame_registro()
        
        # Cargar la imagen de regresar
        self.imagen = PhotoImage(file="imagenes/regresar.png")  # Cambia esto a la ruta correcta de tu imagen
        self.boton_imagen = tk.Button(self.main_frame, image=self.imagen, command=self.controlador.mostrar_rol, borderwidth=0, bg="#E0F7FA", activebackground="#E0F7FA")
        self.boton_imagen.place(x=80, y=30)  # Ajusta la posición como desees
        
    def crear_frame_registro(self):
        # Frame para el formulario de registro con dimensiones fijas
        self.form_frame = tk.Frame(self.main_frame, bg="#ffffff", relief=tk.GROOVE, borderwidth=2)
        self.form_frame.place(relx=0.5, rely=0.5, anchor="center", width=800, height=700)  # Establecer tamaño y centrar

        # Label de bienvenida
        self.label_bienvenida = tk.Label(self.form_frame, text="Registro de Pacientes", font=("Helvetica", 26, "bold"), bg="#ffffff", fg="black")
        self.label_bienvenida.grid(row=0, column=0, columnspan=5, padx=(70, 50), pady=(30, 0), sticky="w")

        self.label_intruccion = tk.Label(self.form_frame, text="Ingresa los datos para acceder al sistema de citas", font=("Helvetica",18, ), bg="#ffffff", fg="#8a8d8e")
        self.label_intruccion.grid(row=1, column=0, columnspan=2, padx=(70, 0), pady=10, sticky="w")
        
        # Campos del formulario
        self.crear_campos_registro()

        # Botón para registrarse
        self.boton_registrarse = tk.Button(self.form_frame, text="Registrarse", font=("Helvetica", 18, "bold"), command=self.registrar_paciente, bg="#332a2a", fg="white", cursor="hand2")
        self.boton_registrarse.grid(row=10, column=0, columnspan=4, padx=(70, 0), pady=10, sticky="we")

        # Label pregunta y Botón iniciar sesión
        self.label_pregunta = tk.Label(self.form_frame, text="¿Ya tienes una cuenta?", font=("Helvetica", 18), bg="#ffffff", fg="black")
        self.label_pregunta.grid(row=11, column=0, columnspan=1, padx=(70, 10), pady=5, sticky="we")
        self.boton_iniciar_sesion = tk.Button(self.form_frame, text="Iniciar sesión", font=("Helvetica", 18, "bold"), command=self.controlador.mostrar_iniciar_sesion, bg="#ffffff", fg="#007FFF", cursor="hand2", borderwidth=0, activebackground="#ffffff")
        self.boton_iniciar_sesion.grid(row=11, column=1, padx=(10, 50), pady=5, sticky="we")

    def crear_campos_registro(self):
        # Label y entrada para el Nombre completo
        self.label_nombre = tk.Label(self.form_frame, text="Nombre completo:", font=("Helvetica", 18), bg="#ffffff")
        self.label_nombre.grid(row=2, column=0, padx=(70, 10), pady=5, sticky="w")
        self.entry_nombre = tk.Entry(self.form_frame, font=("Helvetica", 18), relief=tk.SUNKEN, borderwidth=2)
        self.entry_nombre.grid(row=3, column=0, columnspan=4, padx=(70, 0), pady=5, sticky="we", ipady=5)
        self.set_placeholder(self.entry_nombre, "Juan Pérez Sánchez")
        
        # Label y entrada para la Fecha de Nacimiento
        self.label_fecha_nacimiento = tk.Label(self.form_frame, text="Fecha de Nacimiento:", font=("Helvetica", 18), bg="#ffffff")
        self.label_fecha_nacimiento.grid(row=4, column=0, padx=(70, 10), pady=5, sticky="w")
        self.entry_fecha_nacimiento = tk.Entry(self.form_frame, font=("Helvetica", 18), relief=tk.SUNKEN, borderwidth=2)
        self.entry_fecha_nacimiento.grid(row=5, column=0, columnspan=1, padx=(70, 0), pady=5, sticky="w", ipady=5)
        self.set_placeholder(self.entry_fecha_nacimiento, "DD/MM/YYYY")

        # Label y entrada para el Número de Teléfono
        self.label_telefono = tk.Label(self.form_frame, text="Número de Teléfono:", font=("Helvetica", 18), bg="#ffffff")
        self.label_telefono.grid(row=4, column=1, padx=(70, 10), pady=5, sticky="w")
        self.entry_telefono = tk.Entry(self.form_frame, font=("Helvetica", 18), relief=tk.SUNKEN, borderwidth=2)
        self.entry_telefono.grid(row=5, column=1, columnspan=1, padx=(70, 0), pady=5, sticky="w", ipady=5)
        self.set_placeholder(self.entry_telefono, "987654321")

        # Label y entrada para el Correo Electrónico
        self.label_correo = tk.Label(self.form_frame, text="Correo Electrónico:", font=("Helvetica", 18), bg="#ffffff")
        self.label_correo.grid(row=6, column=0, padx=(70, 10), pady=5, sticky="w")
        self.entry_correo = tk.Entry(self.form_frame, font=("Helvetica", 18), relief=tk.SUNKEN, borderwidth=2)
        self.entry_correo.grid(row=7, column=0, columnspan=4, padx=(70, 0), pady=5, sticky="we", ipady=5)
        self.set_placeholder(self.entry_correo, "usuario@example.com")

        # Label y entrada para la Contrasena
        self.label_contrasena = tk.Label(self.form_frame, text="Contraseña:", font=("Helvetica", 18), bg="#ffffff")
        self.label_contrasena.grid(row=8, column=0, padx=(70, 10), pady=5, sticky="w")
        self.entry_contrasena = tk.Entry(self.form_frame, font=("Helvetica", 18), show='*', relief=tk.SUNKEN, borderwidth=2)
        self.entry_contrasena.grid(row=9, column=0, columnspan=1, padx=(70, 0), pady=5, sticky="w", ipady=5)
        self.set_placeholder(self.entry_contrasena, "*************")

        # Label y entrada para Confirmar Contrasena
        self.label_confirmar_contrasena = tk.Label(self.form_frame, text="Confirmar Contraseña:", font=("Helvetica", 18), bg="#ffffff")
        self.label_confirmar_contrasena.grid(row=8, column=1, padx=(70, 10), pady=5, sticky="w")
        self.entry_confirmar_contrasena = tk.Entry(self.form_frame, font=("Helvetica", 18), show='*', relief=tk.SUNKEN, borderwidth=2)
        self.entry_confirmar_contrasena.grid(row=9, column=1, columnspan=1, padx=(70, 0), pady=5, sticky="w", ipady=5)
        self.set_placeholder(self.entry_confirmar_contrasena, "*************")

    def set_placeholder(self, entry, placeholder_text):
        # Función que gestiona el placeholder
        def placeholder_behavior(event):
            if event.type == tk.EventType.FocusIn and entry.get() == placeholder_text:
                entry.delete(0, tk.END)
                entry.config(fg="black")
            elif event.type == tk.EventType.FocusOut and entry.get() == "":
                entry.insert(0, placeholder_text)
                entry.config(fg="#A9A9A9")

        # Configuración inicial del placeholder
        entry.insert(0, placeholder_text)
        entry.config(fg="#A9A9A9")
        
        # Asignación de eventos con la función anónima
        entry.bind("<FocusIn>", placeholder_behavior)
        entry.bind("<FocusOut>", placeholder_behavior)
            
    def validar_contrasena(self, contrasena):
        if len(contrasena) < 8:
            messagebox.showwarning("Advertencia", "La contrasena debe tener al menos 8 caracteres.")
            return False
        elif not re.search("[A-Za-z]", contrasena) or not re.search("[0-9]", contrasena):
            messagebox.showwarning("Advertencia", "La contrasena debe tener al menos una letra y un número.")
            return False
        return True

    def registrar_paciente(self):
        # Obtener valores del formulario
        nombre = self.entry_nombre.get()
        correo = self.entry_correo.get()
        telefono = self.entry_telefono.get()
        fecha_nacimiento = self.entry_fecha_nacimiento.get()
        contrasena = self.entry_contrasena.get()
        confirmar_contrasena = self.entry_confirmar_contrasena.get()
        
        # Validación de contrasenas
        if contrasena != confirmar_contrasena:
            messagebox.showerror("Error", "Las contrasenas no coinciden.")
            return
        
        if not self.validar_contrasena(contrasena):
            return
        
        # Insertar en la base de datos
        self.conexion.insertar_paciente(nombre, correo, telefono, fecha_nacimiento, contrasena)

        messagebox.showinfo("Éxito", "Paciente registrado correctamente.")
        self.controlador.mostrar_iniciar_sesion()

