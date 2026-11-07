# Álvaro Benjamín Berrío

<p align="center">
  <strong>Python Developer | Flask · Backend · Web Applications</strong>
</p>

<p align="center">
  Estudiante de Ingeniería de Sistemas · Medellín, Colombia 🇨🇴
</p>

<p align="center">
  Desarrollo aplicaciones web con Python y Flask, integrando bases de datos, APIs, pruebas y herramientas de procesamiento multimedia. Busco una oportunidad como aprendiz de tecnología o desarrollador junior.
</p>

<p align="center">
  <a href="mailto:berriobenjamin16@gmail.com">
    <img src="https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white" alt="Email">
  </a>
  <a href="https://www.linkedin.com/in/alvaro-benjamin-berrio-cabello-56a449434/">
    <img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn">
  </a>
  <a href="https://portfolio-hub-90zb.onrender.com/">
    <img src="https://img.shields.io/badge/Portfolio-000000?style=for-the-badge&logo=githubpages&logoColor=white" alt="Portafolio">
  </a>
</p>

---

## 👨‍💻 Sobre mí

Soy estudiante de Ingeniería de Sistemas y desarrollador enfocado en Python y aplicaciones web con Flask.

Construyo proyectos propios para resolver problemas concretos y fortalecer mis conocimientos en desarrollo de software.

He trabajado en aplicaciones que integran:

- Desarrollo backend con Python y Flask.
- Modelado y gestión de bases de datos relacionales.
- Integración de APIs y servicios externos.
- Interfaces web con JavaScript, HTML y CSS.
- Pruebas automatizadas y validación de funcionalidades.
- Manejo de archivos y procesamiento multimedia.
- Corrección de errores y optimización de aplicaciones.
- Control de versiones y despliegue de aplicaciones.

Me interesa especialmente el desarrollo backend, la automatización, la inteligencia artificial aplicada al software y la seguridad de aplicaciones.

**Actualmente busco mi primera oportunidad profesional** como aprendiz de tecnología, practicante o desarrollador junior en Medellín o modalidad remota.

## 🚀 Proyectos destacados

Mis proyectos son una muestra de mi aprendizaje práctico y de mi capacidad para diseñar, construir, probar y mejorar aplicaciones.

### 1. ReviewTap — Sistema de reseñas con NFC y QR

