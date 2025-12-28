# Tema 8 · Permisos i rols en Odoo

```{toctree}
:maxdepth: 2
:caption: Continguts del Tema 8
:hidden:

practica_tema8_patinatge

```

## Introducció
En este tema deixem de “jugar” i comencem a controlar qui pot fer què dins d’Odoo.  
Si no controles els permisos… acabes amb el soci esborrant dades i la directiva amb cara de 🤨.

Treballarem el tema amb el **cas del club de patinatge**, perquè s’entenga de veritat.

::: {admonition} Objectiu pràctic
:class: tip
Al final del tema sabràs:
- Crear grups d’usuaris (rols).
- Donar permisos reals sobre models amb `ir.model.access.csv`.
- Diferenciar permisos (server) de visibilitat (vistes).
- Aplicar record rules per limitar “quins” registres veu cada grup.
:::

---

## 8.1 Usuaris, grups i permisos (idea clau)
En Odoo:
- Un **usuari** pot pertànyer a **un o més grups**
- Els **permisos** s’assignen als **grups**
- Els permisos s’apliquen **als models**

Permisos bàsics:
- read (llegir)
- write (editar)
- create (crear)
- unlink (esborrar)

Si un usuari **no té permís al model**, el sistema el frena encara que “veja” botons.

::: {admonition} Idea clau
:class: important
El que “es veu” és frontend. El que “es pot fer” és seguretat de servidor.  
La seguretat real sempre va en CSV i record rules, no en les vistes.
:::

---

## 8.2 Estructura de seguretat d’un mòdul

```text
patinatge/
├── models/
├── views/
├── security/
│   ├── security.xml
│   └── ir.model.access.csv
└── __manifest__.py
```

L’ordre importa:
1. Primer **grups**
2. Després **permisos**

::: {admonition} Checklist ràpid
:class: note
- Hi ha grups definits en `security.xml`?  
- El model apareix en `ir.model.access.csv`?  
- El manifest carrega `security.xml` i el CSV?  
:::

---

## 8.3 Creació de grups (`security/security.xml`)
El fitxer `security.xml` defineix els grups d’usuaris. Aquest fitxer és opcional, però molt recomanat: és la base per organitzar rols (directiva, entrenadora, patinadora…) i després assignar-los permisos sobre els models.

Cada grup és un registre del model `res.groups`. La categoria ajuda a ordenar-los en el panell d’administració; no dona permisos per si mateixa.

En aquest exemple s’utilitza `base.module_category_tools`. En projectes grans pots crear una categoria pròpia per mantindre-ho net.

```xml
<odoo>
  <data noupdate="1">

    <record id="group_patinatge_directiva" model="res.groups">
      <field name="name">Directiva</field>
      <field name="category_id" ref="base.module_category_tools"/>
    </record>

    <record id="group_patinatge_entrenadora" model="res.groups">
      <field name="name">Entrenadora</field>
      <field name="category_id" ref="base.module_category_tools"/>
    </record>

    <record id="group_patinatge_patinadora" model="res.groups">
      <field name="name">Patinadora</field>
      <field name="category_id" ref="base.module_category_tools"/>
    </record>

  </data>
</odoo>
```

⚠️ `noupdate="1"` evita que Odoo sobreescriga la seguretat en actualitzacions: conserva personalitzacions fetes per l’administrador.

::: {admonition} Errors comuns
:class: warning
- Crear grups però no incloure `security.xml` al manifest.  
- Pensar que “categoria” dona permisos. No, només ordena.  
:::

---

## 8.4 Permisos de model (`ir.model.access.csv`)
El fitxer `ir.model.access.csv` és obligatori si el mòdul crea models. Si un model no apareix ací, per a l’usuari “no existix”.

Format obligatori:
```csv
id,name,model_id:id,group_id:id,perm_read,perm_write,perm_create,perm_unlink
```

Què significa cada columna:
- `id`: identificador de la regla
- `name`: nom descriptiu
- `model_id:id`: referència al model (ex: `module.model_name`)
- `group_id:id`: grup al qual s’aplica
- `perm_read/write/create/unlink`: 1 sí, 0 no

