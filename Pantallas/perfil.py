import tkinter as tk
from tkinter import PhotoImage, filedialog, Toplevel, StringVar, messagebox, ttk
from tkinter.ttk import Combobox, Checkbutton
from PIL import Image, ImageTk, ImageDraw

class PerfilApp(tk.Frame):
    def __init__(self, master=None, controlador=None):
        super().__init__(master)
        master.geometry("1420x800")
        self.controlador = controlador
        self.master = master
        self.configure(bg="#E0F7FA")  # Establecer el color de fondo
        self.create_widgets()
        self.ventana_emergente_abierta = False
        self.icono_predeterminado = PhotoImage(file="imagenes/usuario.png")  # Icono predeterminado
        self.icono_perfil = self.icono_predeterminado  # Inicializar el icono actual
        self.label_icono_perfil = tk.Label(self.form_frame, image=self.icono_perfil, bg="#ffffff")
        self.label_icono_perfil.grid(row=1, column=0, columnspan=2, padx=(420, 420), pady=(5, 5), sticky="we")
        
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
        self.crear_frame_perfil()
        
        # Cargar la imagen (asegúrate de que la ruta sea correcta)
        self.imagen = PhotoImage(file="imagenes/regresar.png")  # Cambia esto a la ruta correcta de tu imagen
        
        # Botón de imagen
        self.boton_imagen = tk.Button(self.main_frame, image=self.imagen, command=self.controlador.mostrar_menu, borderwidth=0, bg="#E0F7FA", activebackground="#E0F7FA")
        self.boton_imagen.place(x=80, y=30)  # Ajusta la posición como desees
        
    def crear_frame_perfil(self):
        # Frame para el formulario de inicio de sesión con dimensiones fijas
        self.form_frame = tk.Frame(self.main_frame, bg="#ffffff", relief=tk.GROOVE, borderwidth=2)
        self.form_frame.place(relx=0.5, rely=0.5, anchor="center", width=1050, height=690)  # Establecer tamaño y centrar

        # Label de bienvenida
        self.label_bienvenida = tk.Label(self.form_frame, text="Perfil del usuario", font=("Helvetica", 26, "bold"), bg="#ffffff", fg="black")
        self.label_bienvenida.grid(row=0, column=0, columnspan=5, padx=50 ,pady=(10,10), sticky="we")

        # Icono de perfil
        self.icono_perfil = PhotoImage(file="imagenes/usuario.png")
        self.label_icono_perfil = tk.Label(self.form_frame, image=self.icono_perfil, bg="#ffffff")
        self.label_icono_perfil.grid(row=1, column=0, columnspan=2, padx=(40, 40), pady=(5, 5), sticky="we")

        # Botón para subir la imagen de perfil
        self.boton_subir_imagen = tk.Button(self.form_frame, text="Subir imagen", font=("Helvetica", 16), command=self.subir_imagen, bg="#332a2a", fg="white", relief=tk.RAISED, borderwidth=2)
        self.boton_subir_imagen.grid(row=2, column=0, padx=(315, 0), pady=(5, 5), sticky="w")

        # Quitar imagem
        self.boton_quitar_imagen = tk.Button(self.form_frame, text="Quitar imagen", font=("Helvetica", 16), command=self.quitar_imagen, bg="#332a2a", fg="white", relief=tk.RAISED, borderwidth=2)
        self.boton_quitar_imagen.grid(row=2, column=1, padx=(50, 0), pady=(5, 5), sticky="w")      
          
        # Label y entrada para el nombre
        self.label_nombre = tk.Label(self.form_frame, text="Nombre completo:", font=("Helvetica", 18), bg="#ffffff")
        self.label_nombre.grid(row=3, column=0, padx=(50, 0), pady=(5, 5), sticky="w")
        self.entry_nombre = tk.Entry(self.form_frame, font=("Helvetica", 18), relief= tk.SUNKEN, borderwidth=2)
        self.entry_nombre.grid(row=4, column=0, padx=(50, 0), pady=(5, 5), sticky="w", ipady=5, ipadx=70)
        self.set_placeholder(self.entry_nombre, "Dr. Juan Pérez")

        # Label y entrada para el correo electrónico
        self.label_correo = tk.Label(self.form_frame, text="Correo Electrónico:", font=("Helvetica", 18), bg="#ffffff")
        self.label_correo.grid(row=3, column=1, padx=(50, 50), pady=(5, 5), sticky="w")
        self.entry_correo = tk.Entry(self.form_frame, font=("Helvetica", 18), relief= tk.SUNKEN, borderwidth=2)
        self.entry_correo.grid(row=4, column=1, padx=(50, 50), pady=(5, 5), sticky="w", ipady=5, ipadx=70)
        self.set_placeholder(self.entry_correo, "doctos@example.com")
        
        # Label y entrada para la especialidad
        self.label_especialidad = tk.Label(self.form_frame, text="Especialidad:", font=("Helvetica", 18), bg="#ffffff")
        self.label_especialidad.grid(row=5, column=0, padx=(50, 0), pady=(5, 5), sticky="w")
        self.entry_especialidad = tk.Entry(self.form_frame, font=("Helvetica", 18), relief= tk.SUNKEN, borderwidth=2)
        self.entry_especialidad.grid(row=6, column=0, padx=(50, 0), pady=(5, 5), sticky="w", ipady=5, ipadx=70)
        self.set_placeholder(self.entry_especialidad, "Cardiología")
        
        # Label y entrada para el telefono
        self.label_telefono = tk.Label(self.form_frame, text="Teléfono de contacto:", font=("Helvetica", 18), bg="#ffffff")
        self.label_telefono.grid(row=5, column=1, padx=(50, 50), pady=(5, 5), sticky="w")
        self.entry_telefono = tk.Entry(self.form_frame, font=("Helvetica", 18), relief= tk.SUNKEN, borderwidth=2)
        self.entry_telefono.grid(row=6, column=1, padx=(50, 50), pady=(5, 5), sticky="w", ipady=5, ipadx=70)
        self.set_placeholder(self.entry_telefono, "Ej: +52 123 456 7890")
        
        # Label y entrada para la la cedula
        self.label_cedula = tk.Label(self.form_frame, text="Número de Cédula Profesional:", font=("Helvetica", 18), bg="#ffffff")
        self.label_cedula.grid(row=7, column=0, padx=(50, 0), pady=(5, 5), sticky="w")
        self.entry_cedula = tk.Entry(self.form_frame, font=("Helvetica", 18), relief= tk.SUNKEN, borderwidth=2)
        self.entry_cedula.grid(row=8, column=0, padx=(50, 0), pady=(5, 5), sticky="w", ipady=5, ipadx=70)
        self.set_placeholder(self.entry_cedula, "12345678")
        
        # Label y entrada para la direccion
        self.label_direccion = tk.Label(self.form_frame, text="Dirección de la clínica o consultorio:", font=("Helvetica", 18), bg="#ffffff")
        self.label_direccion.grid(row=7, column=1, padx=(50, 50), pady=(5, 5), sticky="w")
        self.entry_direccion = tk.Entry(self.form_frame, font=("Helvetica", 18), relief= tk.SUNKEN, borderwidth=2)
        self.entry_direccion.grid(row=8, column=1, padx=(50, 50), pady=(5, 5), sticky="w", ipady=5, ipadx=70)
        self.set_placeholder(self.entry_direccion, "Ingresa la direccion completa")
        
        # Botón para abrir la ventana emergente del horario
        self.label_horario = tk.Label(self.form_frame, text="Horario de Atención:", font=("Helvetica", 18), bg="#ffffff")
        self.label_horario.grid(row=9, column=0, padx=(50, 0), pady=(5, 5), sticky="w")
        
        self.boton_horario = tk.Button(self.form_frame, text="Seleccionar Horario de Atención", font=("Helvetica", 14), anchor="w", padx=10, command=self.abrir_ventana_horario, bg="white", fg="black", cursor="hand2")
        self.boton_horario.grid(row=10, column=0, columnspan=2, padx=(50, 50), pady=(5, 5), sticky="we", ipady=5, ipadx=70)
        
        # Botón para guardar cambios
        self.boton_cambiar_contraseña = tk.Button(self.form_frame, text="Cambiar Contraseña", font=("Helvetica", 14, "bold"), command=self.cambiar_contraseña, bg="white", fg="black", cursor="hand2")
        self.boton_cambiar_contraseña.grid(row=11, column=0, padx=120, pady=10, sticky="w", ipadx=40, ipady=5)
        
        # Botón para cambiar contraseña
        self.boton_guardar_cambios = tk.Button(self.form_frame, text="Guardar Cambios", font=("Helvetica", 14, "bold"), command=self.guardar_cambios, bg="#332a2a", fg="white", cursor="hand2")
        self.boton_guardar_cambios.grid(row=11, column=1, padx=90, pady=10, sticky="w", ipadx=40, ipady=5)
    
    def abrir_ventana_horario(self):
        # Crear una ventana emergente estilizada
        self.ventana_horario = Toplevel(self)
        self.ventana_horario.grab_set()  # Bloquear la interacción con la ventana principal
        self.ventana_horario.title("Seleccionar Horario")
        self.ventana_horario.geometry("400x400")
        self.ventana_horario.config(bg="#ffffff")
        self.ventana_horario.iconbitmap("imagenes/chequeo.ico")
        
        # Centrar la ventana en la pantalla
        self.centrar_ventana(self.ventana_horario)

        # Frame para contener los días
        frame_dias = tk.Frame(self.ventana_horario, bg="white", padx=10, pady=10)
        frame_dias.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
        
        # Crear checklist para los días de la semana
        self.dias_seleccionados = []
        self.dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
        for i, dia in enumerate(self.dias_semana):
            var = StringVar()
            check = tk.Checkbutton(frame_dias, text=dia, variable=var, onvalue=dia, offvalue="", bg="white", font=("Helvetica", 14, "bold"))
            check.grid(row=i, column=0, sticky="w", pady=2)
            self.dias_seleccionados.append(var)

        # Frame para contener las horas de entrada y salida
        frame_horas = tk.Frame(self.ventana_horario, bg="white", padx=10, pady=10)
        frame_horas.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")

        horas = [f"{h:02d}:00" for h in range(24)]
        self.hora_entrada = StringVar(value=horas[0])
        self.hora_salida = StringVar(value=horas[0])

        tk.Label(frame_horas, text="Hora de Entrada:", bg="white", font=("Helvetica", 14, "bold")).grid(row=0, column=0, sticky="w", pady=(40, 0))
        self.combobox_entrada = ttk.Combobox(frame_horas, textvariable=self.hora_entrada, values=horas, state="readonly")
        self.combobox_entrada.grid(row=1, column=0, pady=10, ipady=5, ipadx=5)

        tk.Label(frame_horas, text="Hora de Salida:", bg="white", font=("Helvetica", 14, "bold")).grid(row=2, column=0, sticky="w")
        self.combobox_salida = ttk.Combobox(frame_horas, textvariable=self.hora_salida, values=horas, state="readonly")
        self.combobox_salida.grid(row=3, column=0, pady=10, ipady=5, ipadx=5)

        # Botón para guardar el horario
        boton_guardar = tk.Button(self.ventana_horario, text="Guardar", command=self.guardar_horario, bg="#332a2a", fg="white", font=("Helvetica", 18, "bold"))
        boton_guardar.grid(row=1, column=0, columnspan=2, pady=10, ipady=3, ipadx=10)

        # Hacer que la ventana sea responsive
        self.ventana_horario.columnconfigure(0, weight=1)
        self.ventana_horario.columnconfigure(1, weight=1)
        
    def centrar_ventana(self, ventana):
        ventana.update_idletasks()  # Actualizar las tareas de la ventana
        width = ventana.winfo_width()  # Obtener el ancho de la ventana
        height = ventana.winfo_height()  # Obtener la altura de la ventana

        # Obtener las dimensiones de la pantalla
        screen_width = ventana.winfo_screenwidth()
        screen_height = ventana.winfo_screenheight()

        # Calcular la posición x, y para centrar la ventana
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)

        ventana.geometry(f"{width}x{height}+{x}+{y}")  # Establecer la geometría de la ventana

    def guardar_horario(self):
        # Obtener los días seleccionados
        dias = [var.get() for var in self.dias_seleccionados if var.get()]

        if not dias:
            messagebox.showwarning("Advertencia", "Debe seleccionar al menos un día")
            return
        
        # Obtener las horas seleccionadas
        entrada = self.hora_entrada.get()
        salida = self.hora_salida.get()

        # Validar horas
        if entrada >= salida:
            messagebox.showwarning("Advertencia", "La hora de entrada debe ser anterior a la hora de salida.")
            return

        # Actualizar el texto del botón principal
        dias_texto = ", ".join(dias)
        self.boton_horario.config(text=f"{dias_texto} de {entrada} a {salida}")

        # Cerrar la ventana emergente
        self.ventana_horario.destroy()
        
    def subir_imagen(self):
        # Abrir el diálogo para seleccionar una imagen
        ruta_imagen = filedialog.askopenfilename(filetypes=[("Imagenes", "*.jpg *.jpeg *.png *.gif")])
        
        if ruta_imagen:
            # Abrir la imagen con Pillow
            imagen = Image.open(ruta_imagen)
            
            # Adaptar la imagen a un tamaño específico (por ejemplo, 80x80 píxeles)
            imagen = imagen.resize((80, 80), Image.LANCZOS)

            # Crear una máscara circular
            mascara = Image.new("L", (80, 80), 0)
            draw = ImageDraw.Draw(mascara)
            draw.ellipse((0, 0, 80, 80), fill=255)

            # Aplicar la máscara a la imagen
            imagen_circular = Image.new("RGBA", (80, 80))
            imagen_circular.paste(imagen, (0, 0), mascara)

            # Convertir la imagen a PhotoImage para usar en Tkinter
            self.icono_perfil = ImageTk.PhotoImage(imagen_circular)

            # Sustituir la imagen en el label
            self.label_icono_perfil.config(image=self.icono_perfil)
            self.label_icono_perfil.image = self.icono_perfil  # Mantener una referencia de la imagen

    def quitar_imagen(self):
        # Restaurar el icono predeterminado
        self.label_icono_perfil.config(image=self.icono_predeterminado)
        self.label_icono_perfil.image = self.icono_predeterminado  # Mantener una referencia del icono predeterminado
        self.icono_perfil = self.icono_predeterminado  # Actualizar la variable del icono actual

            
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
    
    def cambiar_contraseña(self):
        # Crear una ventana emergente para cambiar la contraseña
        self.ventana_cambiar_contraseña = Toplevel(self)
        self.ventana_cambiar_contraseña.grab_set()  # Bloquear la interacción con la ventana principal
        self.ventana_cambiar_contraseña.title("Cambiar Contraseña")
        self.ventana_cambiar_contraseña.geometry("400x350")
        self.ventana_cambiar_contraseña.config(bg="#ffffff")
        self.ventana_cambiar_contraseña.iconbitmap("imagenes/chequeo.ico")

        # Centrar la ventana
        self.ventana_cambiar_contraseña.update_idletasks()
        x = (self.winfo_screenwidth() // 2) - (self.ventana_cambiar_contraseña.winfo_width() // 2)
        y = (self.winfo_screenheight() // 2) - (self.ventana_cambiar_contraseña.winfo_height() // 2)
        self.ventana_cambiar_contraseña.geometry(f"+{x}+{y}")

        # Frame para contener el formulario
        frame_formulario = tk.Frame(self.ventana_cambiar_contraseña, bg="white", padx=10, pady=10)
        frame_formulario.pack(padx=20, pady=20, fill=tk.BOTH, expand=True)

        # Variables para almacenar las contraseñas
        self.contraseña_actual = StringVar()
        self.contraseña_nueva = StringVar()
        self.confirmar_contraseña = StringVar()

        # Etiquetas y campos de entrada
        tk.Label(frame_formulario, text="Contraseña Actual:", bg="white", font=("Helvetica", 14, "bold")).pack(anchor="w", pady=5)
        entry_actual = tk.Entry(frame_formulario, textvariable=self.contraseña_actual, show="*", relief=tk.GROOVE, font=("Helvetica", 14))
        entry_actual.pack(fill=tk.X, pady=5)
        self.set_placeholder(entry_actual, "****************")

        tk.Label(frame_formulario, text="Contraseña Nueva:", bg="white", font=("Helvetica", 14, "bold")).pack(anchor="w", pady=5)
        entry_nueva = tk.Entry(frame_formulario, textvariable=self.contraseña_nueva, show="*", relief=tk.GROOVE, font=("Helvetica", 14))
        entry_nueva.pack(fill=tk.X, pady=5)
        self.set_placeholder(entry_nueva, "****************")

        tk.Label(frame_formulario, text="Confirmar Contraseña:", bg="white", font=("Helvetica", 14, "bold")).pack(anchor="w", pady=5)
        entry_confirmar = tk.Entry(frame_formulario, textvariable=self.confirmar_contraseña, show="*", relief=tk.GROOVE, font=("Helvetica", 14))
        entry_confirmar.pack(fill=tk.X, pady=5)
        self.set_placeholder(entry_confirmar, "****************")

        # Botón para cambiar la contraseña
        boton_cambiar = tk.Button(frame_formulario, text="Cambiar Contraseña", command=self.guardar_cambio_contraseña, bg="#332a2a", fg="white", font=("Helvetica", 14, "bold"))
        boton_cambiar.pack(pady=10)

    def guardar_cambio_contraseña(self):
        # Obtener las contraseñas ingresadas
        actual = self.contraseña_actual.get()
        nueva = self.contraseña_nueva.get()
        confirmar = self.confirmar_contraseña.get()

        # Validar que todos los campos estén llenos
        if not actual or not nueva or not confirmar:
            tk.messagebox.showerror("Error", "Por favor, completa todos los campos.")
            return

        # Validar que la nueva contraseña y la confirmación coincidan
        if nueva != confirmar:
            tk.messagebox.showerror("Error", "Las contraseñas no coinciden.")
            return

        # Aquí implementas la lógica para verificar la contraseña actual y cambiarla
        # Por ahora, mostrar un mensaje de éxito como ejemplo
        tk.messagebox.showinfo("Éxito", "Contraseña cambiada con éxito.")
    
    def guardar_cambios(self):
        pass
        
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Medicita")  # Título de la ventana
    root.iconbitmap("imagenes/chequeo.ico")  # Cambia esto a la ruta correcta de tu icono

    app = PerfilApp(master=root)
    app.pack(fill=tk.BOTH, expand=True)

    root.mainloop()
