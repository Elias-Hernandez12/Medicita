import tkinter as tk
from tkinter import PhotoImage

class RegistrarseApp(tk.Frame):
    def __init__(self, master=None, controlador=None,):
        super().__init__(master)
        master.geometry("1420x800")
        self.controlador = controlador
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
        self.imagen = PhotoImage(file="imagenes/regresar.png")  # Cambia esto a la ruta correcta de tu imagen
        
        # Botón de imagen
        self.boton_imagen = tk.Button(self.main_frame, image=self.imagen, command=self.controlador.mostrar_inicio, borderwidth=0, bg="#E0F7FA", activebackground="#E0F7FA")
        self.boton_imagen.place(x=80, y=30)  # Ajusta la posición como desees
        
    def crear_frame_iniciar_sesion(self):
        # Frame para el formulario de inicio de sesión con dimensiones fijas
        self.form_frame = tk.Frame(self.main_frame, bg="#ffffff", relief=tk.GROOVE, borderwidth=2)
        self.form_frame.place(relx=0.5, rely=0.5, anchor="center", width=800, height=680)  # Establecer tamaño y centrar

        # Label de bienvenida
        self.label_bienvenida = tk.Label(self.form_frame, text="Registrarse", font=("Helvetica", 26, "bold"), bg="#ffffff", fg="black")
        self.label_bienvenida.grid(row=0, column=0, columnspan=5, padx=(70, 50) ,pady=(30, 0), sticky="w")

        # Label de instrucciones
        self.label_instruccion = tk.Label(self.form_frame, text="Crea una nueva cuenta para acceder al sistema de citas", font=("Helvetica", 18, "bold"), bg="#ffffff", fg="#8a8d8e")
        self.label_instruccion.grid(row=1, column=0, columnspan=2, padx=(70, 0) ,pady=10, sticky="w")

        # Label y entrada para el Nombre completo
        self.label_nombre = tk.Label(self.form_frame, text="Nombre completo:", font=("Helvetica", 18), bg="#ffffff")
        self.label_nombre.grid(row=2, column=0, padx=(70, 10), pady=5, sticky="w")
        self.entry_nombre = tk.Entry(self.form_frame, font=("Helvetica", 18), relief= tk.SUNKEN, borderwidth=2)
        self.entry_nombre.grid(row=3, column=0, columnspan=4, padx=(70, 0), pady=5, sticky="we", ipady=5)
        self.set_placeholder(self.entry_nombre, "Dr. Juan Pérez")
        
        # Label y entrada para el correo electrónico
        self.label_correo = tk.Label(self.form_frame, text="Correo Electrónico:", font=("Helvetica", 18), bg="#ffffff")
        self.label_correo.grid(row=4, column=0, padx=(70, 10), pady=5, sticky="w")
        self.entry_correo = tk.Entry(self.form_frame, font=("Helvetica", 18), relief= tk.SUNKEN, borderwidth=2)
        self.entry_correo.grid(row=5, column=0, columnspan=4, padx=(70, 0), pady=5, sticky="we", ipady=5)
        self.set_placeholder(self.entry_correo, "doctor@example.com")
        
        # Label y entrada para la contraseña
        self.label_contrasena = tk.Label(self.form_frame, text="Contraseña:", font=("Helvetica", 18), bg="#ffffff")
        self.label_contrasena.grid(row=6, column=0, padx=(70, 10), pady=5, sticky="w")
        self.entry_contrasena = tk.Entry(self.form_frame, font=("Helvetica", 18), show='*', relief= tk.SUNKEN, borderwidth=2)
        self.entry_contrasena.grid(row=7, column=0, columnspan=4, padx=(70, 0), pady=5, sticky="we", ipady=5)
        self.set_placeholder(self.entry_contrasena, "*************")
        
        # Label y entrada para confirmar la contraseña
        self.label_confirmar_contraseña = tk.Label(self.form_frame, text="Confirmar Contraseña:", font=("Helvetica", 18), bg="#ffffff")
        self.label_confirmar_contraseña.grid(row=8, column=0, padx=(70, 10), pady=5, sticky="w")
        self.entry_confirmar_contraseña = tk.Entry(self.form_frame, font=("Helvetica", 18), show='*', relief= tk.SUNKEN, borderwidth=2)
        self.entry_confirmar_contraseña.grid(row=9, column=0, columnspan=4, padx=(70, 0), pady=5, sticky="we", ipady=5)
        self.set_placeholder(self.entry_confirmar_contraseña, "*************")
        
        # Botón para registrarse
        self.boton_registrarse = tk.Button(self.form_frame, text="Registrarse", font=("Helvetica", 18, "bold"), command=self.registrarse, bg="#332a2a", fg="white", cursor="hand2")
        self.boton_registrarse.grid(row=10, column=0, columnspan=4, padx=(70, 0), pady=10, sticky="we")
        
        # Label pregunta y Boton iniciar sesion
        self.label_pregunta = tk.Label(self.form_frame, text="¿Ya tienes una cuenta?", font=("Helvetica", 18), bg="#ffffff", fg="black")
        self.label_pregunta.grid(row=11, column=0, columnspan=1, padx=(70, 10), pady=5, sticky="we")
        self.boton_iniciar_sesion = tk.Button(self.form_frame, text="Iniciar sesión", font=("Helvetica", 18, "bold"), command=self.iniciar_sesion, bg="#ffffff", fg="#007FFF", cursor="hand2", borderwidth=0, activebackground="#ffffff")
        self.boton_iniciar_sesion.grid(row=11, column=1, padx=(10, 50), pady=5, sticky="we")
    
    def set_placeholder(self, entry, placeholder_text):
        # Establecer el texto de placeholder
        entry.insert(0, placeholder_text)
        entry.config(fg="#A9A9A9")  # Color gris para el placeholder

        # Asociar eventos para el manejo de focus
        entry.bind("<FocusIn>", lambda event: self.on_focus(event, entry, placeholder_text))
        entry.bind("<FocusOut>", lambda event: self.on_focus_out(event, entry, placeholder_text))

    def on_focus(self, event, entry, placeholder_text):
        if entry.get() == placeholder_text:
            entry.delete(0, tk.END)  # Eliminar el placeholder
            entry.config(fg="black")  # Cambiar el color del texto a negro cuando se enfoca

    def on_focus_out(self, event, entry, placeholder_text):
        if entry.get() == "":
            entry.insert(0, placeholder_text)  # Restaura el texto inicial
            entry.config(fg="#A9A9A9")  # Cambiar el color del texto de nuevo al color del placeholder

    def regresar(self):
        print("Regresar...")  # Este es un ejemplo
        
    def iniciar_sesion(self):
        print("Registro...")  # Este es un ejemplo

    def registrarse(self):
        pass

                
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Medicita")  # Título de la ventana
    root.iconbitmap("imagenes/chequeo.ico")  # Cambia esto a la ruta correcta de tu icono

    app = RegistrarseApp(master=root)
    app.pack(fill=tk.BOTH, expand=True)

    root.mainloop()
