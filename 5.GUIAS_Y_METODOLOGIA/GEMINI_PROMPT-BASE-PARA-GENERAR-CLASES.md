# ⏱ ACTUALIZADO: 2026-06-03

# GEMINI_PROMPT-BASE-PARA-GENERAR-CLASES.md — Curso Robótica v2

Plantilla de referencia para generar una clase completa.
Leer también GEMINI_CONOCIMIENTO-GEMINI.md antes de empezar.

---

## FLUJO DE CREACIÓN POR CLASE — EN CASCADA Y ACUMULATIVO

El flujo es estrictamente secuencial y acumulativo. Los prompts para Gemini en AI Studio (ficheros 4 y 5) se generan **ÚNICAMENTE** después de haber depurado físicamente el HTML de la fase anterior en AI Studio e incorporado las mejoras reales obtenidas. Nunca se generan al principio.

> [!IMPORTANT]
> **REGLA DE AISLAMIENTO DE CHATS**: Cada clase nueva requiere abrir un chat limpio desde cero en el entorno de la IA. Antigravity tiene la obligación activa de vigilar esta transición: si el usuario comienza a hablar, planificar o solicitar tareas de una clase diferente, Antigravity debe recordarle de inmediato que inicie un chat nuevo y detener cualquier generación hasta que se haga el cambio.

```
INICIO DE CLASE NUEVA
│
├─ PASO 1 — Antigravity genera inicialmente (sin esperar nada):
│     · T0.DEBATE.pdf
│     · 1.Teoria_para_NLM.txt
│     · 2.Ejemplo_real_para_NLM.txt
│     · 3.Prompt_P1.txt
│     · 6.Fuente-y-Prompt-Nanobana.txt
│     · P4.JUEGO.html
│
├─ PASO 2 — El profesor depura P1.CONSTRUCCION con Gemini en AI Studio
│     → Entrega las mejoras y correcciones encontradas a Antigravity
│     → Antigravity actualiza GEMINI_CONOCIMIENTO-GEMINI.md con las nuevas reglas
│     → Antigravity genera 4.Prompt_P2.txt (incorporando lo aprendido en P1)
│
├─ PASO 3 — El profesor depura P2.EJEMPLO-REAL con Gemini en AI Studio
│     → Entrega las mejoras y correcciones encontradas a Antigravity
│     → Antigravity actualiza GEMINI_CONOCIMIENTO-GEMINI.md con las nuevas reglas
│     → Antigravity genera 5.Prompt_P3.txt (incorporando lo aprendido en P1 y P2)
│
└─ PASO 4 — El profesor depura P3.BLOQUES con Gemini en AI Studio
      → Entrega las mejoras finales
      → Antigravity actualiza GEMINI_CONOCIMIENTO-GEMINI.md
      → Listo para la siguiente clase
```

**Por qué este orden:**
- Los ficheros 4 y 5 se generan **una sola vez** y ya son mejores porque incorporan depuraciones reales.
- El conocimiento en `GEMINI_CONOCIMIENTO-GEMINI.md` crece de forma acumulativa clase a clase.
- Evitamos generar prompts en frío que luego habría que reescribir.

---

## CHECKLIST ANTES DE GENERAR (PASO 1)

1. Leer el enunciado de la clase en GEMINI_INDICE-DEL-CURSO.md.
2. Leer GEMINI_CONOCIMIENTO-GEMINI.md — bugs y reglas acumuladas hasta hoy.
3. Consultar skills disponibles: `SKILL-humanoid-babylon.md`, `SKILL-coche-elegoo-babylon.md`, `SKILL-brazo-robotico-base.md`, `SKILL-brazo-robotico-hombro.md`.
4. Verificar que ninguna simulación repite mecánica de clases anteriores.
5. Confirmar que el bloque NUEVO de esta clase está marcado visualmente.
6. Confirmar que las preguntas de debate sean particulares sobre la física/lógica del robot de la clase (no genéricas) y que sean de opinión, sin respuesta correcta.
7. Test: ¿aparece el robot o alguna de sus piezas/componentes (como robot, brazo, pinza, ruedas, etc.) en el fichero 1.Teoria? Si SÍ ➔ reescribir.

---

## FICHEROS POR PASO

| Paso | Fichero | Quién genera | Cuándo |
|---|---|---|---|
| 1 | `T0.DEBATE.pdf` | Antigravity | Al inicio de la clase |
| 1 | `1.Teoria_para_NLM.txt` | Antigravity | Al inicio de la clase |
| 1 | `2.Ejemplo_real_para_NLM.txt` | Antigravity | Al inicio de la clase |
| 1 | `3.Prompt_P1.txt` | Antigravity | Al inicio de la clase |
| 1 | `6.Fuente-y-Prompt-Nanobana.txt` | Antigravity | Al inicio de la clase |
| 1 | `P4.JUEGO.html` | Antigravity | Al inicio de la clase |
| 2 | `4.Prompt_P2.txt` | Antigravity | Tras depurar P1 con Gemini |
| 3 | `5.Prompt_P3.txt` | Antigravity | Tras depurar P2 con Gemini |

