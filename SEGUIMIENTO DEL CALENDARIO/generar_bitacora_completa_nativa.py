#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
generar_bitacora_completa_nativa.py
Genera 'BITACORA_SEGUIMIENTO_CLASES.xlsx' utilizando EXCLUSIVAMENTE
la biblioteca estándar de Python (sin pip, sin openpyxl, sin dependencias externas).
Crea 3 hojas oficiales:
1. 'Bitacora de Clases' (Registro real acumulado hasta Clase 11 + Resumen de Métricas).
2. 'Calendario de Clases B1-B6' (Itinerario Oficial Planificado de referencia).
3. 'Escenario 3 - Ciclo Robótica-IA' (Nueva Pestaña 3 con ciclo Robótica -> IA -> Robótica -> Monográfico/IA,
   con Monográfico 2 el 19/11 y Monográfico 3 el 24/11).
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
  <Override PartName="/xl/worksheets/sheet3.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.worksheet+xml"/>
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
  <Relationship Id="rId3" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/worksheet" Target="worksheets/sheet3.xml"/>
  <Relationship Id="rId4" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/styles" Target="styles.xml"/>
</Relationships>"""

workbook_xml = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<workbook xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships">
  <sheets>
    <sheet name="Bitacora de Clases" sheetId="1" r:id="rId1"/>
    <sheet name="Calendario de Clases B1-B6" sheetId="2" r:id="rId2"/>
    <sheet name="Escenario 3 - Ciclo Robótica-IA" sheetId="3" r:id="rId3"/>
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
# Style 10: Fila Morado Pastel (EDEDF8, borde) -> IA
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

def xml_escape(s):
    if not isinstance(s, str):
        s = str(s)
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")

def cell_xml(ref, val, style_id=None, is_formula=False):
    s_attr = f' s="{style_id}"' if style_id is not None else ""
    if is_formula:
        return f'<c r="{ref}"{s_attr}><f>{xml_escape(val)}</f></c>'
    if isinstance(val, (int, float)):
        return f'<c r="{ref}"{s_attr}><v>{val}</v></c>'
    else:
        escaped = xml_escape(str(val))
        return f'<c r="{ref}"{s_attr} t="inlineStr"><is><t>{escaped}</t></is></c>'

# Días festivos y vacaciones comunes
holidays_dict = {
    datetime.date(2026, 12, 8): "Festivo Nacional: Inmaculada Concepción",
    datetime.date(2026, 12, 22): "Vacaciones de Navidad (18 dic - 6 ene)",
    datetime.date(2026, 12, 24): "Vacaciones de Navidad (Nochebuena)",
    datetime.date(2026, 12, 29): "Vacaciones de Navidad",
    datetime.date(2026, 12, 31): "Vacaciones de Navidad (Nochevieja)",
    datetime.date(2027, 1, 5): "Vacaciones de Navidad (Víspera Reyes)",
    datetime.date(2027, 3, 23): "Semana Santa 2027 (Martes Santo)",
    datetime.date(2027, 3, 25): "Semana Santa 2027 (Jueves Santo - Festivo)",
    datetime.date(2027, 5, 18): "Semana de Mayores (Tercera semana de mayo - Vacaciones)",
    datetime.date(2027, 5, 20): "Semana de Mayores (Tercera semana de mayo - Vacaciones)"
}

# Clases reales impartidas (1 a 11)
clases_impartidas_data = [
    (1, "01/10/2026", "Jueves", 1.5, "Presentación inaugural", 1.5, "Primer día de clase", "General"),
    (2, "06/10/2026", "Martes", 1.5, "Guía de Classroom y Gemini", 3.0, "Segunda clase organizativa", "General"),
    (3, "08/10/2026", "Jueves", 1.5, "Sesión IA 01 (Tranquilidad Jubilación - Sesión 1)", 4.5, "Sesión IA 01 impartida", "IA"),
    (4, "13/10/2026", "Martes", 1.5, "Sesión IA 01 (Tranquilidad Jubilación - Sesión 2)", 6.0, "Consolidación simulador", "IA"),
    (5, "15/10/2026", "Jueves", 1.5, "Sesión IA 01 (Tranquilidad Jubilación - Sesión 3)", 7.5, "Profundización práctica", "IA"),
    (6, "20/10/2026", "Martes", 1.5, "Sesión IA 01 (Tranquilidad Jubilación - Sesión 4)", 9.0, "Cierre Sesión IA 01 (4 clases en total)", "IA"),
    (7, "22/10/2026", "Jueves", 1.5, "ROB.1: 1.1 Puerta supermercado", 10.5, "Práctica de motor y engranajes (1 día)", "Robótica"),
    (8, "27/10/2026", "Martes", 1.5, "Monográfico 2 IA entero (Mundo Digital Senior)", 12.0, "Monográfico completado en 1 clase", "IA"),
    (9, "29/10/2026", "Jueves", 1.5, "ROB.1: 1.2 Lavadora + IA: Sesión 2 (Ítems 09 y 09B)", 13.5, "Clase combinada (1.2 Lavadora en 1 día)", "Mixta"),
    (10, "03/11/2026", "Martes", 1.5, "IA: Sesión 02 (Radar Anti-Estafas - Hasta ítem 09 incluido)", 15.0, "Impartida hasta ítem 09 incluido", "IA"),
    (11, "05/11/2026", "Jueves", 1.5, "ROB.1: 1.3 Ascensor + IA: Sesión 02 (Ítems 10 a 13)", 16.5, "Impartido ROB 1.3 Ascensor y avance de IA Sesión 02 (ítems 10 a 13)", "Mixta")
]

# ==============================================================================
# HOJA 1: BITÁCORA DE CLASES
# ==============================================================================
h1_rows = []
h1_rows.append('<row r="1" ht="20">' + cell_xml("A1", "BITÁCORA Y SEGUIMIENTO DEL CALENDARIO DE CLASES", 1) + '</row>')
h1_rows.append('<row r="2" ht="16">' + cell_xml("A2", "Horario: Martes y Jueves (1.5 horas/sesión) | Excluye festivos, Navidad y Semana Santa", 6) + '</row>')

# Resumen general (A4:B6) y métricas oficiales (I4:J11)
h1_rows.append('<row r="4" ht="18">' +
               cell_xml("A4", "RESUMEN GENERAL", 2) + cell_xml("B4", "VALOR", 2) +
               cell_xml("I4", "MÉTRICAS OFICIALES AL 30 DE MAYO", 2) +
               cell_xml("J4", "VALOR / ESTADO PLANIFICADO", 2) + '</row>')

h1_rows.append('<row r="5" ht="16">' +
               cell_xml("A5", "Total Sesiones Transcurridas", 5) + cell_xml("B5", 11, 4) +
               cell_xml("I5", "Total Sesiones Lectivas Restantes", 5) + cell_xml("J5", "48 clases (72.0 h)", 4) + '</row>')

h1_rows.append('<row r="6" ht="16">' +
               cell_xml("A6", "Total Horas Lectivas Impartidas", 5) + cell_xml("B6", 16.5, 4) +
               cell_xml("I6", "Clases de Robótica Restantes", 5) + cell_xml("J6", "23 clases (B1 a B6 selectivo)", 4) + '</row>')

h1_rows.append('<row r="7" ht="16">' +
               cell_xml("I7", "Clases de IA Restantes", 5) + cell_xml("J7", "25 clases (6 monos + 19 ses)", 4) + '</row>')

h1_rows.append('<row r="8" ht="18">' +
               cell_xml("A8", "Nº SESIÓN", 2) + cell_xml("B8", "FECHA", 2) + cell_xml("C8", "DÍA", 2) +
               cell_xml("D8", "DURACIÓN (H)", 2) + cell_xml("E8", "TEMARIO / CONTENIDO", 2) +
               cell_xml("F8", "HORAS ACUM.", 2) + cell_xml("G8", "OBSERVACIONES", 2) +
               cell_xml("I8", "Techo Alcanzado en Robótica", 7) + cell_xml("J8", "Bloque 6 (Star Wars / ISS)", 7) + '</row>')

for idx, (num, fecha, dia, dur, tem, h_acum, obs, area) in enumerate(clases_impartidas_data, start=9):
    extra = ""
    if idx == 9:
        extra = cell_xml("I9", "Techo Alcanzado en IA", 7) + cell_xml("J9", "Sesión 14 de 60 (Clausura y Proyectos)", 7)
    elif idx == 10:
        extra = cell_xml("I10", "Ajuste al Calendario Escolar", 5) + cell_xml("J10", "🎯 ENCAJE EXACTO (48 / 48 clases)", 4)
    elif idx == 11:
        extra = cell_xml("I11", "Escenario Oficial Recomendado", 6) + cell_xml("J11", "Ver Hoja 3 ('Escenario 3 - Ciclo Robótica-IA')", 6)

    r_str = f'<row r="{idx}" ht="16">'
    r_str += cell_xml(f"A{idx}", num, 5) + cell_xml(f"B{idx}", fecha, 5) + cell_xml(f"C{idx}", dia, 5)
    r_str += cell_xml(f"D{idx}", dur, 5) + cell_xml(f"E{idx}", tem, 5) + cell_xml(f"F{idx}", h_acum, 5) + cell_xml(f"G{idx}", obs, 5)
    r_str += extra + '</row>'
    h1_rows.append(r_str)

sheet1_xml = f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<worksheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main">
  <cols>
    <col min="1" max="1" width="13" customWidth="1"/>
    <col min="2" max="2" width="15" customWidth="1"/>
    <col min="3" max="3" width="14" customWidth="1"/>
    <col min="4" max="4" width="16" customWidth="1"/>
    <col min="5" max="5" width="48" customWidth="1"/>
    <col min="6" max="6" width="16" customWidth="1"/>
    <col min="7" max="7" width="52" customWidth="1"/>
    <col min="8" max="8" width="4" customWidth="1"/>
    <col min="9" max="9" width="38" customWidth="1"/>
    <col min="10" max="10" width="40" customWidth="1"/>
  </cols>
  <sheetData>
    {''.join(h1_rows)}
  </sheetData>
</worksheet>"""

