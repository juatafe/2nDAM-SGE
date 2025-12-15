# Tema 6 · Creació de vistes en Odoo
```{toctree}
:maxdepth: 2
:caption: Continguts del Tema 6
:hidden:

practica_tema6_patinatge


```


## 1. Introducció · Creació de vistes en Odoo

Fins ara hem treballat la part que **no es veu**, però que és fonamental:  
hem creat el mòdul, els models, les relacions i els permisos. Tot això ja funciona, encara que **encara no ho puguem vore des de la interfície d’usuari**.

És habitual que, en este punt, aparega la pregunta:

> *“Profe, si el model ja està fet… per què no apareix res?”*

La resposta és senzilla: **perquè encara no li hem dit a Odoo com ha de mostrar les dades**.

En el Tema 5 ens han dit que Odoo és capaç de generar **vistes automàtiques** a partir dels models, però també sabem que:
- Sense **menús**, no podem accedir a aquestes vistes, i sense **vistes definides**, l’aspecte és funcional però poc agradable.

En este **Tema 6** començarem a treballar la part visible dels mòduls d’Odoo, com es mostren les dades, com s’organitzen els formularis, i com navega l’usuari dins del mòdul.

Abans de crear vistes personalitzades, el primer pas serà el més bàsic:
**crear un menú** que ens permeta accedir als nostres models.

A partir d’ací, primer observarem què fa Odoo **per defecte** i després començarem a **decidir nosaltres** com han de ser les vistes.

Si fins ara hem muntat el motor, ara toca **posar el volant** 🚗


## 2. Creació del fitxer XML per a menús i vistes
Per a crear menús i vistes personalitzades, cal crear un fitxer XML nou dins de la carpeta `views/` del mòdul. Anomenarem el fitxer `patinatge_menus.xml`. El contingut inicial del fitxer serà el següent:

```xml
<?xml version="1.0" encoding="utf-8"?>
<odoo>

    <!-- Acció de finestra mínima -->
    <record id="action_patinatge_patinadores" model="ir.actions.act_window">
        <field name="name">Patinadores</field>
        <field name="res_model">patinatge.patinadora</field>
        <field name="view_mode">tree,form</field>
    </record>

    <!-- Menú principal -->
    <menuitem id="menu_patinatge_root"
              name="Patinatge"
              sequence="10"/>

    <!-- Submenú amb acció -->
    <menuitem id="menu_patinatge_patinadores"
              name="Patinadores"
              parent="menu_patinatge_root"
              action="action_patinatge_patinadores"/>

</odoo>

```

Aquest fitxer XML conté un menú principal per al mòdul de gestió del club de patinatge. També defineix una acció de finestra que permet accedir al model `patinatge.patinadora` des d’un submenú anomenat "Patinadores". Açò és clau per a que Odoo mostre el menú, si no hi ha una acció associada no mostra res. Per tal que Odoo reconega aquest nou fitxer, cal afegir-lo a la llista de fitxers de dades en el fitxer `__manifest__.py`.

```python
'data': [
        'security/ir.model.access.csv',
        'views/patinatge_menus.xml',

``` 

Amb això, ja podem reiniciar Odoo i actualitzar el mòdul per a vore els canvis. Com es pot observar a la imatge  , ara ja apareix el menú "Patinatge".


```{image} /_static/assets/img/Tema6/menus-Pat.png
:alt: menú Patinatge
:height: 30%
:align: center
```

Al fer clic al menú "Patinatge", Odoo ens mostra la vista de llistat (tree view) per defecte del model `patinatge.patinadora`, encara que sense cap registre, ja que no n’hem creat cap.

```{image} /_static/assets/img/Tema6/vista-Patinadores.png
:alt: Vista Patinadores
:width: 80%
:align: center
```
Si ara fem clic en el botó "Crear", Odoo ens mostra la vista de formulari (form view) per defecte del model `patinatge.patinadora`, on podem introduir les dades d’una nova patinadora.

```{image} /_static/assets/img/Tema6/vista-Crear-Patinadora.png
:alt: Vista Crear Patinadora
:width: 80%
:align: center
``` 


## 3. L’acció `ir.actions.act_window`: què fa i per què és necessària 

Ara anem al detall què és `ir.actions.act_window` i com funciona. Aquest registre defineix una acció que obri una finestra amb una vista específica del model `patinatge.patinadora`. El camp `view_mode` indica que primer es mostrarà la vista de llistat (tree) i després la vista de formulari (form) quan es seleccione un registre. Aquesta acció s’associa al submenú "Patinadores" mitjançant l’atribut `action`, permetent als usuaris accedir fàcilment a la gestió de patinadores des del menú principal del mòdul.    

En Odoo, els **menús no executen accions per si mateixos**.  
Un menú és només un punt d’entrada: allò que realment fa que s’obriga una pantalla és una **acció**.