---

## T0.DEBATE.pdf

Antigravity genera este PDF directamente.

**Estilo:** cabecera `#1F4E79` blanco, cada pregunta en bloque numerado, detonadores en gris más pequeño.

**Estructura de cada pregunta:**
```
PREGUNTA 1
[Pregunta de opinión polémica — sin respuesta correcta]

Si nadie responde:
• [Detonador 1]
• [Detonador 2]
```

3 preguntas por clase. Regla de Oro (Bloque 4 - Brazo robótico): las preguntas deben comparar la articulación robótica de la clase con su equivalente en el cuerpo humano (Clase 4.1: base vs. tronco humano; Clase 4.2: hombro vs. hombro humano; Clase 4.3: codo; Clase 4.4: muñeca; etc.). Deben analizarse explícitamente los ángulos y límites máximos de movimiento del humano frente al robot y las diferencias entre articulaciones biológicas y mecánicas.

**Guía Didáctica para el Profesor (Obligatoria al final del PDF):**
Al final del PDF de debate, se debe incorporar obligatoriamente una sección de apoyo docente que contenga para cada pregunta:
1. **Enfoque conceptual**: Qué concepto o principio físico/lógico se busca reflexionar.
2. **Realidad en nuestro robot (aula)**: Explicación de los límites, carencias y comportamiento real de nuestra maqueta de clase (ej. carece de sensores de corriente o torque, el movimiento es de bisagra simple, los topes se definen por software, etc.).
3. **Solución industrial real**: Cómo solucionan este reto los robots profesionales en la industria actual.
4. **Cierre sugerido**: Una respuesta/reflexión concisa y clara que el profesor puede utilizar para resumir y concluir el tema ante los alumnos.

---

## 1.Teoria_para_NLM.txt

Concepto abstracto de la clase mediante metáforas cotidianas. NLM lo convierte en diapositivas pptx.

> [!IMPORTANT]
> **SUPER-REGLA DE ORO PEDAGÓGICA:** Este fichero habla **SOLO** de funcionamientos que una persona puede ver en la vida real que le rodea (ej. coger un vaso de agua con las manos y los ojos cerrados). 
> **ESTÁ TOTALMENTE PROHIBIDO** hacer mención a tecnicismos o jerga robótica (servomotor, actuador, efector terminal, sensor, lazo cerrado, etc.) ni a piezas del robot. Todo el vocabulario técnico queda reservado para el Fichero 2.

**Estructura:**
```
CLASE X.X — [Título del concepto]
CAPÍTULO X — [Nombre del bloque]

[SECCIÓN 1 — título]
[3-5 líneas. Lenguaje accesible 65-70 años. Sin tecnicismos.]

[SECCIÓN 2 — título]
[...]
```

Temas habituales: qué es el concepto, por qué es útil, analogía cotidiana, cómo lo usa una máquina, por qué es mejor que hacerlo a mano.

---

## 2.Ejemplo_real_para_NLM.txt

El robot concreto de la clase aplicando el concepto. NLM lo usa para enriquecer las diapositivas.

> [!IMPORTANT]
> **SUPER-REGLA DE ORO PEDAGÓGICA:** Aquí es donde se "traduce" la metáfora de la vida real (Fichero 1) al lenguaje técnico y robótico. Se debe usar toda la jerga industrial pertinente (actuación, servomotor, percepción, lazo cerrado, sensor de proximidad), pero limitándose **estrictamente** a la tecnología real implementada en la simulación 3D de esta clase (si la clase es solo un sensor infrarrojo, no hables de ventosas ni sensores de color).

**Estructura:**
```
[TÍTULO — el robot y su entorno]

[2-3 párrafos. El robot en una situación cotidiana reconocible para mayores de 65 años.]

QUÉ SE DEBE ANALIZAR:
• [Mínimo 4 puntos de observación concretos]

RESULTADO ESPERADO:
[Qué debe entender el alumno al terminar. 1-2 frases.]
```

---

## 3.Prompt_P1.txt

Prompt completo para que Gemini genere P1.CONSTRUCCION.
Consultar `SKILL-coche-elegoo-babylon.md` o el skill del robot de la clase (como `SKILL-brazo-robotico-base.md` y `SKILL-brazo-robotico-hombro.md`) antes de escribirlo.

