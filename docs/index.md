# Unitat 1. Identificació de sistemes ERP
## 1. Introducció a la gestió empresarial

La **gestió empresarial** és la ciència social que té per objecte l’estudi de les organitzacions i la tècnica encarregada de la **planificació, organització, direcció i control** dels recursos (humans, financers, materials, tecnològics, coneixement, etc.) d’una organització, per obtenir eficiència o el màxim benefici possible.  

Aquest benefici pot ser **social, econòmic o estratègic**, depenent dels fins perseguits per l’organització. 

---

## Quadre de comandament integral

```{graphviz}
digraph G {
  layout=neato
  overlap=false
  splines=true
  bgcolor="transparent"
  node [shape=box, style=filled, fontname="Helvetica", fontsize=12]

  V [label="Visió i Estratègia", fillcolor="#d6eaf8", color="#2980b9", pos="0,0!"]

  F [label="Financer\nÈxit financer", fillcolor="#abebc6", color="#27ae60", pos="0,2!"]
  P [label="Processos Interns\nEn què hem de sobresortir?", fillcolor="#aed6f1", color="#2874a6", pos="2,0!"]
  A [label="Aprenentatge i Creixement\nCom mantenir la capacitat?", fillcolor="#d7bde2", color="#8e44ad", pos="0,-2!"]
  C [label="Client\nCom hem de ser vistos?", fillcolor="#f5b7b1", color="#922b21", pos="-2,0!"]

  V -> F
  V -> P
  V -> A
  V -> C

  F -> P
  P -> A
  A -> C
  C -> F
}

```


---

## Característiques de l’administració

L’**administració** organitza i coordina els recursos d’un organisme social per aconseguir els seus objectius de manera **eficaç** (arribar al que es proposa) i **eficient** (optimitzar els mitjans).  
Es fonamenta en la **planificació, organització, integració de personal, direcció i control**, i té en la **presa de decisions** el seu nucli fonamental.

---

## Taula comparativa de característiques

| **Característica**       | **Definició / Explicació breu** |
|---------------------------|---------------------------------|
| **Universalitat**         | Present en qualsevol organisme social (empresa, estat, exèrcit, escola, església…). Els elements bàsics són els mateixos encara que hi haja variants. |
| **Especificitat**         | L’administració és un fenomen propi, no es pot confondre amb altres ciències o tècniques. Encara que s’hi recolze, manté la seua identitat. |
| **Unitat temporal**       | És un procés **continu**: planificar, organitzar, dirigir i controlar tenen lloc de manera simultània en la vida de l’empresa. |
| **Unitat jeràrquica**     | Tots els nivells jeràrquics participen de la mateixa funció administrativa, des del gerent general fins a l’últim supervisor. |
| **Valor instrumental**    | No és un fi en si mateixa: és un **mitjà** per assolir els objectius de manera eficient. |
| **Amplitud d’exercici**   | Es pot aplicar a tots els nivells i rols: presidents, gerents, supervisors… fins i tot a la gestió domèstica (ex. una ama de casa). |
| **Interdisciplinarietat** | Integra coneixements d’altres ciències: matemàtiques, estadística, economia, comptabilitat, dret, sociologia, psicologia, filosofia, antropologia, ciència política. |
| **Flexibilitat**          | Els seus principis i tècniques s’adapten a diferents empreses, sectors i contextos socials. |

---

## Diagrama visual de les característiques

```{graphviz}
digraph G {
  layout=circo
  bgcolor="transparent"
  node [shape=box, style=filled, fontname="Helvetica", fontsize=11, fillcolor="#eaf2f8", color="#2980b9"]

  A [label="Administració", fillcolor="#d6eaf8", color="#1f618d"]

  B [label="Universalitat"]
  C [label="Especificitat"]
  D [label="Unitat temporal"]
  E [label="Unitat jeràrquica"]
  F [label="Valor instrumental"]
  G [label="Amplitud d’exercici"]
  H [label="Interdisciplinarietat"]
  I [label="Flexibilitat"]

  A -> {B C D E F G H I}
}

```
---

## 2 Evolució de la informàtica de gestió empresarial

El terme **Sistemes d’Informació (SI)** és genèric i pot tindre diferents significats:

- **En informàtica:** qualsevol sistema o subsistema de telecomunicacions o computació interconnectat per a obtindre, emmagatzemar, manipular, administrar, transmetre o rebre dades i veu. Inclou tant el programari com el maquinari.
- **En teoria de sistemes:** un sistema (manual o automatitzat) format per persones, màquines i mètodes organitzats per a la recol·lecció, processament i transmissió de dades que representen informació per a l’usuari.

