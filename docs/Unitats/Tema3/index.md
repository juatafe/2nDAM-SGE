# 📘 Tema 3 · Implantació de sistemes ERP-CRM en una empresa

```{toctree}
:maxdepth: 2
:caption: Continguts del Tema 3
:hidden:
```

## 1. Context i objectius

Als temes anteriors hem après:  
- **Tema 1:** què és un ERP/CRM i per què són importants per a la gestió empresarial.  
- **Tema 2:** com instal·lar i configurar Odoo en diferents entorns.  

Ara farem un pas més: veurem **com implantar un ERP dins d’una empresa real**.  
És a dir, adaptar-lo a les seues necessitats (clients, proveïdors, productes, comptabilitat, vendes, compres…).

:::{admonition} Objectius del tema
:class: note
- Conéixer el procés d’implantació d’un ERP.  
- Gestionar bases de dades i còpies de seguretat.  
- Instal·lar mòduls propis i externs.  
- Configurar l’empresa en Odoo amb dades reals.  
- Preparar l’entorn per a l’ús diari.  
:::

---

## 2. Accés i gestió de bases de dades

### 2.1 Accés pel client web
```{code-block} bash
http://IP_servidor:8069
```

```{image} /_static/assets/img/Tema3/img1_T3.png
:alt: Pantalla inicial d’Odoo
:width: 70%
:align: center
```

També podem accedir amb `http://localhost:8069` si treballem en local o amb Docker.

:::{admonition} Nota
:class: tip
Quan entrem per primera vegada hem de:  
- Crear una **base de dades**.  
- Escollir **usuari, idioma i país**.  
:::

### 2.2 Còpia de seguretat
```{image} /_static/assets/img/Tema3/img3_T3.png
:alt: Còpia de seguretat de la BD
:width: 70%
:align: center
```

Odoo genera un fitxer `.zip` que podem guardar per restaurar-lo si hi ha problemes.

---

## 3. Accés i gestió des del servidor

| **Opció** | **Quan s’utilitza** | **Eina** | **Avantatges** |
|-----------|---------------------|----------|----------------|
| VNC       | Revisió remota amb entorn gràfic | RealVNC, TightVNC | Veiem el mateix que al servidor |
| SSH       | Administració segura sense gràfic | `ssh usuari@ip` | Més ràpid i segur |
| Docker    | Treball amb contenidors | `docker exec -it` | Aïllament i facilitat de proves |

:::{admonition} Exemple amb SSH
:class: tip
1. Instal·lar el servei:  
   ```{code-block} bash
   sudo apt-get install openssh-server
   ```
2. Connectar-se:  
   ```{code-block} bash
   ssh alumne@192.168.1.20
   ```
:::

---

## 4. Instal·lació de mòduls

### 4.1 Mòduls propis
Odoo ja porta mòduls bàsics com **CRM, Vendes, Inventari, Facturació**.  

```{image} /_static/assets/img/Tema3/img5_T3.png
:alt: Llista de mòduls d’Odoo
:width: 100%
:align: center
```

### 4.2 Mòduls externs

A més dels mòduls oficials existeixen paquets de la comunitat (OCA) i tercers. Entrarem en més detall als propers temes però ací et deixe el procediment recomanat:

Passos bàsics
1. Crear carpeta d’addons extra (p. ex. `/opt/odoo/extra-addons`) i donar permisos:
    ```bash
    sudo mkdir -p /opt/odoo/extra-addons
    sudo chown -R odoo:odoo /opt/odoo/extra-addons
    ```
2. Descarregar el mòdul (git o arxiu):
    ```bash
    # amb git
    cd /opt/odoo/extra-addons
    git clone https://github.com/OCA/some-module.git

    # o descarregar zip i descomprimir
    wget https://.../module.zip && unzip module.zip -d /opt/odoo/extra-addons
    ```
3. Afegir la ruta a `addons_path` en `odoo.conf` (separa rutes amb comas):
    ```ini
    [options]
    addons_path = /usr/lib/python3/dist-packages/odoo/addons,/opt/odoo/extra-addons
    ```
4. Reiniciar el servei Odoo:
    ```bash
    sudo systemctl restart odoo
    ```