**Estructura del prompt (Enfoque de Esqueleto HTML/CSS - OBLIGATORIO):**
Para evitar que Gemini entregue archivos incompletos o sin estilos en las siguientes iteraciones, el prompt debe consistir en un archivo HTML casi completo, donde todo el HTML y el CSS estén ya escritos con diseño de alta calidad (Outfit font, glassmorphism, responsive) y se le pida a Gemini únicamente rellenar la lógica del bloque `<script>`.

```markdown
Tienes el siguiente fichero HTML casi completo. Le falta únicamente el contenido del bloque <script>.
Tu única tarea es escribir el JavaScript que va entre las etiquetas <script> y </script>.

NO reescribas el HTML. NO reescribas el CSS. NO añadas texto fuera del bloque de código.
Devuelve el fichero COMPLETO (del <!DOCTYPE> al </html>) con el JavaScript ya relleno.

[REGLA CRÍTICA CONTRA LA SEGMENTACIÓN DEL CÓDIGO]:
- TODO EL ARCHIVO HTML DEBE IR DENTRO DE UN ÚNICO BLOQUE DE CÓDIGO ```html ... ```.
- ESTÁ ABSOLUTAMENTE PROHIBIDO CERRAR EL BLOQUE Y VOLVERLO A ABRIR en la mitad del documento (por ejemplo, al terminar la etiqueta </style> o al abrir la etiqueta <script>). No escribas las palabras "code", "Code" ni utilices triples comillas inversas secundarias. El bloque ```html inicial abierto en tu respuesta solo debe cerrarse al final del archivo tras la etiqueta </html>.

`html
[Comentario de mejoras técnico]
<!DOCTYPE html>
...
<style>
[Todos los estilos CSS de la interfaz y canvas ya escritos]
</style>
...
<body>
[Toda la estructura HTML con los divs, panel, lista de piezas, canvas y banners]
</body>
<script>
// ==========================================
// ESCRIBE AQUÍ EL JAVASCRIPT COMPLETO
// ==========================================
//
// Instrucciones detalladas de:
// 1. Inicialización de escena (WebGPU fallback WebGL, niebla exp2, cámara orbital, luces, sombras, etc.).
// 2. Definición de materiales PBR (naranja, negro, metal, holo).
// 3. Creación de la jerarquía de mallas estáticas sólidas del robot y los indicadores holográficos.
// 4. Lógica de Drag & Drop para acoplar las piezas en orden.
// 5. Animación de las piezas y bucle de simulación.
// 6. Demostración interactiva y confeti al completar.
// 7. Función de reinicio de la escena.
//
// IMPORTANTE: Evita autoparentesco (ej. domeBase.parent = domeBase) para que la pantalla no quede negra.
</script>
</html>
`
```

---

## 4.Prompt_P2.txt

Prompt completo para que Gemini genere P2.EJEMPLO-REAL.
**Generar SOLO después de depurar P1 con Gemini y actualizar GEMINI_CONOCIMIENTO-GEMINI.md.**
Consultar `SKILL-coche-elegoo-babylon.md` (VARIANTE B — opaco) si el robot es el coche ELEGOO.

**Estructura del prompt:**
```
Crea una simulación interactiva de [ROBOT] en un único fichero HTML.

Pon en el HTML la etiqueta <title>P2.EJEMPLO-REAL</title>
Escribe al inicio del HTML, antes del DOCTYPE, un comentario con las decisiones técnicas.

HEADER OBLIGATORIO: [valores exactos del CONOCIMIENTO-GEMINI]

CONCEPTO DIDÁCTICO: [qué debe ver y entender el alumno — 2-3 líneas]

COCHE/ROBOT — usar VARIANTE B (opaco): alpha=1.0, PBRMATERIAL_OPAQUE.
[O pegar skill completo del robot si no es el coche ELEGOO]

ESCENA: [descripción visual — circuito doble carril, eventos separados ≥8u, etc.]

PANEL DE CONTROL — glass-ui: [qué datos muestra, qué sliders, qué botones]

LÓGICA: [máquina de estados explícita con nombres de estados]

[Reglas técnicas de GEMINI_CONOCIMIENTO-GEMINI.md § P2.EJEMPLO-REAL]

> [!CAUTION]
> **SUPER-REGLA DE ORO DE MATEMÁTICAS 3D Y SLIDERS (Para Brazo Robótico):**
> 1. Para que el brazo se mueva correctamente en el plano 2D de la pantalla, el cálculo en `setupRenderLoop` debe usar SIEMPRE `(90 - angulo)` en lugar de `(angulo - 90)`. Ejemplo correcto: `shoulderNode.rotation.x = (90 - currentAngles.shoulder) * Math.PI / 180;`.
> 2. Los rangos nativos de los sliders deben ser coherentes para llegar a las posturas extremas sin usar trucos de CSS como `dir="rtl"` o inversiones en JS. Ejemplo: Hombro min="0" max="180", Codo min="-90" max="180", Muñeca Pitch min="-135" max="90".

