#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
generar_bitacora_completa_nativa.py
Genera 'BITACORA_SEGUIMIENTO_CLASES.xlsx' utilizando EXCLUSIVAMENTE
la biblioteca estándar de Python (sin pip, sin openpyxl, sin dependencias externas).
Crea 2 hojas oficiales:
1. 'Bitacora de Clases' (Registro real acumulado + Resumen de Métricas).
2. 'Calendario de Clases B1-B6' (Itinerario Oficial Planificado con 19 Robótica + 30 IA = 49 clases restantes).
"""

import os
import zipfile
import datetime

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
# Style 8: Fila Verde Pastel (E2EFDA, borde)
# Style 9: Fila Naranja Pastel (FCE4D6, borde)
# Style 10: Fila Morado Pastel (EDEDF8, borde)
# Style 11: Fila Gris Festivo (F2F2F2, texto gris, borde)
styles_xml = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<styleSheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main">
  <fonts count="6">
    <font><sz val="11"/><name val="Calibri"/></font>
    <font><b/><sz val="14"/><color rgb="FF1F497D"/><name val="Calibri"/></font>
    <font><b/><sz val="11"/><color rgb="FFFFFFFF"/><name val="Calibri"/></font>
    <font><b/><sz val="11"/><name val="Calibri"/></font>
    <font><i/><sz val="10"/><color rgb="FF595959"/><name val="Calibri"/></font>
    <font><b/><sz val="11"/><color rgb="FF9C0006"/><name val="Calibri"/></font>
  </fonts>
  <fills count="10">
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
  <cellXfs count="13">
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
  </cellXfs>
</styleSheet>"""

# Función auxiliar para escapar texto XML
def xml_escape(s):
    if not isinstance(s, str):
        s = str(s)
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")

# Función para construir celdas
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

octubre_reales = {
    1: ("General", "Presentación inaugural", "Primer día de curso"),
    2: ("General", "Guía de Classroom y Gemini", "Segunda clase organizativa"),
    3: ("IA", "Sesión IA 01 (Tranquilidad Jubilación - Sesión 1)", "Inicio Sesión IA 01"),
    4: ("IA", "Sesión IA 01 (Tranquilidad Jubilación - Sesión 2)", "Consolidación simulador"),
    5: ("IA", "Sesión IA 01 (Tranquilidad Jubilación - Sesión 3)", "Profundización práctica"),
    6: ("IA", "Sesión IA 01 (Tranquilidad Jubilación - Sesión 4)", "Cierre Sesión IA 01 (4 clases en total)"),
    7: ("Robótica", "ROB.1: 1.1 Puerta supermercado", "Práctica de motor y engranajes (1 día)"),
    8: ("IA", "Monográfico 2 IA entero (Mundo Digital Senior)", "Monográfico completado en 1 clase"),
    9: ("Mixta", "ROB.1: 1.2 Lavadora + IA: Sesión 2 (Ítems 09 y 09B)", "Clase combinada (1.2 Lavadora en 1 día)"),
    10: ("IA", "IA: Sesión 02 (Radar Anti-Estafas - Hasta ítem 09 incluido)", "Impartida hoy martes 03/11 hasta ítem 09 incluido")
}

# ==============================================================================
# CONSTRUCCIÓN DE HOJA 1: BITÁCORA DE CLASES
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
               cell_xml("A5", "Total Sesiones Transcurridas", 5) + cell_xml("B5", 10, 4) +
               cell_xml("I5", "Total Sesiones Lectivas Restantes", 5) + cell_xml("J5", "49 clases (73.5 h)", 4) + '</row>')

h1_rows.append('<row r="6" ht="16">' +
               cell_xml("A6", "Total Horas Lectivas Impartidas", 5) + cell_xml("B6", 15.0, 4) +
               cell_xml("I6", "Clases de Robótica Restantes", 5) + cell_xml("J6", "19 clases (B1 a B6 selectivo)", 4) + '</row>')

h1_rows.append('<row r="7" ht="16">' +
               cell_xml("I7", "Clases de IA Restantes", 5) + cell_xml("J7", "30 clases (6 monos + 24 ses)", 4) + '</row>')

