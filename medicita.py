import tkinter as tk
from Pantallas.inicio import InicioApp

def main():
    root = tk.Tk()
    root.title("Medicita")
    root.iconbitmap("imagenes\chequeo.ico")
    root.resizable(1,1)
    
    inicio_app = InicioApp(root)
    inicio_app.pack(fill=tk.BOTH, expand=True)
    
    root.mainloop()

if __name__ == "__main__":
    main()