import tkinter as tk
from tkinter import ttk

class HistorialApp(tk.Tk):
    def __init__(self, controlador=None):
        super().__init__()
        self.controlador = controlador
        self.geometry("400x300")
        self.title("Selector de Hora")

        # Frame para los Combobox
        self.frame_combobox = tk.Frame(self)
        self.frame_combobox.pack(pady=20)

        # Combobox para la hora
        self.combo_hora = ttk.Combobox(self.frame_combobox, values=[f"{i:02d}" for i in range(1, 13)], width=5)
        self.combo_hora.grid(row=0, column=0, padx=0)
        self.combo_hora.set("01")  # Valor por defecto
        self.combo_hora.bind("<<ComboboxSelected>>", self.mostrar_hora)  # Evento al seleccionar

        # Combobox para los minutos
        self.combo_minutos = ttk.Combobox(self.frame_combobox, values=[f"{i:02d}" for i in range(0, 60)], width=5)
        self.combo_minutos.grid(row=0, column=1, padx=0)
        self.combo_minutos.set("00")  # Valor por defecto
        self.combo_minutos.bind("<<ComboboxSelected>>", self.mostrar_hora)  # Evento al seleccionar

        # Combobox para AM/PM
        self.combo_am_pm = ttk.Combobox(self.frame_combobox, values=["AM", "PM"], width=5)
        self.combo_am_pm.grid(row=0, column=2, padx=0)
        self.combo_am_pm.set("AM")  # Valor por defecto
        self.combo_am_pm.bind("<<ComboboxSelected>>", self.mostrar_hora)  # Evento al seleccionar

    def mostrar_hora(self, event=None):
        hora = self.combo_hora.get()
        minutos = self.combo_minutos.get()
        am_pm = self.combo_am_pm.get()
        print(f"Hora seleccionada: {hora}:{minutos} {am_pm}")

if __name__ == "__main__":
    app = HistorialApp()
    app.mainloop()
