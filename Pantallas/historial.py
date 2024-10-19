import tkinter as tk

def crear_frame(master, texto, tipo_relief):
    frame = tk.Frame(master, relief=tipo_relief, borderwidth=2, bg="#B2EBF2", padx=10, pady=10)
    frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
    label = tk.Label(frame, text=texto, bg="#B2EBF2")
    label.pack()

root = tk.Tk()
root.title("Ejemplo de Diferentes Reliefs")

# Crear diferentes frames con distintos tipos de relief
crear_frame(root, "Flat", tk.FLAT)
crear_frame(root, "Raised", tk.RAISED)
crear_frame(root, "Sunken", tk.SUNKEN)
crear_frame(root, "Groove", tk.GROOVE)
crear_frame(root, "Ridge", tk.RIDGE)
crear_frame(root, "Solid", tk.SOLID)

root.mainloop()
