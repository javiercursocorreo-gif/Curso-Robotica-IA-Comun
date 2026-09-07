# 🏆 GUÍA MAESTRA DE INFOGRAFÍAS Y PROMPTS DE IA PARA EL CURSO DE ROBÓTICA
**Fichero:** `GEMINI/PROMPTS_MODELOS_E_INFOGRAFIAS.md`  
**Alcance:** Genérico para todas las clases del curso (Coches Elegoo, Brazos Robóticos, Drones, Sensores, Manos Hidráulicas, etc.)  
**Motores de IA Aplicables:** Nano Banana Pro / Gemini Advanced / Imagen 3 / Midjourney v6 / DALL-E 3  

---

## 🎨 1. LA FILOSOFÍA "PURA DIRECCIÓN DE ARTE" Y EL ESTÁNDAR AEROESPACIAL

Para conseguir imágenes de calidad de **museo de ciencias de clase mundial o publicación científica 4K**, sustituimos los prompts confusos por estructuras visuales precisas orientadas al renderizado 3D industrial:

### 🌟 El Estándar Panorámico 16:9 (Keyshot / Unreal Engine 5)
1. **Ocupación y Respiración:** El objeto central debe ocupar exactamente el **55-65% del frame**, inclinando la perspectiva isométrica en 3/4 para revelar volumen y profundidad.
2. **Materiales Fotorrealistas:** Definir con rigor las texturas: polímero ABS mate, metal anodizado, vidrio, caucho o fibra de carbono.
3. **Simplicidad y Limpieza Visual (Especial para todas las edades):**
   * En todas las diapositivas (5B, 6, 7 y 8) se debe mantener una estética 100% 3D panorámica limpia, sin sobrecarga de textos, sin esquemas abstractos 2D y sin leyendas complejas.
   * *Nota importante:* En los Ficheros 6 (Biológica/Física) y 7 (Anatomía Hardware) NO se deben incluir leyendas de colores complejas ni dividir artificialmente la pantalla, preservando un render 3D inmersivo, elegante y fácil de entender.
4. **Formulación 100% Positiva del Idioma (Regla 5.2):** Prohibido usar frases negativas como "prohibido inglés" o "cero inglés", ya que hacen que el modelo genere textos en inglés por atención al token. Todos los prompts deben empezar siempre con la afirmación positiva rotunda:
   `IDIOMA Y TEXTOS DE LA IMAGEN: ESPAÑOL (CASTELLANO). TODAS LAS PALABRAS, TÍTULOS Y LEYENDAS ESCRITAS EN LA IMAGEN DEBEN ESTAR EXCLUSIVAMENTE EN ESPAÑOL. NO SE PERMITEN PALABRAS EN INGLÉS NI ABREVIATURAS DE CANTIDAD.`
5. **Rótulo Superior de Título Obligatorio en Todas las Slides:** Para evitar que el generador invente títulos en inglés o los omita, TODAS las diapositivas (5B, 6, 7 y 8) deben incluir explícitamente en su lista de textos el Rótulo Superior de Título Principal en español.

### ⚠️ REGLA DE ORO CONTRA ALUCINACIONES DE TEXTO Y "CANT:" (ELIMINAR ABREVIATURAS DE CANTIDAD)
**¡NUNCA pongas en el prompt final variables ni la expresión "Cant:" o "(Cant: X)" dentro del texto de las etiquetas!**
Si incluyes "Cant:" o "(Cant: X)" en las comillas, los motores de difusión imprimirán literalmente la palabra "Cant:" en el lienzo, ensuciando el gráfico. **Cuando vayas a generar la imagen, pon exclusivamente el nombre técnico limpio en español**, por ejemplo:
* `— Falanges Óseas`
* `— Tendones Extensores`

---

## 🛠️ 2. PLANTILLAS MAESTRAS UNIVERSALES REUTILIZABLES (`[OBJETO]`)

