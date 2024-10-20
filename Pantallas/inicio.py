import tkinter as tk
from tkinter import PhotoImage

class InicioApp(tk.Frame):
    def __init__(self, master=None, controlador=None):
        super().__init__(master)
        master.geometry("1420x800")
        master.minsize(1420, 800)
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

        # Botón de registrarse
        self.boton_registrarse = tk.Button(self.header_frame, text="Registrarse", font=("Helvetica", 18, "bold"), command=self.controlador.mostrar_registrarse, width=12, height=2, bg="black", fg="white", cursor="hand2")
        self.boton_registrarse.pack(side=tk.RIGHT, padx=(10, 10))

        # Botón de iniciar sesión
        self.boton_iniciar_sesion = tk.Button(self.header_frame, text="Iniciar sesión", font=("Helvetica", 18, "bold"), command=self.controlador.mostrar_iniciar_sesion, width=12, height=2, bg="white", fg="black", cursor="hand2")
        self.boton_iniciar_sesion.pack(side=tk.RIGHT, padx=(10, 20))

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
        self.create_frame(self.frames_row, "Fácil de usar", "Programa tus citas con pocos clics", "imagenes/chasquido.png")
        self.create_frame(self.frames_row, "Disponible 24/7", "Accede a tu calendario de citas siempre", "imagenes/24-7.png")
        self.create_frame(self.frames_row, "Recordatorios", "Recibe notificaciones", "imagenes/recordatorio.png")

    def create_frame(self, parent, title, subtitle, image_path):
        # Crear un frame
        frame = tk.Frame(parent, bg="#ffffff", relief=tk.GROOVE, borderwidth=2)
        frame.pack(side=tk.LEFT, padx=(10, 10), pady=(30, 30), fill=tk.BOTH, expand=True)

        # Título en el frame
        label_title = tk.Label(frame, text=title, font=("Arial", 16), bg="#ffffff")
        label_title.pack(pady=(10, 5))

        # Mostrar la imagen usando un Label
        image_label = tk.Label(frame, bg="#ffffff")
        image_label.pack(pady=(0, 5))

        button_image = PhotoImage(file=image_path)  # Cambia esta ruta a tu imagen
        image_label.config(image=button_image)  # Configura el Label para mostrar la imagen
        image_label.image = button_image  # Mantener una referencia a la imagen

        # Subtítulo en el frame
        label_subtitle = tk.Label(frame, text=subtitle, font=("Arial", 12), bg="#ffffff")
        label_subtitle.pack(pady=(5, 10))
        
    def registrarse(self):
        pass

    def iniciar_sesion(self):
        pass
        
if __name__ == "__main__":
    root = tk.Tk()
    controlador = Controlador(master=root)
    root.mainloop()