5. Actualitzar la llista d’aplicacions i instal·lar:
    - Via interfície: Activa “Developer mode” → Apps → Update Apps List → cerca i instal·la.
    - Via CLI (instal·lació directa d’un mòdul):
    ```bash
    odoo -c /etc/odoo/odoo.conf -d nom_bd -i nom_modul --stop-after-init
    ```

Consells i bones pràctiques
- Comprova compatibilitat del mòdul amb la versió d’Odoo abans d’instal·lar.  
- Utilitza branches o tags del repositori que parin a la teva versió.  
- Evita modificar mòduls de tercers directament: usa fork o manteniment separadament.  
- Controla permisos i propietat dels fitxers perquè Odoo pugui llegir-los.  
- Revisa dependències en el manifest (`__manifest__.py`) i instal·la requisits Python si cal.

Nota de seguretat
- Instal·la només mòduls de fonts fiables i prova en un entorn de staging abans de producció.
- Revisa codi i permisos per evitar filtracions de dades o privilegis indeguts.

---

## 5. Fases d’implantació d’un ERP

```{mermaid}
flowchart TD
    S[Selecció] --> I[Implantació]
    I --> P[Posada en marxa]
    P --> C[Tancament]
```

1. **Selecció de l’ERP**  
   - Objectiu: triar la solució que millor s’adapti a processos, pressupost i calendari.  
   - Activitats: anàlisi de requisits, comparativa de funcionalitats, proves pilot/demos, valoració de vendors i cost total (TCO).  
   - Entregables: document de requisits, informe de comparativa, prova pilot o POC, decisió i pla de projecte inicial.  
   - Riscos: requeriments incomplets, compatibilitat amb sistemes existents.

2. **Implantació**  
   - Objectiu: adaptar, configurar i integrar l’ERP amb l’entorn de l’empresa.  
   - Activitats: definició de processos (fit-gap), configuració d’usuaris i permisos, integracions (comptabilitat, SSO, APIs), migració de dades, desenvolupaments específics i proves unitàries.  
   - Entregables: entorn de preproducció, fitxers de migració, documentació de configuració, llistat de personalitzacions i proves passades.  
   - Riscos: migració de dades errònia, desviaments de calendari, personal insuficient.

3. **Posada en marxa (Go-live)**  
   - Objectiu: iniciar l’ús productiu amb mínim impacte en l’operativa.  
   - Activitats: validació final de dades, formació a usuaris clau i finals, suport intensiu en període d’arrencada, monitorització de rendiment i incidències.  
   - Entregables: aprovació de Go-live, registre d’incidències i pla d’acció, manuals d’usuari i sessions de formació.  
   - Riscos: resistència d’usuaris, errors crítics en processos vitals.

4. **Tancament del projecte i millora contínua**  
   - Objectiu: formalitzar la finalització del projecte i planificar evolucions.  
   - Activitats: lliurament formal, lliçó apreses, transferència de coneixement a l’equip de suport, plan de manteniment i evolució.  
   - Entregables: acta de tancament, informe d’avaluació, backlog de millores i SLA de suport.  
   - Riscos: manca de recursos per al manteniment, regressions en actualitzacions.

Checklist ràpid abans del Go‑live:
- Dades migrades i validades? Sí/No  
- Usuaris formats i rols assignats? Sí/No  
- Integracions testeades en preproducció? Sí/No  
- Pla de reversió i backups verificats? Sí/No  
- Suport dedicat per a les primeres 2–4 setmanes? Sí/No

Notes pràctiques:
- Prioritza una prova pilot amb processos crítics.  
- Fes desplegaments per fases si l’entitat és gran.  
- Mantén comunicació constant amb usuaris i patrocinadors del projecte.

---

## 6. Configuració de l’empresa a Odoo

| **Element** | **Exemple** |
|-------------|-------------|
| Nom i logo  | “Tavernes SL”, logotip corporatiu |
| Adreça i dades fiscals | Carrer Major, CIF, telèfon, web |
| Clients i proveïdors | Crear fitxes amb dades de contacte |
| Productes   | Llista d’articles amb preus i categories |
| Pla comptable | Instal·lar mòdul **l10n_es (PGC2008)** |
| TPV         | Instal·lar mòdul de punt de venda |

