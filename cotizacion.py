from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry  # Importamos DateEntry desde tkcalendar
from cotizacion2 import MaterialApoyo  # Importar la nueva ventana

class Cotizacion(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Cotización")
        self.geometry(f"{self.winfo_screenwidth()}x{self.winfo_screenheight()}+0+0")
        self.config(bg="#C6D9E3")
        self.resizable(False, False)
        self.master = master
        self.widgets()

    def go_back(self):
        self.destroy()
        self.master.deiconify()

    def open_material_apoyo(self):
        self.withdraw()  # Oculta la ventana actual
        MaterialApoyo(self)  # Abre la nueva ventana

    def widgets(self):
        # Header frame
        frame1 = tk.Frame(self, bg="#dddddd", highlightbackground="gray", highlightthickness=1)
        frame1.place(x=0, y=0, width=self.winfo_screenwidth(), height=80)

        # Title label
        titulo = tk.Label(self, text="Cotizacion", bg="#dddddd", font="sans 24 bold", anchor="center")
        titulo.place(x=5, y=0, width=self.winfo_screenwidth() - 10, height=70)

        # Back button
        btn_back = Button(self, text="Volver", font="sans 12 bold", bg="#ff5555", fg="white", command=self.go_back)
        btn_back.place(x=20, y=20, width=90, height=30)

        # Frame for client information
        lblframe = LabelFrame(self, text="Información del Cliente", bg="#C6D9E3", font="sans 14 bold")
        lblframe.place(x=20, y=100, width=self.winfo_screenwidth() - 40, height=260)

        # Input labels and entry fields inside the frame
        labels = ["Nombre(s):", "Teléfono:", "Dirección:", "Presente:", "Referencia:"]
        self.entries = {}

        x_label = 20  # X position for labels inside lblframe
        x_entry = 200  # X position for entry fields inside lblframe
        y_position = 30  # Starting Y position for inputs inside lblframe

        for label in labels:
            lbl = tk.Label(lblframe, text=label, bg="#C6D9E3", font="sans 12 bold", anchor="w")
            lbl.place(x=x_label, y=y_position, width=150, height=25)

            entry = tk.Entry(lblframe, font="sans 10")
            entry.place(x=x_entry, y=y_position, width=400, height=25)

            # Save references for future use
            self.entries[label.strip(":")] = entry
            y_position += 40  # Move to the next row

        # Add "Fecha" label and date picker
        lbl_fecha = tk.Label(lblframe, text="Fecha:", bg="#C6D9E3", font="sans 12 bold", anchor="w")
        lbl_fecha.place(x=x_label + 720, y=30, width=150, height=25)

        # Use DateEntry for selecting a date
        entry_fecha = DateEntry(lblframe, font="sans 10", date_pattern="yyyy-mm-dd", locale="es_ES")
        entry_fecha.place(x=x_entry + 620, y=30, width=110, height=25)

        # Store reference for later use
        self.entries["Fecha"] = entry_fecha

        # Frame for Losas information
        losas_frame = LabelFrame(self, text="Características de la Losa", bg="#C6D9E3", font="sans 14 bold")
        losas_frame.place(x=20, y=380, width=self.winfo_screenwidth() - 40, height=250)

        losa_labels = [
            "Espesor total de losa (H):",
            "Espesor total del complemento (h):",
            "Espesor, capa de compresión (e):",
            "Separación de viguetas de eje a eje (L):",
        ]

        y_position = 30
        self.losa_entries = {}

        for i, text in enumerate(losa_labels):
            lbl = tk.Label(losas_frame, text=text, bg="#C6D9E3", font="sans 12 bold", anchor="w")
            lbl.place(x=20, y=y_position, width=300, height=25)

            entry = tk.Entry(losas_frame, font="sans 12")
            entry.place(x=340, y=y_position, width=50, height=25)
            self.losa_entries[text.strip(":")] = entry

            if i != 1:  
                var = tk.StringVar(value="cm")
                cm_btn = tk.Radiobutton(
                    losas_frame, text="cm", variable=var, value="cm", bg="#C6D9E3", font="sans 14 bold"
                )
                cm_btn.place(x=420, y=y_position)

                m_btn = tk.Radiobutton(
                    losas_frame, text="m", variable=var, value="m", bg="#C6D9E3", font="sans 14 bold"
                )
                m_btn.place(x=480, y=y_position)
                self.losa_entries[f"{text.strip(':')} Unidad"] = var

            y_position += 40

        # Frame for Carga information
        carga_frame = LabelFrame(losas_frame, text="Carga", bg="#C6D9E3", font="sans 14 bold")
        carga_frame.place(x=580, y=20, width=320, height=130)  # Ajusta el ancho y alto

        carga_labels = ["Carga Muerta:", "Carga Viva:"]
        self.carga_entries = {}

        carga_y = 30  # Ajusta la posición inicial en Y
        for label in carga_labels:
            lbl = tk.Label(carga_frame, text=label, bg="#C6D9E3", font="sans 12 bold", anchor="w")
            lbl.place(x=20, y=carga_y, width=120, height=25)  # Ajusta la posición en X

            entry = tk.Entry(carga_frame, font="sans 12")
            entry.place(x=150, y=carga_y, width=100, height=25)  # Ajusta la posición en X

            self.carga_entries[label.strip(":")] = entry
            carga_y += 40  # Aumenta el espacio entre las filas

        btn_material = Button(self, text="Siguente Página", font="sans 12 bold", bg="#ff5555", fg="white", command=self.open_material_apoyo)
        btn_material.place(x=120, y=20, width=150, height=30)