from tkinter import *
import tkinter as tk
from ventas import Ventas
from cotizacion import Cotizacion
from PIL import Image, ImageTk

class Container(tk.Frame):  # Cambiado a Frame para que funcione con Manager
    def __init__(self, padre, controlador):
        super().__init__(padre, bg="#C6D9E3")
        self.controlador = controlador
        self.pack(fill="both", expand=True)
        self.widgets()

    def show_frames(self, container):
        self.controlador.withdraw()  # Oculta la ventana principal
        new_window = container(self.controlador)
        new_window.mainloop()

    def ventas(self):
        self.show_frames(Ventas)

    def cotizacion(self):
        self.show_frames(Cotizacion)

    def widgets(self):
        frame1 = tk.Frame(self, bg="#C6D9E3")
        frame1.pack()
        frame1.place(x=0, y=0, width=800, height=400)

        btnventas = Button(frame1, bg="#f4b400", fg="white", font="sans 18 bold", text="Ir a Venta", command=self.ventas)
        btnventas.place(x=500, y=100, width=240, height=60)

        btncotizacion = Button(frame1, bg="#270ed9", fg="white", font="sans 18 bold", text="Ir a Cotizacion", command=self.cotizacion)
        btncotizacion.place(x=500, y=200, width=240, height=60)

        self.logo_image = Image.open("img/vigueta.png")
        self.logo_image = self.logo_image.resize((280, 280))
        self.logo_image = ImageTk.PhotoImage(self.logo_image)
        self.logo_label = tk.Label(frame1, image=self.logo_image, bg="#C6D9E3")
        self.logo_label.place(x=100, y=30)

        copyright_label = tk.Label(frame1, text="Copyright © 2025", font="sans 12 bold", bg="#C6D9E3", fg="gray")
        copyright_label.place(x=180, y=350)
