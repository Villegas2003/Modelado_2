# Simulación de Movimientos de Calistenia

Este proyecto tiene como objetivo simular los movimientos de calistenia utilizando una interfaz gráfica construida con **Tkinter** en Python. Los usuarios pueden ajustar los ángulos de las articulaciones del cuerpo humano (como codos, hombros, rodillas y caderas) y observar cómo cambian las fuerzas y torques aplicados en el sistema. Además, el sistema genera una visualización de los movimientos del cuerpo en función de los ángulos seleccionados.

## Requisitos

Antes de ejecutar el proyecto, asegúrate de tener instaladas las siguientes dependencias:

- Python 3.x
- `numpy` para los cálculos matemáticos.
- `matplotlib` para la visualización de gráficos.
- `tkinter` para la creación de la interfaz gráfica.

Puedes instalar las dependencias necesarias ejecutando:

```bash
pip install numpy matplotlib
```

## Estructura del Proyecto

Este proyecto tiene la siguiente estructura de directorios:

```
calistenia_simulacion/
│
├── src/
│   ├── __init__.py
│   ├── config.py         # Parámetros de configuración como masa de los segmentos y distancias.
│   ├── physics.py        # Cálculos de fuerzas y torques para los movimientos.
│   ├── gui.py            # Interfaz gráfica de usuario con los controles y visualización.
│   ├── visualization.py  # Funciones para actualizar la visualización gráfica de los movimientos.
│   └── main.py           # Archivo principal para ejecutar la simulación.
│
└── README.md             # Documentación del proyecto.
```

## Funcionamiento

El proyecto permite simular los movimientos del cuerpo humano ajustando los ángulos de las siguientes articulaciones:

- **Codo izquierdo y derecho**
- **Hombro izquierdo y derecho**
- **Rodilla izquierda y derecha**
- **Cadera izquierda y derecha**

### Interfaz Gráfica

- **Controles**: La interfaz tiene controles deslizantes (sliders) para modificar los ángulos de las articulaciones. Los ángulos también se pueden ajustar manualmente a través de un campo de texto asociado.
- **Simulación**: Al hacer clic en el botón "Simular Movimiento", el sistema calcula las fuerzas y torques en cada articulación y muestra estos valores en la interfaz.
- **Visualización**: Se muestra una figura que representa el cuerpo humano con las articulaciones ajustadas según los ángulos seleccionados. Los movimientos de las articulaciones se actualizan en tiempo real.

## Cómo Ejecutar el Proyecto

1. **Clona el repositorio** o descarga los archivos del proyecto.
2. **Abre una terminal** o una consola de comandos y navega al directorio del proyecto.
3. Ejecuta el siguiente comando para iniciar la simulación:

```bash
python -m src.main
```

Este comando iniciará la interfaz gráfica de usuario donde podrás ajustar los ángulos y observar los resultados de la simulación.

## Funcionalidades

- **Entrada de Ángulos**: Los usuarios pueden ajustar los ángulos de las articulaciones usando sliders o campos de texto.
- **Cálculo de Fuerzas y Torques**: El sistema calcula las fuerzas y torques en cada articulación usando las masas de los segmentos y las distancias de las articulaciones definidas en el archivo `config.py`.
- **Visualización de Movimiento**: Utilizando **matplotlib**, la simulación genera una visualización gráfica que muestra la relación entre los ángulos de las articulaciones, las fuerzas y los torques aplicados.
- **Actualización en Tiempo Real**: Los gráficos y la figura en la interfaz gráfica se actualizan en tiempo real cuando el usuario cambia los valores de los ángulos.
