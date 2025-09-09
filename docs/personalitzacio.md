# Personalització

El fitxer `conf.py` és el cor del projecte Sphinx. Ací pots configurar el tema, els estils, els logos, les opcions de navegació, i la generació del PDF.

---

## Tema i opcions visuals

El tema utilitzat és **PyData Sphinx Theme**, un tema modern i molt configurable:

```python
html_theme = "pydata_sphinx_theme"
html_theme_options = {
    "show_nav_level": 1,          # Mostra des del nivell 1 del TOC
    "navigation_depth": 4,        # Profunditat màxima del menú lateral
    "collapse_navigation": False, # Evita que es col·lapse automàticament
    "secondary_sidebar_items": ["page-toc", "sourcelink", "edit-this-page"],
    "use_edit_page_button": True,
    "show_prev_next": True,
    "show_toc_level": 2,
    "navbar_end": ["theme-switcher", "navbar-icon-links"],
    "icon_links": [
        {"name": "GitHub", "url": "...", "icon": "fa-brands fa-github"},
        {"name": "Issues", "url": "...", "icon": "fa-solid fa-circle-exclamation"},
        {"name": "PDF", "url": pdf_url, "icon": "fa-solid fa-file-pdf"},
    ],
}
```

---

## Logos i favicon

Es defineixen així dins del bloc HTML:

```python
html_logo = "_static/assets/img/logos/logoJust.png"
html_favicon = "_static/assets/img/logos/logo50.ico"
```

Pots substituir-los per les teues pròpies imatges mantenint la ruta dins de `docs/_static/...`.

---

## Fulls d’estil (CSS)

El paràmetre `html_css_files` permet carregar fulls d’estil personalitzats. L’ordre és important: van del més general al més específic.

```python
html_css_files = [
    "assets/stylesheets/extracsspdf.css",  # estil per a PDF
    "assets/stylesheets/customs.css",      # layout general
    "assets/stylesheets/extra.css",        # modificacions puntuals
]
```

Els fitxers han d’estar dins de `docs/_static/`. Recomanat: crea subcarpetes (`assets/stylesheets/`) per mantindre net el projecte.

---

## Plantilles HTML i rutes

Si necessites modificar la distribució HTML, declara la carpeta de plantilles:

```python
templates_path = ["_templates"]
```

Aquesta ruta conté fitxers `.html` que sobreescriuen parcialment els del tema. Pots personalitzar, per exemple, el layout base, els blocs de la barra lateral o la capçalera.

---

## PDF: títol, fonts i llengua

La generació del PDF via LaTeX es configura amb:

```python
latex_engine = "xelatex"

latex_elements = {
    "fontpkg": r"""
\usepackage{fontspec}
\setmainfont{TeX Gyre Pagella}
\setsansfont{TeX Gyre Heros}
\setmonofont{Latin Modern Mono}
""",
    "preamble": r"""
\usepackage{polyglossia}
\setmainlanguage{catalan}
""",
}
```

Aquest fragment assegura que el PDF utilitza fonts modernes i correcte llengua (valencià/català). Pots substituir les fonts si ho necessites.

---

## PDF: nom fix segons el repositori

El nom del PDF es genera automàticament a partir del repositori GitHub:

```python
_repo = os.environ.get("GITHUB_REPOSITORY", "")
site_slug = _repo.split("/")[-1] if _repo else slugify(project)
pdf_url = f"pdf/{site_slug}.pdf"
```

Això assegura que el fitxer `.pdf` tinga un nom coherent amb el repo (ideal per a repositoris educatius).

<!-- 

```{toctree}
:hidden:
:maxdepth: 2


``` -->