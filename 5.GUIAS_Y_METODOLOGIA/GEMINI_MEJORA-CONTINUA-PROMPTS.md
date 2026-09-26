# ⏱ ACTUALIZADO: 2026-06-03

# GEMINI_MEJORA-CONTINUA-PROMPTS.md — Memoria de Antigravity

Leer este documento COMPLETO antes de generar cualquier fichero de clase.
Las mejoras aquí anotadas se aplican automáticamente a todas las clases siguientes.

---

## NOMBRES DE FICHERO — REGLA FIJA

Los ficheros auxiliares tienen nombre genérico. La clase va en la carpeta, NO en el nombre del fichero.

| Correcto | Incorrecto |
|---|---|
| `5.Bloques_para_GEMINI.txt` | `5.Bloques_para_GEMINI_3.4_Robot-repartidor.txt` |
| `4.Ejemplo_real_para_GEMINI.txt` | `4.Ejemplo_real_para_GEMINI_3.4_Robot-repartidor.txt` |
| `1.Teoria_para_NLM.txt` | `1.Teoria_para_NLM_3.4_Robot-repartidor.txt` |
| `6.Fuente-y-Prompt-Nanobana.txt` | `6.Fuente-y-Prompt-Nanobana_3.4_Robot-repartidor.txt` |
| `T0.DEBATE.pdf` | `T0.DEBATE_3.4_Robot-repartidor.pdf` |
| `P4.JUEGO.html` | `P4.JUEGO_3.4_Robot-repartidor.html` |

---

## FLUJO CORRECTO DE MEJORAS Y CREACIÓN EN CASCADA

1. El profesor depura un HTML de Gemini y pasa las notas a Antigravity.
2. Antigravity decide a qué documento va cada mejora:
   - **Técnica / código Babylon.js o Three.js** → `GEMINI_CONOCIMIENTO-GEMINI.md`
   - **Pedagógica / conceptual / terminología / estructura de ficheros** → este documento
   - Puede ir a los dos si aplica a ambos niveles.
3. Antigravity genera los `.md` actualizados como outputs.
4. **Metodología de Creación Acumulativa**:
   - Para evitar prompts en frío que no incorporen depuraciones reales, los prompts de generación de código `4.Ejemplo_real_para_GEMINI.txt` y `5.Bloques_para_GEMINI.txt` **no se generan al inicio de la clase**.
   - **Fase 1**: Se escriben inicialmente solo los ficheros de teoría, ejemplo real para NLM, la simulación de construcción inicial, el debate, el juego de repaso y los prompts para infografía con Nano Banana:
     - `1.Teoria_para_NLM.txt`
     - `2.Ejemplo_real_para_NLM.txt`
     - `3.Simulacion_construccion_para_GEMINI.txt`
     - `6.Fuente-y-Prompt-Nanobana.txt`
     - `T0.DEBATE.pdf`
     - `P4.JUEGO.html`
   - **Fase 2**: Una vez que el profesor ha depurado físicamente en Gemini la práctica `P1.CONSTRUCCION` (montada a partir del fichero 3) y se han incorporado los nuevos aprendizajes y bugs a `GEMINI_CONOCIMIENTO-GEMINI.md`, Antigravity escribe `4.Ejemplo_real_para_GEMINI.txt`.
   - **Fase 3**: Del mismo modo, una vez depurada la práctica `P2.EJEMPLO-REAL` e integrado su conocimiento en el documento correspondiente, Antigravity escribe `5.Bloques_para_GEMINI.txt`.
5. **Suma inteligente:** al incorporar mejoras, Antigravity NO yuxtapone — fusiona, elimina duplicados y consolida reglas similares. Los documentos deben crecer lo mínimo posible.

---

## TERMINOLOGÍA — DECISIONES FIJAS

| Término técnico | Término del curso | Motivo |
|---|---|---|
| Función / subrutina | **Tarea guardada** | Más natural para personas de 65-70 años. Aprobado en clase 3.4. |

---

## SEPARACIÓN TEORÍA / EJEMPLO REAL

