## Guia ràpida

### 1) Desenvolupament en local(no és necessari)
No és necessari treballar en local: la plantilla ja està preparada perquè GitHub compile la documentació i la publique automàticament quan faces push a main.
Si vols treballar i previsualitzar en local abans de publicar, segueix les instruccions indicades:

```bash
# 1) Crear i activar l'entorn virtual
python3 -m venv .venv
source .venv/bin/activate

# 2) Instal·lar dependències (o usa el contenidor del workflow)
pip install -r requirements.txt

# 3) Compilar l'HTML (des de l'arrel del repo)
sphinx-build -b html docs _build/html

# 4) Obrir en el navegador (tria el teu sistema)
xdg-open _build/html/index.html        # Linux
# open _build/html/index.html          # macOS
# start _build/html/index.html         # Windows (PowerShell)
```

### 2) Estructura
```
docs/
  ├─ index.md
  ├─ guia-rapida.md
  ├─ personalitzacio.md
  ├─ duplicar-plantilla.md
  ├─ _static/
  ├─ _templates/
  └─ conf.py
```

### 3) Publicació
Només cal fer *push* a `main`. El workflow compila **HTML** i **PDF** i els puja a `gh-pages`.
Abans, guarda i envia els canvis amb:
```
git add .
git commit -m "Actualització de contingut"
git push
```

<!-- 

```{toctree}
:hidden:
:maxdepth: 2


``` -->