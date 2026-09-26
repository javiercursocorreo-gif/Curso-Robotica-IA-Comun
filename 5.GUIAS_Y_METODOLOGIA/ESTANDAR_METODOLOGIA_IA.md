# ESTÁNDAR DE METODOLOGÍA DE AGENTES (AGENT LOOP ENGINEERING & MÉTODO PLAN → BUCLE)

Este documento define la arquitectura maestra y la metodología de trabajo innegociable que el sistema de IA (Antigravity u otros agentes autónomos) debe seguir al interactuar con este repositorio. 

El objetivo es superar el "prompting manual paso a paso" e implantar una **Delegación por Objetivos (Goal-oriented delegation)** perfectamente calibrada mediante **Bucles Autónomos Verificables**, fusionando las mejores prácticas de *Agent Loop Engineering* con el **Método Plan → Bucle (DiarioVida)**.

Cualquier nuevo agente o hilo de chat que asuma el control de este proyecto debe leer y aplicar este archivo antes de ejecutar comandos complejos.

---

## 1. EL CAMBIO DE PARADIGMA: DE PROMPT A GOAL Y EL MÉTODO PLAN → BUCLE

* **Evitar el Micromanagement:** El usuario no debe dictar cada línea de código ni supervisar cada micro-paso.
* **Uso de `/goal`:** El trabajo debe iniciarse proporcionando a la IA un objetivo final claro (ej. `/goal Migrar clase 4.5 al nuevo estándar cinemático`).
* **Filosofía Core (*"El modelo caduca; el método no"*):** Los modelos de IA evolucionan, pero la metodología basada en bucles verificables y criterios de éxito es universal y perenne.
* **Reparto Inteligente en 2 Fases Estrictas:** Todo objetivo complejo se divide innegociablemente en dos etapas secuenciales:
  1. **FASE 1: PLANIFICAR (Planificador Puro - Razonamiento Profundo).**
  2. **FASE 2: EJECUTAR EN BUCLE (Ejecutor Autónomo - Iteración Verificable).**

---

## 2. FASE 1: EL PLANIFICADOR PURO (INVESTIGACIÓN Y DISEÑO DE ALTA PRECISIÓN)

En la Fase 1, el agente actúa exclusivamente como **Planificador Estratégico**.
* **Cero Ejecución:** En esta fase está **terminantemente prohibido** modificar código, crear ficheros de producción o ejecutar comandos de modificación en el proyecto. Solo se investiga, se razona y se diseña.
* **Regla Anti-Suposición (Preguntas antes de actuar):** Si un requisito es ambiguo o falta contexto, el Planificador **nunca supone**. Debe formular al usuario las preguntas necesarias antes de consolidar el plan. Preguntas clave del buen planificador:
  * ¿Cuál es exactamente el resultado final deseado y cómo sabremos que está logrado?
  * ¿Qué restricciones existen (tiempo, herramientas, formato, rendimiento, librerías permitidas)?
  * ¿Qué **NO** debe hacerse bajo ningún concepto? ¿Qué elementos son sagrados o intocables en el código o arquitectura?
  * ¿Existencias de ejemplos "esto sí / esto no" que sirvan de referencia?
* **Anatomía del Plan Aprobado (`implementation_plan.md`):**
  Un plan maestro bien redactado debe incluir siempre:
  1. **Desglose de Tareas en `task.md`:** Subtareas concretas, ordenadas lógicamente (dependencias primero).
  2. **Criterio de Éxito por Tarea (*Condition of Done*):** Por cada tarea, debe especificarse exactamente **CÓMO se verificará matemáticamente, lógicamente o visualmente que está bien hecha** antes de pasar a la siguiente.
  3. **Riesgos y Decisiones Asumidas:** Identificación de posibles fricciones o dependencias críticas.
  4. **Compuerta de Producción (*Human-in-the-Loop*):** Presentación del plan completo al usuario para su aprobación formal antes de iniciar cualquier modificación.

---

## 3. FASE 2: EL EJECUTOR EN BUCLE (`While Objetivo_No_Cumplido`)

Una vez aprobado el plan, el agente transiciona al rol de **Ejecutor en Bucle**. Toma el plan aprobado como "ley" y ejecuta una unidad de trabajo o bucle iterativo que no se detiene hasta cumplir el objetivo.

### Las 5 Reglas de Oro del Bucle de Ejecución

1. **Orden de Iteración Autónoma Ininterrumpida:**
   * La IA debe avanzar paso a paso de forma autogestionada. Al terminar cada subtarea, ejecuta su verificación, corrige lo que falle y avanza a la siguiente sin detenerse a pedir confirmación al usuario en cada micro-paso intermedio.
