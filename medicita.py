import tkinter as tk
from controlador import Controlador 

def main():
    root = tk.Tk()
    root.title("Medicita")
    root.iconbitmap(r"imagenes\chequeo.ico")
    root.resizable(1,1)
    root.geometry("1420x800")
    root.minsize(1420, 800)
    
    controlador = Controlador(master=root) 
    root.mainloop()

if __name__ == "__main__":
    main()