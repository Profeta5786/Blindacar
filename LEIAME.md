# Blindacar / Ojocar

App para condutores em Espanha: radares, avisos da comunidade (polícia, controlos, acidentes, obras), aviso por voz e velocímetro.

## O que há neste repositório

| Pasta | O que é |
|---|---|
| `public/`, `api/`, `vercel.json` | **Blindacar** (Vercel): login Google (Supabase), pagamento único (Stripe), base de dados com RLS. Ver `README.md` para configurar. |
| `prototipo-ojocar/` | **Ojocar**: protótipo web sem login. Radares de toda a Espanha (OpenStreetMap), rotas (OSRM), clima (Open-Meteo), avisos confirmados, eventos no trajeto. |

## Ojocar (protótipo)
- Editar sempre `prototipo-ojocar/src.html`.
- Gerar a versão final: `npm i leaflet@1.9.4 && python3 prototipo-ojocar/build.py` → cria `prototipo-ojocar/index.html` (um só ficheiro, pronto para Netlify/Vercel).
- Avisos da comunidade usam o canal público `ntfy.sh/ojocar-prueba-x7k2q9` (só para testes).

## Próximos passos sugeridos
1. Testar o Ojocar na estrada.
2. Juntar as funções do Ojocar ao Blindacar (login + pagamento + base de dados Supabase em vez do ntfy).
3. Coordenadas reais das cabinas de Pamplona.
