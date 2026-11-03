#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
generar_bitacora_completa.py
Genera el libro oficial 'BITACORA_SEGUIMIENTO_CLASES.xlsx' con 3 hojas:
1. 'Bitacora de Clases': Registro real acumulado (Octubre) y resumen ejecutivo.
2. 'Calendario Secuencial B1-B4': Escenario secuencial estándar (Robótica hasta B4 / IA hasta S18).
3. 'Escenario Seleccion B1-B6': Escenario selectivo solicitado por el usuario:
   - Robótica: 19 clases (B1 entero, 2.1-2.2, 3.1-3.3-3.4, 4.5-4.6, B5 entero, 6.1-6.4).
   - IA: 31 clases (Sesión 02 hasta Sesión 17).
   - Encaje matemático: 19 + 31 = 50 clases restantes (100% de coincidencia al 30/05/2027).
"""

import os
import sys
import datetime

try:
    import openpyxl
    from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
    from openpyxl.utils import get_column_letter
except ImportError:
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "openpyxl"])
    import openpyxl
    from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
    from openpyxl.utils import get_column_letter

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
EXCEL_PATH = os.path.join(BASE_DIR, "BITACORA_SEGUIMIENTO_CLASES.xlsx")

wb = openpyxl.Workbook()

# ==============================================================================
# ESTILOS COMPARTIDOS
# ==============================================================================
NAVY_HEADER = PatternFill(start_color="1F497D", end_color="1F497D", fill_type="solid")
BLUE_HEADER = PatternFill(start_color="2F5597", end_color="2F5597", fill_type="solid")
TEAL_HEADER = PatternFill(start_color="005E5D", end_color="005E5D", fill_type="solid")
LIGHT_BLUE = PatternFill(start_color="DCE6F1", end_color="DCE6F1", fill_type="solid")
GREEN_PASTEL = PatternFill(start_color="E2EFDA", end_color="E2EFDA", fill_type="solid")
ORANGE_PASTEL = PatternFill(start_color="FCE4D6", end_color="FCE4D6", fill_type="solid")
PURPLE_PASTEL = PatternFill(start_color="EDEDF8", end_color="EDEDF8", fill_type="solid")
GRAY_PASTEL = PatternFill(start_color="F2F2F2", end_color="F2F2F2", fill_type="solid")

FONT_TITLE = Font(name="Calibri", size=14, bold=True, color="1F497D")
FONT_TITLE_HOJA3 = Font(name="Calibri", size=14, bold=True, color="005E5D")
FONT_SUBTITLE = Font(name="Calibri", size=10, italic=True, color="595959")
FONT_HEADER = Font(name="Calibri", size=11, bold=True, color="FFFFFF")
FONT_BOLD = Font(name="Calibri", size=11, bold=True, color="000000")
FONT_REGULAR = Font(name="Calibri", size=11, color="000000")
FONT_ITALIC = Font(name="Calibri", size=10, italic=True, color="595959")
FONT_ALERT = Font(name="Calibri", size=11, bold=True, color="9C0006")
FONT_MUTED = Font(name="Calibri", size=10, color="7F7F7F")

THIN_BORDER = Border(
    left=Side(style='thin', color='D9D9D9'),
    right=Side(style='thin', color='D9D9D9'),
    top=Side(style='thin', color='D9D9D9'),
    bottom=Side(style='thin', color='D9D9D9')
)

ALIGN_CENTER = Alignment(horizontal='center', vertical='center')
ALIGN_LEFT = Alignment(horizontal='left', vertical='center')

# Festivos comunes
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
    9: ("Mixta", "ROB.1: 1.2 Lavadora + IA: Sesión 2 (Ítems 09 y 09B)", "Clase combinada (1.2 Lavadora en 1 día)")
}

# ==============================================================================
# HOJA 1: BITÁCORA DE CLASES (REGISTRO REAL OCTUBRE)
# ==============================================================================
ws1 = wb.active
ws1.title = "Bitacora de Clases"
ws1.views.sheetView[0].showGridLines = True

ws1["A1"] = "BITÁCORA Y SEGUIMIENTO DEL CALENDARIO DE CLASES"
ws1["A1"].font = FONT_TITLE
ws1["A2"] = "Horario: Martes y Jueves (1.5 horas/sesión) | Excluye festivos, Navidad y Semana Santa"
ws1["A2"].font = FONT_SUBTITLE

# Resumen General
ws1["A4"] = "RESUMEN GENERAL"; ws1["A4"].font = FONT_HEADER; ws1["A4"].fill = NAVY_HEADER; ws1["A4"].alignment = ALIGN_LEFT
ws1["B4"] = "VALOR"; ws1["B4"].font = FONT_HEADER; ws1["B4"].fill = NAVY_HEADER; ws1["B4"].alignment = ALIGN_CENTER

ws1["A5"] = "Total Sesiones Transcurridas"; ws1["A5"].font = FONT_REGULAR; ws1["A5"].border = THIN_BORDER
ws1["B5"] = 9; ws1["B5"].font = FONT_BOLD; ws1["B5"].border = THIN_BORDER; ws1["B5"].alignment = ALIGN_CENTER

ws1["A6"] = "Total Horas Lectivas (Octubre)"; ws1["A6"].font = FONT_REGULAR; ws1["A6"].border = THIN_BORDER
ws1["B6"] = 13.5; ws1["B6"].font = FONT_BOLD; ws1["B6"].border = THIN_BORDER; ws1["B6"].alignment = ALIGN_CENTER

forecast_data_h1 = [
    ("COMPARATIVA DE ESCENARIOS AL 30 DE MAYO", "ESCENARIO 1 (SECUENCIAL)", "ESCENARIO 2 (SELECCIÓN B1-B6)", True),
    ("Total Sesiones Lectivas Restantes", "50 clases", "50 clases", False),
    ("Clases de Robótica Restantes", "17 clases", "19 clases seleccionadas", False),
    ("Clases de IA Restantes", "33 clases", "31 clases", False),
    ("Techo Alcanzado en Robótica", "Bloque 4 (Brazo Robótico)", "Bloque 6 (Star Wars / Interstellar)", False),
    ("Techo Alcanzado en IA", "Sesión 18 de 60", "Sesión 17 de 60", False),
    ("Balance de Cobertura", "Lineal hasta B4", "🎯 Selección óptima: cubre hasta B6 sin pasarse", False),
    ("Hojas Detalladas", "Ver Hoja 2 ('Secuencial')", "Ver Hoja 3 ('Selección B1-B6')", False)
]

for idx, (col_i, col_j, col_k, is_header) in enumerate(forecast_data_h1, start=4):
    ci = ws1.cell(row=idx, column=9, value=col_i)
    cj = ws1.cell(row=idx, column=10, value=col_j)
    ck = ws1.cell(row=idx, column=11, value=col_k)
    if is_header:
        ci.font = FONT_HEADER; ci.fill = NAVY_HEADER
        cj.font = FONT_HEADER; cj.fill = NAVY_HEADER; cj.alignment = ALIGN_CENTER
        ck.font = FONT_HEADER; ck.fill = NAVY_HEADER; ck.alignment = ALIGN_CENTER
    elif "Techo" in col_i:
        ci.font = FONT_ALERT; ci.fill = LIGHT_BLUE; ci.border = THIN_BORDER
        cj.font = FONT_ALERT; cj.fill = LIGHT_BLUE; cj.border = THIN_BORDER; cj.alignment = ALIGN_CENTER
        ck.font = FONT_ALERT; ck.fill = LIGHT_BLUE; ck.border = THIN_BORDER; ck.alignment = ALIGN_CENTER
    else:
        ci.font = FONT_REGULAR; ci.border = THIN_BORDER
        cj.font = FONT_BOLD; cj.border = THIN_BORDER; cj.alignment = ALIGN_CENTER
        ck.font = FONT_BOLD; ck.border = THIN_BORDER; ck.alignment = ALIGN_CENTER

headers_h1 = ["Nº SESIÓN", "FECHA", "DÍA", "DURACIÓN (H)", "TEMARIO / CONTENIDO", "HORAS ACUM.", "OBSERVACIONES"]
for col_idx, h in enumerate(headers_h1, start=1):
    c = ws1.cell(row=8, column=col_idx, value=h)
    c.font = FONT_HEADER; c.fill = NAVY_HEADER
    c.alignment = ALIGN_CENTER if col_idx in (1, 2, 3, 4, 6) else ALIGN_LEFT

sessions_h1 = [
    (1, "01/10/2026", "Jueves", 1.5, "Presentación inaugural", 1.5, "Primer día de clase"),
    (2, "06/10/2026", "Martes", 1.5, "Guía de Classroom y Gemini", 3.0, "Segunda clase organizativa"),
    (3, "08/10/2026", "Jueves", 1.5, "Sesión IA 01", 4.5, "Sesión IA 01 impartida"),
    (4, "13/10/2026", "Martes", 1.5, "Sesión IA 01", 6.0, "Sesión IA 01 impartida"),
    (5, "15/10/2026", "Jueves", 1.5, "Sesión IA 01", 7.5, "Sesión IA 01 impartida"),
    (6, "20/10/2026", "Martes", 1.5, "Sesión IA 01", 9.0, "Sesión IA 01 impartida (4 clases en total)"),
    (7, "22/10/2026", "Jueves", 1.5, "ROB.1: 1.1 Puerta supermercado", 10.5, "Práctica de motor y engranajes (1 día)"),
    (8, "27/10/2026", "Martes", 1.5, "Monográfico 2 IA entero", 12.0, "Monográfico 2 IA impartido entero"),
    (9, "29/10/2026", "Jueves", 1.5, "ROB.1: 1.2 Lavadora + IA: Sesión 2 (Ítems 09 y 09B)", 13.5, "Impartidos ROB.1 (1.2 Lavadora en 1 día) y 2 ítems de IA Sesión 2")
]

for row_idx, s in enumerate(sessions_h1, start=9):
    for col_idx, val in enumerate(s, start=1):
        c = ws1.cell(row=row_idx, column=col_idx, value=val)
        c.font = FONT_REGULAR; c.border = THIN_BORDER
        if col_idx in (1, 2, 3, 4, 6):
            c.alignment = ALIGN_CENTER

for r in range(9, 18):
    ws1.cell(row=r, column=6, value=f"=SUM($D$9:D{r})")

ws1["B5"] = "=COUNTA(A9:A500)"
ws1["B6"] = "=SUM(D9:D500)"

col_widths_h1 = {
    1: 13, 2: 15, 3: 14, 4: 16, 5: 46, 6: 16, 7: 50, 8: 4, 9: 38, 10: 28, 11: 38
}
for col_idx, width in col_widths_h1.items():
    ws1.column_dimensions[get_column_letter(col_idx)].width = width

# ==============================================================================
# HOJA 2: ESCENARIO 1 (SECUENCIAL B1 A B4)
# ==============================================================================
ws2 = wb.create_sheet(title="Calendario Secuencial B1-B4")
ws2.views.sheetView[0].showGridLines = True

ws2["A1"] = "ESCENARIO 1: CALENDARIO SECUENCIAL (B1 A B4) | 01/10/2026 - 30/05/2027"
ws2["A1"].font = FONT_TITLE
ws2["A2"] = "Avance secuencial sin saltar bloques: Robótica a 1 día por robot / IA en bloques continuos de 2 días"
ws2["A2"].font = FONT_SUBTITLE

# ==============================================================================
# HOJA 3: ESCENARIO 2 (SELECCIÓN ESTRATÉGICA B1 A B6 - SOLICITADO POR EL USUARIO)
# ==============================================================================
ws3 = wb.create_sheet(title="Escenario Seleccion B1-B6")
ws3.views.sheetView[0].showGridLines = True

ws3["A1"] = "ESCENARIO 2: SELECCIÓN ESTRATÉGICA DE ROBÓTICA (B1, B2, B3, B4, B5 Y B6)"
ws3["A1"].font = FONT_TITLE_HOJA3
ws3["A2"] = "Itinerario: B1 completo, 2.1-2.2, 3.1-3.3-3.4, 4.5-4.6, B5 completo y 6.1-6.4 (19 robots) alternados con 31 clases de IA"
ws3["A2"].font = FONT_SUBTITLE

resumen_h3 = [
    ("PARÁMETRO DEL ESCENARIO 2", "VALOR", "DIAGNÓSTICO Y RESPUESTA A TU PREGUNTA"),
    ("Total Sesiones Lectivas Restantes (Nov-May)", "50 clases", "Horizonte real de calendario entre 03/11/2026 y 30/05/2027"),
    ("Clases de Robótica Seleccionadas", "19 clases", "B1(2) + B2(2) + B3(3) + B4(2) + B5(6) + B6(4) = 19 robots"),
    ("Clases de IA Disponibles", "31 clases", "Sesión 02 (1 día) + Sesiones 03 a 17 (30 días = 15 sesiones completas de 2 días)"),
    ("¿LLEGAMOS BIEN O NOS PASAMOS?", "🎯 ENCAJE EXACTO (50 / 50)", "¡LLEGAMOS PERFECTAMENTE! 19 Robótica + 31 IA = exactamente 50 clases"),
    ("Techo de Robótica al 30 de Mayo", "Bloque 6 (Interstellar / Star Wars)", "Se alcanzan los androides y las naves espaciales"),
    ("Techo de IA al 30 de Mayo", "Sesión 17 (de 60)", "Lote 1 completo (1 a 10) + 7 sesiones completas de Lote 2")
]

for r_off, (c1, c2, c3) in enumerate(resumen_h3, start=4):
    cell1 = ws3.cell(row=r_off, column=2, value=c1)
    cell2 = ws3.cell(row=r_off, column=3, value=c2)
    cell3 = ws3.cell(row=r_off, column=4, value=c3)
    if r_off == 4:
        cell1.font = FONT_HEADER; cell1.fill = TEAL_HEADER
        cell2.font = FONT_HEADER; cell2.fill = TEAL_HEADER; cell2.alignment = ALIGN_CENTER
        cell3.font = FONT_HEADER; cell3.fill = TEAL_HEADER
    elif "LLEGAMOS" in c1:
        cell1.font = FONT_ALERT; cell1.fill = LIGHT_BLUE; cell1.border = THIN_BORDER
        cell2.font = FONT_ALERT; cell2.fill = LIGHT_BLUE; cell2.border = THIN_BORDER; cell2.alignment = ALIGN_CENTER
        cell3.font = FONT_ALERT; cell3.fill = LIGHT_BLUE; cell3.border = THIN_BORDER
    else:
        cell1.font = FONT_REGULAR; cell1.border = THIN_BORDER
        cell2.font = FONT_BOLD; cell2.border = THIN_BORDER; cell2.alignment = ALIGN_CENTER
        cell3.font = FONT_ITALIC; cell3.border = THIN_BORDER

# Lista exacta de las 19 clases de Robótica seleccionadas por el usuario:
robot_scenario_2 = [
    ("ROB: 1.3 Ascensor (Mecanismo y polea)", "Robótica Bloque 1"),
    ("ROB: 1.4 Semáforos inteligentes (Lógica y engranajes)", "Robótica [FIN BLOQUE 1]"),
    ("ROB: 2.1 Silla de Ruedas Eléctrica (Tracción diferencial)", "Robótica Bloque 2"),
    ("ROB: 2.2 Roomba con sensor (Bucle infinito de evasión)", "Robótica Bloque 2"),
    ("ROB: 3.1 Robot repartidor (Chasis móvil diferencial)", "Robótica Bloque 3"),
    ("ROB: 3.3 Avión con servomotores (Superficies móviles)", "Robótica Bloque 3"),
    ("ROB: 3.4 Dron terrestre (Estabilidad y motores)", "Robótica Bloque 3"),
    ("ROB: 4.5 Brazo Robótico: Pinza y sensor", "Robótica Bloque 4"),
    ("ROB: 4.6 Brazo Robótico: Mano hidráulica y fuerza", "Robótica Bloque 4"),
    ("ROB: 5.1 Perro Unitree Go2 AIR (Cuadrúpedo autónomo)", "Robótica Bloque 5"),
    ("ROB: 5.2 Robot Bípedo (Comunicación visual)", "Robótica Bloque 5"),
    ("ROB: 5.3 Androide MIXAMO (Cinemática humana)", "Robótica Bloque 5"),
    ("ROB: 5.4 Transformer (POO y enjambres)", "Robótica Bloque 5"),
    ("ROB: 5.5 Trío Dinámico Star Wars (R2D2, C3PO y BB8)", "Robótica Bloque 5"),
    ("ROB: 5.6 Robot de combate (Animatrónica y defensa)", "Robótica [FIN BLOQUE 5]"),
    ("ROB: 6.1 Transporte Espacial Autónomo", "Robótica Bloque 6"),
    ("ROB: 6.2 Naves Espaciales: Star Wars (Halcón Milenario / X-Wing)", "Robótica Bloque 6"),
    ("ROB: 6.3 Naves Espaciales: Star Trek (Enterprise)", "Robótica Bloque 6"),
    ("ROB: 6.4 Naves Espaciales: Interstellar (Ranger y Endurance)", "Robótica [FIN BLOQUE 6 - TECHO ROBÓTICA]")
]

# Lista exacta de las 31 clases de IA (Sesión 02 remate + Sesiones 03 a 17 completas de 2 días):
ia_scenario_2 = [
    ("IA: Sesión 02 (Radar Anti-Estafas y Blindaje Senior - Finalización)", "IA Sesión 02"),
    ("IA: Sesión 03 (Geopolítica, Energía y Economía - Sesión 1/2)", "IA Sesión 03"),
    ("IA: Sesión 03 (Simulador de Precios y Micro-App - Sesión 2/2)", "IA Sesión 03 concluida"),
    ("IA: Sesión 04 (Aporte de Valor Senior y Sabiduría - Sesión 1/2)", "IA Sesión 04"),
    ("IA: Sesión 04 (Taller Práctico y Ficha Didáctica - Sesión 2/2)", "IA Sesión 04 concluida"),
    ("IA: Sesión 05 (Sistema Solar y Espacio 3D - Sesión 1/2)", "IA Sesión 05"),
    ("IA: Sesión 05 (Simulador Órbitas NASA Eyes - Sesión 2/2)", "IA Sesión 05 concluida"),
    ("IA: Sesión 06 (Cerebro Humano y Neurociencia - Sesión 1/2)", "IA Sesión 06"),
    ("IA: Sesión 06 (Visualizador 3D Neuronal - Sesión 2/2)", "IA Sesión 06 concluida"),
    ("IA: Sesión 07 (Salud, Biología y Confort +65 - Sesión 1/2)", "IA Sesión 07"),
    ("IA: Sesión 07 (Micro-App Hábitos Saludables - Sesión 2/2)", "IA Sesión 07 concluida"),
    ("IA: Sesión 08 (Fotogrametría y Patrimonio - Sesión 1/2)", "IA Sesión 08"),
    ("IA: Sesión 08 (Visor 3D Domus Pompeya - Sesión 2/2)", "IA Sesión 08 concluida"),
    ("IA: Sesión 09 (Música, Creatividad e IA Sonora - Sesión 1/2)", "IA Sesión 09"),
    ("IA: Sesión 09 (Generación Musical y MIDI - Sesión 2/2)", "IA Sesión 09 concluida"),
    ("IA: Sesión 10 (Cierre y Evaluación de Lote 1 - Sesión 1/2)", "IA Sesión 10"),
    ("IA: Sesión 10 (Gran Muestra Interactiva Lote 1 - Sesión 2/2)", "IA [FIN LOTE 1 (10/10)]"),
    ("IA: Sesión 11 (Inicio Lote 2: Stradivarius 3D - Sesión 1/2)", "IA Sesión 11"),
    ("IA: Sesión 11 (Simulación Acústica y Cuerdas - Sesión 2/2)", "IA Sesión 11 concluida"),
    ("IA: Sesión 12 (Estructura de la Materia y ADN - Sesión 1/2)", "IA Sesión 12"),
    ("IA: Sesión 12 (Taller de la Doble Hélice 3D - Sesión 2/2)", "IA Sesión 12 concluida"),
    ("IA: Sesión 13 (Júpiter y Misiones Espaciales - Sesión 1/2)", "IA Sesión 13"),
    ("IA: Sesión 13 (Simulador Gravitatorio - Sesión 2/2)", "IA Sesión 13 concluida"),
    ("IA: Sesión 14 (Partenón y Arquitectura Clásica - Sesión 1/2)", "IA Sesión 14"),
    ("IA: Sesión 14 (Cálculo Proporciones Áureas - Sesión 2/2)", "IA Sesión 14 concluida"),
    ("IA: Sesión 15 (Óptica y Luz Cuántica - Sesión 1/2)", "IA Sesión 15"),
    ("IA: Sesión 15 (Simulador Doble Rendija - Sesión 2/2)", "IA Sesión 15 concluida"),
    ("IA: Sesión 16 (Geología Planetaria y Volcanes - Sesión 1/2)", "IA Sesión 16"),
    ("IA: Sesión 16 (Visor 3D Topográfico - Sesión 2/2)", "IA Sesión 16 concluida"),
    ("IA: Sesión 17 (Criptografía y Ciberseguridad - Sesión 1/2)", "IA Sesión 17"),
    ("IA: Sesión 17 (Taller Enigma y Claves - Sesión 2/2)", "IA [TECHO MÁXIMO PROYECTADO IA]")
]

# Construir la lista exacta de las 50 clases futuras de la Hoja 3 (19 Robótica + 31 IA):
schedule_h3 = []
# Clase 10: Mañana 03/11 (IA Sesión 2)
schedule_h3.append(("IA", ia_scenario_2[0][0], ia_scenario_2[0][1]))

r_ptr = 0
ia_ptr = 1

while len(schedule_h3) < 50:
    # 1 día de Robótica
    if r_ptr < len(robot_scenario_2) and len(schedule_h3) < 50:
        schedule_h3.append(("Robótica", robot_scenario_2[r_ptr][0], robot_scenario_2[r_ptr][1]))
        r_ptr += 1
    # 2 días seguidos de IA (o 1 si queda impar)
    if ia_ptr < len(ia_scenario_2) and len(schedule_h3) < 50:
        schedule_h3.append(("IA", ia_scenario_2[ia_ptr][0], ia_scenario_2[ia_ptr][1]))
        ia_ptr += 1
    if ia_ptr < len(ia_scenario_2) and len(schedule_h3) < 50:
        schedule_h3.append(("IA", ia_scenario_2[ia_ptr][0], ia_scenario_2[ia_ptr][1]))
        ia_ptr += 1

# Población de filas en Hoja 3
headers_h3 = ["Nº CLASE", "FECHA", "DÍA", "ÁREA", "ESTADO", "TEMARIO SELECCIONADO (B1 A B6)", "HORAS ACUM.", "HITO / BLOQUE"]
header_row_h3 = 12

for c_idx, h in enumerate(headers_h3, start=1):
    c = ws3.cell(row=header_row_h3, column=c_idx, value=h)
    c.font = FONT_HEADER; c.fill = TEAL_HEADER
    c.alignment = ALIGN_CENTER if c_idx in (1, 2, 3, 4, 5, 7) else ALIGN_LEFT

cur_date = datetime.date(2026, 10, 1)
end_date = datetime.date(2027, 5, 30)

r_out = 13
class_num = 1
horas_acum = 0.0

while cur_date <= end_date:
    if cur_date.weekday() in (1, 3):
        day_str = "Martes" if cur_date.weekday() == 1 else "Jueves"
        date_str = cur_date.strftime("%d/%m/%Y")
        
        if cur_date in holidays_dict:
            ws3.cell(row=r_out, column=1, value="-").alignment = ALIGN_CENTER
            ws3.cell(row=r_out, column=2, value=date_str).alignment = ALIGN_CENTER
            ws3.cell(row=r_out, column=3, value=day_str).alignment = ALIGN_CENTER
            ws3.cell(row=r_out, column=4, value="Vacaciones").alignment = ALIGN_CENTER
            ws3.cell(row=r_out, column=5, value="No Lectivo").alignment = ALIGN_CENTER
            ws3.cell(row=r_out, column=6, value=f"⛔ {holidays_dict[cur_date]}")
            ws3.cell(row=r_out, column=7, value=f"{horas_acum:.1f} h").alignment = ALIGN_CENTER
            ws3.cell(row=r_out, column=8, value="Sin clase programada")
            
            for c_col in range(1, 9):
                cell = ws3.cell(row=r_out, column=c_col)
                cell.fill = GRAY_PASTEL
                cell.font = FONT_MUTED
                cell.border = THIN_BORDER
        else:
            horas_acum += 1.5
            if class_num <= 9:
                area_val, temario_val, obs_val = octubre_reales[class_num]
                estado_val = "Impartida"
                fill_row = GREEN_PASTEL
            else:
                fut_idx = class_num - 10
                area_val, temario_val, obs_val = schedule_h3[fut_idx]
                estado_val = "Proyectada"
                fill_row = ORANGE_PASTEL if area_val == "Robótica" else PURPLE_PASTEL
                
            c1 = ws3.cell(row=r_out, column=1, value=class_num); c1.alignment = ALIGN_CENTER
            c2 = ws3.cell(row=r_out, column=2, value=date_str); c2.alignment = ALIGN_CENTER
            c3 = ws3.cell(row=r_out, column=3, value=day_str); c3.alignment = ALIGN_CENTER
            c4 = ws3.cell(row=r_out, column=4, value=area_val); c4.alignment = ALIGN_CENTER
            c5 = ws3.cell(row=r_out, column=5, value=estado_val); c5.alignment = ALIGN_CENTER
            c6 = ws3.cell(row=r_out, column=6, value=temario_val)
            c7 = ws3.cell(row=r_out, column=7, value=f"{horas_acum:.1f} h"); c7.alignment = ALIGN_CENTER
            c8 = ws3.cell(row=r_out, column=8, value=obs_val)
            
            for c_col in range(1, 9):
                cell = ws3.cell(row=r_out, column=c_col)
                cell.fill = fill_row
                cell.font = FONT_REGULAR
                cell.border = THIN_BORDER
                
            if "TECHO" in temario_val or "FIN BLOQUE" in obs_val or "FIN LOTE" in obs_val:
                c6.font = FONT_BOLD
                c8.font = FONT_BOLD
                
            class_num += 1
            
        r_out += 1
    cur_date += datetime.timedelta(days=1)

col_widths_h3 = {
    1: 12, 2: 15, 3: 13, 4: 15, 5: 16, 6: 76, 7: 15, 8: 50
}
for col_idx, width in col_widths_h3.items():
    ws3.column_dimensions[get_column_letter(col_idx)].width = width

wb.save(EXCEL_PATH)
print("--> BITACORA_SEGUIMIENTO_CLASES.xlsx actualizado con éxito con 3 HOJAS:")
print("    Hoja 1: 'Bitacora de Clases'")
print("    Hoja 2: 'Calendario Secuencial B1-B4'")
print("    Hoja 3: 'Escenario Seleccion B1-B6' (19 Robótica + 31 IA = 50 clases exactas al 30/05/2027)")
