#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
generar_bitacora_completa_nativa.py
Genera 'BITACORA_SEGUIMIENTO_CLASES.xlsx' utilizando EXCLUSIVAMENTE
la biblioteca estándar de Python (sin pip, sin openpyxl, sin dependencias externas).
Crea 2 hojas oficiales:
1. 'Bitacora de Clases' (Registro real acumulado hasta Clase 13 [12/11/2026] + Resumen de Métricas).
2. 'Calendario Oficial Robótica-IA' (Itinerario oficial definitivo de 46 clases restantes:
   21 Robótica + 7 Monográficos con NASA a 2 días + 18 Sesiones IA Comodín,
   cero clases consecutivas de Robótica y arranque en limpio con Sesión 05 a la vuelta de Navidad).
"""

import os
import zipfile
import datetime
import subprocess
import shutil

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
EXCEL_PATH = os.path.join(BASE_DIR, "BITACORA_SEGUIMIENTO_CLASES.xlsx")

# ------------------------------------------------------------------------------
# DEFINICIÓN DE XMLS BASE (100% ESTÁNDAR ECMA-376)
# ------------------------------------------------------------------------------

content_types = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
  <Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>
  <Default Extension="xml" ContentType="application/xml"/>
  <Override PartName="/xl/workbook.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet.main+xml"/>
  <Override PartName="/xl/worksheets/sheet1.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.worksheet+xml"/>
  <Override PartName="/xl/worksheets/sheet2.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.worksheet+xml"/>
  <Override PartName="/xl/styles.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.styles+xml"/>
</Types>"""

root_rels = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="xl/workbook.xml"/>
</Relationships>"""

wb_rels = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/worksheet" Target="worksheets/sheet1.xml"/>
  <Relationship Id="rId2" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/worksheet" Target="worksheets/sheet2.xml"/>
  <Relationship Id="rId3" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/styles" Target="styles.xml"/>
</Relationships>"""

workbook_xml = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<workbook xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships">
  <sheets>
    <sheet name="Bitacora de Clases" sheetId="1" r:id="rId1"/>
    <sheet name="Calendario Oficial Robótica-IA" sheetId="2" r:id="rId2"/>
  </sheets>
