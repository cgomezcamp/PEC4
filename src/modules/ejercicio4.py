"""
Ejercicio 4: Análisis estadístico automatizado.
"""

import json
import os
from datetime import datetime
import pandas as pd
from scipy.stats import pearsonr, linregress


def analyze_dataset(merged_df: pd.DataFrame):
    """
    Realiza un análisis estadístico completo y guarda el resultado en JSON.
    """
    print("\n4.1. Iniciando análisis estadístico automatizado...")

    # --- 4.1. Sección Metadata ---
    metadata = {
        "fecha_analisis": datetime.now().strftime("%Y-%m-%d"),
        "num_registros": len(merged_df),
        "periodo_temporal": sorted(merged_df['Curs Acadèmic']
                                   .unique().tolist())
    }

    # --- 4.2. Estadísticas Globales ---
    # Calculamos correlación de Pearson
    corr, p_value = pearsonr(
        merged_df['% Abandonament a primer curs'].dropna(),
        merged_df['Taxa rendiment'].dropna())

    globales = {
        "abandono_medio": float(merged_df['% Abandonament a primer curs']
                                .mean()),
        "rendimiento_medio": float(merged_df['Taxa rendiment'].mean()),
        "correlacion_abandono_rendimiento": float(corr)
    }

    # --- 4.3. Análisis por Rama ---
    analisis_ramas = {}
    ramas = merged_df['Branca'].unique()

    for branch in ramas:
        branch_data = merged_df[merged_df['Branca'] == branch]

        # Agrupar por año para tendencias
        branch_by_year = branch_data.groupby('Curs Acadèmic').agg({
            '% Abandonament a primer curs': 'mean',
            'Taxa rendiment': 'mean'
        }).reset_index()


        def calcular_tendencia(valores):
            if len(valores) < 2:
                return "estable"
            slope, _, _, _, _ = linregress(range(len(valores)), valores)
            if slope > 0.01:
                return "creciente"
            if slope < -0.01:
                return "decreciente"
            return "estable"

        analisis_ramas[branch] = {
            "abandono_medio": float(branch_data['% Abandonament a primer curs']
                                    .mean()),
            "abandono_std": float(branch_data['% Abandonament a primer curs']
                                  .std()),
            "abandono_min": float(branch_data['% Abandonament a primer curs']
                                  .min()),
            "abandono_max": float(branch_data['% Abandonament a primer curs']
                                  .max()),
            "rendimiento_medio": float(branch_data['Taxa rendiment'].mean()),
            "rendimiento_std": float(branch_data['Taxa rendiment'].std()),
            "rendimiento_min": float(branch_data['Taxa rendiment'].min()),
            "rendimiento_max": float(branch_data['Taxa rendiment'].max()),
            "tendencia_abandono": calcular_tendencia(
                branch_by_year['% Abandonament a primer curs'].tolist()),
            "tendencia_rendimiento": calcular_tendencia(
                branch_by_year['Taxa rendiment'].tolist()),
            "años_anomalos": []
        }

    # --- 4.4. Ranking de Ramas ---
    resumen = merged_df.groupby('Branca').agg({
        'Taxa rendiment': 'mean',
        '% Abandonament a primer curs': 'mean'
    })

    rankings = {
        "mejor_rendimiento": [resumen['Taxa rendiment'].idxmax()],
        "peor_rendimiento": [resumen['Taxa rendiment'].idxmin()],
        "mayor_abandono": [resumen['% Abandonament a primer curs'].idxmax()],
        "menor_abandono": [resumen['% Abandonament a primer curs'].idxmin()]
    }

    # Consolidación final según el ejemplo
    resultado_final = {
        "metadata": metadata,
        "estadisticas_globales": globales,
        "analisis_por_rama": analisis_ramas,
        "ranking_ramas": rankings
    }

    # Guardar en src/report/
    output_path = os.path.join("src", "report")
    os.makedirs(output_path, exist_ok=True)

    ruta_json = os.path.join(output_path, "analisi_estadistic.json")
    with open(ruta_json, 'w', encoding='utf-8') as f:
        json.dump(resultado_final, f, indent=2, ensure_ascii=False)

    print(f"💾 Informe JSON generado en: {ruta_json}")
