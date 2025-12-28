# Tema 7 · Creació de frontend en Odoo
```{toctree}
:maxdepth: 2
:caption: Continguts del Tema 7
:hidden:

practica_tema7_patinatge
practica_tema7_inscripcions

```


## 1. Introducció 



## 2. Què és QWeb
QWeb és el motor de plantilles XML utilitzat per Odoo per generar contingut HTML i altres formats. Un motor de plantilles del costat del client, implementat completament en codi JavaScript, que es renderitza dins del navegador. És un sistema lleuger i flexible que permet crear interfícies d'usuari personalitzades i dinàmiques. Serveix per a pintar informació que ve del backend en forma de pàgina web.

🧠 On s’usa QWeb?
- Portal d’usuari (/my)
- Web pública
- Tenda online
- Informes (factures, pressupostos…)

👉 O siga:

> Tot el que Odoo mostra fora del backend, passa per QWeb.

## 3. Què necessitem per a modificar una vista frontend?
Per a crear o modificar una vista frontend en Odoo, necessitem els següents components bàsics:
- Un mòdul d’Odoo
- Un fitxer XML amb una plantilla QWeb que heretarà o crearà la vista.
- Un controlador que gestione les rutes i les dades. Recorda que Odoo utilitza model vista-controlador (MVC). El controlador és l’encarregat de gestionar les rutes i passar les dades a la vista.


Abans de canviar res al frontend, identifica:
- Quin mòdul ho defineix
- Quin template QWeb s’està usant.

Mapa ràpid:
- Portal d’usuari → mòdul `portal` → plantilles tipus `portal.portal_layout`, `portal.portal_my_home`
- Web pública → mòdul `website` → plantilles tipus `website.layout`, `website.page`
- Tenda online → mòdul `website_sale` → plantilles tipus `website_sale.products`, `website_sale.product`


Suposem que volem modificar la pàgina principal del portal d’usuari. Hauríem de buscar la plantilla `portal.my_home` dins del mòdul `portal`. El que fem és heretar aquesta plantilla i modificar-la segons les nostres necessitats sense alterar l’original.

 La següent imatge mostra com es veu la pàgina principal del portal d’usuari per defecte:

```{image} /_static/assets/img/Tema7/vista-front-my.png
:alt: Vista frontend portal d'usuari
:class: img-fluid
:align: center
:width: 80%
```
::: note 
En QWeb, les plantilles s’identifiquen amb l’atribut `id`. Per exemple, en la plantilla `portal.portal_my_home`, `portal` és el nom del mòdul i `my_home` és l’identificador de la plantilla. L'herencia es fa mitjançant l'atribut `inherit_id`. 

`inherit_id="portal.portal_my_home"`indica que estem heretant la plantilla `my_home` del mòdul `portal`.

Exemple:
```xml
<template id="portal_my_home_inherit" inherit_id="portal.portal_my_home">
    ...
</template>
``` 
👉 Açò vol dir:
> Estem creant una nova plantilla anomenada `portal_my_home_inherit` que hereta la plantilla `portal_my_home` del mòdul `portal`.


:::

## 4. Exemple pràctic: Modificar la pàgina principal del portal d’usuari
1. **Identificar la plantilla**: Com hem vist abans, la plantilla que volem modificar és `portal.my_home`.
2. **Crear un mòdul personalitzat**: Si encara no tens un mòdul personalitzat, crea’n un nou per a les teues modificacions.
3. **Crear el fitxer XML**: Dins del teu mòdul, crea un fitxer XML per a la plantilla QWeb. Per exemple, `views/portal_templates.xml`.
4. **Modificar la plantilla**: Afegeix el codi XML per a modificar la plantilla. Per exemple, per a afegir un missatge de benvinguda personalitzat:
```xml
<?xml version="1.0" encoding="UTF-8"?>
<odoo>
    <template id="portal_my_home_inherit" inherit_id="portal.portal_my_home" name="Portal Home - Customizations">
        <xpath expr="//div[hasclass('o_portal_my_home')]/h3" position="replace">
            <h3>Benvingut al teu portal personalitzat!</h3>
        </xpath>
    </template>
</odoo>
```

Anem a desglossar aquest codi:

L’expressió XPath indica **exactament quin element del portal volem modificar**.

```xml
<xpath expr="//div[hasclass('o_portal_my_home')]/h3

```

- `//`  Indica que la cerca es fa **des de qualsevol punt del document XML**, no només des del node arrel immediat.

- `div[hasclass('o_portal_my_home')]`  Selecciona el `<div>` que té la classe CSS `o_portal_my_home`.  La funció `hasclass()` és pròpia de QWeb i serveix per a comprovar si un element conté una classe CSS concreta (molt útil quan un element té diverses classes).

- `/h3`  Selecciona l’element `<h3>` que es troba **dins** d’aquest `<div>`.

