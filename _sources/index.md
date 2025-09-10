# Unitat 1. Identificació de sistemes ERP

## Introducció a Odoo i als sistemes ERP

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
    style A fill=#f9e79f,stroke=#b7950b,stroke-width=2px
    style B fill=#f5b7b1,stroke=#922b21,stroke-width=2px
    style C fill=#d6eaf8,stroke=#2874a6,stroke-width=2px
    style D fill=#d5f5e3,stroke=#1e8449,stroke-width=2px
    style E fill=#d5f5e3,stroke=#1e8449,stroke-width=2px
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

## Exercicis

### 1. Què és la gestió empresarial? Quins objectius té?

::::{dropdown} Solució
:animate: fade-in
<span class="release-date" data-release="2025-09-18"></span>

Podríem definir la **gestió empresarial** com l'habilitat per organitzar, controlar i dirigir
una empresa o organització per assolir els objectius proposats utilitzant diverses estratègies.

**Objectius principals:**
- **Planificació:** Identificar objectiu (què fer, com, quan i on).  
- **Organització:** Indicar qui, quant temps i com realitzarà cada tasca.  
- **Direcció:** Líder influent i responsable que coordini totes les actuacions.  
- **Control:** Supervisió i control d'objectius marcats als diferents departaments.  
- **Dotació de personal:** Contractació de personal adequat.  
- **Coordinació:** Integració i sincronització d’esforços.  

::::

---

### 2. Què entens per ERP i què gestiona en una empresa?  
[Fes un resum de paquets ERP](https://en.wikipedia.org/wiki/List_of_ERP_software_packages).

::::{dropdown} Solució
:animate: fade-in
<span class="release-date" data-release="2025-09-18"></span>

Els **ERP** són sistemes d’informació gerencial que integren i gestionen processos de producció i distribució.  

**Exemples del llistat:**
- **Apache OFBiz:** Java, Javascript, Groovy; llicència Apache 2.0, Open Source.  
- **Kuali:** ERP per institucions d’educació superior; Java; llicència AGPL.  
- **Openbravo:** ERP i punt de venda; Java + PostgreSQL/Oracle; llicència OBPL.  
- **Odoo:** Gestió empresarial modular (CRM, comerç electrònic, facturació...); Python + XML; LGPL per comunitat, Enterprise propietària.  

::::

---

### 3. Què és un CRM?  
[Fes un resum de sistemes CRM](https://en.wikipedia.org/wiki/Comparison_of_CRM_systems).

::::{dropdown} Solució
:animate: fade-in
<span class="release-date" data-release="2025-09-18"></span>

Un **CRM** és un sistema d’informació que ajuda a gestionar la relació amb els clients, amb dues parts:  
- Lògica operacional (tasques).  
- Lògica analítica (explotació de dades).  

**Exemples:**  
- **Capsule CRM** (SaaS, MySQL, Java, Javascript).  
- **SugarCRM** (PHP, multiplataforma, BD: MySQL, SQL Server, Oracle; SaaS o propietari).  
- **Base CRM** (Ruby on Rails, Python; apps mòbils; SaaS).  

::::

---

### 4. Descriu l’arquitectura MVC d’Odoo.

::::{dropdown} Solució
:animate: fade-in
<span class="release-date" data-release="2025-09-10"></span>

L’arquitectura d’Odoo és de tipus **Model–Vista–Controlador (MVC)**.  
Això vol dir que, utilitzant aquest patró de tres components, es pot separar la lògica d’aplicació de la lògica de vista (interfície gràfica) a través d’un controlador.  

Aquesta separació permet modificar o personalitzar parts de l’aplicació sense afectar la resta del sistema.  
El **framework d’Odoo** (anomenat *OpenObject*, de tipus RAD) permet ampliar ràpidament Odoo amb mòduls mitjançant la capa ORM, i facilita diversos components que permeten construir l’aplicació seguint l’arquitectura MVC.  

- **Model:** s’encarrega de les dades (ORM i taules PostgreSQL).  
- **Vista:** representació gràfica (XML).  
- **Controlador:** rep peticions, sol·licita dades al model i les envia a la vista.  


```{mermaid}
flowchart LR
    Controller --> Model
    Controller --> View
    View --> Controller
    Model --> View
    View --> Model

    Model[Model<br/>Dades / ORM]
    View[Vista<br/>XML]
    Controller[Controlador<br/>Python]

```

::::

---

### 5. Explica les diferents formes d’instal·lar un ERP. Quina utilitzarem nosaltres?

::::{dropdown} Solució
:animate: fade-in
<span class="release-date" data-release="2025-09-18"></span>

- Instal·lació en **màquina virtual**.  
- Instal·lació amb **paquets gràfics** (assistents).  
- Instal·lació **personalitzada** des de codi font.  
- **Accés online** (SaaS/demos).  

Nosaltres utilitzarem la **màquina virtual + personalitzada**.  

::::

---

### 6. Què entenem per mòdul base? Quins components en formen part en Odoo?

::::{dropdown} Solució
:animate: fade-in
<span class="release-date" data-release="2025-09-18"></span>

El **mòdul base** és el conjunt mínim perquè Odoo funcione.  

Inclou:
- **Empreses:** Fitxa de clients.  
- **Administració:** Configuració i funcionalitat bàsica.  

::::

---

### 7. Nomena els tipus de mòduls que podem instal·lar en un ERP i com es relacionen.

::::{dropdown} Solució
:animate: fade-in
<span class="release-date" data-release="2025-09-18"></span>

- **Gestió comptable i financera** (integrada amb compres i vendes).  
- **Compres, vendes i magatzem.**  
- **Facturació.**  
- **Gestió de personal (RRHH).**  
- **CRM.**  

Els mòduls estan interconnectats i comparteixen informació.  

::::

---

### 8. Per què és important la localització del país en un ERP?

::::{dropdown} Solució
:animate: fade-in
<span class="release-date" data-release="2025-09-18"></span>

La **localització** configura normativa fiscal, idioma, impostos i documents oficials.  

Exemple: IVA Espanya 21% vs. França 20%. Sense localització correcta, les factures serien errònies.  

::::

---


```{toctree}
:maxdepth: 2
:caption: Continguts

situacio
informe
```

