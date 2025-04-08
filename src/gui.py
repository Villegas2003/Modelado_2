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
        
        # Configurar el fondo de la ventana principal
        self.root.config(bg='#f4f4f4')
        
        # Crear un Frame principal para los widgets
        self.main_frame = tk.Frame(self.root, bg='#f4f4f4')
        self.main_frame.grid(row=0, column=0, padx=20, pady=20)

        # Crear un Frame para el Canvas (figura de la persona)
        self.canvas_frame = tk.Frame(self.main_frame, bg='#f4f4f4')
        self.canvas_frame.grid(row=0, column=0, padx=20, pady=20)

        # Crear el Canvas para la figura de la persona
        self.canvas = tk.Canvas(self.canvas_frame, width=500, height=500, bg="white")
        self.canvas.pack()

        # Crear un Frame para los controles
        self.controls_frame = tk.Frame(self.main_frame, bg='#f4f4f4')
        self.controls_frame.grid(row=0, column=1, padx=20, pady=20)

        # Configuración de controles para las articulaciones
        self.angulo_codo = tk.Scale(self.controls_frame, from_=0, to=180, orient='horizontal', label="Ángulo del Codo", bg='#f4f4f4', font=('Arial', 10))
        self.angulo_codo.grid(row=0, column=0, pady=5)

        self.angulo_hombro = tk.Scale(self.controls_frame, from_=0, to=180, orient='horizontal', label="Ángulo del Hombro", bg='#f4f4f4', font=('Arial', 10))
        self.angulo_hombro.grid(row=1, column=0, pady=5)

        self.angulo_rodilla = tk.Scale(self.controls_frame, from_=0, to=180, orient='horizontal', label="Ángulo de la Rodilla", bg='#f4f4f4', font=('Arial', 10))
        self.angulo_rodilla.grid(row=2, column=0, pady=5)

        # Etiquetas de los resultados
        self.label_fuerzas = tk.Label(self.controls_frame, text="Fuerzas: N/A", bg='#f4f4f4', font=('Arial', 12))
        self.label_fuerzas.grid(row=3, column=0, pady=5)

        self.label_torques = tk.Label(self.controls_frame, text="Torques: N/A", bg='#f4f4f4', font=('Arial', 12))
        self.label_torques.grid(row=4, column=0, pady=5)

        # Botón para simular
        self.boton_simular = tk.Button(self.controls_frame, text="Simular Movimiento", command=self.simular, bg='#4CAF50', fg='white', font=('Arial', 12), relief='flat', width=20)
        self.boton_simular.grid(row=5, column=0, pady=10)

        # Botón para resetear
        self.boton_resetear = tk.Button(self.controls_frame, text="Resetear", command=self.resetear, bg='#f44336', fg='white', font=('Arial', 12), relief='flat', width=20)
        self.boton_resetear.grid(row=6, column=0, pady=10)

        # Crear un Frame para el gráfico de Matplotlib
        self.graph_frame = tk.Frame(self.main_frame, bg='#f4f4f4')
        self.graph_frame.grid(row=1, column=0, columnspan=2, padx=20, pady=20)

        # Figura para la visualización del gráfico
        self.figura, self.ax = plt.subplots(figsize=(5, 3))
        self.ax.set_title('Fuerza y Torque')
        self.ax.set_xlabel('Ángulo')
        self.ax.set_ylabel('Fuerza / Torque')

        # Agregar el gráfico a la interfaz
        self.canvas_figure = FigureCanvasTkAgg(self.figura, self.graph_frame)
        self.canvas_figure.get_tk_widget().pack()

    def simular(self):
        angulo_codo = self.angulo_codo.get()
        angulo_hombro = self.angulo_hombro.get()
        angulo_rodilla = self.angulo_rodilla.get()

        # Calcular fuerzas y torques
        fuerzas, torques = calcular_fuerzas_torques(angulo_codo, angulo_hombro, angulo_rodilla)

        # Mostrar los resultados
        self.label_fuerzas.config(text=f"Fuerzas: {fuerzas} N")
        self.label_torques.config(text=f"Torques: {torques} Nm")

        # Actualizar gráfico de fuerza y torque
        self.ax.clear()
        self.ax.plot([0, 1], [0, fuerzas], label='Fuerza Aplicada', color='red')
        self.ax.set_title(f"Fuerzas: {fuerzas} N, Torques: {torques} Nm")
        self.ax.set_xlabel("Ángulo")
        self.ax.set_ylabel("Fuerza / Torque")
        self.ax.legend()
        self.canvas_figure.draw()

        # Actualizar la figura de la persona en el canvas
        self.dibujar_figura(angulo_codo, angulo_hombro, angulo_rodilla)

    def dibujar_figura(self, angulo_codo, angulo_hombro, angulo_rodilla):
        # Limpiar el canvas antes de dibujar una nueva figura
        self.canvas.delete("all")

        # Dibujar un círculo como cabeza (color azul claro)
        self.canvas.create_oval(200, 50, 300, 150, fill="lightblue", outline="black")

        # Dibujar torso (línea) con una línea discontinua
        self.canvas.create_line(250, 150, 250, 300, width=3, fill="black", dash=(5, 5))

        # Dibujar brazos
        self.canvas.create_line(250, 150, 250 + 50 * np.cos(np.radians(angulo_hombro)), 150 + 50 * np.sin(np.radians(angulo_hombro)), width=3, fill="black", dash=(5, 5))  # Hombro
        self.canvas.create_line(250, 150, 250 - 50 * np.cos(np.radians(angulo_hombro)), 150 + 50 * np.sin(np.radians(angulo_hombro)), width=3, fill="black", dash=(5, 5))  # Otro brazo

        # Dibujar piernas
        self.canvas.create_line(250, 300, 250 + 50 * np.cos(np.radians(angulo_rodilla)), 300 + 50 * np.sin(np.radians(angulo_rodilla)), width=3, fill="black", dash=(5, 5))  # Rodilla
        self.canvas.create_line(250, 300, 250 - 50 * np.cos(np.radians(angulo_rodilla)), 300 + 50 * np.sin(np.radians(angulo_rodilla)), width=3, fill="black", dash=(5, 5))  # Otra pierna

        # Dibujar codo con una línea continua más gruesa
        self.canvas.create_line(250, 150, 250 + 50 * np.cos(np.radians(angulo_codo)), 150 + 50 * np.sin(np.radians(angulo_codo)), width=4, fill="black")
        
    def resetear(self):
        self.angulo_codo.set(0)
        self.angulo_hombro.set(0)
        self.angulo_rodilla.set(0)
        self.label_fuerzas.config(text="Fuerzas: N/A")
        self.label_torques.config(text="Torques: N/A")
        self.canvas.delete("all")  # Limpiar el canvas
        self.ax.clear()  # Limpiar el gráfico
        self.canvas_figure.draw()
