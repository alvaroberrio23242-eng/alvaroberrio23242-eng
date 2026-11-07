<h1 align="center">Álvaro Benjamín Berrío</h1>
<p align="center"><b>Desarrollador Python · Aplicaciones web con Flask</b></p>
<p align="center">Estudiante de Ingeniería de Sistemas en Medellín, Colombia 🇨🇴 · Busco mi primera oportunidad como aprendiz o desarrollador junior (remoto o Medellín)</p>

<p align="center">
  <a href="mailto:berriobenjamin16@gmail.com"><img src="https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white" alt="Email"></a>
  <a href="https://www.linkedin.com/in/alvaro-benjamin-berrio-cabello-56a449434/"><img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn"></a>
  <a href="https://portfolio-hub-90zb.onrender.com/"><img src="https://img.shields.io/badge/Portfolio-000000?style=for-the-badge&logo=githubpages&logoColor=white" alt="Portafolio"></a>
</p>

## 👋 Sobre mí

Construyo aplicaciones web completas con Python y Flask: base de datos, autenticación, pruebas, despliegue y documentación. Trabajo proyecto por proyecto y no doy nada por terminado hasta probarlo.

## 🚀 Proyectos destacados

Cada proyecto indica qué hace, qué problema resuelve, cómo lo construí y qué mejoré en el camino.

> Los demos están en el plan gratuito de Render: si llevan tiempo sin visitas, la primera carga puede tardar hasta un minuto.

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

### 🎤 Benja Karaoke — convierte un video en karaoke