</workbook>"""

# Estilos:
# Style 0: normal
# Style 1: Titulo azul negrita 14pt
# Style 2: Cabecera Navy (texto blanco negrita, fondo 1F497D, bordes)
# Style 3: Cabecera Teal (texto blanco negrita, fondo 005E5D, bordes)
# Style 4: Borde normal, negrita
# Style 5: Borde normal, regular
# Style 6: Borde normal, italica gris
# Style 7: Alerta / Destacado (fondo azul claro DCE6F1, texto rojo oscuro negrita, borde)
# Style 8: Fila Verde Pastel (E2EFDA, borde) -> Impartida
# Style 9: Fila Naranja Pastel (FCE4D6, borde) -> Robótica
# Style 10: Fila Morado Pastel (EDEDF8, borde) -> IA Comodín
# Style 11: Fila Gris Festivo (F2F2F2, texto gris, borde) -> Festivo / Vacaciones
# Style 12: Cabecera Púrpura (texto blanco negrita, fondo 4A235A, bordes)
# Style 13: Fila Amarillo Pastel (FFF2CC, borde) -> Monográfico Especial / Hito
styles_xml = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<styleSheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main">
  <fonts count="7">
    <font><sz val="11"/><name val="Calibri"/></font>
    <font><b/><sz val="14"/><color rgb="FF1F497D"/><name val="Calibri"/></font>
    <font><b/><sz val="11"/><color rgb="FFFFFFFF"/><name val="Calibri"/></font>
    <font><b/><sz val="11"/><name val="Calibri"/></font>
    <font><i/><sz val="10"/><color rgb="FF595959"/><name val="Calibri"/></font>
    <font><b/><sz val="11"/><color rgb="FF9C0006"/><name val="Calibri"/></font>
    <font><b/><sz val="11"/><color rgb="FF7D6608"/><name val="Calibri"/></font>
  </fonts>
  <fills count="11">
    <fill><patternFill patternType="none"/></fill>
    <fill><patternFill patternType="gray125"/></fill>
    <fill><patternFill patternType="solid"><fgColor rgb="FF1F497D"/></patternFill></fill>
    <fill><patternFill patternType="solid"><fgColor rgb="FF005E5D"/></patternFill></fill>
    <fill><patternFill patternType="solid"><fgColor rgb="FFDCE6F1"/></patternFill></fill>
    <fill><patternFill patternType="solid"><fgColor rgb="FFE2EFDA"/></patternFill></fill>
    <fill><patternFill patternType="solid"><fgColor rgb="FFFCE4D6"/></patternFill></fill>
    <fill><patternFill patternType="solid"><fgColor rgb="FFEDEDF8"/></patternFill></fill>
    <fill><patternFill patternType="solid"><fgColor rgb="FFF2F2F2"/></patternFill></fill>
    <fill><patternFill patternType="solid"><fgColor rgb="FF4A235A"/></patternFill></fill>
    <fill><patternFill patternType="solid"><fgColor rgb="FFFFF2CC"/></patternFill></fill>
  </fills>
  <borders count="2">
    <border><left/><right/><top/><bottom/><diagonal/></border>
    <border>
      <left style="thin"><color rgb="FFD9D9D9"/></left>
      <right style="thin"><color rgb="FFD9D9D9"/></right>
      <top style="thin"><color rgb="FFD9D9D9"/></top>
      <bottom style="thin"><color rgb="FFD9D9D9"/></bottom>
    </border>
  </borders>
  <cellStyleXfs count="1">
    <xf numFmtId="0" fontId="0" fillId="0" borderId="0"/>
  </cellStyleXfs>
  <cellXfs count="14">
    <xf numFmtId="0" fontId="0" fillId="0" borderId="0" xfId="0"/>
    <xf numFmtId="0" fontId="1" fillId="0" borderId="0" xfId="0" applyFont="1"/>
    <xf numFmtId="0" fontId="2" fillId="2" borderId="1" xfId="0" applyFont="1" applyFill="1" applyBorder="1"/>
    <xf numFmtId="0" fontId="2" fillId="3" borderId="1" xfId="0" applyFont="1" applyFill="1" applyBorder="1"/>
    <xf numFmtId="0" fontId="3" fillId="0" borderId="1" xfId="0" applyFont="1" applyBorder="1"/>
    <xf numFmtId="0" fontId="0" fillId="0" borderId="1" xfId="0" applyBorder="1"/>
    <xf numFmtId="0" fontId="4" fillId="0" borderId="1" xfId="0" applyFont="1" applyBorder="1"/>
    <xf numFmtId="0" fontId="5" fillId="4" borderId="1" xfId="0" applyFont="1" applyFill="1" applyBorder="1"/>
    <xf numFmtId="0" fontId="0" fillId="5" borderId="1" xfId="0" applyFill="1" applyBorder="1"/>
    <xf numFmtId="0" fontId="0" fillId="6" borderId="1" xfId="0" applyFill="1" applyBorder="1"/>
    <xf numFmtId="0" fontId="0" fillId="7" borderId="1" xfId="0" applyFill="1" applyBorder="1"/>
    <xf numFmtId="0" fontId="4" fillId="8" borderId="1" xfId="0" applyFont="1" applyFill="1" applyBorder="1"/>
    <xf numFmtId="0" fontId="2" fillId="9" borderId="1" xfId="0" applyFont="1" applyFill="1" applyBorder="1"/>
    <xf numFmtId="0" fontId="6" fillId="10" borderId="1" xfId="0" applyFont="1" applyFill="1" applyBorder="1"/>
  </cellXfs>
</styleSheet>"""

def escape_xml(v):
    return str(v).replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;').replace('"', '&quot;')

def cell_xml(ref, val, s=0):
    val_str = escape_xml(val)
    if isinstance(val, (int, float)):
        return f'<c r="{ref}" s="{s}"><v>{val}</v></c>'
    return f'<c r="{ref}" t="inlineStr" s="{s}"><is><t>{val_str}</t></is></c>'