# ==============================================================================
# HOJA 2: CALENDARIO DE CLASES B1-B6 (REFERENCIA)
# ==============================================================================
def build_calendar_rows():
    rows = []
    title = "CALENDARIO OFICIAL DE CLASES (B1 A B6)"
    sub = "Itinerario equilibrado: 19 Robótica + 6 Monográficos IA + 24 Sesiones IA (59 lectivas totales)"
    h_style = 3

    rows.append(f'<row r="1" ht="20">{cell_xml("A1", title, 1)}</row>')
    rows.append(f'<row r="2" ht="16">{cell_xml("A2", sub, 6)}</row>')

    r_box = [
        ("PARÁMETRO DEL CURSO", "VALOR", "DIAGNÓSTICO AL 30 DE MAYO"),
        ("Total Sesiones Lectivas Restantes", "48 clases", "De 10/11/2026 a 27/05/2027"),
        ("Robótica Programada", "19 clases", "Bloques 1 a 6 selectivo"),
        ("IA Programada", "29 clases (6 monos + 23 ses)", "Sesión 02 a 14 + Monográficos 2 a 7"),
        ("¿LLEGAMOS BIEN O NOS PASAMOS?", "🎯 ENCAJE EXACTO (48 / 48)", "¡CERO DÍAS DE DESVIACIÓN! Encaje perfecto."),
        ("Techo Robótica al 30 de Mayo", "Bloque 6 (Interstellar / Star Wars)", "Alcanza androides y naves espaciales"),
        ("Techo IA al 30 de Mayo", "Sesión 14 (de 60)", "Lote 1 completo + Clausura y Proyectos")
    ]
    for ro, (c1, c2, c3) in enumerate(r_box, start=4):
        st = h_style if ro == 4 else (7 if "LLEGAMOS" in c1 else 5)
        st_val = h_style if ro == 4 else (7 if "LLEGAMOS" in c1 else 4)
        rows.append(f'<row r="{ro}" ht="16">{cell_xml(f"B{ro}", c1, st)}{cell_xml(f"C{ro}", c2, st_val)}{cell_xml(f"D{ro}", c3, st)}</row>')

    rows.append(f'<row r="12" ht="18">' +
                cell_xml("A12", "Nº CLASE", h_style) + cell_xml("B12", "FECHA", h_style) + cell_xml("C12", "DÍA", h_style) +
                cell_xml("D12", "ÁREA", h_style) + cell_xml("E12", "ESTADO", h_style) +
                cell_xml("F12", "TEMARIO PROYECTADO", h_style) + cell_xml("G12", "HORAS ACUM.", h_style) + cell_xml("H12", "HITO / BLOQUE", h_style) + '</row>')

    # 48 clases restantes para Hoja 2
    future_sheet2 = [
        ("IA", "IA: Sesión 02 (Radar Anti-Estafas - Finalización)", "IA Sesión 02 concluida"),
        ("Robótica", "ROB: 1.4 Semáforos inteligentes (Lógica)", "Robótica [FIN BLOQUE 1]"),
        ("IA (Monográfico)", "IA: Monográfico 2 (Manejo de Gemini Book / NotebookLM)", "IA Monográfico 2"),
        ("IA", "IA: Sesión 03 (Cuento/Cómic con NLM - Día 1/2)", "IA Sesión 03"),
        ("IA (Monográfico)", "IA: Monográfico 3 (Taller Especial Cuento con NLM)", "IA Monográfico 3"),
        ("Robótica", "ROB: 2.1 Silla de Ruedas Eléctrica (Tracción diferencial)", "Robótica Bloque 2"),
        ("IA", "IA: Sesión 03 (Cuento/Cómic con NLM - Día 2/2)", "IA Sesión 03 concluida"),
        ("Robótica", "ROB: 2.2 Roomba con sensor (Evasión de obstáculos)", "Robótica Bloque 2"),
        ("IA (Monográfico)", "IA: Monográfico 4 (Mi Biografía con IA)", "IA Monográfico 4"),
        ("Robótica", "ROB: 2.3 Aparcamiento asistido (Condición IF-ELSE)", "Robótica Bloque 2"),
        ("IA", "IA: Sesión 04 (Aporte de Valor Senior - Día 1/2)", "IA Sesión 04"),
        ("Robótica", "ROB: 2.4 Ozobot (El color como lenguaje)", "Robótica Bloque 2"),
        ("IA (Monográfico)", "IA: Monográfico 5 (El Abuelo Tutor - Matemáticas e Historia)", "IA Monográfico 5"),
        ("Robótica", "ROB: 2.5 Cámara de seguridad (Variable simple)", "Robótica Bloque 2"),
        ("IA", "IA: Sesión 04 (Taller Práctico - Día 2/2)", "IA Sesión 04 concluida"),
        ("Robótica", "ROB: 3.1 Robot repartidor (Chasis diferencial)", "Robótica Bloque 3"),
        ("IA (Monográfico)", "IA: Monográfico 6 (Mapa y Gestión de Proyecto con IA)", "IA Monográfico 6"),
        ("Robótica", "ROB: 3.2 Coche ELEGOO con cámara", "Robótica Bloque 3"),
        ("IA", "IA: Sesión 05 (Sistema Solar 3D - Día 1/2)", "IA Sesión 05"),
        ("Robótica", "ROB: 3.3 Avión con servomotores", "Robótica Bloque 3"),
        ("IA (Monográfico)", "IA: Monográfico 7 (NASA y Exploración Espacial con IA)", "IA [FIN MONOGRÁFICOS]"),
        ("Robótica", "ROB: 3.4 Dron terrestre (Estabilidad)", "Robótica Bloque 3"),
        ("IA", "IA: Sesión 05 (NASA Eyes - Día 2/2)", "IA Sesión 05 concluida"),
        ("Robótica", "ROB: 3.5 Penguin-BOT (Sincronización cinemática)", "Robótica [FIN BLOQUE 3]"),
        ("IA", "IA: Sesión 06 (Cerebro Humano 3D - Día 1/2)", "IA Sesión 06"),
        ("Robótica", "ROB: 4.1 Base giratoria de Brazo Robótico", "Robótica Bloque 4"),
        ("IA", "IA: Sesión 06 (Red Neuronal - Día 2/2)", "IA Sesión 06 concluida"),
        ("Robótica", "ROB: 4.2 Hombro robótico", "Robótica Bloque 4"),
        ("IA", "IA: Sesión 07 (Domótica y Voz - Día 1/2)", "IA Sesión 07"),
        ("Robótica", "ROB: 4.3 Codo robótico", "Robótica Bloque 4"),
        ("IA", "IA: Sesión 07 (Hábitos Saludables - Día 2/2)", "IA Sesión 07 concluida"),
        ("Robótica", "ROB: 4.4 Muñeca robótica", "Robótica Bloque 4"),
        ("IA", "IA: Sesión 08 (Fotogrametría Pompeya - Día 1/2)", "IA Sesión 08"),
        ("Robótica", "ROB: 4.5 Brazo Robótico: Pinza y sensor", "Robótica Bloque 4"),
        ("IA", "IA: Sesión 08 (Visor 3D Arqueología - Día 2/2)", "IA Sesión 08 concluida"),
        ("Robótica", "ROB: 4.6 Brazo Robótico: Mano hidráulica", "Robótica Bloque 4"),
        ("IA", "IA: Sesión 09 (Música e IA Sonora - Día 1/2)", "IA Sesión 09"),
        ("Robótica", "ROB: 5.1 Perro Unitree Go2 AIR (Cuadrúpedo autónomo)", "Robótica Bloque 5"),
        ("IA", "IA: Sesión 09 (Generación MIDI - Día 2/2)", "IA Sesión 09 concluida"),
        ("Robótica", "ROB: 5.2 Robot Bípedo (Comunicación visual)", "Robótica Bloque 5"),
        ("IA", "IA: Sesión 10 (Cierre y Evaluación - Día 1/2)", "IA Sesión 10"),
        ("Robótica", "ROB: 5.3 Androide MIXAMO (Cinemática humana)", "Robótica Bloque 5"),
        ("IA", "IA: Sesión 10 (Muestra Interactiva - Día 2/2)", "IA Sesión 10 concluida"),
        ("Robótica", "ROB: 5.4 Transformer (POO y enjambres)", "Robótica Bloque 5"),
        ("Robótica", "ROB: 5.5 Trío Dinámico Star Wars", "Robótica Bloque 5"),
        ("Robótica", "ROB: 5.6 Robot de combate", "Robótica [FIN BLOQUE 5]"),
        ("Robótica", "ROB: 6.1 Transporte Espacial Autónomo", "Robótica Bloque 6"),
        ("IA", "IA: Sesión 14 (Clausura del Curso y Presentación de Proyectos)", "IA [CLAUSURA DEL CURSO]")
    ]

    cur = datetime.date(2026, 10, 1)
    end = datetime.date(2027, 5, 30)
    r_num = 13
    clase_cont = 1
    h_acum = 0.0

    while cur <= end:
        if cur.weekday() in (1, 3):
            d_name = "Martes" if cur.weekday() == 1 else "Jueves"
            d_str = cur.strftime("%d/%m/%Y")

            if cur in holidays_dict:
                rows.append(f'<row r="{r_num}" ht="16">' +
                            cell_xml(f"A{r_num}", "-", 11) + cell_xml(f"B{r_num}", d_str, 11) + cell_xml(f"C{r_num}", d_name, 11) +
                            cell_xml(f"D{r_num}", "Vacaciones", 11) + cell_xml(f"E{r_num}", "No Lectivo", 11) +
                            cell_xml(f"F{r_num}", f"⛔ {holidays_dict[cur]}", 11) + cell_xml(f"G{r_num}", f"{h_acum:.1f} h", 11) +
                            cell_xml(f"H{r_num}", "Sin clase programada", 11) + '</row>')
            else:
                h_acum += 1.5
                if clase_cont <= 11:
                    item_real = clases_impartidas_data[clase_cont - 1]
                    area_v = item_real[7]
                    tem_v = item_real[4]
                    obs_v = item_real[6]
                    est_v = "Impartida"
                    f_st = 8
                else:
                    f_idx = clase_cont - 12
                    area_v, tem_v, obs_v = future_sheet2[f_idx]
                    est_v = "Proyectada"
                    f_st = 9 if area_v == "Robótica" else 10

                rows.append(f'<row r="{r_num}" ht="16">' +
                            cell_xml(f"A{r_num}", clase_cont, f_st) + cell_xml(f"B{r_num}", d_str, f_st) + cell_xml(f"C{r_num}", d_name, f_st) +
                            cell_xml(f"D{r_num}", area_v, f_st) + cell_xml(f"E{r_num}", est_v, f_st) +
                            cell_xml(f"F{r_num}", tem_v, f_st) + cell_xml(f"G{r_num}", f"{h_acum:.1f} h", f_st) +
                            cell_xml(f"H{r_num}", obs_v, f_st) + '</row>')
                clase_cont += 1
            r_num += 1
        cur += datetime.timedelta(days=1)

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

