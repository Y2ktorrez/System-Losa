from tkinter import *
import tkinter as tk
from fpdf import FPDF
import os
from pathlib import Path

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
            area = float(self.entries["Area (m2)"].get())
            precio_m2 = float(self.entries["Precio Bs/m2"].get())
            precio_total = area * precio_m2
            self.entries["Precio total Bs"].delete(0, END)
            self.entries["Precio total Bs"].insert(0, f"{precio_total:.2f}")
        except ValueError:
            self.entries["Precio total Bs"].delete(0, END)
            self.entries["Precio total Bs"].insert(0, "Error: Verifique los datos")

    def generar_pdf(self):
        pdf = FPDF()
        pdf.add_page()

        # Encabezado grande y en negrita
        pdf.set_font("Arial", style="B", size=16)
        pdf.cell(200, 10, txt="Cotización", ln=True, align="C")
        pdf.ln(10)

        # Información del cliente
        pdf.set_font("Arial", style="B", size=14)
        pdf.cell(200, 10, txt="Información del Cliente", ln=True)
        pdf.set_font("Arial", size=12)
        pdf.cell(200, 10, txt=f"Nombre: {self.master.entries['Nombre(s)'].get()}", ln=True)
        pdf.cell(200, 10, txt=f"Teléfono: {self.master.entries['Teléfono'].get()}", ln=True)
        pdf.cell(200, 10, txt=f"Dirección: {self.master.entries['Dirección'].get()}", ln=True)
        pdf.cell(200, 10, txt=f"Fecha: {self.master.entries['Fecha'].get()}", ln=True)
        pdf.ln(10)

        # Información de la losa
        pdf.set_font("Arial", style="B", size=14)
        pdf.cell(200, 10, txt="Características de la Losa", ln=True)
        pdf.set_font("Arial", size=12)
        for key, entry in self.master.losa_entries.items():
            if "Unidad" not in key:
                pdf.cell(200, 10, txt=f"{key}: {entry.get()}", ln=True)
        pdf.ln(10)

        # Información de la carga
        pdf.set_font("Arial", style="B", size=14)
        pdf.cell(200, 10, txt="Carga", ln=True)
        pdf.set_font("Arial", size=12)
        for key, entry in self.master.carga_entries.items():
            pdf.cell(200, 10, txt=f"{key}: {entry.get()}", ln=True)
        pdf.ln(10)

        # Material de apoyo
        pdf.set_font("Arial", style="B", size=14)
        pdf.cell(200, 10, txt="Material de Apoyo", ln=True)
        pdf.set_font("Arial", size=12)
        for material, var in self.material_vars.items():
            pdf.cell(200, 10, txt=f"{material}: {'Sí' if var.get() else 'No'}", ln=True)
        pdf.ln(10)

        # Cotización total
        pdf.set_font("Arial", style="B", size=14)
        pdf.cell(200, 10, txt="Cotización Total", ln=True)
        pdf.set_font("Arial", size=12)
        for key, entry in self.entries.items():
            pdf.cell(200, 10, txt=f"{key}: {entry.get()}", ln=True)
        pdf.ln(10)

        # Obtener el nombre del cliente para el nombre del archivo
        nombre_cliente = self.master.entries['Nombre(s)'].get().strip().replace(" ", "_")
        if not nombre_cliente:
            nombre_cliente = "Cotizacion"  # Nombre por defecto si no hay nombre de cliente

        # Guardar el PDF en la carpeta de descargas
        downloads_path = str(Path.home() / "Downloads")
        pdf_file = os.path.join(downloads_path, f"{nombre_cliente}_cotizacion.pdf")
        pdf.output(pdf_file)

        # Abrir el PDF automáticamente
        os.system(f"start {pdf_file}")

    def widgets(self):
        frame1 = tk.Frame(self, bg="#dddddd", highlightbackground="gray", highlightthickness=1)
        frame1.place(x=0, y=0, width=self.winfo_screenwidth(), height=80)

        titulo = tk.Label(self, text="Cotización", bg="#dddddd", font="sans 24 bold", anchor="center")
        titulo.place(x=5, y=0, width=self.winfo_screenwidth() - 10, height=70)

        btn_back = Button(self, text="Volver", font="sans 12 bold", bg="#ff5555", fg="white", command=self.go_back)
        btn_back.place(x=20, y=20, width=90, height=30)

        btn_pdf = Button(self, text="Generar PDF", font="sans 12 bold", bg="#4CAF50", fg="white", command=self.generar_pdf)
        btn_pdf.place(x=self.winfo_screenwidth() - 150, y=20, width=120, height=30)

        material_frame = LabelFrame(self, text="Material de Apoyo para su Obra", bg="#C6D9E3", font="sans 14 bold")
        material_frame.place(x=20, y=100, width=self.winfo_screenwidth() - 40, height=240)

        materiales = ["Mescladora", "Vibradora", "Puntales 100%", "Andamios modulares"]
        self.material_vars = {}

        y_position = 30
        for material in materiales:
            var = tk.BooleanVar()
            chk = tk.Checkbutton(material_frame, text=material, variable=var, bg="#C6D9E3", font="sans 12 bold")
            chk.place(x=20, y=y_position)
            self.material_vars[material] = var
            y_position += 40

        cotizacion_frame = LabelFrame(self, text="Cotización Total", bg="#C6D9E3", font="sans 14 bold")
        cotizacion_frame.place(x=20, y=360, width=self.winfo_screenwidth() - 40, height=340)

        labels = ["Area (m2):", "COMP. PLASTOFOR N°:", "Total (m2):", "Precio Bs/m2:", "Precio total Bs:"]
        self.entries = {}

        x_label = 20
        x_entry = 250
        y_position = 30

        for label in labels:
            lbl = tk.Label(cotizacion_frame, text=label, bg="#C6D9E3", font="sans 12 bold", anchor="w")
            lbl.place(x=x_label, y=y_position, width=200, height=25)

            entry = tk.Entry(cotizacion_frame, font="sans 12")
            entry.place(x=x_entry, y=y_position, width=80, height=25)

            self.entries[label.strip(":")] = entry

            if label == "Precio total Bs:":
                btn_calcular = Button(
                    cotizacion_frame, text="Calcular", font="sans 12 bold", bg="#4CAF50", fg="white", command=self.calcular_total
                )
                btn_calcular.place(x=x_entry + 100, y=y_position, width=120, height=25)

            y_position += 40

        dato_frame = LabelFrame(cotizacion_frame, text="Datos técnicos adicionales para el Hormigonado de la Losa", bg="#C6D9E3", font="sans 14 bold")
        dato_frame.place(x=620, y=20, width=580, height=285)

        carga_labels = ["Volumen del hormigon (m3):", "Cantidad de cemento (bolsas):", "Cantidad de arenilla (m3):", 
            "Cantidad de ripio (m3):", "Cantidad de puntales (Pzas):", "Fierro de 1/4 (30x30) (Barras):"]
        self.carga_entries = {}

        carga_y = 30 
        for label in carga_labels:
            lbl = tk.Label(dato_frame, text=label, bg="#C6D9E3", font="sans 10 bold", anchor="w")
            lbl.place(x=50, y=carga_y, width=200, height=25)

            entry = tk.Entry(dato_frame, font="sans 12")
            entry.place(x=270, y=carga_y, width=50, height=25)

            self.carga_entries[label.strip(":")] = entry
            carga_y += 40