# ------------------------------------------------------------------------------
# DATOS HISTÓRICOS REALES (CLASES IMPARTIDAS 1 A 11)
# ------------------------------------------------------------------------------
clases_impartidas_data = [
    (1, "01/10/2026", "Jueves", "1.5 h", "Presentación inaugural", "Primer día de clase", "Presentación del curso y bienvenida", "General"),
    (2, "06/10/2026", "Martes", "1.5 h", "Guía de Classroom y Gemini", "Segunda clase organizativa", "Manejo de herramientas básicas y Classroom", "General"),
    (3, "08/10/2026", "Jueves", "1.5 h", "Sesión IA 01", "Sesión IA 01 impartida", "Introducción a prompts y generación de texto", "IA"),
    (4, "13/10/2026", "Martes", "1.5 h", "Sesión IA 01", "Sesión IA 01 impartida", "Práctica guiada en Gemini", "IA"),
    (5, "15/10/2026", "Jueves", "1.5 h", "Sesión IA 01", "Sesión IA 01 impartida", "Profundización y análisis de respuestas", "IA"),
    (6, "20/10/2026", "Martes", "1.5 h", "Sesión IA 01", "Sesión IA 01 impartida (4 clases en total)", "Conclusión y evaluación Sesión 01", "IA"),
    (7, "22/10/2026", "Jueves", "1.5 h", "ROB.1: 1.1 Puerta supermercado", "Práctica de motor y engranajes (1 día)", "Montaje físico y programación de apertura", "Robótica"),
    (8, "27/10/2026", "Martes", "1.5 h", "Monográfico 2 IA entero", "Monográfico 2 IA impartido entero", "NotebookLM y fuentes documentales", "IA (Monográfico)"),
    (9, "29/10/2026", "Jueves", "1.5 h", "ROB.1: 1.2 Lavadora + IA: Sesión 2 (Ítems 09 y 09B)", "Impartidos ROB.1 (1.2 en 1 día) y 2 ítems de IA Sesión 2", "Lavadora terminada y arranque Sesión 2", "Mixta"),
    (10, "03/11/2026", "Martes", "1.5 h", "IA: Sesión 02 (Radar Anti-Estafas - Hasta ítem 09 incluido)", "Impartida hasta ítem 09 incluido", "Detección de fraudes y timos cotidianos", "IA"),
    (11, "05/11/2026", "Jueves", "1.5 h", "ROB.1: 1.3 Ascensor + IA: Sesión 02 (Ítems 10 a 13)", "Impartido ROB 1.3 Ascensor y avance IA Sesión 02 (10-13)", "Ascensor terminado con éxito", "Mixta"),
    (12, "10/11/2026", "Martes", "1.5 h", "IA: Sesión 02 (Radar Anti-Estafas - Finalización ítems 14 a 19)", "Finalización de Sesión 02", "Radar Anti-Estafas concluido al 100% con éxito", "IA"),
    (13, "12/11/2026", "Jueves", "1.5 h", "ROB.1: 1.4 Semáforos inteligentes (Fase 2: P3. Bloques y P4. Juego)", "Impartida Clase 1.4 Semáforos: P3. Bloques y P4. Juego", "Programación por bloques y retos interactivos de tráfico autónomo", "Robótica")
]