[![Demo](https://img.shields.io/badge/Demo-en_vivo-16a34a)](https://benja-karaoque-api.onrender.com/) [![Código](https://img.shields.io/badge/Código-GitHub-181717?logo=github)](https://github.com/alvaroberrio23242-eng/benja-karaoque)

- **Qué hace:** reproductor de karaoke con modo escenario, salto en la canción, volumen y silencio. El objetivo es separar la voz de un video que sube el usuario.
- **Problema:** hacer un karaoke de cualquier canción exige editar audio a mano.
- **Cómo lo construyo:** Flask + SQLite + ffmpeg, con separación de voz usando Demucs. Solo procesa archivos que sube el usuario, sin descargar de plataformas.
- **Estado:** en desarrollo. Ya publiqué la API en Render y las fases 1 (modo escenario) y 2 (reproductor). Sigue probar la sincronía de letras y la vista en celular.
- **Demuestra:** integración de herramientas de audio y video en una app web.

`Python` `Flask` `SQLite` `ffmpeg` `Demucs` `JavaScript`

---

### 🎸 RockQuest — historia del rock

[![Demo](https://img.shields.io/badge/Demo-PENDIENTE_URL_DEMO-lightgrey)](PENDIENTE_URL_DEMO) [![Código](https://img.shields.io/badge/Código-GitHub-181717?logo=github)](https://github.com/alvaroberrio23242-eng/rockquest)

- **Qué hace:** bandas, artistas, décadas, subgéneros, récords y Grammys, con una Ruta Rockera en mapa.
- **Problema:** comprobar que la arquitectura de SalsaQuest sirve para otro dominio cultural sin empezar de cero.
- **Cómo lo construí:** misma base Flask + SQLAlchemy + SQLite, con un modelo `Banda` (popularidad, Grammys, ventas, influencia) y rutas por sección.
- **Mejoras:** pasé el sitio a una sola página con la Ruta Rockera como portada, unifiqué el pie de página y añadí un script que verifica que las rutas principales respondan 200.
- **Demuestra:** diseño de base de datos relacional y reutilización de arquitectura entre proyectos.

`Python` `Flask` `SQLAlchemy` `SQLite`

---

### ⭐ ReviewTap — reseñas de negocios con NFC y QR

[![Demo](https://img.shields.io/badge/Demo-en_mantenimiento-f59e0b)](#) [![Código](https://img.shields.io/badge/Código-GitHub-181717?logo=github)](https://github.com/alvaroberrio23242-eng/reviewtap)

- **Qué hace:** el cliente escanea un QR o toca un dispositivo NFC y llega a la página de Google para dejar su opinión. El negocio administra ubicaciones y dispositivos desde un panel.
- **Problema:** a los clientes satisfechos les cuesta llegar a dejar una reseña.
- **Cómo lo construí:** Flask con application factory, blueprints y capa de servicios; SQLAlchemy con PostgreSQL en producción y SQLite en pruebas; multi-negocio con roles (admin, dueño, personal). Si alguien pide un recurso que no es suyo, responde 404 en vez de 403 para no revelar que existe.
- **Mejoras:** panel con diálogos para crear y borrar negocios, ubicaciones y dispositivos, descarga de QR y 162 pruebas automáticas.
- **Estado:** el demo está en mantenimiento porque venció la base de datos gratuita de Render.
- **Demuestra:** backend multi-negocio, seguridad de acceso y pruebas automáticas.

`Python` `Flask` `SQLAlchemy` `PostgreSQL` `qrcode` `pytest`

---

### 📊 MarketLens AI — análisis de mercados

[![Demo](https://img.shields.io/badge/Demo-PENDIENTE_URL_DEMO-lightgrey)](PENDIENTE_URL_DEMO) [![Código](https://img.shields.io/badge/Código-GitHub-181717?logo=github)](https://github.com/alvaroberrio23242-eng/marketlens-ai)

- **Qué hace:** análisis de riesgo de portafolio, backtesting e IA explicable.
- **Cómo lo construí:** Python con Flask, pandas, NumPy, Plotly y yfinance. Separa estrictamente los datos sintéticos de los reales para mantener la trazabilidad.
- **Demuestra:** análisis de datos, APIs externas y rigor en trazabilidad.

`Python` `Flask` `pandas` `NumPy` `Plotly` `yfinance`

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

### 📦 EduPack Builder — paquetes pedagógicos con recursos libres

[![Demo](https://img.shields.io/badge/Demo-PENDIENTE_URL_DEMO-lightgrey)](PENDIENTE_URL_DEMO) [![Código](https://img.shields.io/badge/Código-GitHub-181717?logo=github)](https://github.com/alvaroberrio23242-eng/EduPack-Builder)

- **Qué hace:** a partir de un tema, reúne imágenes, videos, ensayos y repositorios con licencia libre y los empaqueta en un ZIP con bibliografía, con vista previa e historial.
- **Problema:** armar material educativo con licencias claras es un trabajo manual.
- **Cómo lo construí:** Flask con trabajos persistidos en disco, detección de trabajos atascados y reintentos de red; las licencias se verifican en Wikimedia Commons (CC-BY, CC0).
- **Mejoras:** corregí un ZIP vacío causado por el orden de los campos de licencia, y las imágenes rotas (páginas de error guardadas como `.jpg`) con validación del tipo de contenido y comprobación con Pillow. Todo con pruebas. Rediseñé la interfaz en tres partes: tipografía y paleta, pantalla de resultados y barra de progreso.
- **Demuestra:** manejo de archivos y licencias, validación de datos y pruebas.

`Python` `Flask` `Pillow` `pytest`

---

### 🕹️ Aventura Antioqueña — trivia sobre Antioquia

[![Demo](https://img.shields.io/badge/Demo-en_vivo-16a34a)](https://alvaroberrio23242-eng.github.io/aventura-antioquena-web/) [![Código](https://img.shields.io/badge/Código-GitHub-181717?logo=github)](https://github.com/alvaroberrio23242-eng/aventura-antioquena-web)

- **Qué hace:** juego de 3 niveles con preguntas de gastronomía, arquitectura y biodiversidad de Antioquia.
- **Problema:** aprender cultura regional de forma entretenida y sin instalar nada.
- **Cómo lo construí:** Pygame, exportado a WebAssembly con pygbag para correr en el navegador, y publicado también en itch.io.
- **Mejoras:** corregí datos de las preguntas (estilo de la Catedral Metropolitana, universidad del campus verde, animal urbano más común), quité respuestas ambiguas y preguntas repetidas, y arreglé errores del personaje y de los cuadros de respuesta.
- **Demuestra:** desarrollo de juegos y despliegue web de apps Python.

`Python` `Pygame` `WebAssembly`

---

**Otros:** [Portafolio](https://portfolio-hub-90zb.onrender.com/) (con demos incrustadas) · CodeAudit (auditor estático de repos Flask públicos, repositorio privado) · LAP Video (editor y compresor de video propio, repositorio privado) · berrio-budget (aplicación web para crear presupuestos, repositorio privado)

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
![Git](https://img.shields.io/badge/Git-F05032?style=flat&logo=git&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat&logo=github&logoColor=white)
![Render](https://img.shields.io/badge/Render-46E3B7?style=flat&logo=render&logoColor=black)

## 🔨 Ahora estoy construyendo

- **Ruta Salsera de Medellín**, dentro de SalsaQuest.
- **LAP Video**, mi propia herramienta para editar y comprimir video.
- **Benja Karaoke**, hacia la separación de voz y la sincronía de letras.
- Explorando IA aplicada al desarrollo de software, automatización y seguridad de aplicaciones.

## 📈 Estadísticas

<p align="center">
  <img height="160" src="https://github-readme-stats.vercel.app/api?username=alvaroberrio23242-eng&show_icons=true&theme=dark&hide_border=true" alt="Estadísticas de GitHub">
  <img height="160" src="https://github-readme-stats.vercel.app/api/top-langs/?username=alvaroberrio23242-eng&layout=compact&theme=dark&hide_border=true" alt="Lenguajes más usados">
</p>

## 🤝 Trabajemos juntos

Busco una posición de **aprendiz o desarrollador junior** en Python, backend o aplicaciones web. Escríbeme por [correo](mailto:berriobenjamin16@gmail.com) o [LinkedIn](https://www.linkedin.com/in/alvaro-benjamin-berrio-cabello-56a449434/).