- **1.Teoria_para_NLM.txt** — concepto abstracto PURO. El robot NO debe aparecer bajo ninguna circunstancia. Tampoco se debe hablar de sus partes (como el brazo, la pinza, las articulaciones o las ruedas) que se tratarán luego en el fichero 2. Solo se permiten analogías cotidianas, analógicas o humanas (ej. lanzar una pelota, cocinar, tocar el piano).
- **2.Ejemplo_real_para_NLM.txt** — el robot concreto aplicando el concepto. Estructura: título + 2-3 párrafos + QUÉ SE DEBE ANALIZAR (mín. 4 puntos) + RESULTADO ESPERADO.
- **Regla de Oro:** El fichero 1 habla de conceptos relacionados con la clase de forma general y cotidiana, NUNCA sobre el robot ni partes robóticas específicas de la práctica posterior.
- **Test antes de entregar:** ¿Aparece el nombre del robot, o palabras como "robot", "pinza robótica", "base giratoria", "servomotores", "eje motriz" en el fichero 1? Si SÍ ➔ reescribir.

---

## MEJORAS DE BABYLON.JS — P1.CONSTRUCCION (depuradas en clase 3.4)

Aplicar en todos los P1.CONSTRUCCION de clases 3.4 en adelante. El código exacto vive en `GEMINI_CONOCIMIENTO-GEMINI.md § P1.CONSTRUCCION`. Aquí solo la intención pedagógica:

1. **Niebla exponencial** — el suelo nunca parece una baldosa flotando. `FOGMODE_EXP2`, densidad 0.035, color igual a `clearColor`. Aplica también a P2 y P3.
2. **Cámara orbital constante** — el giro no se interrumpe con el ratón durante la construcción. Solo para al entrar en Demo Final.
3. **Drag & Drop real** — API nativa HTML5. No resolver con clic simple — confunde al alumno.
4. **Layout Flexbox** — panel lateral nunca con `position:absolute` sobre el canvas.
5. **Indicador holográfico inicial** — Torus emisivo cian hasta que se instala la primera pieza. Escena nunca vacía.
6. **Compatibilidad Babylon.js** — `Vector3` directo (no `setAll`), toggle emisivo con `new Color3`, pivots con `TransformNode`.

---

## MEJORAS DE BABYLON.JS — P2.EJEMPLO-REAL (depuradas en clase 3.4)

Aplicar en todos los P2.EJEMPLO-REAL de clases 3.4 en adelante. El código exacto vive en `GEMINI_CONOCIMIENTO-GEMINI.md § P2.EJEMPLO-REAL`:

1. **Escenarios transitables** — los edificios clave (almacén, casas) no son bloques sólidos. El almacén tiene paredes individuales + puerta animada (tipo garaje). Los edificios de destino tienen puerta corrediza que se abre al llegar.
2. **Máquina de estados logística** — el ciclo de vida del robot tiene estados explícitos y nombrados (SALIENDO / EN_RUTA / NOTIFICANDO / ENTREGANDO / REGRESANDO…). Sin lógica lineal que cause saltos bruscos.
3. **Panel con sliders interactivos** — el alumno puede modificar en tiempo real al menos 2 parámetros (ej. velocidad del robot, tiempo de respuesta del cliente). Hace la simulación pedagógicamente activa, no solo visual.
4. **Humanoides articulados** — los personajes no son cilindros. Torso + cabeza + brazos (pivot en hombro) + piernas (pivot en cadera). Animación de caminata procedural con `Math.sin(time)`.
5. **Distancia de parada segura** — los personajes se detienen a ~1.4 m del robot para interactuar. Nunca se funden con el modelo 3D.
6. **Transferencia de paquetes** — el paquete existe como objeto 3D dentro del robot, cambia de color antes de la entrega, desaparece del robot y aparece en manos del personaje. Los brazos del personaje se bloquean al recogerlo (IK simulada).
7. **Ejecución paralela** — tras entregar, el robot reanuda su ruta inmediatamente mientras el personaje regresa a casa en segundo plano. Sin esperar a que termine la animación del personaje.
8. **Reset limpio completo** — el botón de nueva ronda reinicia robot, personajes, paquetes, puertas y UI sin recargar el navegador. Debe funcionar infinitas veces.
9. **IBL (Image Based Lighting)** — `HDRCubeTexture` vía URL pública como `scene.environmentTexture`. Intensity 0.4-0.8. Da reflejos PBR realistas sin coste de assets locales.
10. **SSAO2** — `SSAO2RenderingPipeline` para micro-sombras de contacto. ratio 0.5, samples 16. Añade profundidad visual en rincones y junturas.
11. **Textos excluidos del GlowLayer** — `glow.addExcludedMesh(labelMesh)` para que las etiquetas no queden borrosas ni brillantes.
12. **Humanoides orgánicos** — cápsulas (`CreateCapsule`), elipsoides (`CreateSphere` con `diameterX/Y/Z`) y esferas en articulaciones. Resultado orgánico sin huecos ni recortes en la malla al animar. Código exacto en `§ P2 — Humanoides orgánicos`.
13. **Anti-atropello con offset lateral** — vecinos en estado WAITING se colocan a ±1.8 en X respecto al disco de entrega, nunca encima. Dan un paso al frente al llegar el robot.
14. **Radio de cámara depurado** — radio 45 (perspectiva) u orthoSize 22 (ortográfica) para que los 4 edificios + almacén encajen sin solapamientos. alpha fijo -PI/2.
15. **Tabla PBR por categoría** — valores exactos de metallic/roughness por tipo de superficie (carrocería, goma, metal, cristal, asfalto). Código exacto en `§ BABYLON.JS valores obligatorios`.
16. **PROHIBIDO .glb/.gltf** — toda la geometría es procedural. Sin dependencias externas. HTML único autocontenido siempre.