ENTREGA: único HTML, comentario antes del DOCTYPE, PROHIBIDO texto fuera del bloque ```html```,
PROHIBIDO "code" suelto, </html> una sola vez, sin botón de descarga.
```

---

## 5.Prompt_P3.txt

Prompt completo para que Gemini genere P3.BLOQUES.
**Generar SOLO después de depurar P2 con Gemini y actualizar GEMINI_CONOCIMIENTO-GEMINI.md.**

**Estructura del prompt:**
```
Crea una simulación de programación por bloques de [ROBOT] en un único fichero HTML.

Pon en el HTML la etiqueta <title>P3.BLOQUES</title>
Escribe al inicio del HTML, antes del DOCTYPE, un comentario con las decisiones técnicas.

HEADER OBLIGATORIO: [valores exactos del CONOCIMIENTO-GEMINI]

> [!CAUTION]
> **SUPER-REGLA DE ORO DE MATEMÁTICAS 3D Y SLIDERS:**
> Aplica LA MISMA regla de `(90 - angulo)` en el Render Loop y los MISMOS rangos de sliders (`min` y `max`) que utilizaste en el archivo P2.EJEMPLO-REAL, para asegurar consistencia absoluta entre ambas simulaciones.

LAYOUT: panel izquierdo 40% (paleta + programa + botones) | canvas derecho 60%.
[CSS obligatorio: palette height fija + flex-shrink:0. program-zone flex:1 + min-height:0.]
[updateOrtho() llamar al inicio Y en resize — sin esto la escena aparece recortada.]

BLOQUES DISPONIBLES — paleta HORIZONTAL (flex-direction:row, overflow-x:auto):
  [Bloques acumulados de clases anteriores — color gris #4a4a5a]
  Bloque NUEVO: [NOMBRE] (fondo [color], borde izq 4px #00f2ff, etiqueta "NUEVO" rojo)
    [Descripción exacta de qué hace, qué devuelve, cómo se usa en un SI]

MISIONES — 5 progresivas:
  M1 — programa pre-cargado completo, alumno solo pulsa EJECUTAR
  M2 — rellenar 1 hueco, pista visible, VER SOLUCIÓN disponible
  M3 — construir una rama, VER SOLUCIÓN disponible
  M4 — combinar los 3 eventos, sin pista, VER SOLUCIÓN disponible
  M5 — reto libre, sin pistas, sin VER SOLUCIÓN

MOTOR: async/await. animObservers[] cancelables. NUNCA location.reload().
Modal éxito: HTML custom, retardo 2s, botones ≥70px.

[Reglas técnicas de GEMINI_CONOCIMIENTO-GEMINI.md § P3.BLOQUES]

ENTREGA: único HTML, comentario antes del DOCTYPE, PROHIBIDO texto fuera del bloque ```html```,
PROHIBIDO "code" suelto, </html> una sola vez, sin botón de descarga.
```

---

## 6.Fuente-y-Prompt-Nanobana.txt

Fichero auxiliar para generar la infografía de la clase utilizando la herramienta Nano Banana Pro (Gemini Advanced / Imagen 3). Contiene:
1. **Fuente (Data)**: Los textos teóricos consolidados de la clase en español (título, conceptos clave, analogías cotidianas, y detalles del estado de visualización del robot).
2. **Prompt**: Instrucción detallada en inglés que guía a la IA de diseño a estructurar visualmente la infografía (16:9, dos columnas para comparación, bloque de analogías, tabla comparativa, esquema de colores y luces realistas especulares, y la regla estricta de que todos los textos renderizados estén en español).

---

## P4.JUEGO.html

Antigravity genera este fichero directamente — no pasa por Gemini.

- Mínimo 4 minijuegos con mecánicas distintas.
- Mecánicas disponibles: trivial, ordenar arrastrando, emparejar, escenarios de decisión, ruleta canvas, barra animada.
- Botón REINICIAR visible siempre en cada minijuego.
- Botón SIGUIENTE explícito tras cada pregunta — NUNCA avance automático.
- Pantalla de fin: trofeo + puntuación + botón JUGAR OTRA VEZ.
- Navegación libre entre minijuegos desde la barra de progreso.
- Distribución `ok` en trivial: posiciones 0,1,2,3 equilibradas — nunca >2 consecutivas iguales.
- Solo conceptos, comportamiento y utilidad del robot — sin electrónica ni código.
