import tkinter as tk
from tkinter import Label, Button

class InicioApp(tk.Frame):
    def __init__(self, root=None):
        super().__init__(root, width=1420, height=800)
        self.grid()  # Coloca el marco en el root
        root.geometry("1420x800")  # Establece el tamaño de la ventana
        root.configure(bg="#E0F7FA")  # Establece el color de fondo de la ventana principal
        self.configure(bg="#E0F7FA")  # Establece el color de fondo del Frame

        # Configura el espaciado entre las columnas
        for col in range(5):  # Columnas 0 a 4
            self.grid_columnconfigure(col, weight=1)  # Permite que todas las columnas se expandan

        self.crear_widgets()  # Llama al método para crear widgets
        
    def crear_widgets(self):
        # Titulo del programa
        self.lbl_titulo = Label(self, text="MediCita", font=("Helvetica", 28, "bold"), bg="#E0F7FA", fg="#007FFF")
        self.lbl_titulo.grid(row=0, column=0, padx=20, pady=10, sticky="w")  # Columna 0, alineado a la izquierda

        # Botones de Registrarse y Iniciar sesión
        self.btn_registrarse = Button(self, text="Regístrate", font=("Helvetica", 14), bg="black", fg="white", width=15, height=2, command=self.registrarse, relief="flat", cursor="hand2", bd=2)
        self.btn_registrarse.grid(row=0, column=3, padx=10, pady=10, sticky="e")  # Columna 3, alineado a la derecha
        
        self.btn_iniciar_sesion = Button(self, text="Inicia Sesión", font=("Helvetica", 14), bg="white", fg="black", width=15, height=2 ,command=self.iniciar_sesion, relief="flat", cursor="hand2", bd=2)
        self.btn_iniciar_sesion.grid(row=0, column=4, padx=10, pady=10, sticky="e")  # Columna 4, alineado a la derecha

        # Subtítulo centrado en columnas 1 y 2
        self.lbl_subtitulo = Label(self, text="Bienvenido a MediCita", font=("Helvetica", 28, "bold"), bg="#E0F7FA", fg="black")
        self.lbl_subtitulo.grid(row=1, column=0, columnspan=4, padx=(430, 350), pady=10, sticky="ew")  # Columna 1 y 2, centrado
        
        # Frames con imágenes y descripción
        self.frame_facil = tk.Frame(self, bg="lightgray")
        self.frame_facil.grid(row=4, column=0, columnspan=1, padx=10, pady=40, sticky="nsew")

        self.frame_disponible = tk.Frame(self, bg="lightblue")
        self.frame_disponible.grid(row=4, column=2, columnspan=1, padx=10, pady=40, sticky="nsew")

        self.frame_recordatorio = tk.Frame(self, bg="lightgreen")
        self.frame_recordatorio.grid(row=4, column=4, columnspan=1, padx=10, pady=40, sticky="nsew")

        # Puedes agregar más widgets a los frames aquí si lo deseas
        self.lbl_facil = Label(self.frame_facil, text="Fácil", font=("Helvetica", 20), bg="lightgray")
        self.lbl_facil.pack(padx=20, pady=20)

        self.lbl_disponible = Label(self.frame_disponible, text="Moderado", font=("Helvetica", 20), bg="lightblue")
        self.lbl_disponible.pack(padx=20, pady=20)

        self.lbl_recordatorio = Label(self.frame_recordatorio, text="Difícil", font=("Helvetica", 20), bg="lightgreen")
        self.lbl_recordatorio.pack(padx=20, pady=20)

    def iniciar_sesion(self):
        pass

    def registrarse(self):
        pass

# Creamos la ejecución del programa
root = tk.Tk()
app = InicioApp(root)
root.mainloop()
