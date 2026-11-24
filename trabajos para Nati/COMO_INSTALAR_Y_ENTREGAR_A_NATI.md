# 💻 Cómo Entregar e Instalar la Aplicación HTML en el Ordenador del Administrador

Una de las grandes ventajas de una aplicación en **un solo archivo HTML** es que **NO requiere instalación**, no pide permisos de administrador de Windows y no necesita programas adicionales (funciona con Google Chrome o Microsoft Edge, que ya vienen en cualquier PC).

---

## 🚀 Las 3 Formas de Entregársela (De más fácil a más cómoda)

### Opción 1: En un Pendrive o por Correo (100% Offline y Directo) ⭐ (Recomendada para empezar)
1. **Copiar el archivo:** Le pasas el archivo (ej. `Generador_Asistencias.html`) por correo o en un lápiz de memoria USB (Pendrive).
2. **Guardarlo en su PC:** Lo guardas en una carpeta fija, por ejemplo en:
   - `C:\CentroMayores\Generador_Asistencias.html` o en su carpeta de `Documentos`.
3. **Crear un acceso directo en su Escritorio de Windows:**
   - Haces clic derecho sobre el archivo `Generador_Asistencias.html` -> **Enviar a -> Escritorio (crear acceso directo)**.
   - Le cambias el nombre al icono por: **"🖨️ Generador de Asistencias"**.
   - Si quieres dejarlo impecable: Clic derecho en el acceso directo -> *Propiedades* -> *Cambiar icono* (le pones un icono de calendario o impresora).
4. **Uso por parte del Administrador:** Cada fin de mes hace doble clic en el icono de su escritorio, se le abre en Chrome/Edge, elige el mes y pulsa imprimir.

---

### Opción 2: Como Enlace Web / Favorito (Cero Archivos en su PC) ⭐⭐ (La más limpia a futuro)
Si subes ese mismo archivo a un alojamiento gratuito (como **GitHub Pages**):
1. La aplicación tiene una dirección web normal (ej. `centromayores.github.io/asistencias`).
2. Vas a su ordenador, abres Google Chrome, entras en la dirección y la guardas en la **Barra de Marcadores / Favoritos** con una estrella.
3. **Gran ventaja para ti:** Si un día cambian un festivo, o cambia el nombre de un profesor, tú lo corriges en 1 minuto en la nube y a el Administrador se le actualiza automáticamente sin que tengas que ir a su ordenador con un Pen ni pedirle que baje un archivo nuevo.

---

### Opción 3: Aplicación Instalable como "App de Escritorio" (PWA con Chrome/Edge)
Google Chrome y Microsoft Edge tienen una función llamada **"Instalar página como aplicación"**:
1. Abres el archivo HTML en su navegador Chrome o Edge.
2. Pulsas en los tres puntos de arriba a la derecha de Chrome (`...`) -> **Guardar y compartir** -> **Instalar página como aplicación**.
3. Se crea una aplicación independiente con su propia ventana (sin barras de navegación de internet) y su icono en la barra de tareas de Windows, como si fuera un programa de pago instalado.

---

## ⚠️ La Gran Pregunta: ¿Cómo se actualizan los alumnos si cambian de mes a mes?

En un centro de mayores es habitual que un alumno se dé de baja y entre otro de la lista de espera:
- **Solución A (Alumnos fijos en el código):** Si las listas casi no cambian durante el curso, se dejan dentro del HTML y sólo se tocan a principio de curso.
- **Solución B (Importar su propio Excel / CSV):** La aplicación puede tener un botón de *"Subir listado de alumnos"* dondel Administrador arrastra el Excel que ella ya tiene, y el HTML simplemente lo maqueta y le pone las casillas `[S] [N] [J]` y los días del mes automáticamente.