### 👑 PLANTILLA GOLD STANDARD: Infografía Isométrica Panorámica 16:9 (Grado Aeroespacial)
*Esta es la plantilla por excelencia para generar presentaciones e ilustraciones principales de cualquier clase del curso:*

C# 🎨 GUÍA MAESTRA DE PROMPTS E INFOGRAFÍAS CAD 8K (GOLD STANDARD V8)
**Objetivo:** Establecer la metodología oficial, innegociable y estandarizada para la generación de infografías y material visual en todas las clases del curso de robótica.

---

## ⚖️ REGLA DE ORO DE REDACCIÓN AUTOMÁTICA (ANTIGRAVITY)
1. **En todas las clases NUEVAS:** El asistente IA (Antigravity) redactará y entregará automáticamente los **Ficheros 6, 7 y 8** terminados en la carpeta `1.FICHEROS-AUXILIARES`. El profesor NUNCA rellenará plantillas ni corchetes a mano.
2. **En las clases ANTIGUAS:** Se irán revisando progresivamente para actualizar o crear sus Ficheros 6, 7 y 8 bajo este nuevo estándar blindado.

---

## 🏆 LA TRILOGÍA OFICIAL DE INFOGRAFÍAS PARA CADA CLASE
Toda lección del curso se apoyará visualmente en exactamente **3 infografías panorámicas 16:9** diseñadas para cubrir el ciclo pedagógico completo (*Naturaleza ➡️ Hardware ➡️ Funciones*):

### 🟢 1. Fichero 6: Slide 3D de Principio Físico o Biológico
* **Propósito:** Mostrar visualmente en 3D el referente biológico natural o el principio físico puro que inspira la ingeniería del robot (ej. una mano humana en 3D estilizada, un sistema de poleas o palancas en 3D).
* **Técnica:** Ilustración digital 3D limpia y espaciosa estilo museo de ciencias moderno, sin sobrecarga científica ni diagramas complejos 2D.

### 🔵 2. Fichero 7: Slide 3D de Anatomía Interna y Hardware del Robot
* **Propósito:** Mostrar el robot visto por dentro en corte anatómico longitudinal (*Cutaway View* / *Exploded View*), revelando servomotores, chasis de aleación, sensores incrustados y placas electrónicas.
* **Técnica:** Ilustración digital 3D estilo manual técnico de ingeniería CAD con 4 o 5 flechas cian señalando componentes con precisión milimétrica.

### 🟡 3. Fichero 8: Slide 3D Funcional / Operativa en Acción
* **Propósito:** Mostrar al robot en su entorno operativo real realizando su función principal (*Engineering Action View*), ilustrando intuitivamente su acción motriz y detección sensorial.
* **Técnica:** Render 3D inmersivo y dinámico en 16:9 con sutiles haces de luz o efectos visuales y 3 o 4 etiquetas directas en español. Prohibido incluir tablas, leyendas complejas o esquemas abstractos.

### 🌟 4. Fichero 5b: Slide de Transición y Portada de Trilogía (`5b.Prompt_Slide_Resumen_Trilogia.txt`)
* **Propósito:** Actuar como diapositiva de portada (Hero Shot) y bienvenida visual justo al iniciar la lección en las presentaciones de teoría (PowerPoint / Keynote), introduciendo con una estética 3D elegante y limpia los tres pilares de estudio: **La Trilogía de la Ingeniería** (1. Principio Físico/Biológico, 2. Anatomía Mecánica, 3. Ciclo Operativo).
* **Técnica:** Ilustración digital 3D 16:9 estilo presentación ejecutiva (estilo Apple / Keynote) con 3 pedestales o paneles holográficos claros y espaciosos que representan los 3 pilares, sin sobrecarga de texto ni diagramas abigarrados, accesible y visual para todas las edades.

---

