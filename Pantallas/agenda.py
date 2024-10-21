import tkinter as tk
from tkinter import PhotoImage, ttk
from tkcalendar import Calendar  # Asegúrate de tener instalado tkcalendar

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
        self.label_titulo = tk.Label(self.header_frame, text="Agenda de Citas", font=("Helvetica", 28, "bold"), bg="#E0F7FA", fg="#007FFF")
        self.label_titulo.pack(side=tk.LEFT)

        # Frame principal que contiene ambos subframes (calendario y citas)
        self.main_frame = tk.Frame(self, bg="#ffffff", relief=tk.GROOVE, borderwidth=2)
        self.main_frame.place(relx=0.5, rely=0.5, anchor="center", width=1050, height=750)

        # Frame izquierdo para el calendario
        self.calendario_frame = tk.Frame(self.main_frame, bg="#E0F7FA", relief=tk.GROOVE, borderwidth=2)
        self.calendario_frame.place(x=10, y=10, width=500, height=730)

        # Título para el calendario
        self.label_calendario = tk.Label(self.calendario_frame, text="Seleccionar Fecha", font=("Helvetica", 22, "bold"), bg="#E0F7FA", fg="black")
        self.label_calendario.pack(pady=10)

        # Calendario
        self.calendario = Calendar(self.calendario_frame, selectmode='day', date_pattern='dd/mm/yyyy')
        self.calendario.pack(padx=20, pady=20)

        # Botón para mostrar citas de la fecha seleccionada
        self.boton_mostrar_citas = tk.Button(self.calendario_frame, text="Mostrar Citas", command=self.mostrar_citas_para_fecha)
        self.boton_mostrar_citas.pack(pady=10)

        # Frame derecho para mostrar las citas
        self.citas_frame = tk.Frame(self.main_frame, bg="#E0F7FA", relief=tk.GROOVE, borderwidth=2)
        self.citas_frame.place(x=530, y=10, width=500, height=730)

        # Título para las citas
        self.label_citas = tk.Label(self.citas_frame, text="Citas Programadas", font=("Helvetica", 22, "bold"), bg="#E0F7FA", fg="black")
        self.label_citas.pack(pady=10)

        # Treeview para mostrar las citas
        self.tree = ttk.Treeview(self.citas_frame, columns=("Hora", "Paciente", "Descripción"), show='headings', height=15)
        self.tree.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        # Definir las columnas
        self.tree.heading("Hora", text="Hora")
        self.tree.heading("Paciente", text="Paciente")
        self.tree.heading("Descripción", text="Descripción")

        # Ajustar el ancho de las columnas
        self.tree.column("Hora", width=150, anchor="center")
        self.tree.column("Paciente", width=200, anchor="center")
        self.tree.column("Descripción", width=300, anchor="center")

        # Botones de Cancelar y Posponer
        self.boton_cancelar = tk.Button(self.citas_frame, text="Cancelar Cita", command=self.cancelar_cita)
        self.boton_cancelar.pack(side=tk.LEFT, padx=20, pady=10)

        self.boton_posponer = tk.Button(self.citas_frame, text="Posponer Cita", command=self.posponer_cita)
        self.boton_posponer.pack(side=tk.RIGHT, padx=20, pady=10)

        # Cargar citas de ejemplo
        self.cargar_citas("20/10/2024")  # Cargar citas para una fecha por defecto

    def mostrar_citas_para_fecha(self):
        # Obtener la fecha seleccionada del calendario
        fecha_seleccionada = self.calendario.get_date()
        self.cargar_citas(fecha_seleccionada)

    def cargar_citas(self, fecha):
        # Limpiar el Treeview antes de cargar nuevas citas
        for row in self.tree.get_children():
            self.tree.delete(row)

        # Ejemplo de citas programadas por fecha (esto puede provenir de una base de datos)
        citas = {
            "20/10/2024": [("09:00 AM", "Laura Mendoza", "Consulta Nutricional")],
            "21/10/2024": [("10:00 AM", "Pedro Fernández", "Examen de laboratorio")],
            "22/10/2024": [("11:00 AM", "Ana Castillo", "Terapia Física")],
        }

        # Obtener citas para la fecha seleccionada, si existen
        citas_para_fecha = citas.get(fecha, [])
        
        # Insertar citas en el Treeview
        for cita in citas_para_fecha:
            self.tree.insert("", tk.END, values=cita)

    def cancelar_cita(self):
        # Obtener la cita seleccionada y realizar la acción de cancelarla
        selected_item = self.tree.selection()
        if selected_item:
            self.tree.delete(selected_item)
            # Aquí puedes añadir la lógica para cancelar la cita en la base de datos o sistema de almacenamiento
            print("Cita cancelada")

    def posponer_cita(self):
        # Obtener la cita seleccionada y realizar la acción de posponerla
        selected_item = self.tree.selection()
        if selected_item:
            print("Posponer lógica aquí")
            # Aquí puedes añadir la lógica para posponer la cita