# ------------------------------------------------------------------------------
# HOJA 1: BITÁCORA DE CLASES (HISTORIAL REAL + MÉTRICAS)
# ------------------------------------------------------------------------------
def build_bitacora_rows():
    rows = []
    title = "BITÁCORA OFICIAL DE SEGUIMIENTO DE CLASES"
    sub = "Registro acumulado de clases impartidas de Robótica e Inteligencia Artificial (Curso 2026-2027)"
    h_style = 2

    rows.append(f'<row r="1" ht="20">{cell_xml("A1", title, 1)}</row>')
    rows.append(f'<row r="2" ht="16">{cell_xml("A2", sub, 6)}</row>')

    r_box = [
        ("MÉTRICA DEL CURSO", "VALOR", "ESTADO AL 12/11/2026"),
        ("Sesiones Impartidas Acumuladas", "13 clases", "Octubre - Noviembre 2026"),
        ("Horas Lectivas Impartidas", "19.5 h", "Equivalente al 22.0% del curso oficial"),
        ("Sesiones Lectivas Restantes", "46 clases (69.0 h)", "Hasta el 27 de mayo de 2027"),
        ("Total Sesiones Planificadas", "59 clases (88.5 h)", "Cálculo oficial con festivos excluidos"),
        ("Robótica Impartida", "4 robots completos", "1.1 Puerta, 1.2 Lavadora, 1.3 Ascensor y 1.4 Semáforos (P3 y P4)"),
        ("IA Impartida", "Sesión 01 + Sesión 02 (100%) + Mono 2", "Próxima sesión arranca Sesión 03")
    ]
    for ro, (c1, c2, c3) in enumerate(r_box, start=4):
        st = h_style if ro == 4 else 5
        st_val = h_style if ro == 4 else 4
        rows.append(f'<row r="{ro}" ht="16">{cell_xml(f"B{ro}", c1, st)}{cell_xml(f"C{ro}", c2, st_val)}{cell_xml(f"D{ro}", c3, st)}</row>')

    rows.append(f'<row r="12" ht="18">' +
                cell_xml("A12", "Nº", h_style) + cell_xml("B12", "FECHA", h_style) + cell_xml("C12", "DÍA", h_style) +
                cell_xml("D12", "DURACIÓN", h_style) + cell_xml("E12", "ÁREA", h_style) + cell_xml("F12", "HORAS ACUM.", h_style) +
                cell_xml("G12", "TEMARIO IMPARTIDO", h_style) + cell_xml("H12", "OBSERVACIONES / DETALLES", h_style) + '</row>')

    h_acum = 0.0
    for r_idx, item in enumerate(clases_impartidas_data, start=13):
        h_acum += 1.5
        c_num, c_fec, c_dia, c_dur, c_tem, c_obs, c_det, c_area = item
        f_st = 8
        rows.append(f'<row r="{r_idx}" ht="16">' +
                    cell_xml(f"A{r_idx}", c_num, f_st) + cell_xml(f"B{r_idx}", c_fec, f_st) + cell_xml(f"C{r_idx}", c_dia, f_st) +
                    cell_xml(f"D{r_idx}", c_dur, f_st) + cell_xml(f"E{r_idx}", c_area, f_st) + cell_xml(f"F{r_idx}", f"{h_acum:.1f} h", f_st) +
                    cell_xml(f"G{r_idx}", c_tem, f_st) + cell_xml(f"H{r_idx}", f"{c_obs} — {c_det}", f_st) + '</row>')

    return f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<worksheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main">
  <cols>
    <col min="1" max="1" width="8" customWidth="1"/>
    <col min="2" max="2" width="14" customWidth="1"/>
    <col min="3" max="3" width="12" customWidth="1"/>
    <col min="4" max="4" width="12" customWidth="1"/>
    <col min="5" max="5" width="18" customWidth="1"/>
    <col min="6" max="6" width="14" customWidth="1"/>
    <col min="7" max="7" width="55" customWidth="1"/>
    <col min="8" max="8" width="55" customWidth="1"/>
  </cols>
  <sheetData>
    {''.join(rows)}
  </sheetData>