h1_rows.append('<row r="8" ht="18">' +
               cell_xml("A8", "Nº SESIÓN", 2) + cell_xml("B8", "FECHA", 2) + cell_xml("C8", "DÍA", 2) +
               cell_xml("D8", "DURACIÓN (H)", 2) + cell_xml("E8", "TEMARIO / CONTENIDO", 2) +
               cell_xml("F8", "HORAS ACUM.", 2) + cell_xml("G8", "OBSERVACIONES", 2) +
               cell_xml("I8", "Techo Alcanzado en Robótica", 7) + cell_xml("J8", "Bloque 6 (Star Wars / Interstellar)", 7) + '</row>')

oct_data = [
    (1, "01/10/2026", "Jueves", 1.5, "Presentación inaugural", 1.5, "Primer día de clase"),
    (2, "06/10/2026", "Martes", 1.5, "Guía de Classroom y Gemini", 3.0, "Segunda clase organizativa"),
    (3, "08/10/2026", "Jueves", 1.5, "Sesión IA 01", 4.5, "Sesión IA 01 impartida"),
    (4, "13/10/2026", "Martes", 1.5, "Sesión IA 01", 6.0, "Sesión IA 01 impartida"),
    (5, "15/10/2026", "Jueves", 1.5, "Sesión IA 01", 7.5, "Sesión IA 01 impartida"),
    (6, "20/10/2026", "Martes", 1.5, "Sesión IA 01", 9.0, "Sesión IA 01 impartida (4 clases en total)"),
    (7, "22/10/2026", "Jueves", 1.5, "ROB.1: 1.1 Puerta supermercado", 10.5, "Práctica de motor y engranajes (1 día)"),
    (8, "27/10/2026", "Martes", 1.5, "Monográfico 2 IA entero", 12.0, "Monográfico 2 IA impartido entero"),
    (9, "29/10/2026", "Jueves", 1.5, "ROB.1: 1.2 Lavadora + IA: Sesión 2 (Ítems 09 y 09B)", 13.5, "Impartidos ROB.1 (1.2 Lavadora en 1 día) y 2 ítems de IA Sesión 2"),
    (10, "03/11/2026", "Martes", 1.5, "IA: Sesión 02 (Radar Anti-Estafas - Hasta ítem 09 incluido)", 15.0, "Impartida hoy martes 03/11 hasta ítem 09 incluido. Próximo día se finaliza.")
]

