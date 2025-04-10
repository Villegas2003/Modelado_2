import tkinter as tk
from tkinter import messagebox
from src.physics import calcular_fuerzas_torques
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class CalisteniaSimulacionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simulación de Movimientos de Calistenia")
        
        # Cambiar el fondo de la ventana principal a negro
        self.root.config(bg='black')
        
        # Crear un Frame principal para los widgets, centrado en la ventana
        self.main_frame = tk.Frame(self.root, bg='black')
        self.main_frame.grid(row=0, column=2, padx=20, pady=20, sticky="nsew")
        
        # Título
        self.title_label = tk.Label(self.main_frame, text="Simulación de Movimientos de Calistenia", 
                                    bg='black', fg='cyan', font=('Arial', 20, 'bold'))
        self.title_label.grid(row=0, column=0, columnspan=2, pady=20)

        # Crear un Frame para los controles con fondo oscuro
        self.controls_frame = tk.Frame(self.main_frame, bg='black')
        self.controls_frame.grid(row=1, column=1, padx=20, pady=20, sticky="nswe")
        
        # Configuración de los controles y la entrada de los ángulos
        self.entry_angulo_codo_izq, self.slider_angulo_codo_izq = self.crear_entrada_slider("Ángulo Codo Izquierdo", 0)
        self.entry_angulo_codo_der, self.slider_angulo_codo_der = self.crear_entrada_slider("Ángulo Codo Derecho", 1)
        self.entry_angulo_hombro_izq, self.slider_angulo_hombro_izq = self.crear_entrada_slider("Ángulo Hombro Izquierdo", 2)
        self.entry_angulo_hombro_der, self.slider_angulo_hombro_der = self.crear_entrada_slider("Ángulo Hombro Derecho", 3)
        self.entry_angulo_rodilla_izq, self.slider_angulo_rodilla_izq = self.crear_entrada_slider("Ángulo Rodilla Izquierda", 4)
        self.entry_angulo_rodilla_der, self.slider_angulo_rodilla_der = self.crear_entrada_slider("Ángulo Rodilla Derecha", 5)
        self.entry_angulo_cadera_izq, self.slider_angulo_cadera_izq = self.crear_entrada_slider("Ángulo Cadera Izquierda", 6)
        self.entry_angulo_cadera_der, self.slider_angulo_cadera_der = self.crear_entrada_slider("Ángulo Cadera Derecha", 7)

        # Labels para mostrar los resultados de fuerzas y torques con color brillante
        self.label_fuerzas = tk.Label(self.controls_frame, text="Fuerzas: N/A", bg='black', fg='cyan', font=('Arial', 12))
        self.label_fuerzas.grid(row=18, column=0, pady=5)

        self.label_torques = tk.Label(self.controls_frame, text="Torques: N/A", bg='black', fg='cyan', font=('Arial', 12))
        self.label_torques.grid(row=19, column=0, pady=5)

        # Botón para simular, con un color más llamativo
        self.boton_simular = tk.Button(self.controls_frame, text="Simular Movimiento", command=self.simular, 
                                       bg='#4CAF50', fg='white', font=('Arial', 12), relief='flat', width=20)
        self.boton_simular.grid(row=20, column=0, pady=10)

        # Crear un Canvas para dibujar la figura
        self.canvas_frame = tk.Frame(self.main_frame, bg='black')
        self.canvas_frame.grid(row=1, column=0, padx=20, pady=20)
        self.canvas = tk.Canvas(self.canvas_frame, width=400, height=400, bg='white')
        self.canvas.pack()

        # Botones de ejercicios
        self.boton_pushup = tk.Button(self.controls_frame, text="Flexiones (Push-ups)", command=self.ejercicio_pushup,
                                      bg='#FF5733', fg='white', font=('Arial', 12), relief='flat', width=20)
        self.boton_pushup.grid(row=21, column=0, pady=10)

        self.boton_squat = tk.Button(self.controls_frame, text="Sentadillas (Squats)", command=self.ejercicio_squat,
                                     bg='#FF5733', fg='white', font=('Arial', 12), relief='flat', width=20)
        self.boton_squat.grid(row=22, column=0, pady=10)

    def ejercicio_pushup(self):
        """Simula el movimiento de flexiones (Push-ups)"""
        # Cambiar los ángulos para las flexiones
        self.slider_angulo_codo_izq.set(90)
        self.slider_angulo_codo_der.set(90)
        self.slider_angulo_hombro_izq.set(45)
        self.slider_angulo_hombro_der.set(45)
        self.slider_angulo_rodilla_izq.set(180)
        self.slider_angulo_rodilla_der.set(180)
        self.slider_angulo_cadera_izq.set(180)
        self.slider_angulo_cadera_der.set(180)

        self.simular()

    def ejercicio_squat(self):
        """Simula el movimiento de sentadillas (Squats)"""
        # Cambiar los ángulos para las sentadillas
        self.slider_angulo_codo_izq.set(0)
        self.slider_angulo_codo_der.set(0)
        self.slider_angulo_hombro_izq.set(180)
        self.slider_angulo_hombro_der.set(180)
        self.slider_angulo_rodilla_izq.set(90)
        self.slider_angulo_rodilla_der.set(90)
        self.slider_angulo_cadera_izq.set(90)
        self.slider_angulo_cadera_der.set(90)

        self.simular()

    def crear_entrada_slider(self, label, row):
        """Crea un campo de texto y un slider para los ángulos de las articulaciones"""
        # Etiqueta para la entrada con color vibrante
        tk.Label(self.controls_frame, text=label, bg='black', fg='cyan', font=('Arial', 10)).grid(row=row*2, column=0)
        
        # Entrada de texto
        entry = tk.Entry(self.controls_frame, bg='#333', fg='white', font=('Arial', 10))
        entry.grid(row=row*2 + 1, column=0)

        # Slider para los ángulos
        slider = tk.Scale(self.controls_frame, from_=0, to=180, orient='horizontal', bg='#333', 
                          fg='white', font=('Arial', 10), sliderlength=25)
        slider.grid(row=row*2 + 1, column=1)

        # Actualizar el TextBox cuando el slider se mueve
        slider.bind("<Motion>", lambda event: self.actualizar_entry(entry, slider))

        return entry, slider

    def actualizar_entry(self, entry, slider):
        """Actualizar el valor del entry con el valor del slider"""
        entry.delete(0, tk.END)
        entry.insert(0, slider.get())

    def validar_entrada(self, entrada):
        """Valida que la entrada no esté vacía y sea un número válido"""
        try:
            valor = float(entrada.get())
            if valor < 0 or valor > 180:
                raise ValueError("El ángulo debe estar entre 0 y 180 grados.")
            return valor
        except ValueError as e:
            messagebox.showerror("Error", f"Valor no válido: {e}")
            return None

    def simular(self):
        # Validar las entradas
        angulo_codo_izq = self.validar_entrada(self.entry_angulo_codo_izq)
        angulo_codo_der = self.validar_entrada(self.entry_angulo_codo_der)
        angulo_hombro_izq = self.validar_entrada(self.entry_angulo_hombro_izq)
        angulo_hombro_der = self.validar_entrada(self.entry_angulo_hombro_der)
        angulo_rodilla_izq = self.validar_entrada(self.entry_angulo_rodilla_izq)
        angulo_rodilla_der = self.validar_entrada(self.entry_angulo_rodilla_der)
        angulo_cadera_izq = self.validar_entrada(self.entry_angulo_cadera_izq)
        angulo_cadera_der = self.validar_entrada(self.entry_angulo_cadera_der)

        # Si alguna de las entradas es inválida, no realizar la simulación
        if None in [angulo_codo_izq, angulo_codo_der, angulo_hombro_izq, angulo_hombro_der, angulo_rodilla_izq, angulo_rodilla_der, angulo_cadera_izq, angulo_cadera_der]:
            return

        # Calcular fuerzas y torques
        fuerzas, torques = calcular_fuerzas_torques(angulo_codo_izq, angulo_hombro_izq, angulo_rodilla_izq, angulo_codo_der, angulo_hombro_der, angulo_rodilla_der)

        # Mostrar los resultados
        self.label_fuerzas.config(text=f"Fuerzas: {fuerzas} N")
        self.label_torques.config(text=f"Torques: {torques} Nm")

        # Actualizar la visualización de la figura
        self.dibujar_figura(angulo_codo_izq, angulo_hombro_izq, angulo_rodilla_izq, angulo_codo_der, angulo_hombro_der, angulo_rodilla_der, angulo_cadera_izq, angulo_cadera_der)

    def dibujar_figura(self, angulo_codo_izq, angulo_hombro_izq, angulo_rodilla_izq, angulo_codo_der, angulo_hombro_der, angulo_rodilla_der, angulo_cadera_izq, angulo_cadera_der):
        # Limpiar el canvas antes de dibujar una nueva figura
        self.canvas.delete("all")

        # Dibujar la cabeza (círculo)
        self.canvas.create_oval(190, 50, 210, 70, fill="lightblue", outline="black")

        # Cuerpo (línea del tronco)
        self.canvas.create_line(200, 70, 200, 150, width=3, fill="black")

        # Brazo izquierdo (línea del hombro al codo)
        self.canvas.create_line(200, 100, 200 + 50 * np.cos(np.radians(angulo_hombro_izq)), 100 - 50 * np.sin(np.radians(angulo_hombro_izq)), width=3, fill="black")
        self.canvas.create_oval(200 + 50 * np.cos(np.radians(angulo_hombro_izq)) - 5, 100 - 50 * np.sin(np.radians(angulo_hombro_izq)) - 5, 200 + 50 * np.cos(np.radians(angulo_hombro_izq)) + 5, 100 - 50 * np.sin(np.radians(angulo_hombro_izq)) + 5, fill="red", outline="black")

        # Brazo izquierdo (línea del codo a la muñeca)
        self.canvas.create_line(200 + 50 * np.cos(np.radians(angulo_hombro_izq)), 100 - 50 * np.sin(np.radians(angulo_hombro_izq)),
                                200 + 100 * np.cos(np.radians(angulo_hombro_izq)) - 50 * np.cos(np.radians(angulo_codo_izq)),
                                100 - 50 * np.sin(np.radians(angulo_hombro_izq)) - 100 * np.sin(np.radians(angulo_codo_izq)), width=3, fill="black")
        self.canvas.create_oval(200 + 100 * np.cos(np.radians(angulo_hombro_izq)) - 50 * np.cos(np.radians(angulo_codo_izq)) - 5,
                                100 - 50 * np.sin(np.radians(angulo_hombro_izq)) - 100 * np.sin(np.radians(angulo_codo_izq)) - 5,
                                200 + 100 * np.cos(np.radians(angulo_hombro_izq)) - 50 * np.cos(np.radians(angulo_codo_izq)) + 5,
                                100 - 50 * np.sin(np.radians(angulo_hombro_izq)) - 100 * np.sin(np.radians(angulo_codo_izq)) + 5, fill="blue", outline="black")

        # Brazo derecho (línea del hombro al codo)
        self.canvas.create_line(200, 100, 200 - 50 * np.cos(np.radians(angulo_hombro_der)), 100 - 50 * np.sin(np.radians(angulo_hombro_der)), width=3, fill="black")
        self.canvas.create_oval(200 - 50 * np.cos(np.radians(angulo_hombro_der)) - 5, 100 - 50 * np.sin(np.radians(angulo_hombro_der)) - 5, 200 - 50 * np.cos(np.radians(angulo_hombro_der)) + 5, 100 - 50 * np.sin(np.radians(angulo_hombro_der)) + 5, fill="red", outline="black")

        # Brazo derecho (línea del codo a la muñeca)
        self.canvas.create_line(200 - 50 * np.cos(np.radians(angulo_hombro_der)), 100 - 50 * np.sin(np.radians(angulo_hombro_der)),
                                200 - 100 * np.cos(np.radians(angulo_hombro_der)) + 50 * np.cos(np.radians(angulo_codo_der)),
                                100 - 50 * np.sin(np.radians(angulo_hombro_der)) + 100 * np.sin(np.radians(angulo_codo_der)), width=3, fill="black")
        self.canvas.create_oval(200 - 100 * np.cos(np.radians(angulo_hombro_der)) + 50 * np.cos(np.radians(angulo_codo_der)) - 5,
                                100 - 50 * np.sin(np.radians(angulo_hombro_der)) + 100 * np.sin(np.radians(angulo_codo_der)) - 5,
                                200 - 100 * np.cos(np.radians(angulo_hombro_der)) + 50 * np.cos(np.radians(angulo_codo_der)) + 5,
                                100 - 50 * np.sin(np.radians(angulo_hombro_der)) + 100 * np.sin(np.radians(angulo_codo_der)) + 5, fill="blue", outline="black")
        
        # Dibujo de las piernas y demás sigue igual...

        # Pierna izquierda (línea del muslo a la rodilla)
        self.canvas.create_line(200, 150, 200 + 50 * np.cos(np.radians(angulo_cadera_izq)), 150 + 50 * np.sin(np.radians(angulo_cadera_izq)), width=3, fill="black")
        self.canvas.create_oval(200 + 50 * np.cos(np.radians(angulo_cadera_izq)) - 5, 150 + 50 * np.sin(np.radians(angulo_cadera_izq)) - 5, 200 + 50 * np.cos(np.radians(angulo_cadera_izq)) + 5, 150 + 50 * np.sin(np.radians(angulo_cadera_izq)) + 5, fill="red", outline="black")

        # Pierna izquierda (línea de la rodilla al pie)
        self.canvas.create_line(200 + 50 * np.cos(np.radians(angulo_cadera_izq)), 150 + 50 * np.sin(np.radians(angulo_cadera_izq)),
                                200 + 100 * np.cos(np.radians(angulo_rodilla_izq)) - 50 * np.cos(np.radians(angulo_rodilla_izq)),
                                150 + 50 * np.sin(np.radians(angulo_rodilla_izq)) + 100 * np.sin(np.radians(angulo_rodilla_izq)), width=3, fill="black")
        self.canvas.create_oval(200 + 100 * np.cos(np.radians(angulo_rodilla_izq)) - 50 * np.cos(np.radians(angulo_rodilla_izq)) - 5,
                                150 + 50 * np.sin(np.radians(angulo_rodilla_izq)) + 100 * np.sin(np.radians(angulo_rodilla_izq)) - 5,
                                200 + 100 * np.cos(np.radians(angulo_rodilla_izq)) - 50 * np.cos(np.radians(angulo_rodilla_izq)) + 5,
                                150 + 50 * np.sin(np.radians(angulo_rodilla_izq)) + 100 * np.sin(np.radians(angulo_rodilla_izq)) + 5, fill="red", outline="black")

        # Pierna derecha (línea del muslo a la rodilla)
        self.canvas.create_line(200, 150, 200 - 50 * np.cos(np.radians(angulo_cadera_der)), 150 + 50 * np.sin(np.radians(angulo_cadera_der)), width=3, fill="black")
        self.canvas.create_oval(200 - 50 * np.cos(np.radians(angulo_cadera_der)) - 5, 150 + 50 * np.sin(np.radians(angulo_cadera_der)) - 5, 200 - 50 * np.cos(np.radians(angulo_cadera_der)) + 5, 150 + 50 * np.sin(np.radians(angulo_cadera_der)) + 5, fill="red", outline="black")

        # Pierna derecha (línea de la rodilla al pie)
        self.canvas.create_line(200 - 50 * np.cos(np.radians(angulo_cadera_der)), 150 + 50 * np.sin(np.radians(angulo_cadera_der)),
                                200 - 100 * np.cos(np.radians(angulo_rodilla_der)) + 50 * np.cos(np.radians(angulo_rodilla_der)),
                                150 + 50 * np.sin(np.radians(angulo_rodilla_der)) + 100 * np.sin(np.radians(angulo_rodilla_der)), width=3, fill="black")
        self.canvas.create_oval(200 - 100 * np.cos(np.radians(angulo_rodilla_der)) + 50 * np.cos(np.radians(angulo_rodilla_der)) - 5,
                                150 + 50 * np.sin(np.radians(angulo_rodilla_der)) + 100 * np.sin(np.radians(angulo_rodilla_der)) - 5,
                                200 - 100 * np.cos(np.radians(angulo_rodilla_der)) + 50 * np.cos(np.radians(angulo_rodilla_der)) + 5,
                                150 + 50 * np.sin(np.radians(angulo_rodilla_der)) + 100 * np.sin(np.radians(angulo_rodilla_der)) + 5, fill="red", outline="black")
