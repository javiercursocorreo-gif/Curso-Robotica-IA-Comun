#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
generate_panel_inaugural_csv.py
Genera el archivo CSV para Google Classroom:
0.PANEL_PRESENTACION_INAUGURAL.csv -> Clase 'ROB+IA. Introducción'
Incluye:
1. Presentación Inaugural Conjunta (PDF)
2. Guía Visual de Google Classroom (PDF)
"""

import os
import csv
import urllib.parse
import unicodedata

script_dir = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(script_dir) if os.path.basename(script_dir).endswith("PANELES_CSV") else script_dir
OUTPUT_DIR = os.path.join(ROOT_DIR, "6.PANELES_CSV")
os.makedirs(OUTPUT_DIR, exist_ok=True)

BASE_URL = "https://javiercursocorreo-gif.github.io/Curso-Robotica-IA-Comun/"

PANEL_INAUGURAL = {
    "csv_filename": "0.PANEL_PRESENTACION_INAUGURAL.csv",
    "items": [
        {
            "folder": "0.PRESENTACION_PARA_LA_PRIMERA_CLASE",
            "filename_pattern": "*0.INTRODUCCION CONJUNTA.pdf",
            "tema": "ROB+IA. Introducción",
            "titulo": "Presentación Inaugural Conjunta: Introducción General, Robótica e IA (PDF)",
            "descripcion": "Diapositivas completas de la sesión inaugural conjunta: bienvenida, introducción a la robótica y primeros pasos en inteligencia artificial."
        },
        {
            "folder": "1. GOOGLE_CLASSROOM",
            "filename_pattern": "Guía_de_Classroom.pdf",
            "tema": "ROB+IA. Introducción",
            "titulo": "Guía Visual de Google Classroom: Publicación y Gestión del Aula (PDF)",
            "descripcion": "Manual ilustrado paso a paso para el uso, acceso a materiales y gestión de actividades en Google Classroom."
        }
    ]
}

def find_file(folder_path, pattern):
    if not os.path.exists(folder_path):
        return None
    for f in os.listdir(folder_path):
        if pattern in f or unicodedata.normalize('NFC', pattern) in unicodedata.normalize('NFC', f) or unicodedata.normalize('NFD', pattern) in unicodedata.normalize('NFD', f):
            return f
        if pattern.replace('Guía', 'Gu') in f or pattern.replace('í', '') in f:
            return f
    return None

def export_panel(panel_def):
    csv_file = os.path.join(OUTPUT_DIR, panel_def["csv_filename"])
    rows = []
    
    for item in panel_def["items"]:
        folder_path = os.path.join(ROOT_DIR, item["folder"])
        found_name = find_file(folder_path, item["filename_pattern"])
        if not found_name:
            print(f"⚠️ Archivo no encontrado para patrón '{item['filename_pattern']}' en {folder_path}")
            continue
            
        file_path = os.path.join(folder_path, found_name)
        rel_path = os.path.relpath(file_path, ROOT_DIR)
        rel_path_nfc = unicodedata.normalize('NFC', rel_path)
        url_github = BASE_URL + urllib.parse.quote(rel_path_nfc)
        
        # Limpiar comas internas para parseo estricto
        desc_clean = item["descripcion"].replace(",", " -")
        
        rows.append([
            '',
            item["tema"],
            item["titulo"],
            desc_clean,
            url_github
        ])
    
    header = ['ID_CURSO', 'TEMA_CLASSROOM', 'TITULO_MATERIAL', 'DESCRIPCION_MATERIAL', 'URL_GITHUB']
    
    with open(csv_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(rows)
    print(f"✅ CSV generado con éxito en: {csv_file}")

if __name__ == "__main__":
    export_panel(PANEL_INAUGURAL)