---

## Tipus de sistemes d’informació

Segons la funció o l’usuari final (Laudon & Laudon, 2004):

* **TPS (Transaction Processing Systems).** Gestionen la informació de les transaccions d’una empresa.  
* **MIS (Management Information Systems).** Orientats a solucionar problemes generals de gestió.  
* **DSS (Decision Support Systems).** Analitzen variables de negoci per a donar suport a la presa de decisions.  
* **EIS (Executive Information Systems).** Per a directius: monitoren l’estat de les variables internes i externes d’una unitat de l’empresa.  
* **OAS (Office Automation Systems).** Aplicacions per a facilitar el treball diari administratiu.  
* **SE (Sistemes Experts).** Emulen el comportament d’un expert en un domini concret.  
* **ERP (Enterprise Resource Planning).** Integren informació i processos de tota l’organització en un únic sistema.


```{image} /_static/assets/img/Tema1/img2_T1.png
:alt: Tipus de sistemes d'Informació
:width: 65%
:align: center
```
---

## Evolució històrica dels SI en l’empresa

```{image} /_static/assets/img/Tema1/img3_T1.png
:alt: Evolució històrica dels SI
:width: 100%
:align: center
```

---

# Organització d’una empresa i els seus entorns

L’**entorn de l’empresa** està format per tots els elements i factors externs que poden influir en el seu funcionament. Es distingeixen dos tipus:

## Macroentorn
Factors que afecten totes les empreses:  
- Tecnològics  
- Jurídics  
- Demogràfics  
- Socioculturals  
- Econòmics  

```{image} /_static/assets/img/Tema1/img4_T1.png
:alt: Quadre macro i microentorn
:width: 65%
:align: center
```

## Microentorn
Factors que afecten individualment una empresa:  
- Proveïdors  
- Clients  
- Intermediaris  
- Competidors  

---



## 3 Introducció a Odoo i als sistemes ERP

Els **ERP (Enterprise Resource Planning)** són programes de **gestió empresarial integrada**.  
Permeten unificar en una sola plataforma àrees com:

- Comptabilitat  
- Inventari  
- Vendes  
- Producció  
- Recursos humans  
- Atenció ciutadana  

---

### Avantatges dels ERP en una empresa

👉 Un ERP ajuda a:

- Evitar duplicitat de dades  
- Reduir errors humans  
- Facilitar la presa de decisions en temps real  
- Millorar la coordinació entre departaments  

```{mermaid}
flowchart TD
    A[Dades disperses] -->|Sense ERP| B[Errors i duplicitats]
    A -->|Amb ERP| C[Base de dades comuna]
    C --> D[Decisions més ràpides]
    C --> E[Millor coordinació]

    style A fill:#f9e79f,stroke:#b7950b,stroke-width:2px
    style B fill:#f5b7b1,stroke:#922b21,stroke-width:2px
    style C fill:#d6eaf8,stroke:#2874a6,stroke-width:2px
    style D fill:#d5f5e3,stroke:#1e8449,stroke-width:2px
    style E fill:#d5f5e3,stroke:#1e8449,stroke-width:2px
```

---

### Tipus d’ERP

- **Propietaris:** *SAP, Dynamics, Sage*  
- **Lliures:** *Odoo, Dolibarr*  

---

### El cas d’Odoo

Odoo destaca per:

- 💰 **Cost inicial baix** (Community gratis, Enterprise amb subscripció)  
- 🧩 **Arquitectura modular i escalable**  
- 🖥️ **Interfície moderna i fàcil d’usar**  
- 🌍 **Gran comunitat de desenvolupadors i mòduls**  

➡️ En aquest mòdul utilitzarem **Odoo Community 16** com a referència.

---


# Concepte d’ERP (Sistemes de planificació de recursos empresarials)

Un **ERP** és un sistema de planificació creat per reduir temps de resposta, optimitzar la qualitat, millorar la gestió d’actius i reduir costos, integrant processos de negoci de manera unificada.  

Funcionalitats principals:  
- Ordres de compra, facturació, inventari, comptabilitat.  
- Processos modulars i integrats.  
- Universalitat i estandardització.  

```{image} /_static/assets/img/Tema1/img5_T1.png
:alt: Concepte d'ERP
:width: 65%
:align: center
```
## Característiques dels ERP
- **Integrals:** controlen tots els processos i eviten duplicitats.  
- **Modulars:** cada funcionalitat està dividida en mòduls (Vendes, Finances, Magatzem, etc.).  
- **Adaptables:** es configuren segons les necessitats de cada empresa.  

