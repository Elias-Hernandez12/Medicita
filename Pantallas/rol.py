import tkinter as tk
from tkinter import PhotoImage

class RolApp(tk.Frame):
    def __init__(self, master=None, controlador=None):
        super().__init__(master)
        self.controlador = controlador
        master.geometry("1420x800")
        master.minsize(1420, 800)
        self.configure(bg="#E0F7FA")
        self.create_widgets()

    def create_widgets(self):
        self.header_frame = tk.Frame(self, bg="#E0F7FA")
        self.header_frame.pack(padx=20, pady=10, fill=tk.X)

        self.label_titulo = tk.Label(self.header_frame, text="MediCita", font=("Helvetica", 28, "bold"), bg="#E0F7FA", fg="#007FFF")
        self.label_titulo.pack(side=tk.LEFT)

        self.main_frame = tk.Frame(self, bg="#E0F7FA")
        self.main_frame.pack(padx=20, pady=20, fill=tk.BOTH, expand=True)
        
        self.imagen = PhotoImage(file=r"imagenes\regresar.png")
        self.boton_regresar = tk.Button(self.main_frame, image=self.imagen, command=self.controlador.mostrar_inicio, borderwidth=0, bg="#E0F7FA", activebackground="#E0F7FA")
        self.boton_regresar.place(x=80, y=30)

        self.label_instrucciones = tk.Label(self.main_frame, text="Selecciona tu rol para registrarte:", font=("Helvetica", 22, "bold"), bg="#E0F7FA", fg="black")
        self.label_instrucciones.pack(pady=(20, 20))

        self.btn_paciente = tk.Button(self.main_frame, text="Paciente", font=("Helvetica", 18, "bold"), command=self.registrar_paciente, width=12, height=2, bg="#007FFF", fg="white", cursor="hand2")
        self.btn_paciente.pack(pady=10)

        self.btn_doctor = tk.Button(self.main_frame, text="Doctor", font=("Helvetica", 18, "bold"), command=self.registrar_doctor, width=12, height=2, bg="#007FFF", fg="white", cursor="hand2")
        self.btn_doctor.pack(pady=10)

    def registrar_paciente(self):
        self.controlador.mostrar_registrar_paciente()  

    def registrar_doctor(self):
        self.controlador.mostrar_registrar_doctor()