:::{admonition} Pas important
:class: warning
El mòdul de **localització del país** (en el nostre cas `l10n_es`) és imprescindible per tindre impostos i pla comptable correctes.  
:::

---

## 7. Resum

:::{admonition} Resum del tema
:class: important
En aquest tema hem après a:  
- Accedir i gestionar Odoo (client web i servidor).  
- Crear i protegir bases de dades.  
- Instal·lar mòduls propis i externs.  
- Configurar l’empresa amb dades reals.  

➡️ L’objectiu final és deixar Odoo **llest per a la gestió diària d’una empresa**.  
:::

---

## 8. Diagrama de procés d’implantació

```{mermaid}
flowchart TD
    A[Crear base de dades] --> B[Instal·lar mòduls bàsics]
    B --> C[Afegir mòduls externs]
    C --> D[Configurar empresa]
    D --> E[Proves amb dades reals]
    E --> F[Odoo llest per a l'ús]
```

---

## 9. Casos pràctics per a analitzar

Encara que **no crearem mòduls** en aquest punt del curs, és important entendre com Odoo pot donar resposta a necessitats reals d’una organització.  

### 9.1 Digitalització d’expedients en paper
Molts ajuntaments o institucions tenen **estanteries plenes d’expedients vius en paper** que ocupen molt d’espai i resulten difícils de consultar.  
Un projecte pilot podria consistir en:  
- Assignar un **número d’expedient** únic.  
- Digitalitzar i indexar documents.  
- Consultar-los via Odoo de forma segura.  
- Reduir espai físic i millorar l’accessibilitat.

### 9.2 Gestió d’una responsabilitat patrimonial
Quan un veí reclama una **responsabilitat patrimonial** (per exemple, danys en un vehicle per mal estat d’un carrer), cal obrir un **expedient complet**.  
Odoo podria donar suport al procés mitjançant un mòdul de gestió d’expedients que permeta:  
- Iniciar la reclamació amb dades del sol·licitant.  
- Requerir documentació i informes tècnics.  
- Assignar tasques a diferents rols (TAG, policia, tècnics).  
- Tindre un flux de validació i resolució.

:::{admonition} Exemple interactiu
:class: tip
A la mateixa carpeta del tema trobaràs el fitxer **ResponsabilitatPatrimonial.html**, una demo en HTML amb el flux complet de passos.  
Obri’l amb el navegador per analitzar el procés.  
:::

---

## 10. Model de dades i arxiu dels expedients

:::{admonition} Idea clau
:class: important
Els expedients poden tindre fitxers grans i sensibles. No és recomanable guardar-los dins la base de dades d’Odoo. Guarda els fitxers en un NAS o object storage i, a Odoo, només les metadades i l’enllaç/ubicació.
:::

### 10.1 Opcions de desat de fitxers

- NAS (NFS/CIFS) muntat al servidor d’Odoo
  - Simple i barat. Backups clars al NAS.
  - A Odoo, desa el path o una URL cap a la carpeta de l’expedient.
- Filestore d’Odoo sobre NAS
  - Muntes el NAS i apuntes `data_dir` allí; Odoo guarda adjunts al sistema de fitxers, no a PostgreSQL.
- Object Storage (S3/MinIO)
  - Escalable i robust. Usa mòduls OCA (p. ex. `attachment_s3`, `base_attachment_object_storage`).
- DMS extern (Nextcloud/ownCloud/SharePoint/WebDAV)
  - Odoo guarda l’enllaç compartit i metadades; el DMS gestiona versions i permisos.

:::{admonition} Pros/contres ràpids
:class: tip
- NAS: fàcil, local, però cal vigilar permisos i creixement.
- Filestore+NAS: integrat amb Odoo; còpies via NAS; manteniment senzill.
- S3/MinIO: alta disponibilitat; cost/control segons proveïdor.
- DMS: workflow documental potent, però integra dues plataformes.
:::

### 10.2 Configuració bàsica (exemples)