Una vegada localitzat l’element, la instrucció:

```xml
position="replace"
```

Indica que **el contingut seleccionat serà reemplaçat completament** pel nou contingut que definim a la plantilla. En aquest cas, l’etiqueta `<h3>` original del portal és substituïda pel nostre missatge de benvinguda personalitzat.

::: note
👉 En resum:  
**busquem un element concret del portal i el substituïm pel nostre**, sense tocar la plantilla original.
:::


1. **Actualitzar el mòdul**: Una vegada hages fet les modificacions, actualitza el teu mòdul per a aplicar els canvis.
2. **Provar els canvis**: Accedeix al portal d’usuari per a veure els canvis aplicats.      
Amb aquests passos, hauràs modificat amb èxit la pàgina principal del portal d’usuari utilitzant QWeb en Odoo com es pot observar en la següent imatge:

```{image} /_static/assets/img/Tema7/vista-front-my-personalitzada.png
:alt: Vista frontend portal d'usuari
:class: img-fluid
:align: center
:width: 80%
```
:::{admonition} Nota
:class: tip
En este exemple no utilitzem controlador perquè no estem creant cap pàgina nova ni cap ruta nova. Només estem modificant una vista que Odoo ja genera i a la qual ja li passen les dades necessàries. El controlador serà necessari quan vulguem mostrar informació pròpia del nostre mòdul o crear pàgines noves. 
:::


Resulta imprescindible conéixer bé l'estructura HTML i les classes CSS que Odoo utilitza en les seves plantilles QWeb per a poder fer modificacions efectives i precises. Això ens permetrà personalitzar l’aspecte i la funcionalitat del frontend segons les necessitats específiques del nostre projecte. A la imatge següent es mostra la vista del portal d’usuari amb l'inspector d'elements del navegador obert, permetent veure l'estructura HTML i les classes CSS associades:

```{image} /_static/assets/img/Tema7/vista-front-my-portal.png
:alt: Vista frontend portal d'usuari
:class: img-fluid
:align: center
:width: 80%
```


# 5. Creem un controlador per a una pàgina nova
En aquest apartat, crearem un controlador senzill per a una pàgina nova en el frontend d’Odoo. Això ens permetrà entendre com funcionen els controladors i com es poden utilitzar per a gestionar rutes i mostrar contingut personalitzat.

Al portal de l’usuari (/my) apareix un enllaç nou anomenat "Pàgina Personalitzada". Quan l’usuari fa clic en aquest enllaç, volem que es mostri una pàgina nova amb un missatge de benvinguda. Quan l’usuari fa clic:

    - Odoo crida un controlador
    - El controlador retorna una plantilla QWeb

Així es veu clar:
👉 vista XML ≠ controlador ≠ ruta web


Primer afegirem el link a la pàgina principal del portal d’usuari. Per a això, heretarem la plantilla `portal.portal_my_home` i afegirem l’enllaç. Ho farem a un fitxer XML dins del nostre mòdul personalitzat, per exemple, `views/portal_templates.xml`:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<odoo>
    <template id="portal_my_home_inherit" inherit_id="portal.portal_my_home" name="Portal Home - Customizations">
        <xpath expr="//div[hasclass('o_portal_my_home')]/h3" position="replace">
            <h3>Benvingut al teu portal personalitzat!</h3>
        </xpath>
        <xpath expr="//div[hasclass('o_portal_my_home')]" position="inside">
            <a href="/my/custom_page" class="btn btn-primary mt-3">Pàgina Personalitzada</a>
        </xpath>
    </template>
</odoo>
``` 
```{image} /_static/assets/img/Tema7/vista-personalitzada-boto.png
:alt: Vista frontend pàgina personalitzada
:class: img-fluid
:align: center
:width: 100%
```

 En fer clic en aquest botó, l’usuari serà redirigit a la ruta `/my/custom_page`. Aquesta ruta serà gestionada pel controlador que crearem a continuació. Com ara no hi ha cap controlador definit per a aquesta ruta, Odoo mostrarà una pàgina d'error 404 com es veu a la imatge següent:
```{image} /_static/assets/img/Tema7/vista-personalitzada-no-bot.png
:alt: Vista frontend pàgina personalitzada no va a cap lloc
:class: img-fluid
:align: center
:width: 80%
```
Ara, crearem el controlador que gestionarà la ruta `/my/custom_page` i retornarà la plantilla QWeb corresponent. El controlador es defineix en un fitxer Python dins del nostre mòdul personalitzat, per exemple, `controllers/main.py`:

## 5.1 Estructura del controlador

Quan el scaffold crea el mòdul, et deixa això:
```bash

├── controllers/
│   ├── __init__.py
│   └── controllers.py
```

El codi que t’ha creat scaffold és només un exemple, no fa res útil per al nostre cas. El podem esborrar quasi tot i quedar-nos amb l’estructura.

```python
# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request