---

## MEJORAS DE BABYLON.JS — P3.BLOQUES con joystick (depuradas en clase 3.4)

Aplicar cuando el P3 use control manual con joystick. El código exacto vive en `GEMINI_CONOCIMIENTO-GEMINI.md § P3.BLOQUES-JOYSTICK`:

1. **Robot empieza fuera del almacén** — posición inicial en la calle (ej. z=4.5), nunca dentro de los colliders del almacén.
2. **Colisiones contra `chassis`, no contra `TransformNode`** — evaluar `chassis.intersectsMesh(c)` donde `chassis` es una malla física real. Evaluar contra el nodo vacío padre crashea la detección y vuelve invisible al robot.
3. **Dirección del joystick basada en `camera.alpha`** — no usar `getViewMatrix().invert()` sin `attachControl`. Calcular `fw` y `rw` directamente desde el ángulo fijo de la cámara isométrica.
4. **Joystick con `setPointerCapture`** — garantiza que el knob no se escape aunque el ratón salga del contenedor.
5. **Slider de velocidad en tiempo real** — `<input type="range">` de 2 a 12 m/s. La rotación de ruedas se sincroniza matemáticamente con la velocidad actual.
6. **Etiquetas flotantes `BILLBOARDMODE_ALL`** — `CreatePlane` con `DynamicTexture` sobre cada edificio y almacén. Siempre mirando a la cámara. Usar `StandardMaterial` con `disableLighting:true` (excepción permitida para etiquetas 2D).
7. **Modal custom, nunca `alert()`** — ventana emergente HTML con fondo semitransparente, texto 22px, botón explícito ≥70px. Nunca avance automático.
8. **Máquina de estados DRIVING/DELIVERING** — igual que en P2. La cinemática de humanoides, stopDist y transferencia de paquetes se reutilizan íntegramente desde las reglas de P2.

---

## MEJORAS DE BABYLON.JS — P3.BLOQUES (depuradas en clase 3.4)

Aplicar en todos los P3.BLOQUES de clases 3.4 en adelante. El código exacto vive en `GEMINI_CONOCIMIENTO-GEMINI.md § P3.BLOQUES-reglas-adicionales`:

1. **Cámara isométrica ortográfica** — NUNCA vista cenital plana para maquetas urbanas. `ORTHOGRAPHIC_CAMERA` con alpha=-PI/4, beta=PI/3.5. Recalcular `orthoLeft/Right/Top/Bottom` en cada resize.
2. **Pathfinding en L (Taxicab)** — el robot nunca atraviesa obstáculos en diagonal. Mover primero eje Z (calle principal), luego eje X (lateral).
3. **Observables cancelables** — todo `onBeforeRenderObservable` activo se registra en array global `animObservers`. Al pulsar PARAR o REINICIAR: `remove()` de todos. Sin esto el robot sigue moviéndose como fantasma.
4. **checkWin con ruta completa** — validar el historial completo incluyendo el regreso al almacén. No cortar en el primer objetivo.
5. **Huecos dinámicos con replaceWith()** — al soltar bloque en bucle, usar `querySelector(':scope > .hueco-pista')` + `replaceWith()`, no `appendChild()`.
6. **Botón X en bloques del usuario** — visible con `:hover`, oculto en bloques `🔒` por CSS.
7. **Lógica anticipada de vecinos** — estados IDLE/WAITING. Si LLAMAR AL VECINO se ejecuta antes de llegar el robot, el vecino espera y la entrega es instantánea al llegar.
8. **Efectos procedurales sin assets** — ondas y partículas con `CreateTorus` + `DynamicTexture` animando escala y alpha. Sin imágenes externas.

---

## NOTAS DEL PROFESOR Y CONTROL DE VERSIONES

### 2026-05-20
- Flujo correcto confirmado: mejoras → documentos, no regenerar prompts ya hechos.
- Suma inteligente: no yuxtaponer mejoras — fusionar, eliminar duplicados, consolidar. Los documentos no deben crecer innecesariamente.

### 2026-05-23 — Clase 2.3 Penguin BOT (P2.EJEMPLO-REAL)
- 6 mejoras técnicas Babylon.js incorporadas a `GEMINI_CONOCIMIENTO-GEMINI.md`: B21–B25 en tabla de errores + nueva sección `§ P2.EJEMPLO-REAL — robots bípedos`.
- Todas las mejoras son técnicas → van solo a CONOCIMIENTO-GEMINI, no a este documento.
- Errores conceptuales corregidos en 1.Teoria y 2.Ejemplo: el Penguin BOT NO tiene ruedas (tiene 2 patas rígidas + 4 servos). No es equilibrio dinámico (puede estar parado sin caerse). El concepto correcto es coordinación en 4 tiempos.

### 2026-05-23 — Clase 2.3 Penguin BOT (P3.BLOQUES)
- Incorporadas 6 mejoras nuevas a sección `§ P2.EJEMPLO-REAL — robots bípedos` de CONOCIMIENTO-GEMINI: SPEED_MULTIPLIER 1.333, avance Z 0.72 u/s sincronizado con waddling, raycaster desde ojos físicos (no centro), `runSpecialAnim` motor de acrobacias aisladas.
- Nueva sección `§ Movimientos especiales Penguin BOT`: 9 acrobacias matemáticas (voltereta, salto, moonwalk, cangrejo, reverencia, saludar, temblar, tropezar, baile).
- Categorización de bloques por color semántico: rojo=BALANCEAR, naranja=acrobacias, morado=REPETIR, cian=SENSOR, gris=heredados.

### 2026-06-03 — Clase 4.2 Brazo Robótico (Hombro)
- **Metodología de Creación Acumulativa**: Los prompts 4 y 5 solo se generan secuencialmente conforme se depuren físicamente las prácticas anteriores en AI Studio y se consolide el conocimiento en `GEMINI_CONOCIMIENTO-GEMINI.md`.
- **Temática de T0.DEBATE (Regla de Oro)**: Los documentos de debate (`T0.DEBATE.pdf`) del Bloque 4 (Brazo robótico) deben comparar la articulación del robot con su equivalente en el cuerpo humano (Clase 4.1: base vs. tronco humano; Clase 4.2: hombro vs. hombro humano; Clase 4.3: codo; Clase 4.4: muñeca; etc.). Deben analizarse explícitamente los ángulos y límites máximos de movimiento del humano frente al robot y las diferencias entre articulaciones biológicas (rótulas, etc.) y mecánicas.
- **Restricción de Simetría de Diales**: Para evitar distorsiones de perspectiva en 3D, el hombro debe ser simétrico. Se estandarizan las alturas de `shoulderServo` y `jointCover` a `0.3`, con diales en `X = 0.915` / `-0.915` y punteros en `X = 0.935` / `-0.935` (altura `Y = 1.88`).
- **Orientación de Texto en Diales**: Para mantener los números legibles y orientados correctamente a ambos lados (evitando textos invertidos/boca abajo), la rotación del texto en la textura dinámica del dial derecho es antihoraria (`rad`), mientras que el dial izquierdo se dibuja en sentido horario (`Math.PI - rad`).
- **Compactación de UI de Bloques**: Para evitar que el espacio de trabajo se superponga con los botones de control (EJECUTAR, PARAR, LIMPIAR) en pantallas compactas, se limita el contenedor `#workspace` a un máximo de `200px` (o proporcional) y se reducen los botones de control a una altura de `44px`.
- Se eliminaron todas las referencias y acrónimos obsoletos del motor Claude, unificando todo bajo el entorno Antigravity y la nomenclatura de ficheros del proyecto `GEMINI_`.
- **Decisión de diseño futuro**: En la clase final del bloque (Clase 4.6), cuando el brazo robótico esté completamente construido, se incorporará un sistema de control por **IA Real** que se conectará directamente con la **API de Gemini (Google AI Studio)** vía API Key. Esto permitirá a los alumnos dictar órdenes abiertas y complejas en lenguaje natural y ver al brazo completo reaccionar en tiempo real en la vista 3D.
- **Cambio de metodología de infografías**: Se establece que todas las infografías de las clases del curso se generarán utilizando la herramienta Nano Banana Pro (con Gemini Advanced / Imagen 3) para garantizar acabados más realistas, luz natural y un efecto 3D más limpio. Antigravity generará un archivo auxiliar llamado `6.Fuente-y-Prompt-Nanobana.txt` en la carpeta `1.FICHEROS-AUXILIARES` de cada clase, conteniendo la fuente de datos estructurada y el prompt de diseño en inglés que exige textos estrictamente en español. Ya se ha generado este fichero para las clases 4.1 y 4.2.

