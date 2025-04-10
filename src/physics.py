# physics.py

import numpy as np
from src.config import GRAVEDAD, MASA_SEGMENTO_BRAZO, MASA_SEGMENTO_PIERNAS, DISTANCIA_CODO, DISTANCIA_HOMBRO, DISTANCIA_RODILLA, DISTANCIA_CADERA, VELOCIDAD_ANGULAR_MAX

def calcular_fuerzas_torques(angulo_codo_izq, angulo_hombro_izq, angulo_rodilla_izq, angulo_codo_der, angulo_hombro_der, angulo_rodilla_der):
    # Cálculo dinámico de distancias según los ángulos
    distancia_codo_izq = DISTANCIA_CODO * np.cos(np.radians(angulo_codo_izq))
    distancia_hombro_izq = DISTANCIA_HOMBRO * np.cos(np.radians(angulo_hombro_izq))
    distancia_rodilla_izq = DISTANCIA_RODILLA * np.cos(np.radians(angulo_rodilla_izq))
    
    distancia_codo_der = DISTANCIA_CODO * np.cos(np.radians(angulo_codo_der))
    distancia_hombro_der = DISTANCIA_HOMBRO * np.cos(np.radians(angulo_hombro_der))
    distancia_rodilla_der = DISTANCIA_RODILLA * np.cos(np.radians(angulo_rodilla_der))

    # Cálculo de la fuerza gravitacional (peso)
    W_brazo = MASA_SEGMENTO_BRAZO * GRAVEDAD
    W_piernas = MASA_SEGMENTO_PIERNAS * GRAVEDAD

    # Torque para cada articulación ajustado por la distancia
    torque_codo_izq = W_brazo * distancia_codo_izq * np.sin(np.radians(angulo_codo_izq))
    torque_hombro_izq = W_brazo * distancia_hombro_izq * np.sin(np.radians(angulo_hombro_izq))
    torque_rodilla_izq = W_piernas * distancia_rodilla_izq * np.sin(np.radians(angulo_rodilla_izq))
    
    torque_codo_der = W_brazo * distancia_codo_der * np.sin(np.radians(angulo_codo_der))
    torque_hombro_der = W_brazo * distancia_hombro_der * np.sin(np.radians(angulo_hombro_der))
    torque_rodilla_der = W_piernas * distancia_rodilla_der * np.sin(np.radians(angulo_rodilla_der))

    # Torques totales sumados de cada segmento
    torques_totales = torque_codo_izq + torque_hombro_izq + torque_rodilla_izq + torque_codo_der + torque_hombro_der + torque_rodilla_der

    # Fuerza total aplicada
    fuerzas_totales = W_brazo + W_piernas  # Fuerza total en ambos brazos y piernas
    
    return fuerzas_totales, torques_totales
