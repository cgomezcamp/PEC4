# PEC4 - Cristina Gómez Campos

## 📋 Descripción

Este proyecto ha sido desarrollado para la **PEC4**, centrándose en el análisis del sistema universitario catalán.

---

## 📁 Estructura del Proyecto

```
PEC4/
│
├── main.py                          # Punto de entrada y orquestador del proyecto
├── README.md                        # Documentación del proyecto
├── requirements.txt                 # Dependencias necesarias
│
├── src/
│   ├── modules/                     # Lógica central dividida por ejercicios
│   │   ├── __init__.py
│   │   ├── ejercicio1.py            # Carga y Análisis Exploratorio (EDA)
│   │   ├── ejercicio2.py            # Limpieza, normalización y fusión
│   │   ├── ejercicio3.py            # Análisis visual y series temporales
│   │   └── ejercicio4.py            # Estadística avanzada y exportación JSON
│   │
│   ├── utils/
│   │   └── ejecutar_ejercicios.py   # Gestión del flujo de ejecución
│   │
│   ├── img/                         # Gráficos generados (.png)
│   └── report/                      # Informes finales (.json)
│
├── data/                            # Almacén de datos
│   ├── rendiment_estudiants.xlsx
│   ├── taxa_abandonament.xlsx
│   └── dataset_fusionado.csv
│
└── tests/                           # Pruebas unitarias
    ├── test_ejercicio1.py           # Tests para load_dataset y EDA
    ├── test_ejercicio2.py           # Tests para limpieza y fusión
    ├── test_ejercicio3.py           # Tests para análisis visual
    ├── test_ejercicio4.py           # Tests para análisis estadístico
    ├── test_ejecutar_ejercicios.py  # Tests para módulo ejecutor
    ├── test_main.py                 # Tests para punto de entrada
    └── run_tests.py                 # Script ejecutor de tests
```

---

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

---

## 💻 Ejecución

### Comandos disponibles

| Objetivo                       | Comando              |
|-------------------------------|----------------------|
| Ejecutar todo el flujo         | `python main.py`       |
| Solo Ejercicio 1 (EDA)         | `python main.py -ex 1` |
| Solo Ejercicio 2 (Fusión)      | `python main.py -ex 2` |
| Solo Ejercicio 3 (Gráficos)    | `python main.py -ex 3` |
| Solo Ejercicio 4 (Estadística) | `python main.py -ex 4` |

### Ver ayuda

```bash
python main.py -h
```

---

## 🔄 Funcionamiento

### Flujo de Ejecución Ejercicio 1

1. **Configuración inicial**: El programa pregunta si deseas usar una ruta personalizada
   - **Si respondes `s`**: Introduces la ruta completa del archivo
   - **Si respondes `n`**: El programa muestra dos opciones predefinidas (1 o 2)

2. **Carga del dataset**: Se carga el archivo Excel seleccionado

3. **Análisis exploratorio (EDA)**: Se ejecutan automáticamente:
   - **1.1** Muestra las primeras 5 filas
   - **1.2** Lista todas las columnas
   - **1.3** Información del DataFrame (tipos, valores nulos, memoria)

### Flujo de Ejecución Ejercicio 2

- Se ejecuta todo sin interacción del usuario.

### Flujo de Ejecución Ejercicio 3

- Se ejecuta.
- Solicita el nombre para guardar la imagen.

### Flujo de Ejecución Ejercicio 4

- Se ejecuta todo sin interacción del usuario.

---

## 🧪 Tests Unitarios

Este proyecto incluye una suite completa de tests unitarios con `unittest` que cubren todos los módulos principales.

### Estructura de Tests

```
tests/
├── test_ejercicio1.py          # Tests para load_dataset y EDA
├── test_ejercicio2.py          # Tests para limpieza y fusión
├── test_ejercicio3.py          # Tests para análisis visual
├── test_ejercicio4.py          # Tests para análisis estadístico
├── test_ejecutar_ejercicios.py # Tests para módulo ejecutor
├── test_main.py                # Tests para punto de entrada
└── run_tests.py                # Script ejecutor de tests
```

### Ejecutar los Tests

#### Opción 1: Ejecutar todos los tests

```bash
# Windows (PowerShell)
$env:PYTHONPATH = $PWD
python tests/run_tests.py
```

#### Opción 2: Ejecutar tests específicos

```bash
# Un módulo completo
python -m unittest tests.test_ejercicio1 -v
```

### Cobertura de Tests

Para medir la cobertura de código:

```bash
# Instalar coverage
pip install coverage

# Ejecutar tests con cobertura
coverage run -m unittest discover -s tests -p "test_*.py"

# Ver reporte en consola
coverage report -m

# Generar reporte HTML interactivo
coverage html
start htmlcov/index.html
```

**Cobertura actual:** ~95% del código ✅

---

## 📚 Documentación

La documentación del proyecto se genera automáticamente desde los docstrings del código usando Sphinx.

### Generar Documentación

#### Requisitos previos

```bash
pip install sphinx sphinx-rtd-theme
```

#### Generar HTML

```bash
cd docs
sphinx-build -b html source build/html
```

#### Ver documentación

```bash
# Windows
start build/html/index.html
```

---

## 🔍 Linter (Calidad de Código)

El proyecto utiliza **pylint** para garantizar que el código sigue las convenciones de estilo de Python (PEP8) y mantiene alta calidad.

### Ejecutar Análisis

```bash
# Analizar todo el código
pylint src/ main.py

# Ver reporte detallado con score
pylint src/ main.py --reports=y
```

### Configuración

El archivo `.pylintrc` contiene las excepciones justificadas para este proyecto:

- Nombres cortos aceptados en ciencia de datos (`df`, `ax`, `fig`)
- Límites ajustados para funciones de análisis complejas
- Exclusión de warnings de librerías externas (pandas, matplotlib)

### Score de Calidad

**Score obtenido: > 9.85/10** ✅

---

## 📦 Dependencias

Ver `requirements.txt`

---

## 💡 Nota sobre Gestión de Dependencias

> **Nota del desarrollador:** Personalmente prefiero usar **Pipenv** y **Pipfile** para la gestión de dependencias y entornos virtuales en Python, ya que ofrece:
> 
> - Gestión integrada de dependencias y entornos virtuales
> - Resolución automática de conflictos de versiones
> - Lock file determinístico para builds reproducibles
> - Separación clara entre dependencias de producción y desarrollo
>
> Sin embargo, para este proyecto se ha utilizado **virtualenv** y **requirements.txt** siguiendo las especificaciones de la PEC.
>
> **Alternativa con Pipenv:**
> 
> ```bash
> # Si prefieres usar Pipenv
> pip install pipenv
> pipenv install pandas numpy matplotlib openpyxl scipy
> pipenv install --dev pytest coverage pylint sphinx
> pipenv shell
> ```

---

## 📄 Licencia

Este proyecto es de uso académico para la asignatura **Programación para la Ciencia de Datos**.

---

## 👤 Autor

**Cristina Gómez Campos**  
Universitat Oberta de Catalunya (UOC)  
Programación para la Ciencia de Datos - PEC4  
Enero 2026