## 🛡️ BLINDAJE ANTIALUCINACIONES (REGLAS OBLIGATORIAS EN TODO PROMPT)
Todo prompt generado debe incorporar los bloques herméticos de la Regla 5.2 y 5.3:
1. **Cabecera Positiva de Idioma:** `IDIOMA Y TEXTOS DE LA IMAGEN: ESPAÑOL (CASTELLANO). TODAS LAS PALABRAS, TÍTULOS Y LEYENDAS ESCRITAS EN LA IMAGEN DEBEN ESTAR EXCLUSIVAMENTE EN ESPAÑOL. NO SE PERMITEN PALABRAS EN INGLÉS NI ABREVIATURAS DE CANTIDAD.`
2. **Rótulo Superior de Título Obligatorio:** Toda imagen incluirá siempre un título superior en español en la cabecera para evitar que el motor lo omita o lo genere en inglés.
3. **Anclaje Físico Directo:** Asignar cada etiqueta a su zona del lienzo y exigir que la línea indicadora cian toque físicamente el componente.

ETIQUETAS Y ANOTACIONES EXACTAS — REGLAS ESTRICTAS:
A) Todo el texto estrictamente en español (castellano). Prohibido incluir "Cant:" en las etiquetas.
B) Rótulo superior de título principal:
— Título "[NOMBRE DE LA CLASE O PROYECTO]" en tipografía grande y luminosa en la parte superior.
C) Etiquetas indicadoras:
— [COMPONENTE 1]
— [COMPONENTE 2]
— [COMPONENTE 3]
— [COMPONENTE 4]

ESTILO:
— Estilo: manual técnica de ingeniería aeroespacial premium y museo de ciencias de clase mundial en 3D.
— Todo el texto estrictamente en español. Nivel de detalle: publicación científica 4K.
— Simplicidad visual: sin tablas de leyendas (salvo Fichero 8), sin sobrecarga cognitiva, optimizado para comprensión clara.

---

### 🔹 PLANTILLA 1: Corte Anatómico Técnico CAD (Anatomía Interna para Teoría P2)
```text
IDIOMA Y TEXTOS DE LA IMAGEN: ESPAÑOL (CASTELLANO). TODAS LAS PALABRAS, TÍTULOS Y LEYENDAS ESCRITAS EN LA IMAGEN DEBEN ESTAR EXCLUSIVAMENTE EN ESPAÑOL. NO SE PERMITEN PALABRAS EN INGLÉS NI ABREVIATURAS DE CANTIDAD.

Ilustración digital 3D de alta definición estilo manual técnica de ingeniería que muestra un único dibujo central de [OBJETO/ROBOT] en vista isométrica sobre un fondo azul marino sólido (#0A1118) con una sutil cuadrícula técnica. El robot se muestra en corte anatómico interno donde la mitad revela la carcasa exterior y la otra mitad deja ver el interior con sus motores, sensores y circuitos.

REGLA CRÍTICA DE TEXTOS Y LÍNEAS INDICADORAS:
La imagen debe mostrar EXCLUSIVAMENTE los siguientes textos limpios en español:
1. Rótulo superior de título principal (en la cabecera superior, en tipografía grande, audaz y luminosa color cian neón):
"[TÍTULO DE ANATOMÍA EN ESPAÑOL, ej: ANATOMÍA DEL ASCENSOR / ANATOMÍA DE SEMÁFOROS]"
2. Cinco cajas de texto descriptivas con una línea indicadora recta y nítida de color cian que toque físicamente y apunte con precisión al componente real que describe:
— "[ETIQUETA 1]" -> (la línea apunta directamente a [UBICACIÓN FÍSICA 1]).
— "[ETIQUETA 2]" -> (la línea apunta exactamente a [UBICACIÓN FÍSICA 2]).
— "[ETIQUETA 3]" -> (la línea apunta al componente [UBICACIÓN FÍSICA 3]).
— "[ETIQUETA 4]" -> (la línea apunta a [UBICACIÓN FÍSICA 4]).
— "[ETIQUETA 5]" -> (la línea apunta físicamente a [UBICACIÓN FÍSICA 5]).

Estilo ultra nítido, sin marcas de agua, sin repeticiones de texto y con estricto control tipográfico en español. Prohibida la leyenda de colores en este documento de hardware.
```

