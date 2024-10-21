import tkinter as tk
from tkinter import PhotoImage, ttk
import datetime
class RegistrarCitaApp(tk.Frame):
    def __init__(self, master=None, controlador=None):
        super().__init__(master)
        master.geometry("1420x800")
        master.minsize(1420, 800)
        self.controlador = controlador
        self.master = master
        self.configure(bg="#E0F7FA")  # Establecer el color de fondo
        self.create_widgets()
        self.entry_paciente.bind("<KeyRelease>", self.validar_nombre)
        
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

        # Crear el formulario de registro de cita dentro de un frame
        self.crear_frame_agenda()
        
        # Cargar la imagen (asegúrate de que la ruta sea correcta)
        self.imagen = PhotoImage(file="imagenes/regresar.png")  # Cambia esto a la ruta correcta de tu imagen
        
        # Botón de imagen
        self.boton_imagen = tk.Button(self.main_frame, image=self.imagen, command=self.controlador.mostrar_menu, borderwidth=0, bg="#E0F7FA", activebackground="#E0F7FA")
        self.boton_imagen.place(x=80, y=30)  # Ajusta la posición como desees
        
    def crear_frame_agenda(self):
        # Frame para el formulario de registro de cita con dimensiones fijas
        self.form_frame = tk.Frame(self.main_frame, bg="#ffffff", relief=tk.GROOVE, borderwidth=2)
        self.form_frame.place(relx=0.5, rely=0.5, anchor="center", width=920, height=620)  # Establecer tamaño y centrar

        # Label de bienvenida
        self.label_bienvenida = tk.Label(self.form_frame, text=" Registrar Cita", font=("Helvetica", 26, "bold"), bg="#ffffff", fg="black")
        self.label_bienvenida.grid(row=0, column=0, columnspan=5, padx=(70, 50), pady=(60, 0), sticky="w")

        # Label y entrada para el nombre del paciente
        self.label_paciente = tk.Label(self.form_frame, text="Nombre del paciente:", font=("Helvetica", 18), bg="#ffffff")
        self.label_paciente.grid(row=1, column=0, columnspan=3, padx=(70, 10), pady=(30, 0), sticky="w")
        self.entry_paciente = tk.Entry(self.form_frame, font=("Helvetica", 18), relief=tk.SUNKEN, borderwidth=2)
        self.entry_paciente.grid(row=2, column=0, columnspan=3, padx=(70, 0), pady=(0, 10), sticky="we", ipady=5, ipadx=25)
        self.set_placeholder(self.entry_paciente, "Ingrese el nombre del paciente")
        
        # Label y entrada para la fecha
        self.label_fecha = tk.Label(self.form_frame, text="Fecha:", font=("Helvetica", 18), bg="#ffffff")
        self.label_fecha.grid(row=3, column=0, columnspan=3, padx=(70, 10), pady=(30, 0), sticky="w")
        self.entry_fecha = tk.Entry(self.form_frame, font=("Helvetica", 18), relief=tk.SUNKEN, borderwidth=2)
        self.entry_fecha.grid(row=4, column=0, columnspan=3, padx=(70, 0), pady=(0, 10), sticky="we", ipady=5)
        self.set_placeholder(self.entry_fecha, "dd/mm/aaaa")
        self.entry_fecha.bind("<KeyRelease>", self.validar_fecha)
        
        # Comboboxes para seleccionar la hora (hora, minutos, AM/PM)
        self.label_hora = tk.Label(self.form_frame, text="Hora:", font=("Helvetica", 18), bg="#ffffff")
        self.label_hora.grid(row=5, column=0, columnspan=3, padx=(70, 10), pady=5, sticky="w")

        self.combo_hora = ttk.Combobox(self.form_frame, font=("Helvetica", 18), width=5, values=[f"{i:02d}" for i in range(1, 13)], state="readonly")
        self.combo_hora.grid(row=6, column=0, padx=(70,0), pady=5, sticky="we")
        self.combo_hora.set("01")  # Valor por defecto
        self.combo_hora.bind("<<ComboboxSelected>>", self.mostrar_hora)

        self.combo_minutos = ttk.Combobox(self.form_frame, font=("Helvetica", 18), width=5, values=[f"{i:02d}" for i in range(0, 60)], state="readonly")
        self.combo_minutos.grid(row=6, column=1, padx=0, pady=5, sticky="we")
        self.combo_minutos.set("00")  # Valor por defecto
        self.combo_minutos.bind("<<ComboboxSelected>>", self.mostrar_hora)

        self.combo_am_pm = ttk.Combobox(self.form_frame, font=("Helvetica", 18), width=5, values=["AM", "PM"], state="readonly")
        self.combo_am_pm.grid(row=6, column=2, padx=0, pady=5, sticky="we")
        self.combo_am_pm.set("AM")  # Valor por defecto
        self.combo_am_pm.bind("<<ComboboxSelected>>", self.mostrar_hora)

        # Label y área de texto para el motivo de consulta
        self.label_motivo = tk.Label(self.form_frame, text="Motivo de consulta:", font=("Helvetica", 18), bg="#ffffff")
        self.label_motivo.grid(row=1, column=3, padx=(70, 10), pady=(30, 0), sticky="w")
        self.text_motivo = tk.Text(self.form_frame, font=("Helvetica", 18), relief=tk.SUNKEN, borderwidth=2, width=30, height=10)  # Ajusta el tamaño según sea necesario
        self.text_motivo.grid(row=2, rowspan=5, column=3, padx=(70, 0), pady=(10, 10), sticky="w")
        self.set_placeholder(self.text_motivo, "Describa brevemente el motivo de la consulta")

        # Botón para registrar cita
        self.boton_registrar_cita = tk.Button(self.form_frame, text="Registrar Cita", font=("Helvetica", 18, "bold"), command=None, bg="#332a2a", fg="white", cursor="hand2")
        self.boton_registrar_cita.grid(row=7, column=0, columnspan=4, padx=(70, 0), pady=(20, 10), sticky="we")
    
    def mostrar_hora(self, event=None):
        hora = self.combo_hora.get()
        minutos = self.combo_minutos.get()
        am_pm = self.combo_am_pm.get()
        print(f"Hora seleccionada: {hora}:{minutos} {am_pm}")

    def set_placeholder(self, widget, placeholder_text):
        # Establecer el texto de placeholder
        widget.insert("1.0" if isinstance(widget, tk.Text) else 0, placeholder_text)
        widget.config(fg="#A9A9A9")  # Color gris para el placeholder

        # Asociar eventos para el manejo de focus
        widget.bind("<FocusIn>", lambda event: self.on_focus(event, widget, placeholder_text))
        widget.bind("<FocusOut>", lambda event: self.on_focus_out(event, widget, placeholder_text))

    def on_focus(self, event, widget, placeholder_text):
        if isinstance(widget, tk.Entry):
            if widget.get() == placeholder_text:
                widget.delete(0, tk.END)  # Eliminar el placeholder
                widget.config(fg="black")  # Cambiar el color del texto a negro cuando se enfoca
        elif isinstance(widget, tk.Text):
            if widget.get("1.0", tk.END).strip() == placeholder_text:
                widget.delete("1.0", tk.END)  # Eliminar el placeholder
                widget.config(fg="black")  # Cambiar el color del texto a negro cuando se enfoca

    def on_focus_out(self, event, widget, placeholder_text):
        if isinstance(widget, tk.Entry):
            if widget.get() == "":
                widget.insert(0, placeholder_text)  # Restaura el texto inicial
                widget.config(fg="#A9A9A9")  # Cambiar el color del texto de nuevo al color del placeholder
        elif isinstance(widget, tk.Text):
            if widget.get("1.0", tk.END).strip() == "":
                widget.insert("1.0", placeholder_text)  # Restaura el texto inicial
                widget.config(fg="#A9A9A9")  # Cambiar el color del texto de nuevo al color del placeholder

    def validar_nombre(self, event=None):
        nombre = self.entry_paciente.get()
        
        # Limitar a 50 caracteres
        if len(nombre) > 50:
            nombre = nombre[:50]
        
        # Permitir solo letras y espacios
        nuevo_nombre = ''.join(c for c in nombre if c.isalpha() or c.isspace())
        
        # Actualizar la entrada con el nuevo nombre validado
        self.entry_paciente.delete(0, tk.END)
        self.entry_paciente.insert(0, nuevo_nombre)

    def validar_fecha(self, event=None):
            fecha = self.entry_fecha.get().replace('/', '')  # Eliminar las barras para la validación
            nuevo_fecha = ''.join(c for c in fecha if c.isdigit())  # Permitir solo dígitos

            # Limitar a 8 caracteres
            if len(nuevo_fecha) > 8:
                nuevo_fecha = nuevo_fecha[:8]

            # Volver a insertar la fecha con formato
            formatted_fecha = ""
            for i, char in enumerate(nuevo_fecha):
                formatted_fecha += char
                if i == 1 or i == 3:  # Agregar diagonal después del día y el mes
                    formatted_fecha += '/'

            # Actualizar la entrada
            self.entry_fecha.delete(0, tk.END)
            self.entry_fecha.insert(0, formatted_fecha)

            # Validar que se ingresaron exactamente 8 dígitos sin contar las diagonales
            if len(nuevo_fecha) == 8:
                dia, mes, año = int(nuevo_fecha[:2]), int(nuevo_fecha[2:4]), int(nuevo_fecha[4:8])
                año_actual = datetime.datetime.now().year

                # Validar año
                if año < año_actual:
                    self.entry_fecha.delete(0, tk.END)
                    self.entry_fecha.insert(0, "Año no válido")
                    return

                # Validar día
                if mes < 1 or mes > 12 or dia < 1 or dia > 31:
                    self.entry_fecha.delete(0, tk.END)
                    return

                # Validar días por mes
                if (mes in [4, 6, 9, 11]) and dia > 30:  # Meses con 30 días
                    self.entry_fecha.delete(0, tk.END)
                    return
                elif mes == 2:  # Febrero
                    if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
                        if dia > 29:  # Año bisiesto
                            self.entry_fecha.delete(0, tk.END)
                            return
                    else:
                        if dia > 28:  # No bisiesto
                            self.entry_fecha.delete(0, tk.END)
                            return
        
if __name__ == "__main__":
    root = tk.Tk()
    app = RegistrarCitaApp(master=root)
    app.pack(fill=tk.BOTH, expand=True)
    root.mainloop()
