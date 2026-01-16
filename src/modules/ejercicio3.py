"""
Ejercicio 3: Análisis Visual de Tendencias Temporales.
"""

import os
import matplotlib.pyplot as plt
import pandas as pd


def generar_graficos_series_temporales(df: pd.DataFrame, nombre_alumno: str):
    """
    Genera y guarda visualizaciones de series temporales.
    """
    print("\n3.1. Generando gráficos de series temporales...")

    # Configurar el estilo y la figura
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 10))
    fig.tight_layout(pad=6.0)

    # Obtener ramas únicas para iterar
    ramas = df['Branca'].unique()
    colors = plt.cm.tab10.colors

    for i, branca in enumerate(ramas):
        # Filtrar datos por rama
        df_branca = df[df['Branca'] == branca].sort_values('Curs Acadèmic')
        color = colors[i % len(colors)]

        # Gráfico 1: % Abandonamiento
        ax1.plot(df_branca['Curs Acadèmic'],
                 df_branca['% Abandonament a primer curs'],
                 marker='o', label=branca, color=color)

        # Gráfico 2: Tasa de Rendimiento
        ax2.plot(df_branca['Curs Acadèmic'],
                 df_branca['Taxa rendiment'],
                 marker='s', label=branca, color=color)

    # Configurar Gráfico 1
    ax1.set_title("Evolución del % de Abandono por Curso Académico",
                  fontsize=14, fontweight='bold')
    ax1.set_ylabel("% Abandono")
    ax1.legend(title="Rama de Estudio",
               bbox_to_anchor=(1.05, 1), loc='upper left')
    ax1.grid(True, linestyle='--', alpha=0.7)

    # Configurar Gráfico 2
    ax2.set_title("Evolución de la Tasa de Rendimiento por Curso Académico",
                  fontsize=14, fontweight='bold')
    ax2.set_ylabel("Tasa Rendimiento")
    ax2.set_xlabel("Curso Académico")
    ax2.legend(title="Rama de Estudio", bbox_to_anchor=(1.05, 1),
               loc='upper left')
    ax2.grid(True, linestyle='--', alpha=0.7)

    # Rotar etiquetas eje X
    plt.setp(ax1.get_xticklabels(), rotation=45)
    plt.setp(ax2.get_xticklabels(), rotation=45)

    # 3.2. Guardar Visualizaciones
    output_dir = "src/img"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"📁 Directorio creado: {output_dir}")

    filename = f"evolucion_{nombre_alumno.lower().replace(' ', '_')}.png"
    save_path = os.path.join(output_dir, filename)

    plt.savefig(save_path, dpi=300, bbox_inches='tight')
    plt.close()  # Cerrar figura para liberar memoria

    print(f"💾 Gráfico guardado en: {save_path}")
