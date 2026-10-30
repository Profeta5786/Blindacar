"""Gera index.html a partir de src.html, embutindo o Leaflet 1.9.4 (para funcionar sem CDN).
Uso: npm i leaflet@1.9.4 && python3 build.py"""
from pathlib import Path
here = Path(__file__).parent
lf = here.parent / "node_modules" / "leaflet" / "dist"
if not lf.exists():
    lf = here / "node_modules" / "leaflet" / "dist"
s = (here / "src.html").read_text()
s = s.replace("<!--LEAFLET_CSS-->", "<style>" + (lf / "leaflet.css").read_text() + "</style>")
s = s.replace("<script>/*LEAFLET_JS*/</script>", "<script>" + (lf / "leaflet.js").read_text().replace("</script", "<\\/script") + "</script>")
(here / "index.html").write_text(s)
print("index.html gerado")
