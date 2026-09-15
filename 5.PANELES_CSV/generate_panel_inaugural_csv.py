#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
generate_panel_inaugural_csv.py
Genera los archivos CSV independientes para Google Classroom:
1. 0.PANEL_PRESENTACION_INAUGURAL.csv -> Clase 'ROB+IA. Introducción' (PDF Presentación Conjunta)
2. 1.PANEL_IA_INDICE.csv             -> Clase 'IA.ÍNDICE' (HTML Mapa Mental Interactivo)
"""

import os
import csv
import urllib.parse
import unicodedata

script_dir = os.path.dirname(os.path.abspath(__file__))
if os.path.basename(script_dir) in ("5.PANELES_CSV", "PANELES_CSV"):
    ROOT_DIR = os.path.dirname(script_dir)
else:
    ROOT_DIR = script_dir

OUTPUT_DIR = os.path.join(ROOT_DIR, "5.PANELES_CSV")
os.makedirs(OUTPUT_DIR, exist_ok=True)

BASE_URL = "https://javiercursocorreo-gif.github.io/Curso-Robotica-IA-Comun/"

# 1. Panel para la clase: 'ROB+IA. Introducción'
PANEL_INAUGURAL = {
    "csv_filename": "0.PANEL_PRESENTACION_INAUGURAL.csv",
    "items": [
        {
            "folder": "0.PRESENTACION_PARA_LA_PRIMERA_CLASE",
            "filename": "0.INTRODUCCION CONJUNTA.pdf",
            "tema": "ROB+IA. Introducción",
            "titulo": "Presentación Inaugural Conjunta: Introducción General, Robótica e IA (PDF)",
            "descripcion": "Diapositivas completas de la sesión inaugural conjunta: bienvenida, introducción a la robótica y primeros pasos en inteligencia artificial."
        }
    ]
}

# 2. Panel para la clase: 'IA.ÍNDICE'
PANEL_INDICE = {
    "csv_filename": "1.PANEL_IA_INDICE.csv",
    "items": [
        {
            "folder": "INDICE_DEL_CURSO",
            "filename": "INDICE_DEL_CURSO.html",
            "tema": "IA.ÍNDICE",
            "titulo": "Índice Interactivo del Curso: Robótica e Inteligencia Artificial (HTML)",
            "descripcion": "Mapa mental interactivo para explorar visualmente todos los bloques de robótica y clases de IA del curso."
        }
    ]
}

def export_panel(panel_def):
    csv_file = os.path.join(OUTPUT_DIR, panel_def["csv_filename"])
    rows = []
    
    for item in panel_def["items"]:
        file_path = os.path.join(ROOT_DIR, item["folder"], item["filename"])
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
    
    with open(csv_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(rows)
    print(f"✅ CSV generado con éxito en: {csv_file}")

def generate_csvs():
    export_panel(PANEL_INAUGURAL)
    export_panel(PANEL_INDICE)

if __name__ == "__main__":
    generate_csvs()