### 2026-07-15 — Blindaje de Teoría para NotebookLM y Enfoque Visual en Infografías
- **Escudo Anti-Robots Obligatorio en `1.Teoria_para_NLM.txt` (Regla R13)**: Aunque el texto del Fichero 1 sea 100% conceptual y cotidiano sin mencionar robots, NotebookLM (`NLM`) frecuentemente infiere por sí mismo una diapositiva final o conclusión sobre robótica/máquinas al generar las presentaciones PPT (`T1`). Para impedir esto, **es obligatorio insertar tanto al inicio como al final de todos los archivos `1.Teoria_para_NLM.txt` una Instrucción de Sistema de Blindaje explícita** (`INSTRUCCIÓN DE SISTEMA OBLIGATORIA PARA NOTEBOOKLM: ESTRICTAMENTE PROHIBIDO MENCIONAR, DIBUJAR O INCLUIR ROBOTS... ESTA PRESENTACIÓN DEBE TRATAR EXCLUSIVAMENTE SOBRE BIOLOGÍA Y VIDA COTIDIANA`). Se ha aplicado ya a las clases 4.1, 4.2, 4.3, 4.4 y 4.5.
- **Enfoque Visual en Primer Plano en Infografías de Módulo (`Fichero 8`)**: En clases que se enfocan en una articulación intermedia o distal (como la Clase 4.4 Muñeca o Clase 4.5 Pinza), si se pide al motor de imagen dibujar "todo el brazo robótico central con un bucle alrededor", el diagrama parecerá centrarse en el codo o el hombro. Para solucionar esto y dar máxima precisión, **las infografías de módulo deben pedir siempre un primer plano / zoom de detalle (`close-up`) exclusivamente del módulo protagonista y la herramienta/efector final**, haciendo que el bucle de las 3 fases rodee únicamente esa articulación.
- **Estricta Separación Estructural en Prompts de Imagen (`Ficheros 6, 7 y 8`)**: Para evitar que Gemini / Imagen 3 intente rotular en 3D párrafos largos explicativos convirtiéndolos en inglés macarrónico/gibberish, se debe separar rígidamente en los ficheros:
  - `SECCIÓN 1: DESCRIPCIÓN VISUAL Y REGLAS ANATÓMICAS DE DIBUJO 3D` *(con advertencia: `ATENCIÓN: NO ESCRIBIR NINGUNO DE ESTOS PÁRRAFOS COMO TEXTO EN LA IMAGEN`)*.
  - `SECCIÓN 2: TEXTOS LITERALES Y CORTOS A ESCRIBIR EN LA IMAGEN` *(sólo las etiquetas exactas entre comillas, sin paréntesis explicativos largos al lado)*.

