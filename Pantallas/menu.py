import tkinter as tk
from tkinter import PhotoImage

class MenuApp(tk.Frame):
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

        # Botón de perfil con imagen
        self.boton_perfil_imagen = PhotoImage(file="imagenes/usuario.png")  # Asegúrate de que la ruta sea correcta
        self.boton_perfil = tk.Button(self.header_frame, image=self.boton_perfil_imagen, command=self.perfil, bg="#E0F7FA", borderwidth=0, activebackground="#E0F7FA")
        self.boton_perfil.pack(side=tk.RIGHT, padx=(20, 10))

        # Botón de cerrar sesión
        self.boton_cerrar_sesion = tk.Button(self.header_frame, text="Cerrar sesión", font=("Helvetica", 18, "bold"), command=self.cerrar_sesion, width=12, height=2, bg="#332a2a", fg="white", cursor="hand2")
        self.boton_cerrar_sesion.pack(side=tk.RIGHT, padx=(10, 20))

        # Frame principal para el contenido
        self.main_frame = tk.Frame(self, bg="#E0F7FA")
        self.main_frame.pack(padx=20, pady=20, fill=tk.BOTH, expand=True)

        # Label de bienvenida
        self.label_bienvenida = tk.Label(self.main_frame, text="Bienvenido a Medicita", font=("Helvetica", 28, "bold"), bg="#E0F7FA", fg="black")
        self.label_bienvenida.pack(pady=(20, 20))

        # Label de gestor de citas
        self.label_gestor = tk.Label(self.main_frame, text="Tu gestor de citas", font=("Helvetica", 22, "bold"), bg="#E0F7FA", fg="#8a8d8e")
        self.label_gestor.pack(pady=(10, 70))

        # Frame para los 3 elementos
        self.frames_row = tk.Frame(self.main_frame, bg="#E0F7FA")
        self.frames_row.pack(fill=tk.X)

        # Crear 3 frames en una fila
        self.create_frame(self.frames_row, "Registrar cita", "imagenes/registrar-cita.png", self.registrar_cita)
        self.create_frame(self.frames_row, "Historial de citas", "imagenes/historial-de-citas.png", self.historial_citas)
        self.create_frame(self.frames_row, "Agenda", "imagenes/agenda.png", self.agenda)

    def create_frame(self, parent, title, image_path, command):
        # Crear un frame
        frame = tk.Frame(parent, bg="#ffffff", relief=tk.GROOVE, borderwidth=2)
        frame.pack(side=tk.LEFT, padx=(10, 10), pady=(30, 30), fill=tk.BOTH, expand=True)

        # Título en el frame
        label_title = tk.Label(frame, text=title, font=("Helvetica", 28, "bold"), bg="#ffffff")
        label_title.pack(pady=(10, 10))

        # Botón que muestra la imagen
        button_image = PhotoImage(file=image_path)  # Carga la imagen
        boton_imagen = tk.Button(frame, image=button_image, command=command, bg="#ffffff", borderwidth=0)
        boton_imagen.pack(pady=(10, 50))
        boton_imagen.image = button_image  # Mantener una referencia a la imagen

    def registrar_cita(self):
        print("Registrar cita...")  # Lógica para registrar cita

    def historial_citas(self):
        print("Historial de citas...")  # Lógica para mostrar historial de citas

    def agenda(self):
        print("Mostrar agenda...")  # Lógica para mostrar la agenda
        
    def perfil(self):
        # Aquí puedes definir la lógica para el perfil
        print("Registro...")  # Este es un ejemplo

    def cerrar_sesion(self):
        # Aquí puedes definir la lógica para cerrar sesión
        print("Iniciar sesión...")  # Este es un ejemplo

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Medicita")  # Título de la ventana
    root.iconbitmap("imagenes/chequeo.ico")  # Cambia esto a la ruta correcta de tu icono

    app = MenuApp(master=root)
    app.pack(fill=tk.BOTH, expand=True)

    root.mainloop()
