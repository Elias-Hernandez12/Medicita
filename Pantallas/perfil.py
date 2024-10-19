import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk, ImageDraw

class PerfilRedondoApp(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.configure(bg="#E0F7FA")
        self.create_widgets()

    def create_widgets(self):
        # Botón para cargar una imagen
        self.boton_cargar_imagen = tk.Button(self, text="Cargar Imagen", command=self.cargar_imagen)
        self.boton_cargar_imagen.pack(pady=20)

        # Label para mostrar la imagen
        self.label_imagen = tk.Label(self)
        self.label_imagen.pack(pady=20)

    def cargar_imagen(self):
        # Abrir un cuadro de diálogo para seleccionar un archivo
        archivo_imagen = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.gif")])
        if archivo_imagen:
            # Cargar la imagen usando Pillow
            imagen_pillow = Image.open(archivo_imagen)
            imagen_redonda = self.recortar_a_circulo(imagen_pillow)
            self.imagen = ImageTk.PhotoImage(imagen_redonda)
            self.label_imagen.configure(image=self.imagen)
            self.label_imagen.image = self.imagen  # Mantener una referencia a la imagen

    def recortar_a_circulo(self, imagen):
        # Obtener el tamaño más pequeño entre ancho y alto
        min_dimension = min(imagen.size)

        # Crear una imagen cuadrada
        imagen_cuadrada = imagen.resize((min_dimension, min_dimension), Image.LANCZOS)  # Cambiado a Image.LANCZOS

        # Crear una máscara circular
        mascara = Image.new('L', (min_dimension, min_dimension), 0)
        draw = ImageDraw.Draw(mascara)
        draw.ellipse((0, 0, min_dimension, min_dimension), fill=255)

        # Aplicar la máscara a la imagen cuadrada
        imagen_redonda = Image.new('RGBA', (min_dimension, min_dimension))
        imagen_redonda.paste(imagen_cuadrada, (0, 0), mascara)

        return imagen_redonda

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Perfil Redondo")
    app = PerfilRedondoApp(master=root)
    app.pack(fill=tk.BOTH, expand=True)
    root.mainloop()
