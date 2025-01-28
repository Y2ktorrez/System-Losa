from tkinter import *
import tkinter as tk

class MaterialApoyo(tk.Toplevel):
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

    def calcular_total(self):
        try:
            # Obteniendo valores de los campos
            area = float(self.entries["Area (m2)"].get())
            precio_m2 = float(self.entries["Precio Bs/m2"].get())

            # Calculando precio total
            precio_total = area * precio_m2

            # Mostrando el resultado en el campo correspondiente
            self.entries["Precio total Bs"].delete(0, END)
            self.entries["Precio total Bs"].insert(0, f"{precio_total:.2f}")
        except ValueError:
            # Si hay algún error en los valores ingresados, se muestra un mensaje de error
            self.entries["Precio total Bs"].delete(0, END)
            self.entries["Precio total Bs"].insert(0, "Error: Verifique los datos")

    def widgets(self):
        # Header frame
        frame1 = tk.Frame(self, bg="#dddddd", highlightbackground="gray", highlightthickness=1)
        frame1.place(x=0, y=0, width=self.winfo_screenwidth(), height=80)

        # Title label
        titulo = tk.Label(self, text="Cotización", bg="#dddddd", font="sans 24 bold", anchor="center")
        titulo.place(x=5, y=0, width=self.winfo_screenwidth() - 10, height=70)

        # Back button
        btn_back = Button(self, text="Volver", font="sans 12 bold", bg="#ff5555", fg="white", command=self.go_back)
        btn_back.place(x=20, y=20, width=90, height=30)

        # Frame for Material de Apoyo
        material_frame = LabelFrame(self, text="Material de Apoyo para su Obra", bg="#C6D9E3", font="sans 14 bold")
        material_frame.place(x=20, y=100, width=self.winfo_screenwidth() - 40, height=240)

        # Materiales disponibles
        materiales = ["Mescladora", "Vibradora", "Puntales 100%", "Andamios modulares"]
        self.material_vars = {}

        y_position = 30
        for material in materiales:
            var = tk.BooleanVar()
            chk = tk.Checkbutton(material_frame, text=material, variable=var, bg="#C6D9E3", font="sans 12 bold")
            chk.place(x=20, y=y_position)
            self.material_vars[material] = var
            y_position += 40

        # Frame for Cotización Total
        cotizacion_frame = LabelFrame(self, text="Cotización Total", bg="#C6D9E3", font="sans 14 bold")
        cotizacion_frame.place(x=20, y=360, width=self.winfo_screenwidth() - 40, height=340)

        # Labels and entry fields for Cotización Total
        labels = ["Area (m2):", "COMP. PLASTOFOR N°:", "Total (m2):", "Precio Bs/m2:", "Precio total Bs:"]
        self.entries = {}

        x_label = 20  # X position for labels
        x_entry = 250  # X position for entry fields
        y_position = 30  # Starting Y position

        for label in labels:
            lbl = tk.Label(cotizacion_frame, text=label, bg="#C6D9E3", font="sans 12 bold", anchor="w")
            lbl.place(x=x_label, y=y_position, width=200, height=25)

            entry = tk.Entry(cotizacion_frame, font="sans 12")
            entry.place(x=x_entry, y=y_position, width=80, height=25)

            # Save references for future use
            self.entries[label.strip(":")] = entry

            # Colocar el botón "Calcular" a la derecha del campo "Precio total Bs"
            if label == "Precio total Bs:":
                btn_calcular = Button(
                    cotizacion_frame, text="Calcular", font="sans 12 bold", bg="#4CAF50", fg="white", command=self.calcular_total
                )
                btn_calcular.place(x=x_entry + 100, y=y_position, width=120, height=25)

            y_position += 40
        
        # Frame for Dato information
        dato_frame = LabelFrame(cotizacion_frame, text="Datos técnicos adicionales para el Hormigonado de la Losa", bg="#C6D9E3", font="sans 14 bold")
        dato_frame.place(x=620, y=20, width=580, height=285)  # Ajusta el ancho y alto

        carga_labels = ["Volumen del hormigon (m3):", "Cantidad de cemento (bolsas):", "Cantidad de arenilla (m3):", 
            "Cantidad de ripio (m3):", "Cantidad de puntales (Pzas):", "Fierro de 1/4 (30x30) (Barras):"]
        self.carga_entries = {}

        carga_y = 30 
        for label in carga_labels:
            lbl = tk.Label(dato_frame, text=label, bg="#C6D9E3", font="sans 10 bold", anchor="w")
            lbl.place(x=50, y=carga_y, width=200, height=25)  # Ajusta la posición en X

            entry = tk.Entry(dato_frame, font="sans 12")
            entry.place(x=270, y=carga_y, width=50, height=25)  # Ajusta la posición en X

            self.carga_entries[label.strip(":")] = entry
            carga_y += 40  # Aumenta el espacio entre las filas

