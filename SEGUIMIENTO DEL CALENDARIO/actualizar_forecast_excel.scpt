set filePath to "/Users/externo/Library/Mobile Documents/com~apple~CloudDocs/PERSONAL/CLASES DE TECNOLOGÍA/CURSO-ROBOTICA-IA-COMUN/SEGUIMIENTO DEL CALENDARIO/BITACORA_SEGUIMIENTO_CLASES.xlsx"

tell application "Microsoft Excel"
    activate
    open workbook workbook file name filePath
    tell sheet "Bitacora de Clases" of active workbook
        -- Encabezado del bloque Forecast
        set value of range "I4" to "PREDICCIÓN Y PROYECCIÓN DEL CURSO (FORECAST)"
        set value of range "J4" to "VALOR"
        set value of range "K4" to "IMPACTO Y DIAGNÓSTICO"
        
        -- Valores de Predicción
        set value of range "I5" to "Fecha de Análisis"
        set value of range "J5" to "02/11/2026"
        set value of range "K5" to "A cierre de Octubre 2026"
        
        set value of range "I6" to "Total Sesiones Calendario (Est.)"
        set value of range "J6" to "60 clases"
        set value of range "K6" to "Horizonte oficial estimado Oct - Jun"
        
        set value of range "I7" to "Total Clases Transcurridas"
        set value of range "J7" to 9
        set value of range "K7" to "15.0% del calendario completado"
        
        set value of range "I8" to "Total Clases Restantes"
        set value of range "J8" to 51
        set value of range "K8" to "85.0% de margen lectivo"
        
        set value of range "I9" to "Velocidad Real IA (Burn Rate)"
        set value of range "J9" to "2.20 clases / sesión"
        set value of range "K9" to "Sesión 01 = 4 clases; Monog. 2 = 1 clase"
        
        set value of range "I10" to "Velocidad Real Robótica"
        set value of range "J10" to "1.50 clases / hito"
        set value of range "K10" to "1.5 clases por práctica/montaje"
        
        set value of range "I11" to "Clases Disponibles para IA (50%)"
        set value of range "J11" to "25.5 clases"
        set value of range "K11" to "Reparto equitativo del tiempo restante"
        
        set value of range "I12" to "Clases Disponibles para Robótica (50%)"
        set value of range "J12" to "25.5 clases"
        set value of range "K12" to "Reparto equitativo del tiempo restante"
        
        set value of range "I13" to "TECHO MÁXIMO IA ESTIMADO"
        set value of range "J13" to "Sesión 14 de 60"
        set value of range "K13" to "⚠️ Cobertura máxima del 23.3% del temario"
        
        set value of range "I14" to "TECHO MÁXIMO ROBÓTICA"
        set value of range "J14" to "Bloque 3 (de 8)"
        set value of range "K14" to "⚠️ Hasta Bloque 3 (Movimiento Avanzado)"
        
        set value of range "I15" to "Sesiones IA Inalcanzables (Gap)"
        set value of range "J15" to "46 sesiones fuera"
        set value of range "K15" to "Sesiones 15 a 60 no se impartirán a este ritmo"
        
        set value of range "I16" to "Diagnóstico Global de Ritmo"
        set value of range "J16" to "Ritmo de Consolidación"
        set value of range "K16" to "Los alumnos requieren afianzar conceptos prácticos"
        
        set value of range "I17" to "Recomendación Estratégica"
        set value of range "J17" to "Poda y Selección"
        set value of range "K17" to "Seleccionar 1 app/taller estrella por bloque"
        
        -- Formato
        set bold of font object of range "I4:K4" to true
        set bold of font object of range "I13:K14" to true
    end tell
    save active workbook
    close active workbook
end tell

