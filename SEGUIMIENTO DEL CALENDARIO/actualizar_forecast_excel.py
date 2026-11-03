#!/usr/bin/env python3
import zipfile, os, shutil, re
from xml.etree import ElementTree as ET

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
EXCEL_PATH = os.path.join(BASE_DIR, "BITACORA_SEGUIMIENTO_CLASES.xlsx")
TEMP_OUT = os.path.join(BASE_DIR, "BITACORA_SEGUIMIENTO_CLASES.tmp.xlsx")

# Pristine base if available in /tmp, otherwise use current file
pristine_tmp = "/tmp/test_bitacora.xlsx"
source_path = pristine_tmp if os.path.exists(pristine_tmp) else EXCEL_PATH

with zipfile.ZipFile(source_path, 'r') as z:
    all_files = {name: z.read(name) for name in z.namelist()}

sst_root = ET.fromstring(all_files['xl/sharedStrings.xml'])
sheet_root = ET.fromstring(all_files['xl/worksheets/sheet1.xml'])
content_types = ET.fromstring(all_files['[Content_Types].xml'])
wb_rels = ET.fromstring(all_files['xl/_rels/workbook.xml.rels'])

ns = '{http://schemas.openxmlformats.org/spreadsheetml/2006/main}'

def get_string_id(text):
    for i, si in enumerate(sst_root.findall(f'{ns}si')):
        t = ''.join([n.text for n in si.iter(f'{ns}t') if n.text])
        if t == text:
            return i
    si = ET.SubElement(sst_root, f'{ns}si')
    t = ET.SubElement(si, f'{ns}t')
    t.text = text
    return len(sst_root) - 1

# Dimension
dim = sheet_root.find(f'{ns}dimension')
if dim is not None:
    dim.attrib['ref'] = 'A1:K17'

# Column widths
cols = sheet_root.find(f'{ns}cols')
if cols is not None:
    existing_cols = {int(c.attrib.get('min', 0)): c for c in cols.findall(f'{ns}col')}
    for col_min, col_max, width in [(8, 8, 4), (9, 9, 32), (10, 10, 22), (11, 11, 42)]:
        if col_min not in existing_cols:
            c = ET.SubElement(cols, f'{ns}col')
            c.attrib['min'] = str(col_min)
            c.attrib['max'] = str(col_max)
            c.attrib['width'] = str(width)
            c.attrib['customWidth'] = '1'

sheet_data = sheet_root.find(f'{ns}sheetData')

# Fix corrupted formulas if present
for f_tag in sheet_data.findall(f'.//{ns}f'):
    if f_tag.text == 'SUM(:D16)':
        f_tag.text = 'SUM($D$9:D16)'
    elif f_tag.text == 'SUM(:D17)':
        f_tag.text = 'SUM($D$9:D17)'

existing_rows = {int(r.attrib['r']): r for r in sheet_data.findall(f'{ns}row')}

forecast_rows = {
    4: [('I', 'PREDICCIÓN Y PROYECCIÓN DEL CURSO (FORECAST)', '2'), ('J', 'VALOR', '2'), ('K', 'IMPACTO Y DIAGNÓSTICO', '2')],
    5: [('I', 'Fecha de Análisis', '3'), ('J', '02/11/2026', '3'), ('K', 'A cierre de Octubre 2026', '5')],
    6: [('I', 'Total Sesiones Calendario (Est.)', '3'), ('J', '60 clases', '3'), ('K', 'Horizonte oficial estimado Oct - Jun', '5')],
    7: [('I', 'Total Clases Transcurridas', '3'), ('J', '9 clases', '3'), ('K', '15.0% del calendario completado', '5')],
    8: [('I', 'Total Clases Restantes', '4'), ('J', '51 clases', '4'), ('K', '85.0% de margen lectivo', '4')],
    9: [('I', 'Velocidad Real IA (Burn Rate)', '3'), ('J', '2.20 clases / sesión', '3'), ('K', 'Sesión 01 = 4 clases; Monog. 2 = 1 clase', '5')],
    10: [('I', 'Velocidad Real Robótica', '3'), ('J', '1.50 clases / hito', '3'), ('K', '1.5 clases por práctica/montaje', '5')],
    11: [('I', 'Clases Disponibles para IA (50%)', '3'), ('J', '25.5 clases', '3'), ('K', 'Reparto equitativo del tiempo restante', '5')],
    12: [('I', 'Clases Disponibles para Robótica (50%)', '3'), ('J', '25.5 clases', '3'), ('K', 'Reparto equitativo del tiempo restante', '5')],
    13: [('I', 'TECHO MÁXIMO IA ESTIMADO', '2'), ('J', 'Sesión 14 de 60', '2'), ('K', '⚠️ Cobertura máxima del 23.3% del temario', '2')],
    14: [('I', 'TECHO MÁXIMO ROBÓTICA', '2'), ('J', 'Bloque 3 (de 8)', '2'), ('K', '⚠️ Hasta Bloque 3 (Movimiento Avanzado)', '2')],
    15: [('I', 'Sesiones IA Inalcanzables (Gap)', '3'), ('J', '46 sesiones fuera', '3'), ('K', 'Sesiones 15 a 60 no se impartirán a este ritmo', '5')],
    16: [('I', 'Diagnóstico Global de Ritmo', '3'), ('J', 'Ritmo de Consolidación', '3'), ('K', 'Los alumnos requieren afianzar conceptos prácticos', '5')],
    17: [('I', 'Recomendación Estratégica', '4'), ('J', 'Poda y Selección', '4'), ('K', 'Seleccionar 1 app/taller estrella por bloque', '4')]
}