2. **Condición de Parada y Criterio de Éxito Estricto:**
   * El bucle evalúa en cada iteración si se ha cumplido exactamente el *Criterio de Éxito* de la subtarea activa. Si no se cumple, el bucle repite la iteración corrigiendo los errores detectados.
3. **Tope de Seguridad Global (*Safety Cap & Drift Gate*):**
   * **Límite de Pasadas Máximas (p. ej. 10 pasadas globales del bucle):** Para evitar bucles infinitos o consumos descontrolados, el agente cuenta con un tope de seguridad.
   * **Compuerta de Deriva (*Drift Gate* - 3 Fallos Consecutivos):** Si una misma tarea o mini-bucle falla 3 veces consecutivas sin lograr el criterio de éxito, el agente **DEBE PARAR OBLIGATORIAMENTE**, documentar con precisión técnica el error exacto y solicitar clarificación o asistencia al usuario.
4. **La Regla de Honestidad (*Honesty Rule / Anti-Alucinación*):**
   * *"Si te bloqueas o algo no se puede resolver de verdad, PARA y explica por qué. **No inventes ni finjas que funciona**."*
   * Está estrictamente prohibido dar por válida una tarea o asumir éxito por pura intuición si los scripts de validación, la matemática trigonométrica o las pruebas TDD demuestran lo contrario.
5. **Evidencia ANTES vs. DESPUÉS (*Show Before & After*):**
   * Al cerrar el bucle de una tarea mayor o al generar el informe final (`walkthrough.md`), el agente debe mostrar obligatoriamente el resultado de la **PRIMERA pasada (Antes)** comparado directamente con la **ÚLTIMA pasada corregida (Después)** —por ejemplo mediante bloques de diff, tablas comparativas o carruseles— demostrando transparentemente la evolución y eficacia del bucle de autocorrección.

---

## 4. TÉCNICAS DE TESTEO Y AUTOCORRECCIÓN TÉCNICA (TDD AUTÓNOMO)

El éxito del bucle depende directamente de la rigurosidad y precisión de la validación técnica en el paso de verificación:
* **TDD (Test Driven Development) Autónomo:** Antes de integrar lógicas matemáticas complejas (rotaciones de Euler en grados sexagesimales, conversión a radianes, cuaterniones, cinemática inversa IK, interpolaciones lerp o detección de colisiones) en los archivos HTML/JS finales, el agente debe escribir pequeños scripts efímeros en Node.js o Python (ej. ejecutados en terminal o en carpeta temporal `scratch/`) para probar y verificar que los números dan el resultado físico exacto.
* **Validación Matemática y Lógica:** Nunca asumir que el código o la cinemática funcionan por inspección visual del código. Emplear la terminal del sistema para ejecutar cálculos de prueba que garanticen que un brazo robótico no atraviesa el suelo ($Y=0$) o que los ángulos iniciales son milimétricamente correctos.
* **Prohibición de la "Ceguera Estática" (Sesgo de Confirmación IA-IA):** Queda terminantemente prohibido validar el cierre de una tarea de simulación (`[x]`) basándose exclusivamente en inspecciones puramente textuales (`grep_search` o ver que el fichero se ha escrito). El bucle iterativo debe verificar empíricamente la ausencia de excepciones Javascript (`Runtime Errors`) o advertir al humano para que valide empíricamente el renderizado real en pantalla si no se dispone de un motor headless E2E. Nunca asumir que una función inventada o alucinada (ej. `CreateGroundLines`) es correcta solo porque aparece escrita en el código.

### 4.1. Checklist de Asertos Visuales y Semánticos Obligatorios en Motores 3D (`Anti-Ceguera Sintáctica`)
Dado que un test de consola en Node (`check_syntax.js`) verifica que no haya excepciones pero es *visualmente ciego* ante opacidades, rotaciones o ángulos mal orientados, el agente queda estrictamente obligado a validar mediante inspección de AST/DOM o scripts de comprobación estructural los siguientes **3 Asertos de Simulación** antes de dar por completada cualquier práctica 3D (`Babylon.js` / `Three.js`):
1. **Aserto de Rotación de Escenario (`Camera Orbit Assert`):** En toda simulación de construcción, taller o reposo, el giro continuo del entorno DEBE realizarse moviendo la cámara alrededor del objeto central (`camera.alpha += speed` en `registerBeforeRender`). Queda prohibido rotar la malla raíz del robot (`robotGroup.rotation.y += speed`) como sustituto del giro de escenario, ya que esto desorienta el sistema de coordenadas de las piezas en el espacio.
2. **Aserto de Transparencia Estructural (`Cutaway Alpha Assert`):** Todo cuerpo central, chasis o carcasa exterior que albergue en su interior subsistemas electrónicos, placas lógicas, sensores o baterías DEBE tener fijada explícitamente una opacidad translúcida (`mat.alpha = 0.35` a `0.45` o material cutaway). Prohibido dejar carcasas con opacidad `1.0` (opaca) si contienen piezas en su interior.
3. **Aserto de Orientación y Cinemática de Ruedas (`Wheel Alignment Assert`):** En trayectorias de demostración o simulación autónoma, el eje de revolución de cualquier rueda (`CreateCylinder`) debe mantenerse rigurosamente perpendicular al vector de velocidad tangencial (`sentido de la marcha`). Prohibido añadir desfases arbitrarios (`+ Math.PI / 2`) sin validar matemáticamente en el script de verificación que las ruedas avanzan rodando y no desplazándose lateralmente.

