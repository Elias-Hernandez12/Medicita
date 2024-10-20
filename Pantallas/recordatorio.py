import tkinter as tk

class Aplicacion(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Ejemplo de Formulario de Matrícula")
        self.geometry("400x400")
        
        # Crear el frame principal
        self.frame_principal = FramePrincipal(self)
        self.frame_principal.pack(fill=tk.BOTH, expand=True)

class FramePrincipal(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg="#E0F7FA")
        self.label = tk.Label(self, text="Bienvenido al Sistema de Matrícula", font=("Helvetica", 16), bg="#E0F7FA")
        self.label.pack(pady=20)
        
        # Botón para abrir el formulario de matrícula
        self.boton_abrir = tk.Button(self, text="Abrir Formulario de Matrícula", command=self.abrir_formulario)
        self.boton_abrir.pack(pady=10)

    def abrir_formulario(self):
        # Crear una nueva instancia de Formulario y mostrarla
        self.formulario = Formulario(self.master)
        self.formulario.grab_set()  # Deshabilitar la ventana principal hasta que se cierre el formulario

class Formulario(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Formulario de Matrícula")
        self.geometry("300x400")
        self.configure(bg="#ffffff")

        # Etiqueta y entrada para el nombre
        self.label_nombre = tk.Label(self, text="Nombre:", font=("Helvetica", 12), bg="#ffffff")
        self.label_nombre.pack(pady=10)
        self.entry_nombre = tk.Entry(self)
        self.entry_nombre.pack(pady=5)

        # Etiqueta y entrada para el apellido
        self.label_apellido = tk.Label(self, text="Apellido:", font=("Helvetica", 12), bg="#ffffff")
        self.label_apellido.pack(pady=10)
        self.entry_apellido = tk.Entry(self)
        self.entry_apellido.pack(pady=5)

        # Etiqueta y entrada para el correo electrónico
        self.label_correo = tk.Label(self, text="Correo Electrónico:", font=("Helvetica", 12), bg="#ffffff")
        self.label_correo.pack(pady=10)
        self.entry_correo = tk.Entry(self)
        self.entry_correo.pack(pady=5)

        # Etiqueta y entrada para el número de teléfono
        self.label_telefono = tk.Label(self, text="Teléfono:", font=("Helvetica", 12), bg="#ffffff")
        self.label_telefono.pack(pady=10)
        self.entry_telefono = tk.Entry(self)
        self.entry_telefono.pack(pady=5)

        # Botón para guardar la información
        self.boton_guardar = tk.Button(self, text="Guardar", command=self.guardar)
        self.boton_guardar.pack(pady=20)

        # Botón para cerrar el formulario
        self.boton_cerrar = tk.Button(self, text="Cerrar", command=self.cerrar)
        self.boton_cerrar.pack(pady=5)

    def guardar(self):
        # Aquí puedes agregar la lógica para guardar la información
        nombre = self.entry_nombre.get()
        apellido = self.entry_apellido.get()
        correo = self.entry_correo.get()
        telefono = self.entry_telefono.get()
        print(f"Guardando información: Nombre: {nombre}, Apellido: {apellido}, Correo: {correo}, Teléfono: {telefono}")
        self.cerrar()  # Cerrar el formulario después de guardar

    def cerrar(self):
        self.destroy()  # Cerrar el formulario

if __name__ == "__main__":
    app = Aplicacion()
    app.mainloop()
