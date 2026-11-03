#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
generar_con_openpyxl.py
Regenera la bitácora oficial completa en formato nativo Excel (.xlsx)
con la tabla de sesiones y el panel de Predicción y Forecast.
Patrón idéntico al utilizado en 'fix_cistitis_excels_formatting.py'.
"""
import os
import sys

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
ws = wb.active
ws.title = "Bitacora de Clases"
ws.views.sheetView[0].showGridLines = True

# Paleta de estilos corporativa
NAVY_HEADER = PatternFill(start_color="1F497D", end_color="1F497D", fill_type="solid")
LIGHT_BLUE = PatternFill(start_color="DCE6F1", end_color="DCE6F1", fill_type="solid")

FONT_TITLE = Font(name="Calibri", size=14, bold=True, color="1F497D")
FONT_SUBTITLE = Font(name="Calibri", size=10, italic=True, color="595959")
FONT_HEADER = Font(name="Calibri", size=11, bold=True, color="FFFFFF")
FONT_BOLD = Font(name="Calibri", size=11, bold=True, color="000000")
FONT_REGULAR = Font(name="Calibri", size=11, color="000000")
FONT_ITALIC = Font(name="Calibri", size=10, italic=True, color="595959")
FONT_ALERT = Font(name="Calibri", size=11, bold=True, color="9C0006")

THIN_BORDER = Border(
    left=Side(style='thin', color='D9D9D9'),
    right=Side(style='thin', color='D9D9D9'),
    top=Side(style='thin', color='D9D9D9'),
    bottom=Side(style='thin', color='D9D9D9')
)

ALIGN_CENTER = Alignment(horizontal='center', vertical='center')
ALIGN_LEFT = Alignment(horizontal='left', vertical='center')

# Título y Subtítulo
ws["A1"] = "BITÁCORA Y SEGUIMIENTO DEL CALENDARIO DE CLASES"
ws["A1"].font = FONT_TITLE
ws["A2"] = "Horario: Martes y Jueves (1.5 horas/sesión) | Excluye festivos, Navidad y Semana Santa"
ws["A2"].font = FONT_SUBTITLE

# Resumen General (A4:B6)
ws["A4"] = "RESUMEN GENERAL"
ws["B4"] = "VALOR"
ws["A4"].font = FONT_HEADER; ws["A4"].fill = NAVY_HEADER; ws["A4"].alignment = ALIGN_LEFT
ws["B4"].font = FONT_HEADER; ws["B4"].fill = NAVY_HEADER; ws["B4"].alignment = ALIGN_CENTER

ws["A5"] = "Total Sesiones Transcurridas"
ws["B5"] = 9
ws["A5"].font = FONT_REGULAR; ws["A5"].border = THIN_BORDER
ws["B5"].font = FONT_BOLD; ws["B5"].border = THIN_BORDER; ws["B5"].alignment = ALIGN_CENTER

ws["A6"] = "Total Horas Lectivas (Octubre)"
ws["B6"] = 13.5
ws["A6"].font = FONT_REGULAR; ws["A6"].border = THIN_BORDER
ws["B6"].font = FONT_BOLD; ws["B6"].border = THIN_BORDER; ws["B6"].alignment = ALIGN_CENTER

# Panel de Predicción y Forecast (I4:K17)
forecast_data = [
    ("PREDICCIÓN Y PROYECCIÓN DEL CURSO (FORECAST)", "VALOR", "IMPACTO Y DIAGNÓSTICO", True),
    ("Fecha de Análisis", "02/11/2026", "A cierre de Octubre 2026", False),
    ("Total Sesiones Calendario (Est.)", "60 clases", "Horizonte oficial estimado Oct - Jun", False),
    ("Total Clases Transcurridas", "9 clases", "15.0% del calendario completado", False),
    ("Total Clases Restantes", "51 clases", "85.0% de margen lectivo", False),
    ("Velocidad Real IA (Burn Rate)", "2.20 clases / sesión", "Sesión 01 = 4 clases; Monog. 2 = 1 clase", False),
    ("Velocidad Real Robótica", "1.50 clases / hito", "1.5 clases por práctica/montaje", False),
    ("Clases Disponibles para IA (50%)", "25.5 clases", "Reparto equitativo del tiempo restante", False),
    ("Clases Disponibles para Robótica (50%)", "25.5 clases", "Reparto equitativo del tiempo restante", False),
    ("TECHO MÁXIMO IA ESTIMADO", "Sesión 14 de 60", "⚠️ Cobertura máxima del 23.3% del temario", False),
    ("TECHO MÁXIMO ROBÓTICA", "Bloque 3 (de 8)", "⚠️ Hasta Bloque 3 (Movimiento Avanzado)", False),
    ("Sesiones IA Inalcanzables (Gap)", "46 sesiones fuera", "Sesiones 15 a 60 no se impartirán a este ritmo", False),
    ("Diagnóstico Global de Ritmo", "Ritmo de Consolidación", "Los alumnos requieren afianzar conceptos prácticos", False),
    ("Recomendación Estratégica", "Poda y Selección", "Seleccionar 1 app/taller estrella por bloque", False)
]

for idx, (col_i, col_j, col_k, is_header) in enumerate(forecast_data, start=4):
    cell_i = ws.cell(row=idx, column=9, value=col_i)
    cell_j = ws.cell(row=idx, column=10, value=col_j)
    cell_k = ws.cell(row=idx, column=11, value=col_k)
    
    if is_header:
        cell_i.font = FONT_HEADER; cell_i.fill = NAVY_HEADER
        cell_j.font = FONT_HEADER; cell_j.fill = NAVY_HEADER; cell_j.alignment = ALIGN_CENTER
        cell_k.font = FONT_HEADER; cell_k.fill = NAVY_HEADER
    elif "TECHO MÁXIMO" in col_i:
        cell_i.font = FONT_ALERT; cell_i.fill = LIGHT_BLUE; cell_i.border = THIN_BORDER
        cell_j.font = FONT_ALERT; cell_j.fill = LIGHT_BLUE; cell_j.border = THIN_BORDER; cell_j.alignment = ALIGN_CENTER
        cell_k.font = FONT_ALERT; cell_k.fill = LIGHT_BLUE; cell_k.border = THIN_BORDER
    else:
        cell_i.font = FONT_REGULAR; cell_i.border = THIN_BORDER
        cell_j.font = FONT_BOLD; cell_j.border = THIN_BORDER; cell_j.alignment = ALIGN_CENTER
        cell_k.font = FONT_ITALIC; cell_k.border = THIN_BORDER

# Cabecera de la tabla de sesiones (A8:G8)
headers = ["Nº SESIÓN", "FECHA", "DÍA", "DURACIÓN (H)", "TEMARIO / CONTENIDO", "HORAS ACUM.", "OBSERVACIONES"]
for col_idx, h in enumerate(headers, start=1):
    c = ws.cell(row=8, column=col_idx, value=h)
    c.font = FONT_HEADER
    c.fill = NAVY_HEADER
    c.alignment = ALIGN_CENTER if col_idx in (1, 2, 3, 4, 6) else ALIGN_LEFT

# Datos de las 9 sesiones de Octubre (A9:G17)
sessions = [
    (1, "01/10/2026", "Jueves", 1.5, "Presentación inaugural", 1.5, "Primer día de clase"),
    (2, "06/10/2026", "Martes", 1.5, "Guía de Classroom y Gemini", 3.0, "Segunda clase"),
    (3, "08/10/2026", "Jueves", 1.5, "Sesión IA 01", 4.5, "Sesión IA 01 impartida"),
    (4, "13/10/2026", "Martes", 1.5, "Sesión IA 01", 6.0, "Sesión IA 01 impartida"),
    (5, "15/10/2026", "Jueves", 1.5, "Sesión IA 01", 7.5, "Sesión IA 01 impartida"),
    (6, "20/10/2026", "Martes", 1.5, "Sesión IA 01", 9.0, "Sesión IA 01 impartida"),
    (7, "22/10/2026", "Jueves", 1.5, "ROB1", 10.5, "Sesión registrada"),
    (8, "27/10/2026", "Martes", 1.5, "Monográfico 2 IA entero", 12.0, "Monográfico 2 IA impartido entero"),
    (9, "29/10/2026", "Jueves", 1.5, "ROB.1: 1.2 Lavadora + IA: Sesión 2 (Ítems 09 y 09B)", 13.5, "Impartidos ROB.1 (1.2 Lavadora) y Sesión 2 de IA (ítems 09 y 09B)")
]

for row_idx, s in enumerate(sessions, start=9):
    for col_idx, val in enumerate(s, start=1):
        c = ws.cell(row=row_idx, column=col_idx, value=val)
        c.font = FONT_REGULAR
        c.border = THIN_BORDER
        if col_idx in (1, 2, 3, 4, 6):
            c.alignment = ALIGN_CENTER

# Fórmulas acumulativas en F9:F17
for r in range(9, 18):
    ws.cell(row=r, column=6, value=f"=SUM($D$9:D{r})")

# Fórmulas de resumen
ws["B5"] = "=COUNTA(A9:A500)"
ws["B6"] = "=SUM(D9:D500)"

# Ajuste óptimo de anchos de columna
col_widths = {
    1: 13,  # A: Nº Sesión
    2: 15,  # B: Fecha
    3: 14,  # C: Día
    4: 16,  # D: Duración
    5: 46,  # E: Temario
    6: 16,  # F: Horas Acum.
    7: 50,  # G: Observaciones
    8: 4,   # H: Separador
    9: 36,  # I: Métrica Forecast
    10: 24, # J: Valor
    11: 48  # K: Impacto
}

for col_idx, width in col_widths.items():
    col_letter = get_column_letter(col_idx)
    ws.column_dimensions[col_letter].width = width

wb.save(EXCEL_PATH)
print("--> BITACORA_SEGUIMIENTO_CLASES.xlsx generado con éxito en formato 100% nativo de Microsoft Excel.")
