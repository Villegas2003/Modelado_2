import matplotlib.pyplot as plt

def actualizar_simulacion(fuerzas, torques):
    # Actualizar la visualización del movimiento
    plt.clf()
    fig, ax = plt.subplots()

    ax.plot([0, 1], [0, fuerzas], label='Fuerza Aplicada', color='red')
    ax.set_title(f"Fuerzas: {fuerzas} N, Torques: {torques} Nm")
    ax.set_xlabel("Ángulo")
    ax.set_ylabel("Fuerza / Torque")
    ax.legend()

    plt.draw()
    plt.pause(0.1)
