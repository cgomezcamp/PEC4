# PEC4 - Ejercicio 1: Load Dataset y EDA

## 📋 Descripción

Implementación del **Ejercicio 1** de la PEC4: carga de datasets y análisis exploratorio de datos (EDA) para el estudio del rendimiento académico y abandono universitario en Cataluña.

## 📁 Estructura del Proyecto
```
proyecto_ej1/
│
├── main.py                      # Punto de entrada principal
├── README.md                    # Esta documentación
├── LICENSE                      # Licencia del proyecto
├── requirements.txt             # Dependencias
│
├── src/
│   └── modules/
│       ├── __init__.py
│       └── ejercicio1.py        # Módulo del ejercicio 1
│
├── tests/
│   └── test_ejercicio1.py      # Tests unitarios
│
└── data/                        # Datasets
    ├── rendiment_estudiants.xlsx
    └── taxa_abandonament.xlsx
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

### Opción 1: Ejecución simple
```powershell
python main.py
```

### Opción 2: Con argumentos
```powershell
# Ejecutar el ejercicio 1 explícitamente
python main.py -ex 1

# Ver ayuda
python main.py -h
```

## 🔄 Funcionamiento

### Flujo de Ejecución

1. **Configuración inicial**: El programa pregunta si deseas usar una ruta personalizada
   - **Si respondes `s`**: Introduces la ruta completa del archivo
   - **Si respondes `n`**: El programa muestra dos opciones predefinidas (1 o 2)

2. **Carga del dataset**: Se carga el archivo Excel seleccionado

3. **Análisis exploratorio (EDA)**: Se ejecutan automáticamente:
   - **1.1** Muestra las primeras 5 filas
   - **1.2** Lista todas las columnas
   - **1.3** Información del DataFrame (tipos, valores nulos, memoria)

### Ejemplo de uso
```
¿Deseas usar una ruta personalizada? (s/n): n

Opciones disponibles:
  1 - rendiment_estudiants.xlsx
  2 - taxa_abandonament.xlsx
Selecciona una opción (1/2): 1

✓ Dataset cargado: 14117 filas, 14 columnas
```

## 📚 Funcionalidades

### `load_dataset(path=None)`
Carga un dataset desde un archivo Excel. Si no se proporciona ruta, pregunta al usuario.

### `realizar_eda(df)`
Ejecuta el análisis exploratorio completo:
- `mostrar_primeras_filas(df, n=5)` - Primeras n filas
- `mostrar_columnas(df)` - Lista de columnas
- `mostrar_info(df)` - Información detallada

## 🧪 Tests
```powershell
# Ejecutar tests
python -m unittest tests/test_ejercicio1.py -v
```

## 📦 Dependencias

- `pandas>=1.3.0` - Manipulación de datos
- `openpyxl>=3.0.0` - Lectura de archivos Excel
- `numpy>=1.21.0` - Operaciones numéricas

## 📄 Licencia

[Especifica tu licencia aquí]

## 👤 Autor

[Tu nombre]  
Programación para la ciencia de datos - PEC4  
Enero 2026