---

### 🔹 PLANTILLA 2: Despiece Técnico (Prácticas de Construcción P1)
```text
IDIOMA Y TEXTOS DE LA IMAGEN: ESPAÑOL (CASTELLANO). TODAS LAS PALABRAS, TÍTULOS Y LEYENDAS ESCRITAS EN LA IMAGEN DEBEN ESTAR EXCLUSIVAMENTE EN ESPAÑOL. NO SE PERMITEN PALABRAS EN INGLÉS NI ABREVIATURAS DE CANTIDAD.

Ilustración digital 3D de alta definición estilo manual técnica de ingeniería de despiece modular del kit de montaje de [OBJETO/ROBOT] en formato panorámico 16:9 sobre un fondo azul marino sólido (#0A1118) con cuadrícula técnica. Todas las piezas modulares flotan separadas en orden de montaje horizontal, conectadas por finas líneas de guía axiales de color cian brillante.

REGLA CRÍTICA DE TEXTOS Y LÍNEAS INDICADORAS:
La imagen debe mostrar EXCLUSIVAMENTE los siguientes textos limpios en español:
1. Rótulo superior de título principal (en la cabecera superior, en tipografía grande, audaz y luminosa color cian neón):
"[TÍTULO DEL DESPIECE EN ESPAÑOL, ej: DESPIECE TÉCNICO DE MONTAJE]"
2. Cinco cajas de texto con los nombres técnicos de las piezas (sin poner "Cant:"). Cada caja de texto debe tener una línea indicadora recta y nítida de color cian que toque físicamente y apunte exactamente a la pieza separada que describe:
— "[ETIQUETA 1]" -> (la línea apunta físicamente a [PIEZA SEPARADA 1]).
— "[ETIQUETA 2]" -> (la línea apunta exactamente a [PIEZA SEPARADA 2]).
— "[ETIQUETA 3]" -> (la línea apunta a [PIEZA SEPARADA 3]).
— "[ETIQUETA 4]" -> (la línea apunta físicamente a [PIEZA SEPARADA 4]).
— "[ETIQUETA 5]" -> (la línea apunta a [PIEZA SEPARADA 5]).

Estilo ultra nítido, sin marcas de agua, sin repeticiones de texto y con estricto control tipográfico en español. Prohibida la leyenda de colores.
```

---

### 🔹 PLANTILLA 3 (Fichero 8): Slide 3D Funcional en Acción (Dinámica Operativa)
```text
IDIOMA Y TEXTOS DE LA IMAGEN: ESPAÑOL (CASTELLANO). TODAS LAS PALABRAS, TÍTULOS Y LEYENDAS ESCRITAS EN LA IMAGEN DEBEN ESTAR EXCLUSIVAMENTE EN ESPAÑOL. NO SE PERMITEN PALABRAS EN INGLÉS NI ABREVIATURAS DE CANTIDAD.

Ilustración digital 3D de alta definición en formato panorámico 16:9 estilo representación técnica en acción sobre un elegante fondo azul marino sólido (#0A1118). La escena muestra a [OBJETO/ROBOT] en su entorno operativo real realizando su función principal: [DESCRIPCIÓN DE LA ACCIÓN EN 3D, ej: el ascensor elevando suavemente la cabina / el semáforo regulando el paso]. Se aprecian sutiles haces de luz o efectos visuales cian/verdes que representan de forma intuitiva el movimiento o la detección de los sensores.

REGLA CRÍTICA DE TEXTOS Y LÍNEAS INDICADORAS:
La imagen debe mostrar EXCLUSIVAMENTE los siguientes textos limpios en español:
1. Rótulo superior de título principal (en la cabecera superior, en tipografía grande, audaz y luminosa color cian neón):
"[TÍTULO FUNCIONAL EN ESPAÑOL, ej: DINÁMICA DE CONTROL EN ACCIÓN]"
2. Tres o cuatro cajas de texto limpias con una línea indicadora cian que apunte directamente a los puntos clave de la acción:
— "[ETIQUETA 1]" -> (apunta al [PUNTO DE ACCIÓN/SENSOR 1]).
— "[ETIQUETA 2]" -> (apunta al [PUNTO DE ACCIÓN/MOTOR 2]).
— "[ETIQUETA 3]" -> (apunta al [PUNTO DE ACCIÓN/OBJETO 3]).
3. Leyenda de flujos operativa (en la esquina inferior izquierda, exclusiva para Fichero 8):
VERDE = 1. SENTIR (Sensores y Lectura)
AZUL = 2. DECIDIR (Lógica y Control)
ROJO = 3. ACTUAR (Motores y Acción)

Estilo 3D inmersivo, claro y dinámico, sin sobrecarga visual, centrado en mostrar qué hace el robot y cómo interactúa con su entorno de manera comprensible para todos los públicos.
```

