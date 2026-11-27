"""Health-check de demos y actualizacion automatica del README.

Lee projects.json (fuente unica), verifica cada demo_url y regenera:
  - El badge global "Demos: N/M online" entre los marcadores DEMOS.
  - La tabla de proyectos entre los marcadores PROJECTS.
Idempotente: solo reescribe README.md si el contenido cambia.
Solo libreria estandar para no requerir pip install en Actions.
"""

import json
import sys
import time
import urllib.request
import urllib.error
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

RAIZ = Path(__file__).resolve().parents[1]
README = RAIZ / "README.md"
PROYECTOS = RAIZ / "projects.json"

TIMEOUT_SEG = 10
ESPERAS = (0, 5, 15, 30)

INICIO_DEMOS = "<!-- DEMOS:AUTO-START -->"
FIN_DEMOS = "<!-- DEMOS:AUTO-END -->"
INICIO_PROYECTOS = "<!-- PROJECTS:AUTO-START -->"
FIN_PROYECTOS = "<!-- PROJECTS:AUTO-END -->"

ESTADOS = {
    "online": "\U0001F7E2 Online",
    "despertando": "\U0001F7E1 Online (despertando)",
    "offline": "\U0001F534 Offline",
    "wip": "\U0001F6A7 En desarrollo",
    "pausada": "\u23F8\uFE0F Demo en pausa",
}


def chequear(url):
    """Devuelve 'online' (1er intento) o 'despertando' (tras reintento)."""
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
            "(KHTML, like Gecko) Chrome/124.0 Safari/537.36"
        )
    }
    for i, espera in enumerate(ESPERAS):
        if espera:
            time.sleep(espera)
        try:
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req, timeout=TIMEOUT_SEG) as resp:
                if resp.status == 200:
                    return "online" if i == 0 else "despertando"
        except (urllib.error.URLError, urllib.error.HTTPError, OSError, ValueError):
            continue
    return "offline"


def evaluar_proyectos(datos):
    resultados = []
    for p in datos["projects"]:
        if p.get("wip"):
            estado = "wip"
        elif p.get("status") == "pausada":
            estado = "pausada"
        elif p.get("demo_url"):
            print(f"Chequeando {p['name']}: {p['demo_url']} ...")
            estado = chequear(p["demo_url"])
        else:
            estado = "offline"
        resultados.append((p, estado))
        print(f"  -> {ESTADOS[estado]}")
    return resultados


def badge_global(resultados):
    activos = [(p, e) for p, e in resultados if e not in ("wip", "pausada")]
    online = sum(1 for _, e in activos if e in ("online", "despertando"))
    total = len(activos)
    if total == 0:
        return ""
    color = "brightgreen" if online == total else ("red" if online == 0 else "yellow")
    texto = f"Demos-{online}%2F{total}%20online-{color}"
    return f"![Demos online](https://img.shields.io/badge/{texto})"


def tabla(resultados):
    lineas = [
        "| Proyecto | Estado | Descripci\u00f3n | Stack | Demo | Repo |",
        "| --- | --- | --- | --- | --- | --- |",
    ]
    for p, estado in resultados:
        nombre = f"{p.get('emoji', '')} **{p['name']}**".strip()
        stack = " \u00b7 ".join(p.get("stack", []))
        demo = f"[Ver \u2197]({p['demo_url']})" if p.get("demo_url") and estado != "pausada" else "\u2014"
        repo = f"[C\u00f3digo \u2197]({p['repo_url']})"
        lineas.append(
            f"| {nombre} | {ESTADOS[estado]} | {p['description']} | {stack} | {demo} | {repo} |"
        )
    return "\n".join(lineas)


def reemplazar_bloque(texto, inicio, fin, contenido):
    try:
        pre, resto = texto.split(inicio, 1)
        _, post = resto.split(fin, 1)
    except ValueError:
        raise SystemExit(f"No se encontraron los marcadores {inicio!r} / {fin!r} en README.md")
    return f"{pre}{inicio}\n{contenido}\n{fin}{post}"


def main():
    datos = json.loads(PROYECTOS.read_text(encoding="utf-8"))
    resultados = evaluar_proyectos(datos)

    original = README.read_text(encoding="utf-8")
    nuevo = reemplazar_bloque(original, INICIO_DEMOS, FIN_DEMOS, badge_global(resultados))
    nuevo = reemplazar_bloque(nuevo, INICIO_PROYECTOS, FIN_PROYECTOS, tabla(resultados))

    if nuevo == original:
        print("Sin cambios en el README.")
        return

    README.write_text(nuevo, encoding="utf-8", newline="\n")
    print("README.md actualizado.")


if __name__ == "__main__":
    sys.exit(main())