El tipus d’acció més habitual és `ir.actions.act_window`, que serveix per a **obrir una finestra amb una o diverses vistes d’un model**.

En el nostre cas, hem definit la següent acció:

```xml
<record id="action_patinatge_patinadores" model="ir.actions.act_window">
    <field name="name">Patinadores</field>
    <field name="res_model">patinatge.patinadora</field>
    <field name="view_mode">tree,form</field>
</record>

```
Aquesta acció indica a Odoo què ha de fer quan l’usuari accedeix al submenú "Patinadores":

### 3.1 Camps principals d’una acció de finestra

Anem a analitzar els camps més importants d’aquesta acció.

- `model="ir.actions.act_window"` 
  Indica que estem creant una acció de finestra, és a dir, una acció que obri una vista dins de la interfície web d’Odoo. Aquest tipus d’acció és la base per a llistar registres, crear-ne de nous, editar-los i consultar-los.

- `name`  
  ```xml
  <field name="name">Patinadores</field>
  ```  
  Títol de la finestra que veu l’usuari. No canvia el funcionament, però afecta la claredat i usabilitat.

- `res_model`  
  ```xml
  <field name="res_model">patinatge.patinadora</field>
  ```  
  Model al qual aplica l’acció. Sense aquest camp, Odoo no sap quines dades mostrar.

- `view_mode`  
  ```xml
  <field name="view_mode">tree,form</field>
  ```  
  Orde de les vistes a mostrar. Primer llistat (tree) i, en obrir o crear un registre, formulari (form). Si no hi ha vistes XML pròpies, Odoo generarà vistes automàtiques a partir del model. Ahhaa! 

## 4. Relació entre menú i acció

Una acció per si sola no és visible. Perquè l’usuari la puga executar, cal associar-la a un menú mitjançant l’atribut `action` del `menuitem`:

```xml
<menuitem id="menu_patinatge_patinadores"
          name="Patinadores"
          parent="menu_patinatge_root"
          action="action_patinatge_patinadores"/>
```

Això fa que, en fer clic a Patinatge, Odoo execute l’acció `action_patinatge_patinadores` i òbriga la finestra amb les vistes del model.

## 5. Ús de record i menuitem en fitxers XML

En XML podem definir elements de dues formes:

- Amb `<record>`  
  Per crear o modificar registres de models d’Odoo: accions (`ir.actions.act_window`), vistes (`ir.ui.view`), regles, configuracions… Cada `<field>` correspon a un camp del model indicat.

- Amb `<menuitem>`  
  Drecera específica per crear menús. Encara que semble especial, crea internament un registre de `ir.ui.menu`. Fa el codi més curt, llegible i fàcil de mantindre.

## 6. Situació actual del mòdul

En aquest punt el mòdul té:
- Un menú funcional.
- Una acció de finestra associada.
- Vistes automàtiques (tree i form) generades per Odoo.

Aquestes vistes funcionen però són bàsiques: mostren pocs camps, sense estructura ni disseny específic. En el següent apartat definirem vistes XML pròpies, començant per la vista de llistat (tree) del model `patinatge.patinadora`

:::{admonition} El comandament `scaffold` genera `templates.xml`de moment, NI TOCAR-LO!
:class: warning

```xml
<template id="listing">
...
</template>
```

És un fitxer de plantilles QWeb, portals web, frontend, website... No té res a vore amb les vistes internes(backend) d’Odoo (tree, form, kanban, etc) i no forma part del tema 6.
:::

El fitxer views.xml que crea scaffolf són exemples genèrics que no s’ajusten a les necessitats del nostre mòdul amb models que no existeixen (patinatge.patinantge), camps inventats (value, value2), menús i accions que no quadren amb res. Per això, en els següents apartats crearem vistes XML pròpies per al model `patinatge.patinadora`, començant per la vista de llistat (tree).

:::{admonition} El codi que crea scaffold no és per a usar-lo directament, és només un exemple genèric, una guia visual de les estructures bàsiques que podem definir en XML.
:class: warning
No cal copiar-lo ni utilitzar-lo directament, ja que no s’ajusta a les necessitats del nostre mòdul. En els següents apartats crearem vistes XML pròpies per al model `patinatge.patinadora`, començant per la vista de llistat (tree).
:::

## 7. Crear la vista de llistat (tree) personalitzada
Per a crear una vista de llistat (tree) personalitzada per al model `patinatge.patinadora`, cal afegir un nou registre de tipus `ir.ui.view` en el fitxer XML de vistes del mòdul. El model `ir.ui.view` s’utilitza en Odoo per a definir com es mostren les dades d’un model a la interfície d’usuari. És el mecanisme que permet decidir quins camps es veuen, en quin ordre apareixen, i amb quin tipus de vista (llistat, formulari, etc.).