---

### 🔹 PLANTILLA 4: Mapa Mental Jerárquico / Diagrama de Síntesis NLM
```text
IDIOMA Y TEXTOS DE LA IMAGEN: ESPAÑOL (CASTELLANO). TODAS LAS PALABRAS, TÍTULOS Y LEYENDAS ESCRITAS EN LA IMAGEN DEBEN ESTAR EXCLUSIVAMENTE EN ESPAÑOL. NO SE PERMITEN PALABRAS EN INGLÉS NI ABREVIATURAS DE CANTIDAD.

Crea una infografía 3D futurista y espectacular de un Mapa Mental y Diagrama de Flujo Conceptual en formato panorámico 16:9 sobre un elegante fondo azul marino tecnológico (#0A1118) con cuadrícula milimetrada sutil. Renderizado calidad Unreal Engine 5 e iluminación de neón volumétrico. En el centro resplandece un nodo hexagonal de cristal cian brillante. Desde el núcleo irradian tres ramas simétricas conectadas por haces de luz cian luminiscente:
— Rama izquierda: ilustra visualmente el concepto [DESCRIPCIÓN VISUAL RAMA 1].
— Rama central: ilustra visualmente el concepto [DESCRIPCIÓN VISUAL RAMA 2].
— Rama derecha: ilustra visualmente el concepto [DESCRIPCIÓN VISUAL RAMA 3].

ETIQUETAS Y ANOTACIONES EXACTAS — REGLAS ESTRICTAS:
A) Todo el texto estrictamente en español (castellano). Prohibido añadir texto decorativo o redundante.
B) Rótulo superior de título principal:
— Título "[TÍTULO GENERAL DEL DIAGRAMA]" en la cabecera superior.
C) Incluir ÚNICAMENTE las siguientes 4 etiquetas literales dentro de las cajas de llamada HUD:
— [TÍTULO CENTRAL] (nodo central)
— [TÍTULO RAMA 1] (rama izquierda)
— [TÍTULO RAMA 2] (rama central)
— [TÍTULO RAMA 3] (rama derecha)
```

---

