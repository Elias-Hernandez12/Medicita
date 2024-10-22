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
        self.orden_ascendente = True  # Variable para controlar el orden

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

        # Frame para la barra de búsqueda y el botón de orden
        self.search_frame = tk.Frame(self.historial_frame, bg="#ffffff")
        self.search_frame.pack(pady=10, padx=20, fill=tk.X)

        # Caja de texto para la búsqueda
        self.entry_buscar = tk.Entry(self.search_frame, font=("Helvetica", 14), fg="grey")
        self.entry_buscar.insert(0, "Buscar")  # Placeholder
        self.entry_buscar.bind("<FocusIn>", self.on_focus_in)  # Elimina el placeholder al hacer clic
        self.entry_buscar.bind("<FocusOut>", self.on_focus_out)  # Devuelve el placeholder si se pierde el foco
        self.entry_buscar.pack(side=tk.LEFT, padx=5, pady=5, fill=tk.X, expand=True)
        self.entry_buscar.bind("<KeyRelease>", self.buscar)

        # Botón para ordenar por fecha
        self.boton_ordenar = tk.Button(self.search_frame, text="Ordenar por Fecha", command=self.ordenar_por_fecha, font=("Helvetica", 14))
        self.boton_ordenar.pack(side=tk.RIGHT, padx=5, pady=5)

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
        self.citas = [
            ("20/10/2024", "10:00 AM", "Juan Pérez", "Consulta General"),
            ("19/10/2024", "02:00 PM", "María López", "Revisión de control"),
            ("18/10/2024", "09:00 AM", "Carlos García", "Chequeo Cardiológico")
        ]
        self.cargar_historial()

    def cargar_historial(self):
        # Limpiar el Treeview antes de cargar los datos
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Cargar las citas en el Treeview
        for cita in self.citas:
            self.tree.insert("", tk.END, values=cita)

    def buscar(self, event):
        query = self.entry_buscar.get().lower()
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Filtrar las citas basadas en el texto de búsqueda
        for cita in self.citas:
            if (query in cita[0].lower() or  # Filtrar por fecha
                query in cita[1].lower() or  # Filtrar por hora
                query in cita[2].lower() or  # Filtrar por paciente
                query in cita[3].lower()):    # Filtrar por descripción
                self.tree.insert("", tk.END, values=cita)

    def ordenar_por_fecha(self):
        self.orden_ascendente = not self.orden_ascendente  # Cambiar el estado de orden
        if self.orden_ascendente:
            self.citas.sort(key=lambda x: x[0])  # Orden ascendente
        else:
            self.citas.sort(key=lambda x: x[0], reverse=True)  # Orden descendente
        self.cargar_historial()

    def on_focus_in(self, event):
        if self.entry_buscar.get() == "Buscar":
            self.entry_buscar.delete(0, tk.END)
            self.entry_buscar.config(fg="black")

    def on_focus_out(self, event):
        if not self.entry_buscar.get():
            self.entry_buscar.insert(0, "Buscar")
            self.entry_buscar.config(fg="grey")

if __name__ == "__main__":
    root = tk.Tk()
    app = HistorialApp(master=root)
    app.pack(fill=tk.BOTH, expand=True)
    root.mainloop()
