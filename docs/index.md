Unitat 1. Identificació de sistemes ERP/CRM
===========================================

Introducció a Odoo i als sistemes ERP-CRM
-----------------------------------------

Els sistemes **ERP (Enterprise Resource Planning)** són programes de gestió empresarial integrada.
Són capaços d’unificar en una sola plataforma àrees com la comptabilitat, inventari, vendes, producció,
recursos humans i atenció ciutadana.

👉 En el cas d’una empresa, això ajuda a:

- Evitar duplicitat de dades.
- Reduir errors humans.
- Facilitar la presa de decisions amb dades en temps real.
- Millorar la coordinació entre departaments.

Els ERP poden ser **propietaris** (SAP, Dynamics, Sage) o **lliures** (Odoo, Dolibarr).

Un cas molt interessant és **Odoo**, que destaca per:

- Cost inicial baix (Community gratis, Enterprise amb subscripció).
- Arquitectura modular i escalable.
- Interfície moderna i fàcil d’usar.
- Gran comunitat de desenvolupadors i mòduls.

Per això en aquest mòdul utilitzarem **Odoo Community 16** com a referència.


---

## Exercicis

### 1. Què és la gestió empresarial? Quins objectius té?

::::{dropdown} Solució
:animate: fade-in
:data-release: 2025-09-20

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
:data-release: 2025-09-20

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
:data-release: 2025-09-22

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
:data-release: 2025-09-22

L’arquitectura d’Odoo és **Model–Vista–Controlador (MVC)**.  
- **Model:** Taules PostgreSQL (ORM).  
- **Vista:** Definida amb XML.  
- **Controlador:** Objectes Python que processen peticions i dades.  

El framework **OpenObject** facilita crear i ampliar mòduls seguint MVC.  

::::

---

### 5. Explica les diferents formes d’instal·lar un ERP. Quina utilitzarem nosaltres?

::::{dropdown} Solució
:animate: fade-in
:data-release: 2025-09-29

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
:data-release: 2025-09-29

El **mòdul base** és el conjunt mínim perquè Odoo funcione.  

Inclou:
- **Empreses:** Fitxa de clients.  
- **Administració:** Configuració i funcionalitat bàsica.  

::::

---

### 7. Nomena els tipus de mòduls que podem instal·lar en un ERP i com es relacionen.

::::{dropdown} Solució
:animate: fade-in
:data-release: 2025-10-06

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
:data-release: 2025-10-06

La **localització** configura normativa fiscal, idioma, impostos i documents oficials.  

Exemple: IVA Espanya 21% vs. França 20%. Sense localització correcta, les factures serien errònies.  

::::

---

## Script per retardar la publicació

```{raw} html
<script>
document.addEventListener("DOMContentLoaded", () => {
  const today = new Date();
  document.querySelectorAll("details.dropdown").forEach(el => {
    const release = el.getAttribute("data-release");
    if (release) {
      const rDate = new Date(release);
      if (today < rDate) {
        el.innerHTML = "<p><em>La solució estarà disponible a partir del "
          + rDate.toLocaleDateString() + ".</em></p>";
      }
    }
  });
});
</script>
```

```{toctree}
:maxdepth: 2
:caption: Continguts

situacio
informe
```

