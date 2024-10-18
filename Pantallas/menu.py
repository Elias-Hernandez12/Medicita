import tkinter as tk
from tkinter import font, PhotoImage, Label, Button

class MenuApp(tk.Frame):
    def __init__(self, root=None):
        super().__init__(root)
        self.root = root
        self.pack(fill=tk.BOTH, expand=True)
        self.configure(bg="#E0F7FA")  # Color de fondo para el Frame
        self.root.title("MediCitAa")
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
        self.btn_cerrar_sesion = Button(self, text="Cerrar sesión", command=self.cerrar_sesion, bg="black", fg="white", width=15, height=2, font=("arial", 14, "bold"), cursor="hand2")
        self.btn_cerrar_sesion.place(x=980, y=20)

        self.icono_perfil = PhotoImage(file="imagenes/usuario.png")
        self.btn_perfil = Button(self, image=self.icono_perfil , command=self.perfil, bg="#E0F7FA", fg="#000000", width=80, height=70, cursor="hand2", relief="flat", activebackground="#E0F7FA", highlightthickness=0, borderwidth=0)
        self.btn_perfil.place(x=1250, y=12)

        # Etiqueta para el título principal
        self.titulo_label = Label(self, text="Bienvenido a MediCita", font=("Helvetica",30 , "bold"), bg="#E0F7FA", fg="black")
        self.titulo_label.pack(pady=(150, 20))

        # Subtítulo
        self.subtitulo_label = Label(self, text="Selecciona una opción", font=self.subtitulo_font, bg="#E0F7FA", fg="gray")
        self.subtitulo_label.pack(pady=20)

        # Cuadro 1
        self.cuadro1 = tk.Frame(self, bg="white", bd=2, relief="groove", width=380, height=250)
        self.cuadro1.place(x=53, y=400)  # Ajustar el espaciado

        self.titulo1 = Label(self.cuadro1, text="Registrar Cita", font=self.subtitulo_font, bg="white")
        self.titulo1.pack(pady=5)

        self.icono1 = PhotoImage(file="imagenes/registrar-cita.png")
        self.boton_icono1 = Button(self.cuadro1, image=self.icono1, command=self.registrar_cita, bg="white", bd=0, cursor="hand2", activebackground="#ffffff", highlightthickness=0, borderwidth=0)
        self.boton_icono1.image = self.icono1  # Mantener una referencia a la imagen
        self.boton_icono1.pack(padx=20, pady=10)

        # Cuadro 2
        self.cuadro2 = tk.Frame(self, bg="white", bd=2, relief="groove", width=380, height=250)
        self.cuadro2.place(x=519, y=400)  # Ajustar el espaciado

        self.titulo2 = Label(self.cuadro2, text="Historial de Citas", font=self.subtitulo_font, bg="white")
        self.titulo2.pack(pady=5)

        self.icono2 = PhotoImage(file="imagenes/historial-de-citas.png")
        self.boton_icono2 = Button(self.cuadro2, image=self.icono2, command=self.historial, bg="white", bd=0, cursor="hand2", activebackground="#ffffff", highlightthickness=0, borderwidth=0)
        self.boton_icono2.image = self.icono2  # Mantener una referencia a la imagen
        self.boton_icono2.pack(padx=20, pady=10)

        # Cuadro 3
        self.cuadro3 = tk.Frame(self, bg="white", bd=2, relief="groove", width=380, height=250)
        self.cuadro3.place(x=986, y=400)  # Ajustar el espaciado

        self.titulo3 = Label(self.cuadro3, text="Agenda", font=self.subtitulo_font, bg="white")
        self.titulo3.pack(pady=5)

        self.icono3 = PhotoImage(file="imagenes/agenda.png")
        self.boton_icono3 = Button(self.cuadro3, image=self.icono3, command=self.agenda, bg="white", bd=0, cursor="hand2", activebackground="#ffffff", highlightthickness=0, borderwidth=0)
        self.boton_icono3.image = self.icono3  # Mantener una referencia a la imagen
        self.boton_icono3.pack(padx=20, pady=10)

        # Establecer un tamaño uniforme para los cuadros
        for cuadro in [self.cuadro1, self.cuadro2, self.cuadro3]:
            cuadro.pack_propagate(False)  # Desactivar el cambio de tamaño basado en el contenido

    def cerrar_sesion(self):
        print("cerrar sesión")  # Aquí puedes agregar la lógica para la pantalla de inicio de sesión

    def perfil(self):
        print("perfil")  # Aquí puedes agregar la lógica para la pantalla de registro
        
    def registrar_cita(self):
        print("registrar_cita")
    
    def historial(self):
        print("Historial de citas")
        
    def agenda(self):
        print("Agenda")
    
if __name__ == "__main__":
    root = tk.Tk()
    app = MenuApp(root)
    root.mainloop()

