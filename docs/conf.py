import os
import sys
import re
sys.path.append(os.path.abspath("."))

# ──────────────── Projecte ────────────────
project = "Sistemes de Gestió Empresarial"
author = "Juan Bautista Talens"
language = "ca"

# ──────────────── Extensions ────────────────
extensions = [
    "myst_parser",
    "sphinx_copybutton",
    "sphinx.ext.imgconverter",
    "sphinx_design",
    "sphinxcontrib.mermaid",
]

myst_enable_extensions = ["colon_fence", "attrs_block", "deflist"]
myst_heading_anchors = 3

# ──────────────── HTML (triar tema ací) ────────────────
# Pots triar via variable d'entorn: SPHINX_THEME=pydata_sphinx_theme make html
html_theme = os.environ.get("SPHINX_THEME", "sphinx_book_theme")  # "furo" | "sphinx_rtd_theme" | "pydata_sphinx_theme" | "alabaster"
html_title = "Sistemes de Gestió Empresarial"
html_baseurl = "https://juatafe.github.io/2nDAM-SGE/"
html_static_path = ["_static"]
# afegir script JS
html_js_files = [
    "release_control.js",
]
templates_path = ["_templates"]
# Logos i favicon (com ja tenies)
html_logo = "_static/assets/img/logos/logoJust.png"
html_favicon = "_static/assets/img/logos/logo50.ico"

# CSS personalitzat (ordre: general → específic)
html_css_files = [
    "assets/stylesheets/extracsspdf.css",
    "assets/stylesheets/customs.css",
    "assets/stylesheets/extra.css",
]

def slugify(s: str) -> str:
    return re.sub(r"[^A-Za-z0-9]+", "-", s).strip("-").lower()

# Slug del site per al nom del PDF (mateixa lògica que tenies)
_repo = os.environ.get("GITHUB_REPOSITORY", "")
_repo_name = _repo.split("/")[-1] if _repo else ""
site_slug = _repo_name or slugify(project)

# Enllaç relatiu al PDF dins del site (p. ex. pdf/plantilla-sphinx.pdf)
pdf_url = f"pdf/{site_slug}.pdf"

# ──────────────── Opcions per tema (cada tema entén les seues) ────────────────
_book_opts = {
    "logo_only": False,  # mostra nom i logo
    "repository_url": "https://github.com/juatafe/2nDAM-SGE",
    "use_repository_button": True,
    "use_issues_button": True,
    "use_download_button": True,
    "navbar_start": ["jb-header-logos"],
}


_pydata_opts = {
    "show_nav_level": 2,
    "navigation_depth": 4,
    "secondary_sidebar_items": ["page-toc"],#, "sourcelink", "edit-this-page"],
    "use_edit_page_button": True,
    "show_prev_next": True,
    "show_toc_level": 2,
    "navbar_end": ["theme-switcher", "navbar-icon-links"],
    "icon_links": [
        {"name": "GitHub", "url": "https://github.com/juatafe/2nDAM-SGE", "icon": "fa-brands fa-github"},
        {"name": "Issues", "url": "https://github.com/juatafe/2nDAM-SGE", "icon": "fa-solid fa-circle-exclamation"},
        {"name": "PDF", "url": pdf_url, "icon": "fa-solid fa-file-pdf"},
    ],
    # Els teus logos en la navbar només quan el tema és PyData:
    "navbar_start": ["navbar-logo", "jb-header-logos"],
}

_rtd_opts = {
    "collapse_navigation": False,
    "sticky_navigation": True,
    "navigation_depth": 4,
    "includehidden": True,
    "titles_only": False,
}

_furo_opts = {
    # Furo té sidebar per pàgina; no hi ha navbar de toctree com PyData
    "light_logo": html_logo,
    "dark_logo": html_logo,
    "sidebar_hide_name": False,
    # Equivalent a "Edita esta pàgina" en Furo:
    "source_repository": "https://github.com/juatafe/2nDAM-SGE",
    "source_branch": "main",
    "source_directory": "docs/",
}

_alabaster_opts = {
    "logo": html_logo,
    "description": "Documentació",
    "fixed_sidebar": True,
    "page_width": "80%",
    "sidebar_width": "240px",
}

# Aplica les opcions segons el tema triat
if html_theme == "pydata_sphinx_theme":
    html_theme_options = _pydata_opts
elif html_theme == "sphinx_rtd_theme":
    html_theme_options = _rtd_opts
elif html_theme == "furo":
    html_theme_options = _furo_opts
elif html_theme == "alabaster":
    html_theme_options = _alabaster_opts
elif html_theme == "sphinx_book_theme":
    html_theme_options = _book_opts
else:
    html_theme_options = {}

# Afig opció global extra
html_theme_options["navigation_with_keys"] = True

# Context per a botó "Edita a GitHub" (el tenies actiu)
html_context = {
    "github_user": "juatafe",
    "github_repo": "plantilla-sphinx",
    "github_version": "main",
    "doc_path": "docs",
}

# Llengua del buscador
html_search_language = "ca"

# ──────────────── LaTeX/PDF ────────────────
latex_engine = "xelatex"
latex_elements = {
    "fontpkg": r"""
\usepackage{fontspec}
\IfFontExistsTF{TeX Gyre Pagella}{
  \setmainfont{TeX Gyre Pagella}
}{
  \setmainfont{Latin Modern Roman}
}
\IfFontExistsTF{TeX Gyre Heros}{
  \setsansfont{TeX Gyre Heros}
}{
  \setsansfont{Latin Modern Sans}
}
\setmonofont{Latin Modern Mono}
""",
    "preamble": r"""
\usepackage{polyglossia}
\setmainlanguage{catalan}
""",
}
latex_documents = [("index", f"{site_slug}.tex", project, author, "manual")]

# ──────────────── Plantilles personalitzades ────────────────