:::{admonition} Muntar un NAS (Ubuntu)
:class: note
```{code-block} bash
# Exemple NFS
sudo apt-get install -y nfs-common
echo "nas.local:/expedients  /mnt/expedients  nfs  defaults,_netdev  0  0" | sudo tee -a /etc/fstab
sudo mount -a
```
:::

:::{admonition} Odoo filestore al NAS
:class: note
```{code-block} ini
# /etc/odoo.conf
[options]
data_dir = /mnt/expedients/odoo_filestore
```
Crea permisos adequats: propietari `odoo:odoo`, i restrictiu per a dades sensibles.
:::

### 10.3 Model a Odoo: metadades i enllaços

- Guarda identificador d’expedient, persona interessada, estat, i la “ruta” (path/URL) on viuen els fitxers.
- Els adjunts grans no van a PostgreSQL; només referències.

```{code-block} python
# Exemple minimal d’un model d’expedient (Odoo)
from odoo import models, fields

class AjtExpedient(models.Model):
    _name = "ajt.expedient"
    _description = "Expedient municipal"

    name = fields.Char("Codi expedient", required=True, copy=False)
    citizen_id = fields.Many2one("res.partner", string="Ciutadà", domain=[("is_company","=",False)])
    manager_id = fields.Many2one("res.users", string="Gestor")
    stage = fields.Selection([("nou","Nou"),("tramitat","En tràmit"),("resolt","Resolt")], default="nou")
    storage_url = fields.Char("Ubicació de fitxers (URL/path)")   # p. ex. /mnt/expedients/2025/EXP-0001
    privacy = fields.Selection([("public","Públic"),("intern","Intern"),("reservat","Reservat")], default="intern")
    notes = fields.Text("Notes")
```

:::{admonition} Alternatives d’enllaç
:class: tip
- Path local: `/mnt/expedients/2025/EXP-0001`
- URL WebDAV/Nextcloud: `https://cloud.ajuntament.local/s/…`
- S3: `s3://expedients/2025/EXP-0001/…` (amb mòdul d’object storage)
:::

### 10.4 Qui és qui a Odoo? Rols i permisos

:::{admonition} Ciutadà
:class: note
- Registre com a contacte (`res.partner`) amb usuari de portal.
- Accés limitat via Portal: presentar sol·licituds, veure l’estat del seu expedient i documents propis.
:::

:::{admonition} Personal municipal
:class: note
- Usuaris interns d’Odoo amb rols segons funció.
- Exemple de rols:
  - Registre/Atenció (crea expedients i valida documentació d’entrada)
  - Gestor/a d’expedients (propietari, edita i coordina)
  - Tècnic/a (aporta informes i evidències)
  - Jurídic (revisió legal, informes)
  - Intervenció/Comptabilitat (si aplica)
  - Supervisor/a (vista global, validacions finals)
  - Admin (configuració i seguretat)
:::

:::{admonition} Permisos mínims recomanats
:class: important
- Ciutadà (Portal): només els seus expedients i documents (lectura i aportació guiada).
- Registre: crear expedients i llegir tots; no pot eliminar.
- Gestor: lectura/escriptura del seu cas; pot convidar tècnics.
- Tècnic/Jurídic: lectura i escriptura en expedients assignats.
- Supervisor: lectura global i validació.
- Admin: configuració, rols i auditories.
Implementa-ho amb grups (`res.groups`) i record rules per propietari/assignació.
:::

### 10.5 Compliment i bones pràctiques

- RGPD: base jurídica, minimització de dades, retenció i dret d’accés.
- Traçabilitat: registre d’activitat i auditories d’accés.
- Nomenclatura de carpetes: any/tipus/identificador (p. ex. `2025/RP/EXP-0001`).
- Backups: NAS versionat + còpia externa; proves de restauració periòdiques.
- Encriptació en trànsit (SMB signing, NFSv4, HTTPS/WebDAV) i, si cal, en repòs.

:::{admonition} Reflexió
:class: tip
- Quina opció d’emmagatzematge s’adapta millor al vostre entorn (NAS, S3, DMS)?
- Quins rols reals necessiteu i quines regles de visibilitat aplicareu?
- Com garantireu retenció i esborrat conforme a RGPD?
:::