for idx, (num, fecha, dia, dur, tem, h_acum, obs) in enumerate(oct_data, start=9):
    extra = ""
    if idx == 9:
        extra = cell_xml("I9", "Techo Alcanzado en IA", 7) + cell_xml("J9", "Sesión 14 de 60 (Clausura y Proyectos)", 7)
    elif idx == 10:
        extra = cell_xml("I10", "Ajuste al Calendario Escolar", 5) + cell_xml("J10", "🎯 ENCAJE EXACTO (49 / 49 clases)", 4)
    elif idx == 11:
        extra = cell_xml("I11", "Calendario Oficial Detallado", 6) + cell_xml("J11", "Ver Hoja 2 ('Calendario de Clases B1-B6')", 6)
        
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
# CONSTRUCCIÓN DE HOJA 2: CALENDARIO DE CLASES B1-B6 (OFICIAL)
# ==============================================================================
def build_calendar_rows():
    rows = []
    title = "CALENDARIO OFICIAL DE CLASES (B1 A B6)"
    sub = "Itinerario equilibrado: 19 Robótica + 6 Monográficos IA + 24 Sesiones IA (59 lectivas totales)"
    h_style = 3
    
    rows.append(f'<row r="1" ht="20">{cell_xml("A1", title, 1)}</row>')
    rows.append(f'<row r="2" ht="16">{cell_xml("A2", sub, 6)}</row>')
    
    # Resumen superior
    r_box = [
        ("PARÁMETRO DEL CURSO", "VALOR", "DIAGNÓSTICO AL 30 DE MAYO"),
        ("Total Sesiones Lectivas Restantes", "49 clases", "De 05/11/2026 a 27/05/2027"),
        ("Robótica Programada", "19 clases", "Bloques 1 a 6 selectivo"),
        ("IA Programada", "30 clases (6 monos + 24 ses)", "Sesión 02 a 14 + Monográficos 2 a 7"),
        ("¿LLEGAMOS BIEN O NOS PASAMOS?", "🎯 ENCAJE EXACTO (49 / 49)", "¡CERO DÍAS DE DESVIACIÓN! Encaje perfecto."),
        ("Techo Robótica al 30 de Mayo", "Bloque 6 (Interstellar / Star Wars)", "Alcanza androides y naves espaciales"),
        ("Techo IA al 30 de Mayo", "Sesión 14 (de 60)", "Lote 1 completo + Clausura y Proyectos")
    ]
    for ro, (c1, c2, c3) in enumerate(r_box, start=4):
        st = h_style if ro == 4 else (7 if "LLEGAMOS" in c1 else 5)
        st_val = h_style if ro == 4 else (7 if "LLEGAMOS" in c1 else 4)
        rows.append(f'<row r="{ro}" ht="16">{cell_xml(f"B{ro}", c1, st)}{cell_xml(f"C{ro}", c2, st_val)}{cell_xml(f"D{ro}", c3, st)}</row>')
        
    # Cabecera tabla
    rows.append(f'<row r="12" ht="18">' +
                cell_xml("A12", "Nº CLASE", h_style) + cell_xml("B12", "FECHA", h_style) + cell_xml("C12", "DÍA", h_style) +
                cell_xml("D12", "ÁREA", h_style) + cell_xml("E12", "ESTADO", h_style) +
                cell_xml("F12", "TEMARIO PROYECTADO", h_style) + cell_xml("G12", "HORAS ACUM.", h_style) + cell_xml("H12", "HITO / BLOQUE", h_style) + '</row>')
    
    # Listas de contenidos oficiales (49 clases restantes exactas)
    future = [
            # Clase 11 (05/11/2026, Jue): Fin de Sesión 2 IA
            ("IA", "IA: Sesión 02 (Radar Anti-Estafas - Finalización)", "IA Sesión 02 concluida"),
            
            # Clase 12 (10/11/2026, Mar): ROB 1.3
            ("Robótica", "ROB: 1.3 Ascensor (Mecanismo y polea)", "Robótica Bloque 1"),
            
            # Clase 13 (12/11/2026, Jue): Monográfico 2 en 1 día
            ("IA (Monográfico)", "IA: Monográfico 2 (Manejo de Gemini Book / NotebookLM)", "IA Monográfico 2"),
            
            # Clase 14 (17/11/2026, Mar): ROB 1.4
            ("Robótica", "ROB: 1.4 Semáforos inteligentes (Lógica)", "Robótica [FIN BLOQUE 1]"),
            
            # Clase 15 y 16 (19/11 y 24/11): Sesión 3 IA (2 días seguidos)
            ("IA", "IA: Sesión 03 (Cuento/Cómic con NLM - Día 1/2)", "IA Sesión 03"),
            ("IA", "IA: Sesión 03 (Cuento/Cómic con NLM - Día 2/2)", "IA Sesión 03 concluida"),
            
            # Clase 17 (26/11/2026, Jue): ROB 2.1
            ("Robótica", "ROB: 2.1 Silla de Ruedas Eléctrica (Tracción diferencial)", "Robótica Bloque 2"),
            
            # Clase 18 (01/12/2026, Mar): Monográfico 3 (1 día)
            ("IA (Monográfico)", "IA: Monográfico 3 (Taller Especial Cuento con NLM)", "IA Monográfico 3"),
            
            # Clase 19 (03/12/2026, Jue): ROB 2.2
            ("Robótica", "ROB: 2.2 Roomba con sensor (Evasión de obstáculos)", "Robótica Bloque 2"),
            
            # Clase 20 y 21 (10/12 y 15/12): Sesión 4 IA (2 días seguidos)
            ("IA", "IA: Sesión 04 (Aporte de Valor Senior - Día 1/2)", "IA Sesión 04"),
            ("IA", "IA: Sesión 04 (Taller Práctico - Día 2/2)", "IA Sesión 04 concluida"),
            
            # Clase 22 (17/12/2026, Jue): ROB 3.1
            ("Robótica", "ROB: 3.1 Robot repartidor (Chasis diferencial)", "Robótica Bloque 3"),
            
            # [Vacaciones de Navidad: 18 dic - 6 ene]
            # Clase 23 (07/01/2027, Jue): Monográfico 4 (1 día)
            ("IA (Monográfico)", "IA: Monográfico 4 (Mi Biografía con IA)", "IA Monográfico 4"),
            
            # Clase 24 (12/01/2027, Mar): ROB 3.3
            ("Robótica", "ROB: 3.3 Avión con servomotores (Superficies móviles)", "Robótica Bloque 3"),
            
            # Clase 25 y 26 (14/01 y 19/01): Sesión 5 IA (2 días seguidos)
            ("IA", "IA: Sesión 05 (Sistema Solar 3D - Día 1/2)", "IA Sesión 05"),
            ("IA", "IA: Sesión 05 (NASA Eyes - Día 2/2)", "IA Sesión 05 concluida"),
            
            # Clase 27 (21/01/2027, Jue): ROB 3.4
            ("Robótica", "ROB: 3.4 Dron terrestre (Estabilidad y motores)", "Robótica Bloque 3"),
            
            # Clase 28 (26/01/2027, Mar): Monográfico 5 (1 día)
            ("IA (Monográfico)", "IA: Monográfico 5 (El Abuelo Tutor - Matemáticas e Historia)", "IA Monográfico 5"),
            
            # Clase 29 (28/01/2027, Jue): ROB 4.5
            ("Robótica", "ROB: 4.5 Brazo Robótico: Pinza y sensor", "Robótica Bloque 4"),
            
            # Clase 30 y 31 (02/02 y 04/02): Sesión 6 IA (2 días seguidos)
            ("IA", "IA: Sesión 06 (Cerebro Humano 3D - Día 1/2)", "IA Sesión 06"),
            ("IA", "IA: Sesión 06 (Red Neuronal - Día 2/2)", "IA Sesión 06 concluida"),
            
            # Clase 32 (09/02/2027, Mar): ROB 4.6
            ("Robótica", "ROB: 4.6 Brazo Robótico: Mano hidráulica", "Robótica Bloque 4"),
            
            # Clase 33 (11/02/2027, Jue): Monográfico 6 (Mapa y Gestión de Proyecto con IA - 1 día)
            ("IA (Monográfico)", "IA: Monográfico 6 (Mapa y Gestión de Proyecto con IA)", "IA Monográfico 6"),
            
            # Clase 34 (16/02/2027, Mar): ROB 5.1
            ("Robótica", "ROB: 5.1 Perro Unitree Go2 AIR (Cuadrúpedo autónomo)", "Robótica Bloque 5"),
            
            # Clase 35 y 36 (18/02 y 23/02): Sesión 7 IA (2 días seguidos)
            ("IA", "IA: Sesión 07 (Salud y Confort +65 - Día 1/2)", "IA Sesión 07"),
            ("IA", "IA: Sesión 07 (Hábitos Saludables - Día 2/2)", "IA Sesión 07 concluida"),
            
            # Clase 37 (25/02/2027, Jue): ROB 5.2
            ("Robótica", "ROB: 5.2 Robot Bípedo (Comunicación visual)", "Robótica Bloque 5"),
            
            # Clase 38 (02/03/2027, Mar): Monográfico 7 (NASA y Exploración Espacial con IA - 1 día)
            ("IA (Monográfico)", "IA: Monográfico 7 (NASA y Exploración Espacial con IA)", "IA [FIN MONOGRÁFICOS]"),
            
            # Clase 39 (04/03/2027, Jue): ROB 5.3
            ("Robótica", "ROB: 5.3 Androide MIXAMO (Cinemática humana)", "Robótica Bloque 5"),
            
            # Clase 40 y 41 (09/03 y 11/03): Sesión 8 IA (2 días seguidos)
            ("IA", "IA: Sesión 08 (Fotogrametría Pompeya - Día 1/2)", "IA Sesión 08"),
            ("IA", "IA: Sesión 08 (Visor 3D Arqueología - Día 2/2)", "IA Sesión 08 concluida"),
            
            # Clase 42 (16/03/2027, Mar): ROB 5.4 -> ¡ALTERNANCIA ESTRICTA!
            ("Robótica", "ROB: 5.4 Transformer (POO y enjambres)", "Robótica Bloque 5"),
            
            # Clase 43 y 44 (18/03 y 30/03): Sesión 9 IA (2 días seguidos)
            ("IA", "IA: Sesión 09 (Música e IA Sonora - Día 1/2)", "IA Sesión 09"),
            ("IA", "IA: Sesión 09 (Generación MIDI - Día 2/2)", "IA Sesión 09 concluida"),
            
            # Clase 45 (01/04/2027, Jue): ROB 5.5
            ("Robótica", "ROB: 5.5 Trío Dinámico Star Wars (R2D2, C3PO, BB8)", "Robótica Bloque 5"),
            
            # Clase 46 y 47 (06/04 y 08/04): Sesión 10 IA (2 días seguidos)
            ("IA", "IA: Sesión 10 (Cierre y Evaluación - Día 1/2)", "IA Sesión 10"),
            ("IA", "IA: Sesión 10 (Muestra Interactiva - Día 2/2)", "IA Sesión 10 concluida"),
            
            # Clase 48 (13/04/2027, Mar): ROB 5.6
            ("Robótica", "ROB: 5.6 Robot de combate (Animatrónica y defensa)", "Robótica [FIN BLOQUE 5]"),
            
            # Clase 49 y 50 (15/04 y 20/04): Sesión 11 IA (2 días seguidos)
            ("IA", "IA: Sesión 11 (Stradivarius y Acústica - Día 1/2)", "IA Sesión 11"),
            ("IA", "IA: Sesión 11 (Cuerdas y Resonancia - Día 2/2)", "IA Sesión 11 concluida"),
            
            # Clase 51 (22/04/2027, Jue): ROB 6.1
            ("Robótica", "ROB: 6.1 Transporte Espacial Autónomo", "Robótica Bloque 6"),
            
            # Clase 52 y 53 (27/04 y 29/04): Sesión 12 IA (2 días seguidos)
            ("IA", "IA: Sesión 12 (Estructura ADN 3D - Día 1/2)", "IA Sesión 12"),
            ("IA", "IA: Sesión 12 (Doble Hélice - Día 2/2)", "IA Sesión 12 concluida"),
            
            # Clase 54 (04/05/2027, Mar): ROB 6.2
            ("Robótica", "ROB: 6.2 Naves Espaciales: Star Wars (Halcón Milenario)", "Robótica Bloque 6"),
            
            # Clase 55 y 56 (06/05 y 11/05): Sesión 13 IA (2 días seguidos)
            ("IA", "IA: Sesión 13 (Júpiter y Lunas - Día 1/2)", "IA Sesión 13"),
            ("IA", "IA: Sesión 13 (Simulador Gravitatorio - Día 2/2)", "IA Sesión 13 concluida"),
            
            # Clase 57 (13/05/2027, Jue): ROB 6.3
            ("Robótica", "ROB: 6.3 Naves Espaciales: Star Trek (Enterprise)", "Robótica Bloque 6"),
            
            # [Semana de Mayores: 17 may - 23 may]
            # Clase 58 (25/05/2027, Mar): ROB 6.4
            ("Robótica", "ROB: 6.4 Naves Espaciales: Interstellar (Ranger)", "Robótica [TECHO ROBÓTICA ALCANZADO]"),
            
            # Clase 59 (27/05/2027, Jue): Sesión 14 Clausura del Curso
            ("IA", "IA: Sesión 14 (Clausura del Curso y Presentación de Proyectos)", "IA [CLAUSURA DEL CURSO]")
    ]

    # Generación cronológica día a día (69 fechas)
    cur = datetime.date(2026, 10, 1)
    end = datetime.date(2027, 5, 30)
    r_num = 13
    clase_cont = 1
    h_acum = 0.0

    while cur <= end:
        if cur.weekday() in (1, 3):  # Martes y Jueves
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
                if clase_cont <= 10:
                    area_v, tem_v, obs_v = octubre_reales[clase_cont]
                    est_v = "Impartida"
                    f_st = 8
                else:
                    f_idx = clase_cont - 11
                    area_v, tem_v, obs_v = future[f_idx]
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
    <col min="4" max="4" width="15" customWidth="1"/>
    <col min="5" max="5" width="16" customWidth="1"/>
    <col min="6" max="6" width="76" customWidth="1"/>
    <col min="7" max="7" width="15" customWidth="1"/>
    <col min="8" max="8" width="50" customWidth="1"/>
  </cols>
  <sheetData>
    {''.join(rows)}
  </sheetData>
