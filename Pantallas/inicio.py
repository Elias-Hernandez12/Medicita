import tkinter as tk
from tkinter import font, PhotoImage, Label, Button

class InicioApp(tk.Frame):
    def __init__(self, root=None):
        super().__init__(root)
        self.root = root
        self.pack(fill=tk.BOTH, expand=True)
        self.configure(bg="#E0F7FA")  # Color de fondo para el Frame
        self.root.title("MediCita")
        self.root.geometry("1420x800")
        self.create_widgets()

    def create_widgets(self):
       
        # Configuración de fuentes
        self.subtitulo_font = font.Font(family="Helvetica", size=25, weight="bold")
        self.texto_cuadro_font = font.Font(family="Helvetica", size=14)

        # Etiqueta para el nombre del programa como header
        self.app_label = Label(self, text="MediCita", font=("Helvetica", 28, "bold"), bg="#E0F7FA", fg="#007FFF")
        self.app_label.place(x=30, y=20)

        # Botones de iniciar sesión y registrarse
        self.btn_iniciar_sesion = Button(self, text="Iniciar sesión", command=self.iniciar_sesion, bg="white", fg="black", width=15, height=2, font=("arial", 14, "bold"), cursor="hand2")
        self.btn_iniciar_sesion.place(x=1150, y=20)

        self.btn_registrarse = Button(self, text="Registrarse", command=self.registrarse, bg="black", fg="white", width=15, height=2, font=("arial", 14, "bold"), cursor="hand2")
        self.btn_registrarse.place(x=900, y=20)

        # Etiqueta para el título principal
        self.titulo_label = Label(self, text="Bienvenido a MediCita", font=("Helvetica",30 , "bold"), bg="#E0F7FA", fg="black")
        self.titulo_label.pack(pady=(150, 20))

        # Subtítulo
        self.subtitulo_label = Label(self, text="Tu gestor de citas", font=self.subtitulo_font, bg="#E0F7FA", fg="gray")
        self.subtitulo_label.pack(pady=20)

        # Cuadro 1
        self.cuadro1 = tk.Frame(self, bg="white", bd=2, relief="groove", width=380, height=250)
        self.cuadro1.place(x=53, y=400)  # Ajustar el espaciado

        self.titulo1 = Label(self.cuadro1, text="Fácil de usar", font=self.subtitulo_font, bg="white")
        self.titulo1.pack(pady=5)

        self.icono1 = PhotoImage(file="imagenes/chasquido.png")
        self.etiqueta_icono1 = Label(self.cuadro1, image=self.icono1, bg="white")
        self.etiqueta_icono1.image = self.icono1  # Mantener una referencia a la imagen
        self.etiqueta_icono1.pack(padx=20, pady=10)

        self.descripcion1 = Label(self.cuadro1, text="Programa tus citas con pocos clics", font=self.texto_cuadro_font, bg="white")
        self.descripcion1.pack(pady=5)

        # Cuadro 2
        self.cuadro2 = tk.Frame(self, bg="white", bd=2, relief="groove", width=380, height=250)
        self.cuadro2.place(x=519, y=400)  # Ajustar el espaciado

        self.titulo2 = Label(self.cuadro2, text="Disponible 24/7", font=self.subtitulo_font, bg="white")
        self.titulo2.pack(pady=5)

        self.icono2 = PhotoImage(file="imagenes/24-7.png")
        self.etiqueta_icono2 = Label(self.cuadro2, image=self.icono2, bg="white")
        self.etiqueta_icono2.image = self.icono2  # Mantener una referencia a la imagen
        self.etiqueta_icono2.pack(padx=20, pady=10)

        self.descripcion2 = Label(self.cuadro2, text="Accede a tu calendario de citas siempre", font=self.texto_cuadro_font, bg="white")
        self.descripcion2.pack(pady=5)

        # Cuadro 3
        self.cuadro3 = tk.Frame(self, bg="white", bd=2, relief="groove", width=380, height=250)
        self.cuadro3.place(x=986, y=400)  # Ajustar el espaciado

        self.titulo3 = Label(self.cuadro3, text="Recordatorios", font=self.subtitulo_font, bg="white")
        self.titulo3.pack(pady=5)

        self.icono3 = PhotoImage(file="imagenes/recordatorio.png")
        self.etiqueta_icono3 = Label(self.cuadro3, image=self.icono3, bg="white")
        self.etiqueta_icono3.image = self.icono3  # Mantener una referencia a la imagen
        self.etiqueta_icono3.pack(padx=20, pady=10)

        self.descripcion3 = Label(self.cuadro3, text="Recibe notificaciones", font=self.texto_cuadro_font, bg="white")
        self.descripcion3.pack(pady=5)

        # Establecer un tamaño uniforme para los cuadros
        for cuadro in [self.cuadro1, self.cuadro2, self.cuadro3]:
            cuadro.pack_propagate(False)  # Desactivar el cambio de tamaño basado en el contenido

    def iniciar_sesion(self):
        print("Iniciar sesión")  # Aquí puedes agregar la lógica para la pantalla de inicio de sesión

    def registrarse(self):
        print("Registrarse")  # Aquí puedes agregar la lógica para la pantalla de registro

