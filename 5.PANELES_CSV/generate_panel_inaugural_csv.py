#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
generate_panel_inaugural_csv.py
Genera el archivo CSV para Google Classroom con el Índice Interactivo (HTML)
y la Presentación Inaugural Conjunta (PDF) en CURSO-ROBOTICA-IA-COMUN.
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

# Definición de materiales para la clase 'ROB+IA. Introducción'
ITEMS = [
    {
        "folder": "INDICE_DEL_CURSO",
        "filename": "INDICE_DEL_CURSO.html",
        "tema": "ROB+IA. Introducción",
        "titulo": "Índice Interactivo del Curso: Robótica e Inteligencia Artificial (HTML)",
        "descripcion": "Mapa mental interactivo para explorar visualmente todos los bloques de robótica y clases de IA del curso."
    },
    {
        "folder": "0.PRESENTACION_PARA_LA_PRIMERA_CLASE",
        "filename": "0.INTRODUCCION CONJUNTA.pdf",
        "tema": "ROB+IA. Introducción",
        "titulo": "Presentación Inaugural Conjunta: Introducción General, Robótica e IA (PDF)",
        "descripcion": "Diapositivas completas de la sesión inaugural conjunta: bienvenida, introducción a la robótica y primeros pasos en inteligencia artificial."
    }
]

def generate_csv():
    csv_paths = [
        os.path.join(OUTPUT_DIR, "0.PANEL_PRESENTACION_INAUGURAL.csv")
    ]
    
    rows = []
    for item in ITEMS:
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
    
    for csv_file in csv_paths:
        with open(csv_file, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(header)
            writer.writerows(rows)
        print(f"✅ CSV generado con éxito en: {csv_file}")

if __name__ == "__main__":
    generate_csv()