</worksheet>"""

sheet1_xml = build_bitacora_rows()

# ------------------------------------------------------------------------------
# HOJA 2: CALENDARIO OFICIAL ROBÓTICA - IA (48 CLASES RESTANTES)
# ------------------------------------------------------------------------------
holidays_dict = {
    datetime.date(2026, 10, 12): "Fiesta Nacional de España",
    datetime.date(2026, 11, 1): "Todos los Santos",
    datetime.date(2026, 11, 2): "Traslado Todos los Santos",
    datetime.date(2026, 11, 9): "La Almudena (Madrid)",
    datetime.date(2026, 12, 6): "Día de la Constitución",
    datetime.date(2026, 12, 7): "Puente de la Constitución",
    datetime.date(2026, 12, 8): "Inmaculada Concepción",
    datetime.date(2027, 1, 6): "Día de Reyes",
    datetime.date(2027, 3, 19): "San José",
    datetime.date(2027, 5, 1): "Fiesta del Trabajo",
    datetime.date(2027, 5, 2): "Fiesta de la Comunidad de Madrid",
    datetime.date(2027, 5, 3): "Traslado Comunidad de Madrid",
    datetime.date(2027, 5, 15): "San Isidro (Madrid)"
}

cur = datetime.date(2026, 12, 22)
while cur <= datetime.date(2027, 1, 7):
    holidays_dict[cur] = "Vacaciones de Navidad"
    cur += datetime.timedelta(days=1)

cur = datetime.date(2027, 3, 22)
while cur <= datetime.date(2027, 3, 30):
    holidays_dict[cur] = "Vacaciones de Semana Santa"
    cur += datetime.timedelta(days=1)

def build_official_calendar_rows():
    rows = []
    title = "CALENDARIO OFICIAL DE CLASES (ROBÓTICA E IA)"
    sub = "Itinerario Definitivo: 21 Robótica + 7 Monográficos IA (NASA 2 días) + 18 Sesiones IA Comodín (59 lectivas totales, Cero Robots Consecutivos)"
    h_style = 3

    rows.append(f'<row r="1" ht="20">{cell_xml("A1", title, 1)}</row>')
    rows.append(f'<row r="2" ht="16">{cell_xml("A2", sub, 6)}</row>')

    r_box = [
        ("PARÁMETRO DEL CURSO", "VALOR", "DIAGNÓSTICO AL 30 DE MAYO"),
        ("Total Sesiones Lectivas Restantes", "46 clases (69.0 h)", "De 17/11/2026 a 27/05/2027"),
        ("Robótica Programada (Bloques 1 al 6)", "21 clases restantes (25 totales)", "2.1-2.3, 3.1, 3.3-3.5, 4.5-4.6, B5 entero (MIXAMO 2 días), B6.1-B6.4 (Star Wars 2 días)"),
        ("IA Programada (Monográficos + Sesiones)", "25 clases restantes (34 totales)", "7 Monográficos (NASA 2 días) + Sesiones 03 a 11 (2 días) + Sesión 12"),
        ("¿LLEGAMOS BIEN O NOS PASAMOS?", "🎯 ENCAJE EXACTO (46 / 46)", "¡CERO DÍAS DE DESVIACIÓN! Cierre oficial el 27/05/2027"),
        ("Consecutividad de Robótica", "0 clases consecutivas", "Siempre IA o Monográfico entre robots (alternancia limpia)"),
        ("Ajuste de Navidad", "Corte limpio en Sesión 04", "Arranque en limpio con Sesión 05 a la vuelta de vacaciones"),
        ("Techo Robótica al 27 de Mayo", "Bloque 6.4 (Interstellar)", "Naves espaciales, Star Trek, Gran Museo Star Wars y Androides"),
        ("Techo IA al 27 de Mayo", "Sesión 12 Comodín + 7 Monográficos", "Lote 1 completo (Sesiones 01 a 10) + Sesiones 11 y 12")
    ]
    for ro, (c1, c2, c3) in enumerate(r_box, start=4):
        st = h_style if ro == 4 else (7 if "LLEGAMOS" in c1 else 5)
        st_val = h_style if ro == 4 else (7 if "LLEGAMOS" in c1 else 4)
        rows.append(f'<row r="{ro}" ht="16">{cell_xml(f"B{ro}", c1, st)}{cell_xml(f"C{ro}", c2, st_val)}{cell_xml(f"D{ro}", c3, st)}</row>')

    rows.append(f'<row r="14" ht="18">' +
                cell_xml("A14", "Nº CLASE", h_style) + cell_xml("B14", "FECHA", h_style) + cell_xml("C14", "DÍA", h_style) +
                cell_xml("D14", "ÁREA", h_style) + cell_xml("E14", "ESTADO", h_style) +
                cell_xml("F14", "TEMARIO PROYECTADO", h_style) + cell_xml("G14", "HORAS ACUM.", h_style) + cell_xml("H14", "HITO PEDAGÓGICO", h_style) + '</row>')

    # 46 clases proyectadas oficiales
    future_schedule = [
        # Clase 14 (17/11/2026, Mar)
        ("IA", "IA: Sesión 03 (Pinacoteca, Estilos Visuales & Arte - Día 1/2)", "Sesión 03 [Sin cómics]"),
        # Clase 15 (19/11/2026, Jue)
        ("IA (Monográfico)", "IA: Monográfico 2 (Mundo Digital Senior / NotebookLM)", "Día 19 - Asistencia completa"),
        # Clase 16 (24/11/2026, Mar)
        ("IA (Monográfico)", "IA: Monográfico 3 (Taller Especial Cuentos y Cómics con NLM)", "Continuación Mono 2"),
        # Clase 17 (26/11/2026, Jue)
        ("Robótica", "ROB: 2.1 Silla de Ruedas Eléctrica (Tracción diferencial)", "Inicio Bloque 2"),
        # Clase 18 (01/12/2026, Mar)
        ("IA", "IA: Sesión 03 (Ciencia, Vida Práctica & Radar Geopolítica - Día 2/2)", "Fin Sesión 03 (15 recursos)"),
        # Clase 19 (03/12/2026, Jue)
        ("Robótica", "ROB: 2.2 Roomba con sensor (Bucle infinito y evasión)", "Bloque 2"),
        # Clase 20 (10/12/2026, Jue)
        ("IA (Monográfico)", "IA: Monográfico 4 (Mi Biografía con IA y Redacción Guiada)", "Monográfico 4"),
        # Clase 21 (15/12/2026, Mar)
        ("Robótica", "ROB: 2.3 Aparcamiento asistido (Condición IF-ELSE)", "Fin Bloque 2"),
        # Clase 22 (17/12/2026, Jue)
        ("IA", "IA: Sesión 04 (Aporte de Valor Senior y Prompts Cotidianos)", "Cierre previo a Navidad"),

        # --- VUELTA DE NAVIDAD: ARRANCAMOS DIRECTO CON SESIÓN 05 (NO SE CONTINÚA LA 4 A MEDIAS) ---
        # Clase 23 (12/01/2027, Mar)
        ("IA", "IA: Sesión 05 (Creatividad Visual y Generación de Imagen - Día 1/2)", "Arranque en limpio Sesión 05"),
        # Clase 24 (14/01/2027, Jue)
        ("IA (Monográfico)", "IA: Monográfico 5 (El Abuelo Tutor: Matemáticas e Historia)", "Monográfico 5"),
        # Clase 25 (19/01/2027, Mar)
        ("Robótica", "ROB: 3.1 Robot repartidor (Chasis diferencial y ruta)", "Inicio Bloque 3"),
        # Clase 26 (21/01/2027, Jue)
        ("IA", "IA: Sesión 05 (Diseño Gráfico, Museos y Modelos - Día 2/2)", "Fin Sesión 05"),
        # Clase 27 (26/01/2027, Mar)
        ("Robótica", "ROB: 3.3 Avión con servos (Posición angular exacta)", "Bloque 3"),
        # Clase 28 (28/01/2027, Jue)
        ("IA (Monográfico)", "IA: Monográfico 6 (Mapa y Gestión de Proyectos con IA)", "Monográfico 6"),
        # Clase 29 (02/02/2027, Mar)
        ("Robótica", "ROB: 3.4 Dron autónomo (Navegación 3D)", "Bloque 3"),
        # Clase 30 (04/02/2027, Jue)
        ("IA", "IA: Sesión 06 (Asistente Personal de Salud y Bienestar - Día 1/2)", "Inicio Sesión 06"),
        # Clase 31 (09/02/2027, Mar)
        ("Robótica", "ROB: 3.5 Penguin-BOT (Sincronización cinemática)", "Fin Bloque 3"),
        # Clase 32 (11/02/2027, Jue)
        ("IA", "IA: Sesión 06 (Medicación y Hábitos de Vida Diaria - Día 2/2)", "Fin Sesión 06"),
        # Clase 33 (16/02/2027, Mar)
        ("Robótica", "ROB: 4.5 Pinza robótica (Sensor de presión y agarre)", "Brazo Robótico"),
        # Clase 34 (18/02/2027, Jue)
        ("IA (Monográfico)", "IA: Monográfico 7 (NASA y Exploración Espacial con IA - Día 1/2: Web y Enlaces)", "Mono 7 NASA [Día 1/2]"),
        # Clase 35 (23/02/2027, Mar)
        ("Robótica", "ROB: 4.6 Mano hidráulica (Cinemática y fuerza)", "Fin Bloque 4"),
        # Clase 36 (25/02/2027, Jue)
        ("IA (Monográfico)", "IA: Monográfico 7 (NASA y Exploración Espacial con IA - Día 2/2: Visores 3D)", "Mono 7 NASA [Día 2/2 - FIN MONOS]"),
        # Clase 37 (02/03/2027, Mar)
        ("Robótica", "ROB: 5.1 Perro Unitree Go2 AIR (LiDAR cuadrúpedo)", "Inicio Bloque 5"),
        # Clase 38 (04/03/2027, Jue)
        ("IA", "IA: Sesión 07 (Domótica y Entorno Inteligente - Día 1/2)", "Inicio Sesión 07"),
        # Clase 39 (09/03/2027, Mar)
        ("Robótica", "ROB: 5.2 Robot Bípedo (Equilibrio dinámico)", "Bloque 5"),
        # Clase 40 (11/03/2027, Jue)
        ("IA", "IA: Sesión 07 (Control por Voz y Asistencia en el Hogar - Día 2/2)", "Fin Sesión 07"),
        # Clase 41 (16/03/2027, Mar)
        ("Robótica", "ROB: 5.3 Androide MIXAMO (Parte 1/2: Captura cinemática)", "MIXAMO [Día 1/2]"),
        # Clase 42 (18/03/2027, Jue)
        ("IA", "IA: Sesión 08 (Fotogrametría y Reconstrucción 3D - Día 1/2)", "Inicio Sesión 08"),

        # --- SEMANA SANTA ---
        # Clase 43 (01/04/2027, Jue)
        ("Robótica", "ROB: 5.3 Androide MIXAMO (Parte 2/2: Prácticas y animación)", "MIXAMO [Día 2/2]"),
        # Clase 44 (06/04/2027, Mar)
        ("IA", "IA: Sesión 08 (Museografía Virtual y Patrimonio - Día 2/2)", "Fin Sesión 08"),
        # Clase 45 (08/04/2027, Jue)
        ("Robótica", "ROB: 5.4 Transformer (POO y cambio morfológico)", "Bloque 5"),
        # Clase 46 (13/04/2027, Mar)
        ("IA", "IA: Sesión 09 (Música e IA Sonora: Composición y MIDI - Día 1/2)", "Inicio Sesión 09"),
        # Clase 47 (15/04/2027, Jue)
        ("Robótica", "ROB: 5.5 Trío Dinámico Star Wars (R2-D2, BB-8, D-O)", "Bloque 5"),
        # Clase 48 (20/04/2027, Mar)
        ("IA", "IA: Sesión 09 (Música e IA Sonora: Síntesis y Audio - Día 2/2)", "Fin Sesión 09"),
        # Clase 49 (22/04/2027, Jue)
        ("Robótica", "ROB: 5.6 Robot de Combate (Estructura reforzada)", "Fin Bloque 5"),
        # Clase 50 (27/04/2027, Mar)
        ("IA", "IA: Sesión 10 (Cierre y Evaluación de Modelos - Día 1/2)", "Inicio Sesión 10"),
        # Clase 51 (29/04/2027, Jue)
        ("Robótica", "ROB: 6.1 Transporte Espacial Autónomo", "Inicio Bloque 6"),
        # Clase 52 (04/05/2027, Mar)
        ("IA", "IA: Sesión 10 (Muestra Interactiva y Proyectos - Día 2/2)", "Fin Lote 1 IA"),
        # Clase 53 (06/05/2027, Jue)
        ("Robótica", "ROB: 6.2 Star Wars (Parte 1/2: Naves y Teoría)", "Star Wars [Día 1/2]"),
        # Clase 54 (11/05/2027, Mar)
        ("IA", "IA: Sesión 11 (Stradivarius y Acústica Musical - Día 1/2)", "Inicio Sesión 11"),
        # Clase 55 (13/05/2027, Jue)
        ("Robótica", "ROB: 6.2 Star Wars (Parte 2/2: El Gran Museo de Star Wars)", "Gran Museo [Día 2/2]"),
        # Clase 56 (18/05/2027, Mar)
        ("IA", "IA: Sesión 11 (Stradivarius y Acústica Musical - Día 2/2)", "Fin Sesión 11"),
        # Clase 57 (20/05/2027, Jue)
        ("Robótica", "ROB: 6.3 Star Trek (Naves estelares)", "Bloque 6"),
        # Clase 58 (25/05/2027, Mar)
        ("IA", "IA: Sesión 12 (Biomedicina, Genética y ADN 3D con IA)", "Sesión 12 Comodín"),
        # Clase 59 (27/05/2027, Jue)
        ("Robótica", "ROB: 6.4 Interstellar (Física orbital y naves)", "Fin de Curso Oficial")
    ]

    cur_d = datetime.date(2026, 10, 1)
    end_d = datetime.date(2027, 5, 30)
    r_num = 15
    clase_cont = 1
    h_acum = 0.0

    while cur_d <= end_d:
        if cur_d.weekday() in (1, 3):
            d_name = "Martes" if cur_d.weekday() == 1 else "Jueves"
            d_str = cur_d.strftime("%d/%m/%Y")

            if cur_d in holidays_dict:
                rows.append(f'<row r="{r_num}" ht="16">' +
                            cell_xml(f"A{r_num}", "-", 11) + cell_xml(f"B{r_num}", d_str, 11) + cell_xml(f"C{r_num}", d_name, 11) +
                            cell_xml(f"D{r_num}", "Vacaciones", 11) + cell_xml(f"E{r_num}", "No Lectivo", 11) +
                            cell_xml(f"F{r_num}", f"⛔ {holidays_dict[cur_d]}", 11) + cell_xml(f"G{r_num}", f"{h_acum:.1f} h", 11) +
                            cell_xml(f"H{r_num}", "Sin clase programada", 11) + '</row>')
            else:
                h_acum += 1.5
                if clase_cont <= 13:
                    item_real = clases_impartidas_data[clase_cont - 1]
                    area_v = item_real[7]
                    tem_v = item_real[4]
                    obs_v = item_real[6]
                    est_v = "Impartida"
                    f_st = 8
                else:
                    f_idx = clase_cont - 14
                    area_v, tem_v, obs_v = future_schedule[f_idx]
                    est_v = "Proyectada"
                    if "Monográfico" in area_v:
                        f_st = 13  # Amarillo Pastel
                    elif area_v == "Robótica":
                        f_st = 9   # Naranja Pastel
                    else:
                        f_st = 10  # Morado Pastel para Sesiones IA Comodín

                rows.append(f'<row r="{r_num}" ht="16">' +
                            cell_xml(f"A{r_num}", clase_cont, f_st) + cell_xml(f"B{r_num}", d_str, f_st) + cell_xml(f"C{r_num}", d_name, f_st) +
                            cell_xml(f"D{r_num}", area_v, f_st) + cell_xml(f"E{r_num}", est_v, f_st) +
                            cell_xml(f"F{r_num}", tem_v, f_st) + cell_xml(f"G{r_num}", f"{h_acum:.1f} h", f_st) +
                            cell_xml(f"H{r_num}", obs_v, f_st) + '</row>')
                clase_cont += 1
            r_num += 1
        cur_d += datetime.timedelta(days=1)

    return f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<worksheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main">
  <cols>
    <col min="1" max="1" width="12" customWidth="1"/>
    <col min="2" max="2" width="15" customWidth="1"/>
    <col min="3" max="3" width="13" customWidth="1"/>
    <col min="4" max="4" width="18" customWidth="1"/>
    <col min="5" max="5" width="16" customWidth="1"/>
    <col min="6" max="6" width="76" customWidth="1"/>
    <col min="7" max="7" width="15" customWidth="1"/>
    <col min="8" max="8" width="50" customWidth="1"/>
  </cols>
  <sheetData>
    {''.join(rows)}
  </sheetData>
</worksheet>"""