Dit d’una manera senzilla:
si el model defineix les dades, la vista defineix com es veuen.

 A continuació es mostra un exemple de com definir aquesta vista:

```xml
<?xml version="1.0" encoding="utf-8"?>
<odoo>

    <!-- Vista de llistat (tree) per a patinadores -->
<record id="view_patinadora_tree" model="ir.ui.view">
    <field name="name">patinatge.patinadora.tree</field>
    <field name="model">patinatge.patinadora</field>
    <field name="arch" type="xml">
        <tree>
            <field name="name"/>
            <field name="cognoms"/>
            <field name="grup_id"/>
        </tree>
    </field>
</record>

</odoo>

```

Quan al fitxer XML escrivim:


```xml
<record id="view_patinadora_tree" model="ir.ui.view">
```
Estem creant un nou registre en el model `ir.ui.view`, que defineix una vista específica per al model `patinatge.patinadora`. El record és el registre i ir.ui.view és el model on s’emmagatzemen les vistes.

| Cosa       | Model                   | Registre                         |
| ---------- | ----------------------- | -------------------------------- |
| Patinadora | `patinatge.patinadora`  | Una patinadora concreta          |
| Vista      | `ir.ui.view`            | Una vista concreta (tree, form…) |
| Acció      | `ir.actions.act_window` | Una acció concreta               |
| Menú       | `ir.ui.menu`            | Un menú concret                  |
Dins del registre de la vista, els camps més importants són:   
- `name`  
  ```xml
  <field name="name">patinatge.patinadora.tree</field>
  ```  
  Nom descriptiu de la vista. No afecta el funcionament, però ajuda a identificar-la.
- `model`  
  ```xml
  <field name="model">patinatge.patinadora</field>
  ````  
  Model al qual s’aplica la vista. Sense aquest camp, Odoo no sap quines dades mostrar.
- `arch`  
  ```xml
  <field name="arch" type="xml">
      <tree>
          <field name="name"/>
          <field name="cognoms"/>
          <field name="grup_id"/>
      </tree>
  </field>
  ```  
  Definició XML de l’estructura de la vista. En aquest cas, una vista de llistat (tree) que mostra els camps `name`, `cognoms` i `grup_id` del model `patinatge.patinadora`. L'arquitectura de la vista es defineix dins de l’etiqueta `<arch>`, utilitzant l’estructura XML específica per a vistes d’Odoo. El `<arch>` no defineix dades, només decideix com es mostren les dades del model.

:::{admonition} I no cal tocar l’acció (de moment)
:class: tip

Esta part és clau:

<field name="view_mode">tree,form</field>


👉 No cal modificar-la
👉 Odoo trobarà automàticament la nova vista tree
👉 I després continuarà mostrant el form automàtic

Açò és màgia… però màgia explicable 😏
Odoo fa això:

 - Busca un registre ir.ui.view de tipus tree per a eixe model, si el troba, l’utilitza, si no, crea una vista automàtica.

👉 Per això no cal tocar l’acció.

:::

En Odoo cal tenir un fitxer per cada responsabilitat clara. Així, el fitxer `patinatge_menus.xml` conté menús i accions, mentre que el fitxer `patinatge_patinadora_views.xml` conté les vistes per al model `patinatge.patinadora`. Això facilita la lectura i manteniment del codi.

📦 No oblides el manifest (important!). Com és un fitxer nou, cal afegir-lo al `__manifest__.py`:

```python
'data': [
    'security/ir.model.access.csv',
    'views/patinatge_menus.xml',
    'views/patinatge_patinadora_views.xml',
],
```

Amb això, ja podem reiniciar Odoo i actualitzar el mòdul per a vore els canvis. Ara, quan accedim al menú "Patinadores", Odoo utilitza la nova vista de llistat (tree) que hem definit, mostrant els camps `name`, `cognoms` i `grup_id` en lloc de la vista automàtica generada per defecte.

```{image} /_static/assets/img/Tema6/vista-Patinadores-personalitzada.png
:alt: Vista Patinadores Personalitzada
:width: 80%
:align: center
```

## 8. Crear la vista de formulari (form) personalitzada

Fins ara tenim una vista de llistat (tree) per veure totes les patinadores d’un colp d’ull. Quan volem crear o editar un registre, Odoo usa una vista de formulari (form). La vista automàtica és funcional però plana: mostra tots els camps seguits, sense ordre ni estructura clara. Ara definirem la nostra vista form.

### 8.1 Què és una vista form
Serveix per a mostrar o editar un sol registre d’un model. Permet veure tots els detalls i camps d’una patinadora concreta. És la vista que s’usa per a:   

  - Crear un registre nou,
  - Editar un registre existent,
  - Consultar totes les dades d’un registre concret.

A diferència de la vista tree (molts registres), la form mostra un sol registre amb tots els seus camps.

### 8.2 Definir la vista form amb `ir.ui.view`
Com la vista de llistat, la form es crea amb un registre d’`ir.ui.view` indicant model i arquitectura (`arch`). Afig al fitxer `views/patinatge_patinadora_views.xml`, just davall de la vista tree:

```xml
<!-- Vista de formulari (form) per a patinadores -->
<record id="view_patinadora_form" model="ir.ui.view">
    <field name="name">patinatge.patinadora.form</field>
    <field name="model">patinatge.patinadora</field>
    <field name="arch" type="xml">
        <form>
            <sheet>
                <group>
                    <group>
                        <field name="name"/>
                        <field name="cognoms"/>
                        <field name="data_naixement"/>
                        <field name="dni"/>
                    </group>
                    <group>
                        <field name="telefon"/>
                        <field name="email"/>
                        <field name="adreca"/>
                        <field name="grup_id"/>
                    </group>
                </group>
                <notebook>
                    <page string="Entrenaments">
                        <field name="entrenaments_ids"/>
                    </page>
                </notebook>
            </sheet>
        </form>
    </field>