[![GitHub](https://img.shields.io/badge/Código-GitHub-181717?logo=github)](https://github.com/alvaroberrio23242-eng/reviewtap)

**Estado:** En mantenimiento.

Aplicación web para facilitar que los clientes accedan a páginas de reseñas de negocios mediante códigos QR o dispositivos NFC.

**Características técnicas:**
- Arquitectura Flask con application factory.
- Blueprints y capa de servicios.
- SQLAlchemy.
- PostgreSQL en producción y SQLite en pruebas.
- Sistema multi-negocio.
- Roles de administrador, propietario y personal.
- Control de acceso a recursos.
- Generación y descarga de códigos QR.
- Pruebas automatizadas.

**Mejoras realizadas:**
- Panel de administración de negocios, ubicaciones y dispositivos.
- Validación de permisos para proteger recursos.
- Respuestas 404 para recursos ajenos, evitando revelar su existencia.
- Desarrollo de una batería de 162 pruebas, pendiente de confirmar su vigencia actual.

**Demo:** En mantenimiento por vencimiento de la base de datos gratuita de Render.

`Python` `Flask` `SQLAlchemy` `PostgreSQL` `SQLite` `pytest` `qrcode`

### 2. SalsaQuest — Cultura salsera de Medellín

[![Demo](https://img.shields.io/badge/Demo-En_vivo-16a34a)](https://salsaquest-1.onrender.com/)
[![GitHub](https://img.shields.io/badge/Código-GitHub-181717?logo=github)](https://github.com/alvaroberrio23242-eng/salsaquest)

Aplicación web interactiva para explorar la cultura salsera de Medellín.

**Características:**
- Mapa interactivo.
- Línea del tiempo con 55 hitos.
- Artistas y orquestas.
- Eventos y trivia.
- Información cultural y geográfica.

**Desarrollo:**
- Backend con Flask.
- SQLAlchemy y SQLite.
- JavaScript y Leaflet.
- Rutas separadas por secciones.
- Datos semilla centralizados.
- Fotografías de Wikimedia Commons con licencias libres.

**Mejoras realizadas:**
- Corrección de inserciones repetidas de eventos.
- Prevención de problemas relacionados con bloqueos de SQLite.
- Orden numérico de la línea del tiempo.
- Optimización de videos de fondo, reduciendo su tamaño de aproximadamente 85–105 MB a unos 20 MB.
- Eliminación de código duplicado.

`Python` `Flask` `SQLAlchemy` `SQLite` `JavaScript` `Leaflet`

### 3. OSINT Search Pro — Búsqueda en fuentes abiertas

[![Demo](https://img.shields.io/badge/Demo-En_vivo-16a34a)](https://osint-search-pro.onrender.com/)
[![GitHub](https://img.shields.io/badge/Código-GitHub-181717?logo=github)](https://github.com/alvaroberrio23242-eng/OSINT_Search_Pro)

Aplicación para consultar diferentes motores de búsqueda desde una misma interfaz y construir consultas avanzadas mediante Google Dorks.

**Características:**
- Búsquedas en diferentes motores.
- Constructor de Google Dorks.
- Integración con APIs de búsqueda.
- Datos de respaldo cuando un motor falla.
- Gestión de errores de servicios externos.

**Desarrollo:**
- Backend con Flask.
- Módulos separados por motor.
- Integración con Brave Search y Google Custom Search.
- JavaScript para la interfaz.

**Mejoras y evolución:**
- Manejo de errores para evitar respuestas 500 cuando falla un motor.
- Incorporación de mecanismos de respaldo.
- Trabajo progresivo en validación de entradas, SSRF, limitación de peticiones y cabeceras de seguridad.

`Python` `Flask` `APIs` `JavaScript` `Seguridad web`

### 4. EduPack Builder — Generador de paquetes pedagógicos

[![GitHub](https://img.shields.io/badge/Código-GitHub-181717?logo=github)](https://github.com/alvaroberrio23242-eng/EduPack-Builder)

Herramienta para recopilar recursos educativos de acceso libre y organizarlos en paquetes descargables.

**Características:**
- Búsqueda de imágenes y recursos educativos.
- Recopilación de videos, ensayos y repositorios.
- Generación de archivos ZIP.
- Bibliografía y referencias.
- Vista previa e historial de trabajos.

**Desarrollo:**
- Flask.
- Gestión de trabajos persistidos en disco.
- Reintentos de solicitudes de red.
- Detección de trabajos atascados.
- Verificación de licencias en Wikimedia Commons.
- Validación de imágenes mediante Pillow.

**Mejoras realizadas:**
- Corrección de un problema que generaba ZIP vacíos.
- Validación del tipo de contenido para evitar guardar páginas de error como imágenes.
- Comprobación de archivos mediante Pillow.
- Rediseño de interfaz y barra de progreso.
- Pruebas automatizadas.

`Python` `Flask` `Pillow` `pytest`

### 5. Benja Karaoke — Aplicación web de karaoke

[![Demo](https://img.shields.io/badge/Demo-En_desarrollo-orange)](https://benja-karaoque-api.onrender.com/)
[![GitHub](https://img.shields.io/badge/Código-GitHub-181717?logo=github)](https://github.com/alvaroberrio23242-eng/benja-karaoque)

Proyecto para desarrollar una experiencia de karaoke desde videos y archivos multimedia proporcionados por el usuario.

**Características y desarrollo:**
- Backend con Flask.
- SQLite.
- Integración con FFmpeg.
- Reproductor multimedia.
- Modo escenario.
- Controles de volumen y silencio.
- Navegación dentro de la canción.
- Trabajo en búsqueda y sincronización de letras.

**Estado:** En desarrollo. La separación de voz y la sincronización avanzada de letras requieren validación antes de presentarse como funcionalidades terminadas.

`Python` `Flask` `SQLite` `FFmpeg` `JavaScript`

### 6. LAP Video — Editor y compresor de video

**Estado:** En desarrollo. Repositorio privado.

Herramienta propia para trabajar con edición y compresión de video.

**Tecnologías y herramientas:**
- Python.
- FFmpeg.
- Procesamiento multimedia.
- Interfaz web.

El proyecto busca ofrecer una experiencia de edición multipista y procesamiento de video desde una herramienta propia.

`Python` `FFmpeg` `JavaScript`

### 7. berrio-budget — Gestión de presupuestos

**Estado:** Proyecto propio. Repositorio privado.

Aplicación web desarrollada con Flask para la gestión de presupuestos.

Forma parte de mis proyectos de aprendizaje y desarrollo de aplicaciones orientadas a resolver necesidades prácticas.

`Python` `Flask`

### 8. RockQuest — Historia del rock

[![GitHub](https://img.shields.io/badge/Código-GitHub-181717?logo=github)](https://github.com/alvaroberrio23242-eng/rockquest)

Aplicación web sobre la historia del rock, sus bandas, artistas, décadas, subgéneros, récords y premios.

**Características:**
- Información sobre bandas y artistas.
- Organización por décadas y subgéneros.
- Datos de Grammys y ventas.
- Ruta Rockera con mapa.

**Desarrollo:**
- Flask.
- SQLAlchemy.
- SQLite.
- Arquitectura basada en secciones.
- Reutilización de componentes y patrones de SalsaQuest.

**Mejoras realizadas:**
- Rediseño hacia una experiencia de una sola página.
- Ruta Rockera como portada.
- Unificación del pie de página.
- Script de comprobación de respuestas de rutas principales.

`Python` `Flask` `SQLAlchemy` `SQLite`

### 9. MarketLens AI — Análisis de mercados

[![GitHub](https://img.shields.io/badge/Código-GitHub-181717?logo=github)](https://github.com/alvaroberrio23242-eng/marketlens-ai)

Proyecto enfocado en análisis de mercados financieros.

**Áreas de trabajo:**
- Análisis de riesgo de portafolios.
- Backtesting.
- Visualización de datos.
- Análisis con herramientas de Python.
- IA explicable.

**Tecnologías:**
- Flask.
- pandas.
- NumPy.
- Plotly.
- yfinance.

El proyecto diferencia datos sintéticos y reales para mantener la trazabilidad de los análisis.

`Python` `Flask` `pandas` `NumPy` `Plotly` `yfinance`

### 10. Aventura Antioqueña — Trivia cultural

[![Demo](https://img.shields.io/badge/Demo-En_vivo-16a34a)](https://alvaroberrio23242-eng.github.io/aventura-antioquena-web/)
[![GitHub](https://img.shields.io/badge/Código-GitHub-181717?logo=github)](https://github.com/alvaroberrio23242-eng/aventura-antioquena-web)

Videojuego de trivia con tres niveles y preguntas sobre gastronomía, arquitectura y biodiversidad de Antioquia.

**Desarrollo:**
- Python y Pygame.
- Exportación a WebAssembly mediante pygbag.
- Ejecución en navegador.
- Publicación web.

**Mejoras realizadas:**
- Corrección de datos y preguntas.
- Eliminación de respuestas ambiguas y preguntas repetidas.
- Corrección de errores del personaje y de los cuadros de respuesta.

`Python` `Pygame` `WebAssembly`

## 🧰 Otros proyectos

También he trabajado en:

- **CodeAudit:** auditor estático de repositorios Flask públicos. Repositorio privado.
- **Portfolio Engine:** herramienta de gestión y generación de portafolios.
- **Benja Karaoke:** evolución de reproductor multimedia a karaoke.
- **Ruta Salsera:** proyecto relacionado con la exploración cultural de Medellín.
- **Postre Berraquito:** proyecto de negocio digital para ventas de postres.

Los proyectos privados no tienen enlaces públicos de código.

## 🛠️ Tecnologías y herramientas

### Lenguajes

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat&logo=javascript&logoColor=black)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=flat&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=flat&logo=css3&logoColor=white)

### Backend y bases de datos

![Flask](https://img.shields.io/badge/Flask-000000?style=flat&logo=flask&logoColor=white)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-D71F00?style=flat)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=flat&logo=sqlite&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=flat&logo=postgresql&logoColor=white)

### Herramientas

![Git](https://img.shields.io/badge/Git-F05032?style=flat&logo=git&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat&logo=github&logoColor=white)
![Render](https://img.shields.io/badge/Render-46E3B7?style=flat&logo=render&logoColor=black)
![FFmpeg](https://img.shields.io/badge/FFmpeg-007808?style=flat&logo=ffmpeg&logoColor=white)

### Otras herramientas y tecnologías utilizadas en proyectos

- Leaflet.
- Pillow.
- pytest.
- Pygame.
- WebAssembly.
- pandas.
- NumPy.
- Plotly.
- yfinance.

## 🧭 Cómo trabajo

Mi metodología de desarrollo se basa en un proceso incremental:

1. Identificar el problema y definir el alcance.
2. Diseñar la estructura y arquitectura.
3. Construir una primera versión funcional.
4. Probar las funcionalidades.
5. Corregir errores y validar resultados.
6. Mejorar seguridad, rendimiento y experiencia de usuario.
7. Documentar los cambios.

Procuro trabajar con cambios pequeños, controlados y verificables. No considero terminado un proyecto simplemente porque la aplicación inicia: también es necesario comprobar su comportamiento.

## 🔨 En qué estoy trabajando

Actualmente estoy desarrollando y mejorando:

- **Ruta Salsera:** experiencia cultural interactiva sobre la salsa en Medellín.
- **LAP Video:** editor y compresor de video con FFmpeg.
- **Benja Karaoke:** reproductor multimedia y sincronización de letras.
- **OSINT Search Pro:** mejoras de seguridad e integración de motores de búsqueda.
- **Postre Berraquito:** desarrollo de una solución digital para un negocio de postres.

También estoy explorando aplicaciones de inteligencia artificial, automatización y seguridad en el desarrollo de software.

## 📈 Estadísticas de GitHub

<p align="center">
  <img height="160" src="https://github-readme-stats.vercel.app/api?username=alvaroberrio23242-eng&show_icons=true&theme=dark&hide_border=true" alt="Estadísticas de GitHub">
  <img height="160" src="https://github-readme-stats.vercel.app/api/top-langs/?username=alvaroberrio23242-eng&layout=compact&theme=dark&hide_border=true" alt="Lenguajes más utilizados">
</p>

## 🤝 Contacto profesional

Estoy interesado en oportunidades de aprendizaje y crecimiento profesional en desarrollo de software, especialmente en Python, backend y aplicaciones web.

Si tienes una oportunidad, un proyecto o una propuesta de colaboración, estaré encantado de conversar.

<p align="center">
  <a href="mailto:berriobenjamin16@gmail.com">Email</a> ·
  <a href="https://www.linkedin.com/in/alvaro-benjamin-berrio-cabello-56a449434/">LinkedIn</a> ·
  <a href="https://portfolio-hub-90zb.onrender.com/">Portafolio</a>
</p>

---

<p align="center">
  <i>Construyendo, aprendiendo y mejorando un proyecto a la vez.</i>
</p>