</worksheet>"""

def build_scenario3_rows():
    rows = []
    title = "ESCENARIO 3: PREDICCIÓN CON CICLO ALTERNO ROBÓTICA - IA"
    sub = "Ciclo: Robótica -> IA (1ª mitad) -> Robótica -> Monográfico -> Robótica -> IA (2ª mitad) | Prioridad 100% Robótica"
    h_style = 12
    
    rows.append(f'<row r="1" ht="20">{cell_xml("A1", title, 1)}</row>')
    rows.append(f'<row r="2" ht="16">{cell_xml("A2", sub, 6)}</row>')
    
    # Resumen superior
    r_box = [
        ("PARÁMETRO DEL CURSO", "VALOR", "DIAGNÓSTICO AL 30 DE MAYO"),
        ("Total Sesiones Lectivas Restantes", "49 clases (73.5 h)", "De 05/11/2026 a 27/05/2027"),
        ("Robótica Programada (Prioridad)", "31 clases (33 totales con octubre)", "Bloques 1 a 6 COMPLETOS al 100% (cero descartes)"),
        ("IA Programada (Ciclo Regular + Monos)", "18 clases (24 totales con octubre)", "6 Monográficos completos + 6 Sesiones regulares completas"),
        ("¿LLEGAMOS BIEN O NOS PASAMOS?", "🎯 ENCAJE EXACTO (49 / 49)", "¡CERO DÍAS DE DESVIACIÓN! Encaje perfecto."),
        ("Techo Robótica al 30 de Mayo", "Bloque 6 (6.7 Estación Espacial ISS)", "Alcanza todos los robots, androides y naves espaciales"),
        ("Techo IA al 30 de Mayo", "6 Monográficos + Sesión 08 (Pompeya)", "Manejo integral de herramientas IA y talleres prácticos"),
        ("Estructura del Ciclo (3 sem. / 6 sesiones)", "ROB -> IA_1 -> ROB -> MONO -> ROB -> IA_2", "6 ciclos (36 clases) + 13 clases finales para culminar Robótica")
    ]
    for ro, (c1, c2, c3) in enumerate(r_box, start=4):
        st = h_style if ro == 4 else (7 if "LLEGAMOS" in c1 else 5)
        st_val = h_style if ro == 4 else (7 if "LLEGAMOS" in c1 else 4)
        rows.append(f'<row r="{ro}" ht="16">{cell_xml(f"B{ro}", c1, st)}{cell_xml(f"C{ro}", c2, st_val)}{cell_xml(f"D{ro}", c3, st)}</row>')
        
    # Cabecera tabla
    rows.append(f'<row r="13" ht="18">' +
                cell_xml("A13", "Nº CLASE", h_style) + cell_xml("B13", "FECHA", h_style) + cell_xml("C13", "DÍA", h_style) +
                cell_xml("D13", "ÁREA", h_style) + cell_xml("E13", "ESTADO", h_style) +
                cell_xml("F13", "TEMARIO PROYECTADO", h_style) + cell_xml("G13", "HORAS ACUM.", h_style) + cell_xml("H13", "HITO / FASE DEL CICLO", h_style) + '</row>')
    
    # 49 clases proyectadas para Escenario 3
    future_s3 = [
        # CICLO 1 (Clases 11 a 16)
        ("Robótica", "ROB: 1.3 Ascensor (Mecanismo y polea)", "Robótica Bloque 1 [Ciclo 1 - Paso 1]"),
        ("IA", "IA: Sesión 03 (Cuento/Cómic con NLM - Parte 1/2)", "IA Sesión 03 [Ciclo 1 - Paso 2]"),
        ("Robótica", "ROB: 1.4 Semáforos inteligentes (Lógica y estados)", "Robótica [FIN BLOQUE 1] [Ciclo 1 - Paso 3]"),
        ("IA (Monográfico)", "IA: Monográfico 2 (Manejo de Gemini Book / NotebookLM)", "IA Monográfico 2 [Ciclo 1 - Paso 4]"),
        ("Robótica", "ROB: 2.1 Silla de Ruedas Eléctrica (Tracción diferencial)", "Robótica Bloque 2 [Ciclo 1 - Paso 5]"),
        ("IA", "IA: Sesión 03 (Cuento/Cómic con NLM - Parte 2/2)", "IA [FIN SESIÓN 03] [Ciclo 1 - Paso 6]"),

        # CICLO 2 (Clases 17 a 22)
        ("Robótica", "ROB: 2.2 Roomba con sensor (Bucle infinito y evasión)", "Robótica Bloque 2 [Ciclo 2 - Paso 1]"),
        ("IA", "IA: Sesión 04 (Aporte de Valor Senior - Parte 1/2)", "IA Sesión 04 [Ciclo 2 - Paso 2]"),
        ("Robótica", "ROB: 2.3 Aparcamiento asistido (Condición IF-ELSE)", "Robótica Bloque 2 [Ciclo 2 - Paso 3]"),
        ("IA (Monográfico)", "IA: Monográfico 3 (Taller Especial Cuento con NLM)", "IA Monográfico 3 [Ciclo 2 - Paso 4]"),
        ("Robótica", "ROB: 2.4 Ozobot (El color como lenguaje y códigos)", "Robótica Bloque 2 [Ciclo 2 - Paso 5]"),
        ("IA", "IA: Sesión 04 (Aporte de Valor Senior - Parte 2/2)", "IA [FIN SESIÓN 04] [Ciclo 2 - Paso 6]"),

        # CICLO 3 (Clases 23 a 28)
        ("Robótica", "ROB: 2.5 Cámara de seguridad (Variable simple y alarma)", "Robótica [FIN BLOQUE 2] [Ciclo 3 - Paso 1]"),
        ("IA", "IA: Sesión 05 (Creatividad Visual y Generación de Imagen - Parte 1/2)", "IA Sesión 05 [Ciclo 3 - Paso 2]"),
        ("Robótica", "ROB: 3.1 Robot repartidor (Chasis diferencial y ruta)", "Robótica Bloque 3 [Ciclo 3 - Paso 3]"),
        ("IA (Monográfico)", "IA: Monográfico 4 (Mi Biografía con IA y Redacción Guiada)", "IA Monográfico 4 [Ciclo 3 - Paso 4]"),
        ("Robótica", "ROB: 3.2 Coche ELEGOO con cámara (Visión artificial básica)", "Robótica Bloque 3 [Ciclo 3 - Paso 5]"),
        ("IA", "IA: Sesión 05 (Creatividad Visual y Diseño - Parte 2/2)", "IA [FIN SESIÓN 05] [Ciclo 3 - Paso 6]"),

        # CICLO 4 (Clases 29 a 34)
        ("Robótica", "ROB: 3.3 Avión con servos (Posición angular exacta)", "Robótica Bloque 3 [Ciclo 4 - Paso 1]"),
        ("IA", "IA: Sesión 06 (Asistente Personal de Salud y Bienestar - Parte 1/2)", "IA Sesión 06 [Ciclo 4 - Paso 2]"),
        ("Robótica", "ROB: 3.4 Dron autónomo (Navegación 3D en tres ejes)", "Robótica Bloque 3 [Ciclo 4 - Paso 3]"),
        ("IA (Monográfico)", "IA: Monográfico 5 (El Abuelo Tutor: Matemáticas e Historia)", "IA Monográfico 5 [Ciclo 4 - Paso 4]"),
        ("Robótica", "ROB: 3.5 Penguin-BOT (Sincronización cinemática de servos)", "Robótica [FIN BLOQUE 3] [Ciclo 4 - Paso 5]"),
        ("IA", "IA: Sesión 06 (Asistente de Salud y Vida Diaria - Parte 2/2)", "IA [FIN SESIÓN 06] [Ciclo 4 - Paso 6]"),

        # CICLO 5 (Clases 35 a 40)
        ("Robótica", "ROB: 4.1 Base giratoria de Brazo Robótico (Parámetro)", "Robótica Bloque 4 [Ciclo 5 - Paso 1]"),
        ("IA", "IA: Sesión 07 (Domótica y Entorno Inteligente - Parte 1/2)", "IA Sesión 07 [Ciclo 5 - Paso 2]"),
        ("Robótica", "ROB: 4.2 Hombro robótico (Coordinación de dos motores)", "Robótica Bloque 4 [Ciclo 5 - Paso 3]"),
        ("IA (Monográfico)", "IA: Monográfico 6 (Mapa y Gestión de Proyectos con IA)", "IA Monográfico 6 [Ciclo 5 - Paso 4]"),
        ("Robótica", "ROB: 4.3 Codo robótico (Secuencia de tres articulaciones)", "Robótica Bloque 4 [Ciclo 5 - Paso 5]"),
        ("IA", "IA: Sesión 07 (Domótica y Control por Voz - Parte 2/2)", "IA [FIN SESIÓN 07] [Ciclo 5 - Paso 6]"),

        # CICLO 6 (Clases 41 a 46)
        ("Robótica", "ROB: 4.4 Muñeca robótica (Variable de orientación espacial)", "Robótica Bloque 4 [Ciclo 6 - Paso 1]"),
        ("IA", "IA: Sesión 08 (Fotogrametría y Reconstrucción 3D Pompeya - Parte 1/2)", "IA Sesión 08 [Ciclo 6 - Paso 2]"),
        ("Robótica", "ROB: 4.5 Pinza robótica (Sensor de presión y agarre)", "Robótica Bloque 4 [Ciclo 6 - Paso 3]"),
        ("IA (Monográfico)", "IA: Monográfico 7 (NASA y Exploración Espacial con IA - 5 Portales 3D)", "IA [FIN MONOGRÁFICOS] [Ciclo 6 - Paso 4]"),
        ("Robótica", "ROB: 4.6 Mano hidráulica (Fuerza controlada y cinemática)", "Robótica [FIN BLOQUE 4] [Ciclo 6 - Paso 5]"),
        ("IA", "IA: Sesión 08 (Fotogrametría y Museografía Virtual - Parte 2/2)", "IA [FIN SESIÓN 08] [Ciclo 6 - Paso 6]"),

        # FASE DE CULMINACIÓN DE ROBÓTICA - BLOQUES 5 Y 6 (Clases 47 a 59)
        ("Robótica", "ROB: 5.1 Perro Unitree Go2 AIR (Navegación cuadrúpeda y LiDAR)", "Robótica Bloque 5 [Prioridad Robótica]"),
        ("Robótica", "ROB: 5.2 Robot Bípedo (Equilibrio dinámico y comunicación visual)", "Robótica Bloque 5 [Prioridad Robótica]"),
        ("Robótica", "ROB: 5.3 Androide MIXAMO (Captura de movimiento y cinemática)", "Robótica Bloque 5 [Prioridad Robótica]"),
        ("Robótica", "ROB: 5.4 Transformer (POO, cambio morfológico y enjambres)", "Robótica Bloque 5 [Prioridad Robótica]"),
        ("Robótica", "ROB: 5.5 Trío Dinámico Star Wars (R2-D2, BB-8, D-O)", "Robótica Bloque 5 [Prioridad Robótica]"),
        ("Robótica", "ROB: 5.6 Robot de Combate (Estructura reforzada y estrategia)", "Robótica [FIN BLOQUE 5] [Prioridad Robótica]"),
        ("Robótica", "ROB: 6.1 Transporte Espacial Autónomo (Trayectoria y telemetría)", "Robótica Bloque 6 [Prioridad Robótica]"),
        ("Robótica", "ROB: 6.2 Naves Espaciales: Star Wars (Halcón Milenario y X-Wing)", "Robótica Bloque 6 [Prioridad Robótica]"),
        ("Robótica", "ROB: 6.3 Naves Espaciales: Star Trek (U.S.S. Enterprise NCC-1701)", "Robótica Bloque 6 [Prioridad Robótica]"),
        ("Robótica", "ROB: 6.4 Naves Espaciales: Interstellar (Ranger y acoplamiento)", "Robótica Bloque 6 [Prioridad Robótica]"),
        ("Robótica", "ROB: 6.5 SpaceX Falcon 9 (Propulsión y aterrizaje vertical)", "Robótica Bloque 6 [Prioridad Robótica]"),
        ("Robótica", "ROB: 6.6 Transbordador Espacial (Reentrada y planeo orbital)", "Robótica Bloque 6 [Prioridad Robótica]"),
        ("Robótica", "ROB: 6.7 Estación Espacial Internacional ISS (Acoplamiento y Clausura)", "Robótica [FIN BLOQUE 6 Y FIN DE CURSO]")
    ]

    cur = datetime.date(2026, 10, 1)
    end = datetime.date(2027, 5, 30)
    r_num = 14
    clase_cont = 1
    h_acum = 0.0

    while cur <= end:
        if cur.weekday() in (1, 3):  # Martes y Jueves
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
                if clase_cont <= 10:
                    area_v, tem_v, obs_v = octubre_reales[clase_cont]
                    est_v = "Impartida"
                    f_st = 8
                else:
                    f_idx = clase_cont - 11
                    area_v, tem_v, obs_v = future_s3[f_idx]
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
    <col min="4" max="4" width="15" customWidth="1"/>
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

import subprocess
import shutil

# Cerrar el libro en Microsoft Excel si estuviese abierto para liberar el bloqueo exclusivo en macOS
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
print("    Hoja 1: 'Bitacora de Clases' (Registro real + Resumen de Métricas).")
print("    Hoja 2: 'Calendario de Clases B1-B6' (Itinerario Oficial Planificado con 49 clases restantes).")
print("    Hoja 3: 'Escenario 3 - Ciclo Robótica-IA' (Predicción con ciclo alterno y prioridad 100% Robótica).")
print("    100% nativo en biblioteca estándar de Python (sin pip ni dependencias externas).")
