#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
generate_panel_inaugural_csv.py
Genera el archivo CSV para Google Classroom con los PDFs de la carpeta
1.PRESENTACION_INAUGURAL_CONJUNTA en CURSO-ROBOTICA-IA-COMUN.
"""

import os
import csv
import urllib.parse
import unicodedata

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
INAUGURAL_DIR = os.path.join(ROOT_DIR, "1.PRESENTACION_INAUGURAL_CONJUNTA")
OUTPUT_DIR = os.path.join(ROOT_DIR, "PANELES_CSV")
os.makedirs(OUTPUT_DIR, exist_ok=True)

BASE_URL = "https://javiercursocorreo-gif.github.io/Curso-Robotica-IA-Comun/"

# Definición de materiales a exportar
ITEMS = [
    {
        "subfolder": "0. INTRODUCCION GENERAL",
        "filename": "1.INTRODUCCION_GENERAL.pdf",
        "tema": "0. Introducción General (Bienvenida y Diagnóstico)",
        "titulo": "1. Presentación Inaugural: Introducción General (Robótica e IA) (PDF)",
        "descripcion": "Diapositivas de la sesión inaugural conjunta: bienvenida, el propósito de la tecnología para personas senior y aprendizaje en grupo sin exámenes."
    },
    {
        "subfolder": "1. INTRODUCCION A LA ROBOTICA",
        "filename": "1.INTRODUCCION_A_LA_ROBOTICA.pdf",
        "tema": "1. Introducción a la Robótica",
        "titulo": "1. Presentación Inaugural: Introducción a la Robótica (PDF)",
        "descripcion": "Diapositivas de introducción a la robótica: qué es un robot, automatización cotidiana y proyectos que construiremos a lo largo del curso."
    },
    {
        "subfolder": "2. INTRODUCCION A LA IA",
        "filename": "1.INTRODUCCION_A_LA_IA.pdf",
        "tema": "2. Introducción a la Inteligencia Artificial",
        "titulo": "1. Presentación Inaugural: Introducción a la IA (PDF)",
        "descripcion": "Diapositivas de introducción a la Inteligencia Artificial: perder el miedo a la IA, qué es y qué no es, y primeros pasos prácticos con Gemini."
    }
]

def generate_csv():
    csv_paths = [
        os.path.join(OUTPUT_DIR, "0.PANEL_PRESENTACION_INAUGURAL.csv"),
        os.path.join(ROOT_DIR, "0.PANEL_PRESENTACION_INAUGURAL.csv")
    ]
    
    rows = []
    for item in ITEMS:
        file_path = os.path.join(INAUGURAL_DIR, item["subfolder"], item["filename"])
        if not os.path.exists(file_path):
            print(f"⚠️ Archivo no encontrado: {file_path}")
            continue
            
        rel_path = os.path.relpath(file_path, ROOT_DIR)
        rel_path_nfc = unicodedata.normalize('NFC', rel_path)
        url_github = BASE_URL + urllib.parse.quote(rel_path_nfc)
        
        rows.append([
            '',
            item["tema"],
            item["titulo"],
            item["descripcion"],
            url_github
        ])
    
    header = ['ID_CURSO', 'TEMA_CLASSROOM', 'TITULO_MATERIAL', 'DESCRIPCION_MATERIAL', 'URL_GITHUB']
    
    for csv_file in csv_paths:
        with open(csv_file, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(header)
            writer.writerows(rows)
        print(f"✅ CSV generado con éxito en: {csv_file}")

if __name__ == "__main__":
    generate_csv()