</record>
```

### 8.3 Explicació de l’estructura del formulari
- `<form>`: definix que és una vista de formulari.  
- `<sheet>`: contenidor principal que aplica disseny i marges correctes; pràcticament tots els forms van dins d’un `sheet`, ja que garanteix una aparença coherent amb la resta del sistema.  
- `<group>`: organitza visualment els camps. Ací usem un grup principal amb dos subgrups per a mostrar dues columnes (més llegible).  
- `<field>`: cada `<field>` correspon a un camp real del model `patinatge.patinadora`. Si el camp no existeix en Python, no es pot usar en la vista.  
- `<notebook>` i `<page>`: amb `<notebook>` es crea el contenidor de pestanyes i amb `<page>` es creen pestanyes. Separem informació principal de la relació amb entrenaments; la pestanya “Entrenaments” mostra `entrenaments_ids` (Many2many).

### 8.4 No cal tocar l’acció (encara)
Mantín:
```xml
<field name="view_mode">tree,form</field>
```
Odoo:
- Buscarà la vista tree definida,
- Buscarà la vista form definida,
- Les usarà en este ordre.
Si no trobés form, mostraria una automàtica. Com que ja la tenim, utilitzarà la nostra.

### 8.5 Resultat final
Ara, en Patinatge → Patinadores veuràs la vista tree personalitzada, i, en Crear o obrir un registre, la vista form personalitzada.

```{image} /_static/assets/img/Tema6/vista-Crear-Patinadora-personalitzada.png
:alt: Vista Crear Patinadora Personalitzada
:width: 80%
:align: center
``` 

A partir d’ara, ja no depens de les vistes automàtiques i pots dissenyar formularis clars i orientats a l’ús real del mòdul.

## 9. Millores en la vista de formulari

Amb el sistema de vistes d’Odoo, les possibilitats de personalització són molt àmplies. Ara que ja tenim una vista de formulari funcional, podem millorar-la afegint detalls com camps obligatoris, camps només de lectura, i reorganitzant la informació per a fer-la més clara i accessible.

::: {admonition} Camps obligatoris i camps només lectura
:class: tip

En una vista de formulari podem indicar que un camp siga obligatori (`required="1"`) o no editable (`readonly="1"`) sense modificar el model Python. Açò només afecta a la interfície, no a la base de dades.

Exemple: fer obligatori el DNI i el grup
```xml
<field name="dni" required="1"/>
<field name="grup_id" required="1"/>
```
Amb això, l’usuari no podrà guardar el registre si no ompli aquests camps i Odoo mostrarà un avís visual.

Exemple: camp només lectura
```xml
<field name="grup_id" readonly="1"/>
```
En aquest cas el camp es mostra, però no es pot modificar des del formulari. Útil quan el camp es calcula automàticament o no volem que l’usuari el canvie manualment.

:::

::: {admonition} Important
:class: tip
`required` i `readonly` en la vista són validacions de UI. Si vols garantir-ho al 100%, declara-ho també en el model Python (p. ex. `required=True`).
:::


## 10. Resum i pròxims passos
En aquest Tema 6 hem après a crear menús i vistes personalitzades en Odoo. Hem vist com definir una acció de finestra (`ir.actions.act_window`) per a obrir vistes específiques d’un model, i com crear vistes de llistat (tree) i formulari (form) amb `ir.ui.view`. Això ens permet controlar completament com es mostren les dades als usuaris, millorant l’experiència i funcionalitat del mòdul.
<!-- En el següent tema, continuarem explorant les possibilitats de personalització de vistes en Odoo, incloent la creació de vistes kanban, calendaris i gràfics, així com l’ús de filtres i grups per a millorar la navegació i gestió de dades. -->
