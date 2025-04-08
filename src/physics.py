import numpy as np
from src.config import GRAVEDAD, MASA_SEGMENTO_BRAZO, MASA_SEGMENTO_PIERNAS, MASA_SEGMENTO_TRONCO, DISTANCIA_CODO, DISTANCIA_HOMBRO, DISTANCIA_RODILLA, DISTANCIA_CADERA, DISTANCIA_TORNO, LONGITUD_BRAZO, LONGITUD_PIERNAS, VELOCIDAD_ANGULAR_MAX

def calcular_fuerzas_torques(angulo_codo, angulo_hombro, angulo_rodilla):
    # Fuerza gravitacional (peso)
    W = MASA_SEGMENTO_BRAZO * GRAVEDAD  # Utilizar la masa del segmento correspondiente
    
    # Torque para cada articulación (simplificado)
    torque_codo = W * DISTANCIA_CODO * np.sin(np.radians(angulo_codo))
    torque_hombro = W * DISTANCIA_HOMBRO * np.sin(np.radians(angulo_hombro))
    torque_rodilla = W * DISTANCIA_RODILLA * np.sin(np.radians(angulo_rodilla))

    # Torques totales
    torques = torque_codo + torque_hombro + torque_rodilla
    fuerzas = W  # Fuerza total aplicada en el sistema
    
    return fuerzas, torques
