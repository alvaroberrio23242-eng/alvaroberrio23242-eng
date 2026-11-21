<h1 align="center">Álvaro Benjamín Berrío</h1>
<p align="center"><b>Desarrollador Python · Aplicaciones web con Flask</b></p>
<p align="center">Estudiante de Ingeniería de Sistemas en Medellín, Colombia · Busco mi primera oportunidad como aprendiz o desarrollador junior (remoto o Medellín)</p>

<p align="center">
  <a href="mailto:berriobenjamin16@gmail.com"><img src="https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white" alt="Email"></a>
  <a href="https://www.linkedin.com/in/alvaro-benjamin-berrio-cabello-56a449434/"><img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn"></a>
  <a href="https://portfolio-hub-90zb.onrender.com/"><img src="https://img.shields.io/badge/Portafolio-000000?style=for-the-badge&logo=githubpages&logoColor=white" alt="Portafolio"></a>
</p>

## 👋 Sobre mí

Construyo aplicaciones web completas con Python y Flask: base de datos, pruebas, despliegue y documentación. Trabajo proyecto por proyecto y no doy nada por terminado hasta probarlo.

## ⚡ Resumen rápido

| Proyecto | Qué es | Stack | Demo |
|---|---|---|---|
| **SalsaQuest** | Cultura salsera de Medellín: mapa, línea del tiempo y trivia | Flask, SQLAlchemy, Leaflet | [Abrir](https://salsaquest-1.onrender.com/) |
| **CodeAudit** | Auditor de seguridad estático para repos Flask | Python, AST, API de GitHub | [Abrir](https://codeaudit-zxc5.onrender.com) |
| **EduPack Builder** | Paquetes educativos con recursos de licencia libre | Flask, Pillow, pytest | [Abrir](https://edupack-builder.onrender.com) |
| **OSINT Search Pro** | Búsqueda en varios motores y Google Dorks | Flask, APIs de búsqueda | [Abrir](https://osint-search-pro.onrender.com/) |
| **RockQuest** | Historia del rock con Ruta Rockera en mapa | Flask, SQLAlchemy | [Abrir](https://rockquest.onrender.com/) |
| **LAP Video** | Editor y compresor de video con línea de tiempo | Flask, FFmpeg | [Abrir](https://lap-video.onrender.com/) |
| **Berrío Budget** | Presupuestos en COP con cálculo en servidor | Flask, pytest | [Abrir](https://berrio-budget.vercel.app/) |
| **Aventura Antioqueña** | Trivia sobre Antioquia en el navegador | Pygame, WebAssembly | [Jugar](https://alvaroberrio23242-eng.github.io/aventura-antioquena-web/) |
| **Benja Karaoke** | Karaoke web con letras sincronizadas | Flask, JavaScript | [Abrir](https://alvaroberrio23242-eng.github.io/benja-karaoque/karaoke.html) |

> Los demos están en planes gratuitos: si llevan tiempo sin visitas, la primera carga puede tardar hasta un minuto.

## 🚀 Proyectos destacados

Cada proyecto indica qué hace, qué problema resuelve, cómo lo construí y qué mejoré en el camino.

---

### 🎵 SalsaQuest — la cultura salsera de Medellín, explorable

[![Demo](https://img.shields.io/badge/Demo-en_vivo-16a34a)](https://salsaquest-1.onrender.com/) [![Código](https://img.shields.io/badge/Código-GitHub-181717?logo=github)](https://github.com/alvaroberrio23242-eng/salsaquest)

- **Qué hace:** mapa interactivo, línea del tiempo de la salsa (55 hitos), artistas, orquestas, eventos y trivia. Pensada para turistas que visitan lugares como Son Havana.
- **Problema:** la historia y los lugares de la salsa están dispersos; no había una experiencia única para recorrerlos.
- **Cómo lo construí:** Flask + SQLAlchemy + SQLite en el backend, rutas separadas por sección, datos semilla en una sola fuente y JavaScript con Leaflet en el frontend. Las fotos salen de Wikimedia Commons con licencias libres.
- **Mejoras:** corregí un bug que reinsertaba los eventos en cada visita (riesgo de `database is locked`), el orden de la línea del tiempo pasó a numérico, los videos de fondo bajaron de ~85-105 MB a ~20 MB y eliminé código duplicado.
- **Demuestra:** modelado de datos, frontend interactivo, manejo de fuentes.

`Python` `Flask` `SQLAlchemy` `SQLite` `JavaScript` `Leaflet`

---

### 🛡️ CodeAudit — auditor estático de repositorios Python/Flask

[![Demo](https://img.shields.io/badge/Demo-en_vivo-16a34a)](https://codeaudit-zxc5.onrender.com) ![Repositorio](https://img.shields.io/badge/Repositorio-privado-lightgrey)

- **Qué hace:** recibe la URL de un repo público de GitHub y genera un reporte de seguridad y calidad. Detecta secretos hardcodeados, SQL por concatenación, inyección de comandos y de plantillas, deserialización insegura, SSRF, path traversal, endpoints huérfanos, imports rotos y configuración débil.
- **Problema:** revisar a mano la seguridad de un proyecto Flask es lento y se olvidan errores comunes.
- **Cómo lo construí:** análisis 100 % estático (regex y AST) en un subproceso aislado, sin ejecutar nunca el código auditado. Incluye límite de peticiones por IP, caché por commit y una rúbrica de severidades A–F. Usa la API de GitHub.
- **Demuestra:** seguridad de aplicaciones, análisis estático y diseño defensivo.

`Python` `Flask` `AST` `API de GitHub`

---

### 📦 EduPack Builder — paquetes pedagógicos con recursos libres

[![Demo](https://img.shields.io/badge/Demo-en_vivo-16a34a)](https://edupack-builder.onrender.com) [![Código](https://img.shields.io/badge/Código-GitHub-181717?logo=github)](https://github.com/alvaroberrio23242-eng/EduPack-Builder)

- **Qué hace:** a partir de un tema, reúne imágenes, videos, ensayos y repositorios con licencia libre y los empaqueta en un ZIP con bibliografía, con vista previa e historial.
- **Problema:** armar material educativo con licencias claras es un trabajo manual.
- **Cómo lo construí:** Flask con trabajos persistidos en disco, detección de trabajos atascados y reintentos de red; las licencias se verifican en Wikimedia Commons (CC-BY, CC0).
- **Mejoras:** corregí un ZIP vacío causado por el orden de los campos de licencia, y las imágenes rotas (páginas de error guardadas como `.jpg`) con validación del tipo de contenido y comprobación con Pillow. Todo con pruebas. Rediseñé la interfaz en tres partes: tipografía y paleta, pantalla de resultados y barra de progreso.
- **Demuestra:** manejo de archivos y licencias, validación de datos y pruebas.

`Python` `Flask` `Pillow` `pytest`

---

### 🔎 OSINT Search Pro — búsqueda en fuentes abiertas

[![Demo](https://img.shields.io/badge/Demo-en_vivo-16a34a)](https://osint-search-pro.onrender.com/) [![Código](https://img.shields.io/badge/Código-GitHub-181717?logo=github)](https://github.com/alvaroberrio23242-eng/OSINT_Search_Pro)

- **Qué hace:** busca en varios motores a la vez e incluye un constructor de Google Dorks que arma la consulta y abre la búsqueda real.
- **Problema:** consultar cada motor por separado es lento, y desde servidores en la nube los motores bloquean el scraping.
- **Cómo lo construí:** Flask con un módulo por motor y datos de muestra como respaldo cuando uno falla. Añadí integración con las APIs oficiales de Brave Search y Google Custom Search, con respaldo al scraping si no hay clave.
- **Mejoras:** un bloqueo de un motor ya no produce un error 500 sino un aviso. Siguiente paso: endurecer la seguridad (SSRF, límite de peticiones, cabeceras y validación).
- **Demuestra:** integración de APIs externas y manejo de errores.

`Python` `Flask` `APIs de búsqueda` `JavaScript`

---

### 🎸 RockQuest — historia del rock

[![Demo](https://img.shields.io/badge/Demo-en_vivo-16a34a)](https://rockquest.onrender.com/) [![Código](https://img.shields.io/badge/Código-GitHub-181717?logo=github)](https://github.com/alvaroberrio23242-eng/rockquest)

- **Qué hace:** bandas, artistas, décadas, subgéneros, récords y Grammys, con una Ruta Rockera en mapa.
- **Problema:** comprobar que la arquitectura de SalsaQuest sirve para otro dominio cultural sin empezar de cero.
- **Cómo lo construí:** misma base Flask + SQLAlchemy + SQLite, con un modelo `Banda` (popularidad, Grammys, ventas, influencia) y rutas por sección.
- **Mejoras:** pasé el sitio a una sola página con la Ruta Rockera como portada, unifiqué el pie de página y añadí un script que verifica que las rutas principales respondan 200.
- **Demuestra:** diseño de base de datos relacional y reutilización de arquitectura entre proyectos.

`Python` `Flask` `SQLAlchemy` `SQLite`

---

### 🎬 LAP Video — editor y compresor de video

[![Demo](https://img.shields.io/badge/Demo-en_vivo-16a34a)](https://lap-video.onrender.com/)

- **Qué hace:** editor web con línea de tiempo de varias pistas, vista previa en vivo, recorte, velocidad y ajustes de color. Exporta cambiando resolución, FPS y calidad, o comprimiendo a un tamaño objetivo en MB.
- **Problema:** editar y comprimir un video suele exigir programas pesados o servicios externos.
- **Cómo lo construí:** backend Flask con un procesador FFmpeg en segundo plano que usa cola, barra de progreso y cancelación, sin bloquear la interfaz. Cubierto por 45 pruebas automáticas.
- **Demuestra:** procesamiento en segundo plano, integración con FFmpeg y pruebas.

`Python` `Flask` `FFmpeg` `JavaScript` `pytest`

---

### 🧾 Berrío Budget — presupuestos en pesos colombianos

[![Demo](https://img.shields.io/badge/Demo-en_vivo-16a34a)](https://berrio-budget.vercel.app/)

- **Qué hace:** organiza productos, servicios y conceptos, registra cantidades y precios unitarios, y calcula subtotales y el total en COP (hasta 100 conceptos por presupuesto).
- **Cómo lo construí:** cálculo y validación en el servidor con Flask, con pruebas automatizadas del backend.
- **Demuestra:** validación de datos y lógica en el servidor.

`Python` `Flask` `JavaScript` `pytest`

---

### 🕹️ Aventura Antioqueña — trivia sobre Antioquia

[![Demo](https://img.shields.io/badge/Demo-jugar-16a34a)](https://alvaroberrio23242-eng.github.io/aventura-antioquena-web/) [![Código](https://img.shields.io/badge/Código-GitHub-181717?logo=github)](https://github.com/alvaroberrio23242-eng/aventura-antioquena-web) [![itch.io](https://img.shields.io/badge/itch.io-FA5C5C?logo=itchdotio&logoColor=white)](https://alvaroberrio23242-eng.itch.io/aventura-antioquea)

- **Qué hace:** juego de 3 niveles con preguntas de gastronomía, arquitectura y biodiversidad de Antioquia.
- **Problema:** aprender cultura regional de forma entretenida y sin instalar nada.
- **Cómo lo construí:** Pygame, exportado a WebAssembly con pygbag para correr en el navegador, y publicado también en itch.io.
- **Mejoras:** corregí datos de las preguntas, quité respuestas ambiguas y preguntas repetidas, y arreglé errores del personaje y de los cuadros de respuesta.
- **Demuestra:** desarrollo de juegos y despliegue web de apps Python.

`Python` `Pygame` `WebAssembly`

---

### 🎤 Benja Karaoke — karaoke web (en desarrollo)

[![Demo](https://img.shields.io/badge/Demo-en_vivo-16a34a)](https://alvaroberrio23242-eng.github.io/benja-karaoque/karaoke.html) [![Código](https://img.shields.io/badge/Código-GitHub-181717?logo=github)](https://github.com/alvaroberrio23242-eng/benja-karaoque)

- **Qué hace:** reproduce audio local con letras sincronizadas por marcas de tiempo, modo escenario, volumen y atajos de teclado.
- **Problema:** hacer un karaoke de cualquier canción exige editar audio a mano.
- **Cómo lo construyo:** interfaz en JavaScript y una API Flask desplegada en Render. Si la API no responde, la reproducción local sigue funcionando.
- **Estado:** en desarrollo. Siguiente paso: separar la voz de un video que suba el usuario.
- **Demuestra:** diseño de interfaz, tolerancia a fallos y pruebas.

`Python` `Flask` `JavaScript` `pytest`

---

**Más trabajo:** [Portafolio completo](https://portfolio-hub-90zb.onrender.com/) con demos incrustadas.

## 🧭 Cómo trabajo

Defino el alcance → diseño la arquitectura → construyo un MVP → refino la experiencia → añado funciones avanzadas → optimizo (pruebas, seguridad, rendimiento) → documento. Pruebo antes de dar algo por terminado y hago cambios pequeños y controlados.

## 🛠️ Tecnologías

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=flat&logo=flask&logoColor=white)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-D71F00?style=flat)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat&logo=javascript&logoColor=black)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=flat&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=flat&logo=css3&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=flat&logo=sqlite&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=flat&logo=postgresql&logoColor=white)
![pytest](https://img.shields.io/badge/pytest-0A9EDC?style=flat&logo=pytest&logoColor=white)
![FFmpeg](https://img.shields.io/badge/FFmpeg-007808?style=flat&logo=ffmpeg&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?style=flat&logo=git&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat&logo=github&logoColor=white)
![Render](https://img.shields.io/badge/Render-46E3B7?style=flat&logo=render&logoColor=black)

## 🔨 Ahora estoy construyendo

- **Ruta Salsera de Medellín**, dentro de SalsaQuest.
- **Benja Karaoke**, hacia la separación de voz y la sincronía de letras.
- Explorando IA aplicada al desarrollo de software, automatización y seguridad de aplicaciones.

## 🤝 Trabajemos juntos

Busco una posición de **aprendiz o desarrollador junior** en Python, backend o aplicaciones web.

📧 [berriobenjamin16@gmail.com](mailto:berriobenjamin16@gmail.com) · 💼 [LinkedIn](https://www.linkedin.com/in/alvaro-benjamin-berrio-cabello-56a449434/) · 🌐 [Portafolio](https://portfolio-hub-90zb.onrender.com/)
