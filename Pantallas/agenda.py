import tkinter as tk
from tkinter import PhotoImage, messagebox, ttk, Toplevel
from tkcalendar import Calendar

class AgendaApp(tk.Frame):
    def __init__(self, master=None, controlador=None):
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

        # Botón de imagen para regresar
        self.imagen = PhotoImage(file="imagenes/regresar.png")  # Asegúrate de que la ruta de la imagen sea correcta
        
        # Colocar el botón en el lado izquierdo del main_frame
        self.boton_imagen = tk.Button(self.main_frame, image=self.imagen, command=self.controlador.mostrar_menu, borderwidth=0, bg="#E0F7FA", activebackground="#E0F7FA")
        self.boton_imagen.pack(side=tk.LEFT, anchor="n", padx=10, pady=10)

        # Llamar a los métodos para crear los frames
        self.frame_calendario()
        self.frame_citas_programadas()
       
    # Frame calendario de lado izquierdo 
    def frame_calendario(self):
        self.left_frame = tk.Frame(self.main_frame, bg="#ffffff", relief=tk.GROOVE, borderwidth=2)
        self.left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Colocar el calendario en el frame izquierdo
        self.calendario = Calendar(self.left_frame, selectmode="day", date_pattern="yyyy-mm-dd")
        self.calendario.pack(padx=10, pady=10, ipady=90, ipadx=89)

        # Agregar evento al seleccionar un día en el calendario
        self.calendario.bind("<<CalendarSelected>>", self.mostrar_citas_del_dia)

    # Frame lista de citas programadas y botones para reprogramar y cancelar
    def frame_citas_programadas(self):
        # Frame principal derecho
        self.right_frame = tk.Frame(self.main_frame, bg="#ffffff", relief=tk.GROOVE, borderwidth=2)
        self.right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Subframe para el Treeview
        self.tree_frame = tk.Frame(self.right_frame, bg="#ffffff")
        self.tree_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Crear Treeview en el frame derecho
        self.tree_citas = ttk.Treeview(self.tree_frame, columns=("Hora", "Paciente", "Descripción"), show="headings")
        self.tree_citas.heading("Hora", text="Hora")
        self.tree_citas.heading("Paciente", text="Paciente")
        self.tree_citas.heading("Descripción", text="Descripción")
        self.tree_citas.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        # Subframe para los botones (Cancelar y Posponer)
        self.button_frame = tk.Frame(self.right_frame, bg="#ffffff")
        self.button_frame.pack(side=tk.RIGHT, fill=tk.Y, padx=10, pady=10)

        # Botón Cancelar
        self.boton_cancelar = tk.Button(self.button_frame, text="Cancelar", command=self.cancelar_cita, bg="#ff4d4d", fg="white", font=("Helvetica", 12))
        self.boton_cancelar.pack(padx=10, pady=5, fill=tk.X)

        # Botón Posponer
        self.boton_posponer = tk.Button(self.button_frame, text="Posponer", command=self.posponer_cita, bg="#007FFF", fg="white", font=("Helvetica", 12))
        self.boton_posponer.pack(padx=10, pady=5, fill=tk.X)

    # Método para mostrar citas del día seleccionado en el Treeview
    def mostrar_citas_del_dia(self, event):
        # Obtener la fecha seleccionada
        fecha_seleccionada = self.calendario.get_date()

        # Limpiar el Treeview antes de agregar nuevas citas
        for row in self.tree_citas.get_children():
            self.tree_citas.delete(row)

        # Aquí se agregan las citas ficticias para la fecha seleccionada (puedes modificarlo según tus datos)
        citas_ficticias = {
            "2024-10-21": [("09:00", "Juan Pérez", "Consulta general"), ("11:00", "Ana Gómez", "Revisión de seguimiento")],
            "2024-10-22": [("10:00", "Luis Martínez", "Consulta de control")]
        }

        # Verificar si hay citas para la fecha seleccionada
        citas = citas_ficticias.get(fecha_seleccionada, [])

        # Insertar las citas en el Treeview
        for cita in citas:
            self.tree_citas.insert("", "end", values=cita)

    # Método para cancelar una cita
    def cancelar_cita(self):
        selected_item = self.tree_citas.selection()
        if selected_item:
            self.tree_citas.delete(selected_item)

    # Método para posponer una cita (abrirá una nueva ventana emergente)
    def posponer_cita(self):
        selected_item = self.tree_citas.selection()
        if not selected_item:
            messagebox.showwarning("Advertencia", "Por favor, selecciona una cita para posponer.")
            return
        
        # Obtener la información de la cita seleccionada
        cita_actual = self.tree_citas.item(selected_item)['values']
        
        posponer_window = Toplevel(self)
        posponer_window.title("Posponer Cita")
        posponer_window.geometry("400x500")
        
        # Frame para el calendario en la ventana emergente
        frame_fecha = tk.Frame(posponer_window)
        frame_fecha.pack(padx=20, pady=20)
        
        label_fecha = tk.Label(frame_fecha, text="Selecciona una nueva fecha:")
        label_fecha.pack(pady=5)
        
        nuevo_calendario = Calendar(frame_fecha, selectmode="day", date_pattern="yyyy-mm-dd")
        nuevo_calendario.pack(pady=5, ipady=30, ipadx=30)
        
        # Frame para seleccionar la hora con combobox
        frame_hora = tk.Frame(posponer_window)
        frame_hora.pack(padx=10, pady=10)
        
        label_hora = tk.Label(frame_hora, text="Selecciona una nueva hora:")
        label_hora.pack(pady=5)
        
        horas = [f"{h:02d}:00" for h in range(7, 22)]  # Horas desde las 7:00 hasta las 21:00
        combobox_horas = ttk.Combobox(frame_hora, values=horas)
        combobox_horas.pack(pady=10)
        
        # Botón para guardar la nueva fecha y hora
        boton_guardar = tk.Button(posponer_window, text="Guardar", 
                                   command=lambda: self.guardar_nueva_cita(posponer_window, nuevo_calendario.get_date(), combobox_horas.get(), selected_item, cita_actual), 
                                   bg="#007FFF", fg="white", font=("Helvetica", 12))
        boton_guardar.pack(pady=20)

    def guardar_nueva_cita(self, ventana, nueva_fecha, nueva_hora, selected_item, cita_actual):
        # Comprobar si se ha seleccionado una hora
        if not nueva_hora:
            messagebox.showwarning("Advertencia", "Por favor, selecciona una nueva hora.")
            return

        # Actualizar el Treeview con la nueva fecha y hora
        self.tree_citas.item(selected_item, values=(nueva_hora, cita_actual[1], cita_actual[2]))  # Reemplazar solo la hora y mantener paciente y descripción
        
        # Cerrar la ventana emergente
        ventana.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = AgendaApp(master=root)
    app.pack(fill=tk.BOTH, expand=True)
    root.mainloop()