sheet2_xml = build_official_calendar_rows()

# ------------------------------------------------------------------------------
# EMPAQUETADO EN ZIP OFICIAL (.XLSX CON EXACTAMENTE 2 HOJAS)
# ------------------------------------------------------------------------------
temp_file = "/tmp/BITACORA_SEGUIMIENTO_CLASES.xlsx"
with zipfile.ZipFile(temp_file, "w", compression=zipfile.ZIP_DEFLATED) as zout:
    zout.writestr("[Content_Types].xml", content_types)
    zout.writestr("_rels/.rels", root_rels)
    zout.writestr("xl/workbook.xml", workbook_xml)
    zout.writestr("xl/_rels/workbook.xml.rels", wb_rels)
    zout.writestr("xl/styles.xml", styles_xml)
    zout.writestr("xl/worksheets/sheet1.xml", sheet1_xml)
    zout.writestr("xl/worksheets/sheet2.xml", sheet2_xml)

# Cerrar el libro en Microsoft Excel si estuviese abierto para liberar el bloqueo en macOS
try:
    subprocess.run([
        'osascript', '-e',
        'tell application "Microsoft Excel" to close (workbooks whose name contains "BITACORA_SEGUIMIENTO_CLASES") saving no'
    ], stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL, check=False)
except Exception:
    pass

try:
    if os.path.exists(EXCEL_PATH):
        os.remove(EXCEL_PATH)
except Exception:
    pass

shutil.copyfile(temp_file, EXCEL_PATH)
print("--> 'BITACORA_SEGUIMIENTO_CLASES.xlsx' GENERADO CON ÉXITO:")
print("    Hoja 1: 'Bitacora de Clases' (Registro real con Clase 13 de hoy 12/11/2026 + Resumen de Métricas).")
print("    Hoja 2: 'Calendario Oficial Robótica-IA' (Itinerario Oficial Definitivo con 46 clases restantes,")
print("            21 Robótica, 7 Monográficos con NASA a 2 días, 18 IA Comodín, 0 robots consecutivos")
print("            y arranque en limpio con Sesión 05 a la vuelta de Navidad).")
print("    100% nativo en biblioteca estándar de Python (sin pip ni dependencias externas).")
