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
:data-release: 2025-09-15

La gestió empresarial és l’habilitat per organitzar, controlar i dirigir una empresa o
organització per assolir els objectius proposats.  
**Objectius principals:**
- Planificació
- Organització
- Direcció
- Control
- Dotació de personal
- Coordinació

::::

---

### 2. Què entens per ERP i què gestiona en una empresa?  
[Fes un resum de paquets ERP](https://en.wikipedia.org/wiki/List_of_ERP_software_packages).

::::{dropdown} Solució
:animate: fade-in
:data-release: 2025-09-15

Un ERP integra processos empresarials (producció, vendes, distribució, compres, finances).  

**Exemples destacats:**
- Apache OFBiz (Java, open source, llicència Apache 2.0).  
- Kuali (educació superior, llicència AGPL).  
- Openbravo (Java + PostgreSQL, punt de venda).  
- Odoo (Python, modular, comunitari LGPL i enterprise propietària).

::::

---

### 3. Què és un CRM?  
[Fes un resum de sistemes CRM](https://en.wikipedia.org/wiki/Comparison_of_CRM_systems).

::::{dropdown} Solució
:animate: fade-in
:data-release: 2025-09-22

Un CRM és un sistema per gestionar la relació amb els clients.  
**Exemples:**  
- Capsule CRM (SaaS, Java, MySQL).  
- SugarCRM (PHP, multiplataforma, BD variades).  
- Base CRM (Ruby on Rails, apps mòbils, MySQL).

::::

---

### 4. Descriu l’arquitectura MVC d’Odoo.

::::{dropdown} Solució
:animate: fade-in
:data-release: 2025-09-22

Odoo utilitza l’arquitectura **Model–Vista–Controlador**:  
- **Model:** dades en taules PostgreSQL (ORM).  
- **Vista:** interfície definida amb XML.  
- **Controlador:** objectes en Python que gestionen la lògica.

::::

---

### 5. Explica les diferents formes d’instal·lar un ERP. Quina utilitzarem nosaltres?

::::{dropdown} Solució
:animate: fade-in
:data-release: 2025-09-29

- Instal·lació en màquina virtual.  
- Instal·lació amb paquets gràfics.  
- Instal·lació personalitzada des de codi font.  
- Accés online (SaaS).  

Nosaltres treballarem amb **màquina virtual + personalitzada**.

::::

---

### 6. Què entenem per mòdul base? Quins components en formen part en Odoo?

::::{dropdown} Solució
:animate: fade-in
:data-release: 2025-09-29

El mòdul base és el conjunt mínim per a què funcione Odoo.  
Inclou:  
- Mòdul **Empreses** (fitxes de clients).  
- Mòdul **Administració** (seguretat i configuració bàsica).

::::

---

### 7. Nomena els tipus de mòduls que podem instal·lar en un ERP i com es relacionen.

::::{dropdown} Solució
:animate: fade-in
:data-release: 2025-10-06

- **Comptabilitat i finances** (integrat amb compres i vendes).  
- **Compres, vendes i magatzem**.  
- **Facturació**.  
- **Gestió de personal (RRHH)**.  
- **CRM**.  

Tots estan interrelacionats i comparteixen informació en temps real.

::::

---

### 8. Per què és important la localització del país en un ERP?

::::{dropdown} Solució
:animate: fade-in
:data-release: 2025-10-06

La localització defineix normativa fiscal, idiomes, impostos i documents oficials.  
Exemple: l’IVA a Espanya (21%) i França (20%) és diferent, i l’ERP ha d’adaptar-se.

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
        el.innerHTML = "<p><em>La solució estarà disponible a partir del " + rDate.toLocaleDateString() + ".</em></p>";
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

