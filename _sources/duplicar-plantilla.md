# Duplicar la plantilla amb l'script

Este script automatitza la creació d’un nou repositori Sphinx:

- Clona l’origen (per defecte, la plantilla oficial),
- Reescriu títols i URL en `conf.py`,
- Ajusta el nom del PDF al workflow,
- Crea el repo a GitHub i activa GitHub Pages (`gh-pages`).

<!-- ```{admonition} Requisits per als botons
Per a que funcionen els botons “Clona la plantilla”, “Descarrega l’script” i “Descarrega el PDF”, has de tindre activada l’extensió `sphinx_design` a `conf.py`:

    extensions = [
        "myst_parser",
        "sphinx_design",
    ]
``` -->

---

## Ús
Per a duplicar la plantilla, executa el següent comandament des de la carpeta del projecte:
``` bash
./scripts/nou_sphinx_repo.sh NOU_REPO "Títol nou" UsuariGitHub [ORIGEN] [NomPDF.pdf]
```

### Paràmetres
- `NOU_REPO`: nom curt del nou repositori GitHub.
- `"Títol nou"`: títol que apareixerà al lloc web generat.
- `UsuariGitHub`: nom d’usuari o organització on es crearà el repo.
- `[ORIGEN]` *(opcional)*: URL del repo base (per defecte, la plantilla).
- `[NomPDF.pdf]` *(opcional)*: nom fix per al PDF generat.

---

### Exemples

``` bash
# Clonar la plantilla bàsica
./scripts/nou_sphinx_repo.sh plantilla-sphinx "Repo de plantilla sphinx" juatafe

# Clonar un repositori diferent i fixar nom del PDF
./scripts/nou_sphinx_repo.sh apunts-xarxes "Apunts de Xarxes" juatafe https://github.com/juatafe/sge.git ApuntsDeXarxes.pdf
```

---

## Publicació

Una vegada creat el repo, només cal afegir canvis i pujar-los:

``` bash
git add .
git commit -m "Primera personalització"
git push origin main
```

GitHub compilarà automàticament **HTML + PDF** i publicarà el lloc a:

```
https://<usuari>.github.io/<repo>
```

---
<!-- 
## 📂 Accions ràpides

```{button-link} https://github.com/juatafe/plantilla-sphinx.git
:color: primary
:shadow:
:expand:
Clona la plantilla a GitHub
```

```{button-link} https://raw.githubusercontent.com/juatafe/plantilla-sphinx/main/scripts/nou_sphinx_repo.sh
:color: success
:shadow:
:expand:
Descarrega l’script
```

```{button-link} ../pdf/plantilla-sphinx.pdf
:color: warning
:shadow:
:expand:
Descarrega el PDF generat
```

---

## Descarrega local de l’script

Si tens l’script dins del projecte (`docs/scripts/`), pots afegir:

```{download}`Descarrega l’script nou_sphinx_repo.sh <scripts/nou_sphinx_repo.sh>`
```

```{note}
El rol `{download}` només funciona si el fitxer està dins de la carpeta *source* (`docs/`).  
Si el tens fora, usa el botó de dalt.
```

---

## 🧭 Per què no veig la barra lateral?

Perquè esta pàgina tinga “Navegació de la Secció”:

1. Ha d’estar inclosa en una `toctree` (p. ex., a `index.md`).
2. El `:maxdepth:` ha de ser almenys 1 o 2.
3. I no amagues `.sidebar-primary-items` amb CSS si no vols! -->


<!-- 

```{toctree}
:hidden:
:maxdepth: 2


``` -->