# config.py

# Parámetros relacionados con la simulación
GRAVEDAD = 9.81  # m/s^2, gravedad de la Tierra

# Masas de los segmentos del cuerpo en kilogramos
MASA_SEGMENTO_BRAZO = 2.5  # Ejemplo, puedes ajustar según los cálculos del cuerpo
MASA_SEGMENTO_PIERNAS = 5.0  # Ejemplo, ajustar según el cuerpo
MASA_SEGMENTO_TRONCO = 10.0  # Ejemplo

# Distancias de cada articulación (en metros)
DISTANCIA_CODO = 0.4  # Distancia del codo al hombro (brazo)
DISTANCIA_HOMBRO = 0.5  # Distancia desde el hombro al torso
DISTANCIA_RODILLA = 0.45  # Distancia de la rodilla al torso
DISTANCIA_CADERA = 0.4  # Distancia de la cadera al torso
DISTANCIA_TORNO = 0.6  # Ejemplo de distancia del torso
LONGITUD_BRAZO = 0.75  # Longitud de los brazos
LONGITUD_PIERNAS = 1.0  # Longitud de las piernas

# Velocidad angular máxima (para limitar la velocidad de los movimientos)
VELOCIDAD_ANGULAR_MAX = 90  # grados por segundo
