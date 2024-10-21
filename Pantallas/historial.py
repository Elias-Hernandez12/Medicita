import tkinter as tk
from tkinter import PhotoImage, ttk

class HistorialApp(tk.Frame):
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
        self.label_titulo = tk.Label(self.header_frame, text="MediCita", font=("Helvetica", 28, "bold"), bg="#E0F7FA", fg="#007FFF")
        self.label_titulo.pack(side=tk.LEFT)

        # Frame principal para el contenido
        self.main_frame = tk.Frame(self, bg="#E0F7FA")
        self.main_frame.pack(padx=20, pady=20, fill=tk.BOTH, expand=True)

        # Botón para regresar al menú principal
        self.imagen = PhotoImage(file="imagenes/regresar.png")  # Asegúrate de tener esta imagen
        self.boton_regresar = tk.Button(self.main_frame, image=self.imagen, command=self.controlador.mostrar_menu, borderwidth=0, bg="#E0F7FA", activebackground="#E0F7FA")
        self.boton_regresar.place(x=10, y=30)

        # Frame para mostrar el historial
        self.historial_frame = tk.Frame(self.main_frame, bg="#ffffff", relief=tk.GROOVE, borderwidth=2)
        self.historial_frame.place(relx=0.5, rely=0.5, anchor="center", width=1150, height=690)

        # Título del historial
        self.label_historial = tk.Label(self.historial_frame, text="Historial de Citas", font=("Helvetica", 26, "bold"), bg="#ffffff", fg="black")
        self.label_historial.pack(pady=10)

        # Aquí puedes usar un Treeview para mostrar el historial en forma de tabla
        self.tree = ttk.Treeview(self.historial_frame, columns=("Fecha", "Hora", "Paciente", "Descripción"), show='headings', height=20)
        self.tree.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        # Definir las columnas
        self.tree.heading("Fecha", text="Fecha")
        self.tree.heading("Hora", text="Hora")
        self.tree.heading("Paciente", text="Paciente")
        self.tree.heading("Descripción", text="Descripción")

        # Ajustar el ancho de las columnas
        self.tree.column("Fecha", width=150, anchor="center")
        self.tree.column("Hora", width=150, anchor="center")
        self.tree.column("Paciente", width=200, anchor="center")
        self.tree.column("Descripción", width=300, anchor="center")

        # Cargar datos de ejemplo
        self.cargar_historial()

    def cargar_historial(self):
        # Ejemplo de cómo añadir elementos al Treeview (podrías cargar los datos de una base de datos aquí)
        citas = [
            ("20/10/2024", "10:00 AM", "Juan Pérez", "Consulta General"),
            ("19/10/2024", "02:00 PM", "María López", "Revisión de control"),
            ("18/10/2024", "09:00 AM", "Carlos García", "Chequeo Cardiológico")
        ]
        for cita in citas:
            self.tree.insert("", tk.END, values=cita)