### 🔹 PLANTILLA 5 (Fichero 5B): Slide de Transición y Portada de Trilogía (`5b.Prompt_Slide_Resumen_Trilogia.txt`)
```text
IDIOMA Y TEXTOS DE LA IMAGEN: ESPAÑOL (CASTELLANO). TODAS LAS PALABRAS, TÍTULOS Y LEYENDAS ESCRITAS EN LA IMAGEN DEBEN ESTAR EXCLUSIVAMENTE EN ESPAÑOL. NO SE PERMITEN PALABRAS EN INGLÉS NI ABREVIATURAS DE CANTIDAD.

Ilustración digital 3D de alta definición en formato panorámico 16:9 estilo presentación ejecutiva de ingeniería aeroespacial y museo de ciencias sobre un elegante fondo azul marino sólido (#0A1118) con cuadrícula milimetrada sutil. La imagen representa una espectacular diapositiva de síntesis y portada de sección visual. En el centro resplandecen tres pedestales o paneles holográficos verticales de cristal templado y marco cian brillante, colocados en perspectiva simétrica y espaciosa, que presentan de forma limpia y accesible para todas las edades los tres pilares de estudio de la Trilogía de la Ingeniería: [OBJETO/SISTEMA].

TEXTOS LITERALES A ESCRIBIR EN LA IMAGEN (ESTRICTAMENTE EN ESPAÑOL):

1. Rótulo superior de título principal (en el centro superior, en tipografía grande, audaz y luminosa color cian neón):
"RESUMEN TÉCNICO: TRILOGÍA DE INGENIERÍA"

2. Subtítulo descriptivo (justo debajo del título central, en color blanco limpio):
"[TÍTULO O SISTEMA ANALIZADO]"

3. Títulos en los tres paneles o columnas holográficas (de izquierda a derecha):
— Panel Izquierdo: "1. PRINCIPIO [BIOLÓGICO/FÍSICO]" (con una ilustración 3D clara de [ILUSTRACIÓN 1]).
— Panel Central: "2. ANATOMÍA MECÁNICA" (con una ilustración 3D limpia de [ILUSTRACIÓN 2]).
— Panel Derecho: "3. CICLO OPERATIVO" (con un gráfico visual de [ILUSTRACIÓN 3]).

Calidad de renderizado 3D estilo Unreal Engine 5 / Keyshot, iluminación de neón volumétrico, tipografía moderna e impecable en español, sin repeticiones de texto, sin sobrecarga cognitiva y con un acabado visual digno de una presentación científica de clase mundial.
```

---

### 🔹 PLANTILLA 6 (Fichero 6): Slide 3D de Principio Físico o Biológico
```text
IDIOMA Y TEXTOS DE LA IMAGEN: ESPAÑOL (CASTELLANO). TODAS LAS PALABRAS, TÍTULOS Y LEYENDAS ESCRITAS EN LA IMAGEN DEBEN ESTAR EXCLUSIVAMENTE EN ESPAÑOL. NO SE PERMITEN PALABRAS EN INGLÉS NI ABREVIATURAS DE CANTIDAD.

Ilustración digital 3D de alta definición en formato panorámico 16:9 estilo diseño industrial y museo de ciencias moderno sobre un elegante fondo azul marino sólido (#0A1118) con sutil iluminación volumétrica. La imagen representa visualmente en 3D el principio [FÍSICO / BIOLÓGICO] que inspira al robot, mostrando de forma clara, espaciosa y atractiva [DESCRIPCIÓN SENCILLA DEL ELEMENTO EN 3D, ej: una mano humana 3D estilizada / un sistema de poleas en 3D / una esclusa de paso limpia].

REGLA CRÍTICA DE TEXTOS Y LÍNEAS INDICADORAS:
La imagen debe mostrar EXCLUSIVAMENTE los siguientes textos limpios en español:
1. Rótulo superior de título principal (en la cabecera superior, en tipografía grande, audaz y luminosa color cian neón):
"[TÍTULO DEL PRINCIPIO EN ESPAÑOL, ej: PRINCIPIO DE POLEAS Y CONTRAPESO]"
2. Tres o cuatro cajas de texto limpias con una línea indicadora cian nítida que apunte directamente a las partes clave:
— "[ETIQUETA 1]" -> (apunta a [PARTE 1]).
— "[ETIQUETA 2]" -> (apunta a [PARTE 2]).
— "[ETIQUETA 3]" -> (apunta a [PARTE 3]).

Estilo 3D muy limpio, espacioso y fácil de comprender a simple vista, sin sobrecarga visual, sin leyendas de colores y con un acabado visual premium.
```