---

## 5. ARQUITECTURA PARA ESCALAR Y EVITAR EL "DRIFT" (RUIDO DE CONTEXTO)

Para tareas que requieran múltiples horas, abarquen muchos archivos o involucren lógica densa, el agente debe proteger su ventana de contexto para prevenir la pérdida de foco y las alucinaciones:

* **Micro-segmentación en `task.md`:** Mantener una lista de tareas (`[ ]`, `[/]`, `[x]`) permanentemente actualizada en archivo físico. Esto garantiza la trazabilidad absoluta y permite recuperar el hilo en caso de recarga de sesión.
* **Sub-agentes Efímeros (`invoke_subagent`):**
  * El agente principal ("Orquestador") debe delegar la investigación extensa de múltiples directorios, la búsqueda masiva o el refactor aislado de archivos concretos a sub-agentes especializados (`Role`, `Prompt` claro).
  * Estos sub-agentes vivirán únicamente el tiempo que tarde su tarea asignada y devolverán respuestas limpias y filtradas al Orquestador.
* **Entornos Aislados (*Worktrees / Branches*):** Para tareas arriesgadas o experimentales, los sub-agentes trabajarán en un entorno de rama (`branch: true` o `share: true`) para asegurar que un fallo en el bucle no corrompa el proyecto principal.
* **Memoria de Estados Persistente (*State Persistence*):** El estado de avance SIEMPRE residirá en archivos físicos (`task.md`, `walkthrough.md`, `ESTANDAR_METODOLOGIA_IA.md`) para que el contexto sea inmutable y recuperable 100%.

---

## 6. USO DE HERRAMIENTAS PARA GARANTIZAR LA AUTONOMÍA REAL

Para asegurar que el bucle de trabajo sea **verdaderamente autónomo** en segundo plano y no interrumpa al usuario exigiendo clics continuos de aprobación (`Submit`) para comandos de terminal:

* **PRIORIDAD ABSOLUTA A HERRAMIENTAS NATIVAS IDE:**
  Para explorar directorios (`list_dir`), buscar código o patrones (`grep_search`), leer archivos (`view_file`), o modificar/crear código fuente (`replace_file_content`, `multi_replace_file_content`, `write_to_file`), el agente **DEBE UTILIZAR SIEMPRE SUS HERRAMIENTAS NATIVAS DE EDICIÓN Y BÚSQUEDA**. Las herramientas nativas operan en segundo plano de forma limpia, segura y sin interrumpir al usuario con diálogos de confirmación de terminal.
* **USO RESTRINGIDO DE LA TERMINAL (`run_command`):**
  La herramienta de terminal (`run_command`) queda reservada **EXCLUSIVAMENTE** para:
  1. Levantar servidores de desarrollo locales (`npm run dev`).
  2. Instalar dependencias necesarias.
  3. Compilar proyectos o generar bundles.
  4. Ejecutar estrictamente los scripts efímeros de validación TDD/matemática autónoma descritos en la Sección 4.
  *(Queda estrictamente prohibido usar la terminal para comandos como `cat`, `grep`, `sed`, `echo` o para escribir/editar código fuente de producción).*

---

## 7. COMPUERTA DE CIERRE DEL BUCLE (REPORT & WALKTHROUGH)

Al terminar con éxito la Fase 2 (cuando todas las tareas cumplan su Criterio de Éxito), el bucle se cierra presentando el informe final al humano en `walkthrough.md`:
* Resumen claro de los cambios implementados y archivos modificados.
* **Demostración Antes vs. Después (*Before & After*)** evidenciando la mejora o corrección.
* Pruebas y validaciones ejecutadas.
* Confirmación de que las reglas universales del curso (ej. no tapar el canvas 3D con carteles emergentes en simulaciones) se cumplen al 100%.

---

**Nota final para Antigravity y futuros agentes:**
Al iniciar cualquier sesión o recibir una orden de gran envergadura (`/goal`), activa de inmediato este esquema: **Planificador Puro (Fase 1) $\rightarrow$ Aprobación $\rightarrow$ Ejecutor en Bucle Verificable (Fase 2) $\rightarrow$ Cierre con Evidencia Antes/Después**.