for r_idx, items in forecast_rows.items():
    if r_idx in existing_rows:
        r_elem = existing_rows[r_idx]
    else:
        r_elem = ET.Element(f'{ns}row')
        r_elem.attrib['r'] = str(r_idx)
        r_elem.attrib['ht'] = '15'
        sheet_data.append(r_elem)
        existing_rows[r_idx] = r_elem
        
    for col_l, text, style_id in items:
        cell_ref = f'{col_l}{r_idx}'
        c_found = None
        for c_existing in r_elem.findall(f'{ns}c'):
            if c_existing.attrib.get('r') == cell_ref:
                c_found = c_existing
                break
        if c_found is None:
            c_found = ET.SubElement(r_elem, f'{ns}c')
            c_found.attrib['r'] = cell_ref
        c_found.attrib['s'] = style_id
        c_found.attrib['t'] = 's'
        v = c_found.find(f'{ns}v')
        if v is None:
            v = ET.SubElement(c_found, f'{ns}v')
        s_idx = get_string_id(text)
        v.text = str(s_idx)

# Set spans
for r_elem in sheet_data.findall(f'{ns}row'):
    cells = r_elem.findall(f'{ns}c')
    if any(c.attrib.get('r', '').startswith(('I', 'J', 'K')) for c in cells):
        r_elem.attrib['spans'] = '1:11'

# Sort cells in row
for r_elem in sheet_data.findall(f'{ns}row'):
    def cell_sort_key(c):
        ref = c.attrib.get('r', 'A1')
        col_part = ''.join([ch for ch in ref if ch.isalpha()])
        row_part = int(''.join([ch for ch in ref if ch.isdigit()]) or 0)
        col_num = 0
        for ch in col_part:
            col_num = col_num * 26 + (ord(ch.upper()) - ord('A') + 1)
        return (row_part, col_num)
    r_elem[:] = sorted(r_elem, key=cell_sort_key)

sheet_data[:] = sorted(sheet_data, key=lambda r: int(r.attrib['r']))

# String count
total_string_refs = len(sheet_root.findall(f'.//{ns}c[@t=\"s\"]'))
sst_root.attrib['count'] = str(total_string_refs)
sst_root.attrib['uniqueCount'] = str(len(sst_root.findall(f'{ns}si')))

# Remove calcChain
for override in list(content_types):
    if override.attrib.get('PartName') == '/xl/calcChain.xml':
        content_types.remove(override)

for rel in list(wb_rels):
    if 'calcChain' in rel.attrib.get('Target', ''):
        wb_rels.remove(rel)

def clean_xml_str(elem):
    raw = ET.tostring(elem, encoding='utf-8', xml_declaration=True).decode('utf-8')
    # Strip ns0 prefixes
    cleaned = raw.replace('<ns0:', '<').replace('</ns0:', '</').replace('xmlns:ns0=', 'xmlns=')
    # Strip undeclared markup-compatibility prefixes that make Excel discard the sheet
    cleaned = re.sub(r'xmlns:ns\d+=\"[^\"]*\"\s*', '', cleaned)
    cleaned = re.sub(r'ns\d+:[a-zA-Z0-9_]+=\"[^\"]*\"\s*', '', cleaned)
    return cleaned

s1_clean = clean_xml_str(sheet_root)

# Clean workbook.xml
wb = all_files['xl/workbook.xml'].decode('utf-8')
wb_clean = re.sub(r'<fileRecoveryPr[^>]*/>', '', wb)
wb_clean = re.sub(r'<xr:revisionPtr[^>]*/>', '', wb_clean)
wb_clean = re.sub(r'xr\d*:[a-zA-Z0-9_]+=\"[^\"]*\"\s*', '', wb_clean)
wb_clean = re.sub(r'<mc:AlternateContent>.*?</mc:AlternateContent>', '', wb_clean, flags=re.DOTALL)

with zipfile.ZipFile(TEMP_OUT, 'w', compression=zipfile.ZIP_DEFLATED) as zout:
    for name, data in all_files.items():
        if name == 'xl/calcChain.xml':
            continue
        elif name == '[Content_Types].xml':
            zout.writestr(name, clean_xml_str(content_types).encode('utf-8'))
        elif name == 'xl/_rels/workbook.xml.rels':
            zout.writestr(name, clean_xml_str(wb_rels).encode('utf-8'))
        elif name == 'xl/sharedStrings.xml':
            zout.writestr(name, clean_xml_str(sst_root).encode('utf-8'))
        elif name == 'xl/worksheets/sheet1.xml':
            zout.writestr(name, s1_clean.encode('utf-8'))
        elif name == 'xl/workbook.xml':
            zout.writestr(name, wb_clean.encode('utf-8'))
        else:
            zout.writestr(name, data)

shutil.move(TEMP_OUT, EXCEL_PATH)
print("Excel reconstruido y normalizado con éxito sin extensiones propietarias conflictivas.")
