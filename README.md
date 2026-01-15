# PEC4 - Ejercicio 1: Load Dataset y EDA

## 📋 Descripción

Este proyecto ha sido desarrollado para la **PEC4**, centrándose en el análisis del sistema universitario catalán.  


## 📁 Estructura del Proyecto
```
PEC4/
│
├── main.py                     # Punto de entrada y orquestador del proyecto
├── README.md                   # Documentación del proyecto
├── requirements.txt            # Dependencias necesarias
│
├── src/
│   ├── modules/                # Lógica central dividida por ejercicios
│   │   ├── __init__.py
│   │   ├── ejercicio1.py       # Carga y Análisis Exploratorio (EDA)
│   │   ├── ejercicio2.py       # Limpieza, normalización y fusión
│   │   ├── ejercicio3.py       # Análisis visual y series temporales
│   │   └── ejercicio4.py       # Estadística avanzada y exportación JSON
│   │
│   ├── utils/
│   │   └── ejecutar_ejercicios.py  # Gestión del flujo de ejecución
│   │
│   ├── img/                    # Gráficos generados (.png)
│   └── report/                 # Informes finales (.json)
│
├── data/                       # Almacén de datos
│   ├── rendiment_estudiants.xlsx
│   ├── taxa_abandonament.xlsx
│   └── dataset_fusionado.csv
│
└── tests/                      # Pruebas unitarias
    └── test_pec4.py
```

## 🚀 Instalación

### 1. Crear el entorno virtual
```powershell
python -m venv venv
```

### 2. Activar el entorno (Windows)
```powershell
.\venv\Scripts\activate
```

### 3. Instalar dependencias
```powershell
pip install -r requirements.txt
```

### 4. Desactivar el entorno (cuando termines)
```powershell
deactivate
```

## 💻 Ejecución

| Objetivo                       | Comando              |
| ------------------------------ | -------------------- |
| Ejecutar todo el flujo         | python main.py       |
| Solo Ejercicio 1 (EDA)         | python main.py -ex 1 |
| Solo Ejercicio 2 (Fusión)      | python main.py -ex 2 |
| Solo Ejercicio 3 (Gráficos)    | python main.py -ex 3 |
| Solo Ejercicio 4 (Estadística) | python main.py -ex 4 |

# Ver ayuda
python main.py -h
```

## 🔄 Funcionamiento

### Flujo de Ejecución ejercicio 1

1. **Configuración inicial**: El programa pregunta si deseas usar una ruta personalizada
   - **Si respondes `s`**: Introduces la ruta completa del archivo
   - **Si respondes `n`**: El programa muestra dos opciones predefinidas (1 o 2)

2. **Carga del dataset**: Se carga el archivo Excel seleccionado

3. **Análisis exploratorio (EDA)**: Se ejecutan automáticamente:
   - **1.1** Muestra las primeras 5 filas
   - **1.2** Lista todas las columnas
   - **1.3** Información del DataFrame (tipos, valores nulos, memoria)

### Flujo de Ejecución ejercicio 2
   - Se ejecuta todo sin interacción del usuario.

### Flujo de Ejecución ejercicio 3
   - Se ejecuta.
   - Solicita el nombre para guardar la imagen.

### Flujo de Ejecución ejercicio 4
   - Se ejecuta todo sin interacción del usuario.



## 🧪 Tests
```powershell
# Ejecutar tests
python -m unittest tests/test_ejercicio1.py -v
```

## 📦 Dependencias

- `pandas` - Manipulación de datos
- `openpyxl` - Lectura de archivos Excel
- `numpy` - Operaciones numéricas
- `spicy` - Funciones estadísticas

## 📄 Licencia

Este proyecto es de uso académico para la asignatura
Programación para la Ciencia de Datos.

## 👤 Autor

Cristina Gómez Campos
Programación para la ciencia de datos - PEC4  
Enero 2026