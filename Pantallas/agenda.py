import wx
import calendar
from datetime import datetime

class ElegantCalendar(wx.Frame):
    def __init__(self):
        super().__init__(None, title="Calendario Elegante", size=(800, 600))
        
        # Configuración inicial para el mes y año actuales
        self.current_year = datetime.now().year
        self.current_month = datetime.now().month

        # Crear un panel principal
        panel = wx.Panel(self)
        panel.SetBackgroundColour("#F5F5F5")  # Fondo suave

        # Crear un sizer vertical
        main_sizer = wx.BoxSizer(wx.VERTICAL)

        # Crear un sizer horizontal para la cabecera (mes/año) y los botones de navegación
        header_sizer = wx.BoxSizer(wx.HORIZONTAL)

        # Botones de navegación
        self.prev_button = wx.Button(panel, label="<", size=(50, 30))
        self.prev_button.SetForegroundColour("#ffffff")
        self.prev_button.SetBackgroundColour("#3F51B5")
        self.prev_button.Bind(wx.EVT_BUTTON, self.cambiar_mes_anterior)
        header_sizer.Add(self.prev_button, 0, wx.ALL, 10)

        # Crear el encabezado con el mes y año
        self.header = wx.StaticText(panel, label=self.obtener_mes_anio_espanol())
        header_font = wx.Font(18, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD)
        self.header.SetFont(header_font)
        header_sizer.Add(self.header, 0, wx.CENTER | wx.ALL, 10)

        # Botón para cambiar al siguiente mes
        self.next_button = wx.Button(panel, label=">", size=(50, 30))
        self.next_button.SetForegroundColour("#ffffff")
        self.next_button.SetBackgroundColour("#3F51B5")
        self.next_button.Bind(wx.EVT_BUTTON, self.cambiar_mes_siguiente)
        header_sizer.Add(self.next_button, 0, wx.ALL, 10)

        # Agregar el sizer de la cabecera al sizer principal
        main_sizer.Add(header_sizer, 0, wx.CENTER)

        # Crear la cuadrícula de días
        self.calendar_grid = wx.GridSizer(7, 7, 10, 10)

        # Crear los nombres abreviados de los días en español (una vez)
        self.crear_dias_semana(panel)

        # Crear los botones de los días del mes actual
        self.crear_dias(panel)

        # Agregar la cuadrícula al sizer principal
        main_sizer.Add(self.calendar_grid, 1, wx.EXPAND | wx.ALL, 10)

        # Configurar el sizer del panel principal
        panel.SetSizer(main_sizer)

        # Mostrar la ventana
        self.Show()

    def obtener_mes_anio_espanol(self):
        """Devuelve el nombre del mes y el año en español."""
        meses_espanol = [
            "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
            "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"
        ]
        return f"{meses_espanol[self.current_month - 1]} {self.current_year}"

    def crear_dias_semana(self, panel):
        """Crea los nombres abreviados de los días de la semana en español."""
        dias_semana_espanol = ["Lun", "Mar", "Mié", "Jue", "Vie", "Sáb", "Dom"]
        for dia in dias_semana_espanol:
            dia_label = wx.StaticText(panel, label=dia)
            dia_label.SetFont(wx.Font(14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))
            dia_label.SetForegroundColour("#616161")
            self.calendar_grid.Add(dia_label, 0, wx.CENTER)

    def crear_dias(self, panel):
        """Crea los botones para los días del mes actual, incluyendo los días del mes anterior y posterior."""
        # Limpiar la cuadrícula antes de agregar nuevos días, pero mantener los nombres de los días de la semana
        children = self.calendar_grid.GetChildren()
        if len(children) > 7:  # Mantener los primeros 7 (los días de la semana)
            for child in children[7:]:
                child.GetWindow().Destroy()  # Elimina el widget pero deja el layout intacto

        # Obtener el primer día del mes actual y cuántos días tiene
        cal = calendar.Calendar()
        dias_mes = list(cal.itermonthdays(self.current_year, self.current_month))

        # Obtener la cantidad de días del mes anterior
        if self.current_month == 1:
            dias_mes_anterior = calendar.monthrange(self.current_year - 1, 12)[1]
        else:
            dias_mes_anterior = calendar.monthrange(self.current_year, self.current_month - 1)[1]

        # Iterar y agregar los días al calendario
        for i, dia in enumerate(dias_mes):
            if dia == 0:  # Si es un día del mes anterior o posterior
                dia_label = wx.StaticText(panel, label=str(dias_mes_anterior - (len(dias_mes) - i) + 1), size=(50, 50))
                dia_label.SetFont(wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL))
                dia_label.SetForegroundColour("#9E9E9E")  # Color gris oscuro para los días fuera del mes
                self.calendar_grid.Add(dia_label, 0, wx.CENTER)
            else:
                boton_dia = wx.Button(panel, label=str(dia), size=(50, 50))
                boton_dia.SetFont(wx.Font(14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))
                boton_dia.SetForegroundColour("#ffffff")  # Texto blanco
                boton_dia.SetBackgroundColour("#03A9F4")  # Azul claro para los días del mes actual
                self.calendar_grid.Add(boton_dia, 0, wx.CENTER)
        
        # Actualizar el layout
        self.calendar_grid.Layout()

    def cambiar_mes_anterior(self, event):
        """Maneja el evento de cambiar al mes anterior."""
        if self.current_month == 1:
            self.current_month = 12
            self.current_year -= 1
        else:
            self.current_month -= 1
        self.actualizar_calendario()

    def cambiar_mes_siguiente(self, event):
        """Maneja el evento de cambiar al siguiente mes."""
        if self.current_month == 12:
            self.current_month = 1
            self.current_year += 1
        else:
            self.current_month += 1
        self.actualizar_calendario()

    def actualizar_calendario(self):
        """Actualiza el calendario con el nuevo mes y año."""
        self.header.SetLabel(self.obtener_mes_anio_espanol())  # Actualizar el encabezado
        self.crear_dias(self.calendar_grid.GetContainingWindow())  # Actualizar los días

if __name__ == "__main__":
    app = wx.App(False)
    frame = ElegantCalendar()
    app.MainLoop()