```
Ací simplement importem les classes i mètodes necessaris per a definir el nostre controlador. La classe `http.Controller` és la base per a crear controladors en Odoo, i `request` ens permet accedir a la informació de la sol·licitud HTTP i renderitzar plantilles QWeb.

## 5.2 Definició del controlador del portal
Ara sí: creem un controlador que gestione la ruta /my/custom_page i retorne una plantilla QWeb.

Afegim el codi complet:
```python
# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request


class PatinatgePortal(http.Controller):

    @http.route('/my/custom_page', type='http', auth='user', website=True)
    def custom_page(self, **kwargs):
        return request.render('patinatge.portal_custom_page')
```
Anem a desglossar aquest codi:
- `class PatinatgePortal(http.Controller):`  Definim una nova classe anomenada `PatinatgePortal` que hereta de `http.Controller`. Aquesta classe contindrà els nostres mètodes de controlador.
- `@http.route('/my/custom_page', type='http', auth='user', website=True)`  Aquest és un decorador que defineix una ruta web. Els paràmetres són:
    - `'/my/custom_page'`: La ruta que volem gestionar.
    - `type='http'`: Indica que aquesta ruta és una sol·licitud HTTP normal.
    - `auth='user'`: Indica que l’usuari ha d’estar autenticat per a accedir a aquesta ruta.
    - `website=True`: Indica que aquesta ruta és per al frontend del lloc web.
- `def custom_page(self, **kwargs):`  Definim un mètode anomenat `custom_page` que s’executarà quan un usuari accedisca a la ruta `/my/custom_page`.
- `return request.render('patinatge.portal_custom_page')`  Aquest mètode retorna la renderització d’una plantilla QWeb anomenada `patinatge.portal_custom_page`. Aquesta plantilla serà la que es mostrarà a l’usuari quan accedisca a la ruta. 
- `patinatge` és el nom del nostre mòdul personalitzat i `portal_custom_page` és l’identificador de la plantilla QWeb que crearem a continuació.

## 5.3 Creació de la plantilla QWeb per a la pàgina personalitzada
Ara que tenim el controlador definit, necessitem crear la plantilla QWeb que es mostrarà quan l’usuari accedisca a la ruta `/my/custom_page`. Crearem aquesta plantilla afegint-la al fitxer XML dins del nostre mòdul personalitzat, per exemple, `views/portal_templates.xml`:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<odoo>
    <template id="portal_custom_page" name="Custom Page">
        <t t-call="portal.portal_layout">
            <div class="container mt-5">
                <h1>Pàgina Personalitzada</h1>
                <p>Benvingut a la teua pàgina personalitzada al portal d'usuari!</p>
                <a href="/my" class="btn btn-secondary">
                    Tornar al portal
                </a>
            </div>
        </t>
    </template>
</odoo>
```
Anem a desglossar aquest codi: 
- `<template id="portal_custom_page" name="Custom Page">`  Definim una nova plantilla QWeb amb l’identificador `portal_custom_page` i el nom `Custom Page`.
- `<t t-call="portal.portal_layout">`  Aquesta línia indica que la nostra plantilla utilitzarà el disseny base del portal d’usuari definit en la plantilla `portal.portal_layout`. Això ens permet mantenir la coherència visual amb la resta del portal.
- `<div class="container mt-5">`  Creem un contenidor amb una classe CSS per a afegir marges superiors.
- `<h1>Pàgina Personalitzada</h1>`  Afegim un títol a la pàgina.
- `<p>Benvingut a la teua pàgina personalitzada al portal d'usuari!</p>`  Afegim un paràgraf de benvinguda.
- `<a href="/my" class="btn btn-secondary">Tornar al portal</a>`  Afegim un botó que permet a l’usuari tornar al portal d’usuari.     
- `</t>`  Tanquem la crida al disseny base del portal.
- `</template>`  Tanquem la definició de la plantilla.

Recorda que ara no sols cal actualitzar el mòdul perquè els canvis tinguen efecte, sinó que també has de reiniciar el servidor d’Odoo per a assegurar-te que el nou controlador i la nova plantilla QWeb es carreguen correctament. Sempre que modifiques codi python, és necessari reiniciar el servidor perquè els canvis es reflecteixen.
```{image} /_static/assets/img/Tema7/vista-personalitzada-custom.png
:alt: Vista frontend pàgina personalitzada
:class: img-fluid
:align: center
:width: 100%
``` 
Amb aquests passos, hem creat un controlador senzill que gestiona una ruta nova en el frontend d’Odoo i retorna una plantilla QWeb personalitzada. Això ens permet mostrar contingut específic als usuaris quan accedeixen a aquesta ruta. Queda clar, per tant, com funciona el frontend en Odoo, QWeb defineix què es mostra, el controlador decideix quan i com, i la ruta connecta l’usuari amb la pàgina.