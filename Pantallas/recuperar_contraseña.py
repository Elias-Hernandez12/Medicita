import tkinter as tk
from tkinter import PhotoImage

class RecuperarPasswordApp(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        master.geometry("1420x800")
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
        
        # Crear el boton regresar
        self.crear_boton_regresar()
        
    def crear_boton_regresar(self):
        # Cargar la imagen (asegúrate de que la ruta sea correcta)
        self.imagen = PhotoImage(file="imagenes/regresar.png")  # Cambia esto a la ruta correcta de tu imagen
        
        # Botón de imagen
        self.boton_imagen = tk.Button(self.main_frame, image=self.imagen, command=self.regresar, borderwidth=0, bg="#E0F7FA", activebackground="#E0F7FA")
        self.boton_imagen.place(x=40, y=30)  # Ajusta la posición como desees
        
    def crear_frame_iniciar_sesion(self):
        # Frame para el formulario de inicio de sesión con dimensiones fijas
        self.form_frame = tk.Frame(self.main_frame, bg="#ffffff", relief=tk.GROOVE, borderwidth=2)
        self.form_frame.place(relx=0.5, rely=0.5, anchor="center", width=1110, height=620)  # Establecer tamaño y centrar

        # Label de bienvenida
        self.label_bienvenida = tk.Label(self.form_frame, text="Recuperar Contraseña", font=("Helvetica", 26, "bold"), bg="#ffffff", fg="black")
        self.label_bienvenida.grid(row=0, column=0, columnspan=5, padx=(30, 30) ,pady=(30, 0), sticky="we")

        # Label de instrucciones
        self.label_gestor = tk.Label(self.form_frame, text="Por favor, ingrese la siguiente información para verificar su identidad y recuperar su contraseña", font=("Helvetica", 16, "bold"), bg="#ffffff", fg="#8a8d8e")
        self.label_gestor.grid(row=1, column=0, columnspan=2, padx=70 ,pady=(20, 30), sticky="w")

        # Label y entrada para el correo electrónico
        self.label_correo = tk.Label(self.form_frame, text="Correo Electrónico:", font=("Helvetica", 18), bg="#ffffff")
        self.label_correo.grid(row=2, column=0, padx=70, pady=(10, 10), sticky="w")
        self.entry_correo = tk.Entry(self.form_frame, font=("Helvetica", 18), relief= tk.SUNKEN, borderwidth=2)
        self.entry_correo.grid(row=3, column=0, padx=70, pady=(10, 10), sticky="w", ipady=5, ipadx=70)
        self.set_placeholder(self.entry_correo, "doctos@example.com")
        
        # Label y entrada para la especialidad
        self.label_especialidad = tk.Label(self.form_frame, text="Especialidad:", font=("Helvetica", 18), bg="#ffffff")
        self.label_especialidad.grid(row=2, column=1, padx=70, pady=(10, 10), sticky="w")
        self.entry_especialidad = tk.Entry(self.form_frame, font=("Helvetica", 18), relief= tk.SUNKEN, borderwidth=2)
        self.entry_especialidad.grid(row=3, column=1, padx=70, pady=(10, 10), sticky="w", ipady=5, ipadx=70)
        self.set_placeholder(self.entry_especialidad, "Cardiología")
        
        # Label y entrada para el Nombre completo
        self.label_nombre = tk.Label(self.form_frame, text="Nombre completo:", font=("Helvetica", 18), bg="#ffffff")
        self.label_nombre.grid(row=4, column=0, padx=70, pady=(10, 10), sticky="w")
        self.entry_nombre = tk.Entry(self.form_frame, font=("Helvetica", 18), relief= tk.SUNKEN, borderwidth=2)
        self.entry_nombre.grid(row=5, column=0, padx=70, pady=(10, 10), sticky="w", ipady=5, ipadx=70)
        self.set_placeholder(self.entry_nombre, "Dr. Juan Pérez")
        
        # Label y entrada para la fecha de nacimiento
        self.label_nacimiento = tk.Label(self.form_frame, text="Fecha de nacimiento:", font=("Helvetica", 18), bg="#ffffff")
        self.label_nacimiento.grid(row=4, column=1, padx=(70, 10), pady=(10, 10), sticky="w")
        self.entry_nacimiento = tk.Entry(self.form_frame, font=("Helvetica", 18), relief= tk.SUNKEN, borderwidth=2)
        self.entry_nacimiento.grid(row=5, column=1, padx=70, pady=(10, 10), sticky="w", ipady=5, ipadx=70)
        self.set_placeholder(self.entry_nacimiento, "dd/mm/aaaa")
        
        # Label y entrada para la contraseña
        self.label_cedula = tk.Label(self.form_frame, text="Número de Cédula Profesional:", font=("Helvetica", 18), bg="#ffffff")
        self.label_cedula.grid(row=6, column=0, padx=(70, 10), pady=(10, 10), sticky="w")
        self.entry_cedula = tk.Entry(self.form_frame, font=("Helvetica", 18), show='*', relief= tk.SUNKEN, borderwidth=2)
        self.entry_cedula.grid(row=7, column=0, padx=70, pady=(10, 10), sticky="w", ipady=5, ipadx=70)
        self.set_placeholder(self.entry_cedula, "12345678")
        
        # Botón para iniciar sesión
        self.boton_recuperar = tk.Button(self.form_frame, text="Verificar y Recuperar Contraseña", font=("Helvetica", 14, "bold"), command=self.recuperar, bg="#332a2a", fg="white", cursor="hand2")
        self.boton_recuperar.grid(row=7, column=1, padx=70, pady=(10, 10), sticky="w", ipadx=40, ipady=5)
    
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
        
    def recuperar(self):
        print("Recuperar contraseña...")
        
        
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Medicita")  # Título de la ventana
    root.iconbitmap("imagenes/chequeo.ico")  # Cambia esto a la ruta correcta de tu icono

    app = RecuperarPasswordApp(master=root)
    app.pack(fill=tk.BOTH, expand=True)

    root.mainloop()