Exemple real:
```csv
id,name,model_id:id,group_id:id,perm_read,perm_write,perm_create,perm_unlink
access_inscripcio_directiva,inscripcio directiva,model_patinatge_inscripcio,patinatge.group_patinatge_directiva,1,1,1,1
access_inscripcio_entrenadora,inscripcio entrenadora,model_patinatge_inscripcio,patinatge.group_patinatge_entrenadora,1,1,0,0
access_inscripcio_patinadora,inscripcio patinadora,model_patinatge_inscripcio,patinatge.group_patinatge_patinadora,1,0,1,0
```

:::{admonition} 🧠 Traducció clara (i realista)
:class: tip
👑 Administrador → ho veu i ho fa tot (no precisa CSV).  
👩‍💼 Directiva → crear, vore, editar i esborrar.  
👩‍🏫 Entrenadora → vore i editar (sense crear ni esborrar).  
🛼 Patinadora → crear i vore la seua inscripció (sense editar ni esborrar).  
:::

Traducció ràpida:
- La **directiva** ho pot fer tot.
- L’**entrenadora** pot vore i editar.
- La **patinadora** només pot vore (i crear la seua).

::: {admonition} ⚠️ Important
:class: warning
El CSV diu “què es pot fer” sobre el model.  
Les record rules diuen “sobre quins registres” exactament. Sense record rules, un grup amb lectura veu tots els registres del model.
:::

---

## 8.5 Permisos ≠ visibilitat
Regla d’or:

> El CSV controla la **seguretat real**  
> Les vistes només controlen el que **es veu**

Amagar un botó NO és seguretat. La seguretat sempre ha d’estar al servidor.

::: {admonition} Idea clau
:class: tip
Si no tens permís, Odoo et para encara que el botó existisca.  
Si només amagues el botó, un usuari amb API o accés indirecte pot fer l’acció igual.
:::

---

## 8.6 Aplicar grups en vistes i menús
Exemple en una vista:
```xml
<button name="action_esborrar"
        string="Esborrar"
        type="object"
        groups="patinatge.group_patinatge_directiva"/>
```

Exemple en un menú:
```xml
<menuitem id="menu_entrenaments"
          name="Entrenaments"
          groups="patinatge.group_patinatge_entrenadora,patinatge.group_patinatge_directiva"
          action="action_entrenaments"/>
```

::: {admonition} Ús correcte
:class: note
- Les vistes “filtren visibilitat”, no permissions.  
- Combina “groups” en vistes amb el CSV per tindre seguretat real.
:::

---

## 8.7 Regles de registre (record rules)
Les **record rules** controlen **quins registres** veu un usuari dins d’un model. Es defineixen en `ir.rule` i es relacionen amb grups.

Exemple:
- Una patinadora només veu **les seues inscripcions**.
- Una entrenadora veu **les del seu grup**.

Les regles:
- globals → apliquen sempre (resten).
- de grup → s’acumulen segons el grup.

Definició en `security/security.xml`:
```xml
<record id="rule_patinadora_veure_propia_inscripcio" model="ir.rule">
  <field name="name">Patinadora: veure pròpia inscripció</field>
  <field name="model_id" ref="model_patinatge_inscripcio"/>
  <field name="domain_force">[('soci_id', '=', user.partner_id.id)]</field>
</record>
```
Ací filtrem perquè la patinadora només veja inscripcions on `soci_id` coincideix amb el seu partner (`user.partner_id.id`).

::: {admonition} Idea clau
:class: tip
- CSV: “què es pot fer” (read, write, create, unlink).  
- Record rules: “sobre quins registres” exactes (dominis).  
:::

---

## 8.8 Resum final

✔️ Els permisos es defineixen **per grups**  
✔️ El CSV és obligatori  
✔️ Les vistes no són seguretat  
✔️ Sense permisos, Odoo et para

O dit més clar:
> En Odoo no mana qui eres,  
> **mana el grup on estàs**.

I qui no controla els permisos… després plora 😄

::: {admonition} Checklist de tancament
:class: tip
- Grups creats i visibles al backend.  
- CSV amb el model i permisos per cada grup.  
- Vistes amb `groups` per a visibilitat.  
- Record rules aplicades si cal limitar registres.  
:::

::: {admonition} Errors que evitem
:class: warning
- Deixar models sense línies en el CSV.  
- Confiar la seguretat només a les vistes.  
- No carregar `security.xml` al manifest.  
:::