---

## Avantatges i inconvenients
Els ERP ofereixen grans beneficis, però també inconvenients (costos, complexitat, necessitat de formació).  

```
{image} /_static/assets/img/Tema1/img6_T1.png
:alt: Avantatges i inconvenients ERP
:width: 80%
:align: center
```
---

## ERP actuals i llicències

Dins del mercat hi ha ERP **privatius** (SAP, Oracle, Microsoft) i ERP **lliures** (Odoo, Openbravo).  
- **Privatius:** llicència de pagament, orientats a grans empreses.  
- **Lliures:** sense cost de llicència, amb comunitats de desenvolupadors i serveis opcionals.  

```{image} /_static/assets/img/Tema1/img7_T1.png
:alt: ERP actuals i llicències
:width: 60%
:align: center
```
[ERP a la Viquipèdia](https://en.wikipedia.org/wiki/list_of_erp_software_packages)  
[Informe anual del mercat ERP](http://www.gartner.com/technology/home.jsp/)

---

## Exemples d’ERP

### SAP
Suite de programes integrats (finances, producció, logística, recursos humans). Basada en la plataforma NetWeaver.  

### Oracle
Família de productes (JD Edwards, PeopleSoft) amb llarga trajectòria en ERP i bases de dades.  

### Microsoft
**Dynamics ERP** (NAV, AX, GP, SL), orientat a empreses mitjanes i divisions de grans companyies.  

### Openbravo
ERP lliure basat en web, modular i extensible, amb integració amb altres aplicacions lliures.  

### Odoo (antic OpenERP)
ERP lliure i modular, amb una gran comunitat i múltiples mòduls (CRM, projectes, compres, vendes, magatzem, fabricació, comptabilitat…).  

```{image} /_static/assets/img/Tema1/img8_T1.png
:alt: Logo Odoo
:width: 25%
:align: center
```
---

# Concepte de CRM (Gestió de les relacions amb clients)

Els **CRM** donen suport a la gestió de les relacions amb clients, vendes i màrqueting.  
- Part **operacional:** registre i gestió de contactes i activitats.  
- Part **analítica:** anàlisi de dades per a millorar les decisions.  

```{image} /_static/assets/img/Tema1/img9_T1.png
:alt: Concepte de CRM
:width: 80%
:align: center
```

[CRM a la Viquipèdia](http://en.wikipedia.org/wiki/comparison_of_crm_systems)  
[Què és un CRM?](http://es.slideshare.net/alfredovela/qu-es-un-crm-utilidad-y-software)

---

# Arquitectura d’un sistema ERP-CRM

Els ERP actuals integren tots els elements interns i externs d’una empresa, recullen i processen informació i la presenten a diferents nivells.  

Odoo (antic OpenERP) utilitza **OpenObject**, un framework RAD amb arquitectura **MVC** i capa **ORM** sobre PostgreSQL.  

Característiques:  
- ORM que gestiona models i dades.  
- Arquitectura multi-tenant.  
- Workflows i dissenyadors d’informes.  
- Traducció multilingüe.  
- Client web i API XML-RPC/JSON-RPC.  

```{image} /_static/assets/img/Tema1/img10_T1.png
:alt: Arquitectura ERP-CRM
:width: 100%
:align: center
```

```{image} /_static/assets/img/Tema1/img11_T1.png
:alt: Client-Servidor Odoo
:width: 100%
:align: center
```

```{image} /_static/assets/img/Tema1/img12_T1.png
:alt: Components Odoo
:width: 50%
:align: center
```

---

# Tipus de llicències de programari

En el mercat existeixen dos grans grups: **programari privatiu** i **programari lliure**.  
- **Privatiu:** cal pagar llicència i manteniment, les actualitzacions estan garantides pel proveïdor.  
- **Lliure:** sense cost de llicència, però depén de la comunitat per a actualitzacions i correccions.  

Avantatges del programari lliure:  
- Cost zero de llicència i actualitzacions.  
- Gran comunitat i documentació.  
- Varietat d’ERP lliures (Odoo, Openbravo…).  

Openbravo (espanyol): [Web oficial](http://www.openbravo.com/es)  
Odoo (belga): [Web oficial](https://www.odoo.com/es_es/)


---

```{toctree}
:maxdepth: 2
:caption: Tema 1

self
situacio
Exercicis1
```