# ==============================================================================
# HOJA 3: ESCENARIO 3 - CICLO ROBÓTICA - IA (NUEVA PESTAÑA CORREGIDA)
# ==============================================================================
def build_scenario3_rows():
    rows = []
    title = "ESCENARIO 3: CICLO ALTERNO ROBÓTICA - IA"
    sub = "Ciclo: Robótica -> Sesión IA -> Robótica -> Monográfico (y Sesión IA tras concluir monográficos) | Monográfico 2 el 19/11 y Monográfico 3 el 24/11"
    h_style = 3  # Mismo estilo Navy/Teal de Hoja 2 solicitado por el usuario

    rows.append(f'<row r="1" ht="20">{cell_xml("A1", title, 1)}</row>')
    rows.append(f'<row r="2" ht="16">{cell_xml("A2", sub, 6)}</row>')

    # Resumen superior
    r_box = [
        ("PARÁMETRO DEL CURSO", "VALOR", "DIAGNÓSTICO AL 30 DE MAYO"),
        ("Total Sesiones Lectivas Restantes", "48 clases (72.0 h)", "De 10/11/2026 a 27/05/2027"),
        ("Robótica Programada (Bloques 1 a 6)", "24 clases restantes (27 totales)", "Bloques 1 a 5 COMPLETOS al 100% + Bloque 6 Transporte Espacial"),
        ("IA Programada (Monográficos + Sesiones)", "24 clases restantes (32 totales)", "6 Monográficos completos + Sesiones IA 02 a 11 + Clausura"),
        ("¿LLEGAMOS BIEN O NOS PASAMOS?", "🎯 ENCAJE EXACTO (48 / 48)", "¡CERO DÍAS DE DESVIACIÓN! Encaje perfecto."),
        ("Estructura del Ciclo Solicitada", "ROB -> IA_SES -> ROB -> MONO (-> IA)", "Monográfico 2 ajustado al 19/11 y Monográfico 3 al 24/11"),
        ("Techo Robótica al 30 de Mayo", "Bloque 5 Completo + Bloque 6.1", "Cubre todos los motores, sensores, brazos, androides y nave espacial"),
        ("Techo IA al 30 de Mayo", "6 Monográficos + Sesión 11 + Clausura", "Manejo completo de NotebookLM, Cuentos, Biografía, Tutor, Proyectos y NASA")
    ]
    for ro, (c1, c2, c3) in enumerate(r_box, start=4):
        st = h_style if ro == 4 else (7 if "LLEGAMOS" in c1 else 5)
        st_val = h_style if ro == 4 else (7 if "LLEGAMOS" in c1 else 4)
        rows.append(f'<row r="{ro}" ht="16">{cell_xml(f"B{ro}", c1, st)}{cell_xml(f"C{ro}", c2, st_val)}{cell_xml(f"D{ro}", c3, st)}</row>')

    rows.append(f'<row r="12" ht="18">' +
                cell_xml("A12", "Nº CLASE", h_style) + cell_xml("B12", "FECHA", h_style) + cell_xml("C12", "DÍA", h_style) +
                cell_xml("D12", "ÁREA", h_style) + cell_xml("E12", "ESTADO", h_style) +
                cell_xml("F12", "TEMARIO PROYECTADO", h_style) + cell_xml("G12", "HORAS ACUM.", h_style) + cell_xml("H12", "HITO / FASE DEL CICLO", h_style) + '</row>')

    # 48 clases proyectadas exactas para Escenario 3
    future_s3 = [
        # Clase 12 (10/11/2026, Mar): Fin de Sesión 2 IA
        ("IA", "IA: Sesión 02 (Radar Anti-Estafas - Finalización)", "IA Sesión 02 concluida"),

        # Clase 13 (12/11/2026, Jue): Robótica (Paso 1 del ciclo)
        ("Robótica", "ROB: 1.4 Semáforos inteligentes (Lógica y estados)", "Robótica [FIN BLOQUE 1]"),

        # Clase 14 (17/11/2026, Mar): Sesión IA (Paso 2 del ciclo)
        ("IA", "IA: Sesión 03 (Cuento/Cómic con NLM - Parte 1/2)", "IA Sesión 03 [Inicio]"),

        # Clase 15 (19/11/2026, Jue): Monográfico 2 (Ajustado al día 19 por asistencia completa)
        ("IA (Monográfico)", "IA: Monográfico 2 (Mundo Digital Senior / Gemini Book / NotebookLM)", "IA Monográfico 2 [Día 19 - Asistencia completa]"),

        # Clase 16 (24/11/2026, Mar): Monográfico 3 (Continuación inmediata solicitada)
        ("IA (Monográfico)", "IA: Monográfico 3 (Taller Especial Cuento con NLM / Cuentos y Cómics)", "IA Monográfico 3 [Continuación Monográfico 2]"),

        # ----------------------------------------------------------------------
        # CICLO REGULAR RECURRENTE: ROBÓTICA -> SESIÓN IA -> ROBÓTICA -> MONOGRÁFICO
        # ----------------------------------------------------------------------

        # CICLO 1 (Clases 17 a 20)
        ("Robótica", "ROB: 2.1 Silla de Ruedas Eléctrica (Tracción diferencial)", "Robótica Bloque 2 [Ciclo 1 - Robótica]"),
        ("IA", "IA: Sesión 03 (Cuento/Cómic con NLM - Parte 2/2)", "IA [FIN SESIÓN 03] [Ciclo 1 - Sesión IA]"),
        ("Robótica", "ROB: 2.2 Roomba con sensor (Bucle infinito y evasión)", "Robótica Bloque 2 [Ciclo 1 - Robótica]"),
        ("IA (Monográfico)", "IA: Monográfico 4 (Mi Biografía con IA y Redacción Guiada)", "IA Monográfico 4 [Ciclo 1 - Monográfico]"),

        # CICLO 2 (Clases 21 a 24)
        ("Robótica", "ROB: 2.3 Aparcamiento asistido (Condición IF-ELSE)", "Robótica Bloque 2 [Ciclo 2 - Robótica]"),
        ("IA", "IA: Sesión 04 (Aporte de Valor Senior - Parte 1/2)", "IA Sesión 04 [Ciclo 2 - Sesión IA]"),
        ("Robótica", "ROB: 2.4 Ozobot (El color como lenguaje y códigos)", "Robótica Bloque 2 [Ciclo 2 - Robótica]"),
        ("IA (Monográfico)", "IA: Monográfico 5 (El Abuelo Tutor: Matemáticas e Historia)", "IA Monográfico 5 [Ciclo 2 - Monográfico]"),

        # CICLO 3 (Clases 25 a 28)
        ("Robótica", "ROB: 2.5 Cámara de seguridad (Variable simple y alarma)", "Robótica [FIN BLOQUE 2] [Ciclo 3 - Robótica]"),
        ("IA", "IA: Sesión 04 (Aporte de Valor Senior - Parte 2/2)", "IA [FIN SESIÓN 04] [Ciclo 3 - Sesión IA]"),
        ("Robótica", "ROB: 3.1 Robot repartidor (Chasis diferencial y ruta)", "Robótica Bloque 3 [Ciclo 3 - Robótica]"),
        ("IA (Monográfico)", "IA: Monográfico 6 (Mapa y Gestión de Proyectos con IA)", "IA Monográfico 6 [Ciclo 3 - Monográfico]"),

        # CICLO 4 (Clases 29 a 32)
        ("Robótica", "ROB: 3.2 Coche ELEGOO con cámara (Visión artificial básica)", "Robótica Bloque 3 [Ciclo 4 - Robótica]"),
        ("IA", "IA: Sesión 05 (Creatividad Visual y Generación de Imagen - Parte 1/2)", "IA Sesión 05 [Ciclo 4 - Sesión IA]"),
        ("Robótica", "ROB: 3.3 Avión con servos (Posición angular exacta)", "Robótica Bloque 3 [Ciclo 4 - Robótica]"),
        ("IA (Monográfico)", "IA: Monográfico 7 (NASA y Exploración Espacial con IA - 5 Portales 3D)", "IA [FIN MONOGRÁFICOS] [Ciclo 4 - Monográfico]"),

        # ----------------------------------------------------------------------
        # TRAS AGOTARSE LOS MONOGRÁFICOS: SESIÓN IA OCUPA SU LUGAR
        # CICLO: ROBÓTICA -> SESIÓN IA -> ROBÓTICA -> SESIÓN IA (Alternancia Continua)
        # ----------------------------------------------------------------------

        # CICLO 5 (Clases 33 a 36)
        ("Robótica", "ROB: 3.4 Dron autónomo (Navegación 3D en tres ejes)", "Robótica Bloque 3 [Ciclo 5 - Robótica]"),
        ("IA", "IA: Sesión 05 (Creatividad Visual y Diseño - Parte 2/2)", "IA [FIN SESIÓN 05] [Ciclo 5 - Sesión IA]"),
        ("Robótica", "ROB: 3.5 Penguin-BOT (Sincronización cinemática de servos)", "Robótica [FIN BLOQUE 3] [Ciclo 5 - Robótica]"),
        ("IA", "IA: Sesión 06 (Asistente Personal de Salud y Bienestar - Parte 1/2)", "IA Sesión 06 [Ciclo 5 - Sesión IA]"),

        # CICLO 6 (Clases 37 a 40)
        ("Robótica", "ROB: 4.1 Base giratoria de Brazo Robótico (Parámetro)", "Robótica Bloque 4 [Ciclo 6 - Robótica]"),
        ("IA", "IA: Sesión 06 (Asistente de Salud y Vida Diaria - Parte 2/2)", "IA [FIN SESIÓN 06] [Ciclo 6 - Sesión IA]"),
        ("Robótica", "ROB: 4.2 Hombro robótico (Coordinación de dos motores)", "Robótica Bloque 4 [Ciclo 6 - Robótica]"),
        ("IA", "IA: Sesión 07 (Domótica y Entorno Inteligente - Parte 1/2)", "IA Sesión 07 [Ciclo 6 - Sesión IA]"),

        # CICLO 7 (Clases 41 a 44)
        ("Robótica", "ROB: 4.3 Codo robótico (Secuencia de tres articulaciones)", "Robótica Bloque 4 [Ciclo 7 - Robótica]"),
        ("IA", "IA: Sesión 07 (Domótica y Control por Voz - Parte 2/2)", "IA [FIN SESIÓN 07] [Ciclo 7 - Sesión IA]"),
        ("Robótica", "ROB: 4.4 Muñeca robótica (Variable de orientación espacial)", "Robótica Bloque 4 [Ciclo 7 - Robótica]"),
        ("IA", "IA: Sesión 08 (Fotogrametría y Reconstrucción 3D Pompeya - Parte 1/2)", "IA Sesión 08 [Ciclo 7 - Sesión IA]"),

        # CICLO 8 (Clases 45 a 48)
        ("Robótica", "ROB: 4.5 Pinza robótica (Sensor de presión y agarre)", "Robótica Bloque 4 [Ciclo 8 - Robótica]"),
        ("IA", "IA: Sesión 08 (Fotogrametría y Museografía Virtual - Parte 2/2)", "IA [FIN SESIÓN 08] [Ciclo 8 - Sesión IA]"),
        ("Robótica", "ROB: 4.6 Mano hidráulica (Fuerza controlada y cinemática)", "Robótica [FIN BLOQUE 4] [Ciclo 8 - Robótica]"),
        ("IA", "IA: Sesión 09 (Música e IA Sonora: Composición y MIDI - Parte 1/2)", "IA Sesión 09 [Ciclo 8 - Sesión IA]"),

        # CICLO 9 (Clases 49 a 52)
        ("Robótica", "ROB: 5.1 Perro Unitree Go2 AIR (Navegación cuadrúpeda y LiDAR)", "Robótica Bloque 5 [Ciclo 9 - Robótica]"),
        ("IA", "IA: Sesión 09 (Música e IA Sonora: Síntesis y Audio - Parte 2/2)", "IA [FIN SESIÓN 09] [Ciclo 9 - Sesión IA]"),
        ("Robótica", "ROB: 5.2 Robot Bípedo (Equilibrio dinámico y comunicación visual)", "Robótica Bloque 5 [Ciclo 9 - Robótica]"),
        ("IA", "IA: Sesión 10 (Cierre y Evaluación de Modelos - Parte 1/2)", "IA Sesión 10 [Ciclo 9 - Sesión IA]"),

        # CICLO 10 (Clases 53 a 56)
        ("Robótica", "ROB: 5.3 Androide MIXAMO (Captura de movimiento y cinemática)", "Robótica Bloque 5 [Ciclo 10 - Robótica]"),
        ("IA", "IA: Sesión 10 (Muestra Interactiva y Proyectos - Parte 2/2)", "IA [FIN SESIÓN 10] [Ciclo 10 - Sesión IA]"),
        ("Robótica", "ROB: 5.4 Transformer (POO, cambio morfológico y enjambres)", "Robótica Bloque 5 [Ciclo 10 - Robótica]"),
        ("IA", "IA: Sesión 11 (Stradivarius y Acústica Musical con IA)", "IA Sesión 11 [Ciclo 10 - Sesión IA]"),

        # FASE FINAL DE CONSOLIDACIÓN (Clases 57 a 59)
        ("Robótica", "ROB: 5.5 Trío Dinámico Star Wars (R2-D2, BB-8, D-O)", "Robótica Bloque 5 [Fase Final]"),
        ("Robótica", "ROB: 5.6 Robot de Combate (Estructura reforzada y defensa)", "Robótica [FIN BLOQUE 5] [Fase Final]"),
        ("Mixta", "ROB: 6.1 Transporte Espacial Autónomo + IA: Clausura y Proyectos Finales", "Robótica y Clausura [FIN DE CURSO]")
    ]

    cur = datetime.date(2026, 10, 1)
    end = datetime.date(2027, 5, 30)
    r_num = 13
    clase_cont = 1
    h_acum = 0.0

    while cur <= end:
        if cur.weekday() in (1, 3):
            d_name = "Martes" if cur.weekday() == 1 else "Jueves"
            d_str = cur.strftime("%d/%m/%Y")

            if cur in holidays_dict:
                rows.append(f'<row r="{r_num}" ht="16">' +
                            cell_xml(f"A{r_num}", "-", 11) + cell_xml(f"B{r_num}", d_str, 11) + cell_xml(f"C{r_num}", d_name, 11) +
                            cell_xml(f"D{r_num}", "Vacaciones", 11) + cell_xml(f"E{r_num}", "No Lectivo", 11) +
                            cell_xml(f"F{r_num}", f"⛔ {holidays_dict[cur]}", 11) + cell_xml(f"G{r_num}", f"{h_acum:.1f} h", 11) +
                            cell_xml(f"H{r_num}", "Sin clase programada", 11) + '</row>')
            else:
                h_acum += 1.5
                if clase_cont <= 11:
                    item_real = clases_impartidas_data[clase_cont - 1]
                    area_v = item_real[7]
                    tem_v = item_real[4]
                    obs_v = item_real[6]
                    est_v = "Impartida"
                    f_st = 8
                else:
                    f_idx = clase_cont - 12
                    area_v, tem_v, obs_v = future_s3[f_idx]
                    est_v = "Proyectada"
                    if "Monográfico" in area_v:
                        f_st = 13  # Amarillo Pastel para Monográficos Especiales
                    elif area_v == "Robótica":
                        f_st = 9   # Naranja Pastel para Robótica
                    elif area_v == "Mixta":
                        f_st = 8   # Verde Pastel para Clausura Mixta
                    else:
                        f_st = 10  # Morado Pastel para Sesiones de IA

                rows.append(f'<row r="{r_num}" ht="16">' +
                            cell_xml(f"A{r_num}", clase_cont, f_st) + cell_xml(f"B{r_num}", d_str, f_st) + cell_xml(f"C{r_num}", d_name, f_st) +
                            cell_xml(f"D{r_num}", area_v, f_st) + cell_xml(f"E{r_num}", est_v, f_st) +
                            cell_xml(f"F{r_num}", tem_v, f_st) + cell_xml(f"G{r_num}", f"{h_acum:.1f} h", f_st) +
                            cell_xml(f"H{r_num}", obs_v, f_st) + '</row>')
                clase_cont += 1
            r_num += 1
        cur += datetime.timedelta(days=1)

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

sheet2_xml = build_calendar_rows()
sheet3_xml = build_scenario3_rows()

# ------------------------------------------------------------------------------
# EMPAQUETADO EN ZIP OFICIAL (.XLSX)
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
    zout.writestr("xl/worksheets/sheet3.xml", sheet3_xml)

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
print("    Hoja 1: 'Bitacora de Clases' (Registro real con Clase 11 de ayer + Resumen de Métricas).")
print("    Hoja 2: 'Calendario de Clases B1-B6' (Itinerario Oficial de Referencia).")
print("    Hoja 3: 'Escenario 3 - Ciclo Robótica-IA' (Nueva Pestaña 3 con ciclo Robótica -> IA -> Robótica -> Monográfico/IA,")
print("            ajustando Monográfico 2 al 19/11 y Monográfico 3 al 24/11).")
print("    100% nativo en biblioteca estándar de Python (sin pip ni dependencias externas).")
