# Parámetros de Física para el modelo de calistenia

# Gravedad (m/s^2)
GRAVEDAD = 9.81

# Parámetros de los segmentos del cuerpo (en kg y metros)
# Estos valores se basan en estimaciones generales y pueden variar según la antropometría
MASA_SEGMENTO_BRAZO = 3.5  # Masa aproximada del brazo (kg)
MASA_SEGMENTO_PIERNAS = 6.0  # Masa aproximada de las piernas (kg)
MASA_SEGMENTO_TRONCO = 30.0  # Masa aproximada del torso (kg)

# Distancia desde la articulación al centro de masa del segmento (en metros)
# Valores aproximados para el centro de masa del brazo, la pierna y el torso.
DISTANCIA_CODO = 0.35  # Distancia del codo al centro de masa del brazo (m)
DISTANCIA_HOMBRO = 0.45  # Distancia del hombro al centro de masa del brazo (m)
DISTANCIA_RODILLA = 0.4  # Distancia de la rodilla al centro de masa de la pierna (m)
DISTANCIA_CADERA = 0.5  # Distancia de la cadera al centro de masa de la pierna (m)
DISTANCIA_TORNO = 0.6  # Distancia del torso al centro de masa del tronco (m)

# Longitudes de los segmentos del cuerpo (en metros) para simular movimiento
LONGITUD_BRAZO = 0.65  # Longitud aproximada de un brazo humano (m)
LONGITUD_PIERNAS = 1.0  # Longitud aproximada de la pierna humana (m)

# Ángulos máximos y mínimos para las articulaciones (en grados)
ANGULO_MAX_CODO = 150  # Máximo ángulo del codo en un ejercicio (grados)
ANGULO_MIN_CODO = 0    # Mínimo ángulo del codo (grados)

ANGULO_MAX_HOMBRO = 180  # Máximo ángulo del hombro (grados)
ANGULO_MIN_HOMBRO = 0    # Mínimo ángulo del hombro (grados)

ANGULO_MAX_RODILLA = 135  # Máximo ángulo de la rodilla (grados)
ANGULO_MIN_RODILLA = 0    # Mínimo ángulo de la rodilla (grados)

# Parámetros de movimiento: velocidad angular (rad/s), si es necesario en cálculos
VELOCIDAD_ANGULAR_MAX = 2.0  # Velocidad máxima de movimiento angular (rad/s)
