# Tema 2 - Instal·lació i configuració d’Odoo

## Introducció
En aquest tema veurem, de forma guiada, com planificar, instal·lar i configurar Odoo 16 en un servidor Linux. Repassarem requisits, base de dades PostgreSQL, entorn Python, arrencada com a servei, recomanacions de seguretat, còpies de seguretat i optimització bàsica.

## Visió general del procés
- Disseny de la instal·lació
- Instal·lació d’equips i programari
- Adaptació i configuració
- Migració de dades
- Proves
- Documentació
- Formació d’usuaris

:::{admonition} SaaS vs On-Premise (matís per a producció)
:class: tip
Abans de començar, valora si convé delegar la infraestructura (SaaS) o gestionar-la internament (On-Premise). El cost, el temps de desplegament i el control tècnic varien molt entre opcions.

En entorns de producció, tingues en compte:
- SLA/SLO i suport: disponibilitat garantida, temps de resposta, 24x7.
- TCO: subscripció, infraestructura, personal, energia i creixement.
- Compliment i residència de dades: RGPD/LOPDGDD, contractes DPA, localització UE.
- Seguretat: aïllament, actualitzacions crítiques, gestió de secrets i accessos.
- Còpies i recuperació de desastres: RPO/RTO, proves periòdiques de restauració.
- Escalabilitat i límits: multitenència, pics de càrrega, quota d’emmagatzematge.
- Personalització i lock‑in: mòduls, APIs, possibilitat de migració entre opcions.
- Finestra de manteniment i versions: cadència d’updates i canvis majors.
- Observabilitat: accés a logs, monitoratge, alarmes i traçabilitat.
:::

## Instal·lació, comprovació i configuració

:::{note}
Les instruccions estan provades a Ubuntu 22.04 LTS. En altres versions/distribucions poden canviar noms de paquets o ordres.
:::

### 1) Preparació del sistema

```{code-block} bash
:caption: Actualització del sistema
sudo apt-get update
sudo apt-get dist-upgrade -y
```

:::{admonition} apt vs apt-get (quan usar cadascun)
:class: tip
Ambdós usen APT per baix, però tenen usos recomanats diferents:

- apt (interactiu, per a humans)
  - Interfície més amigable (barres de progrés, resum).
  - Pot mostrar preguntes i eixir amb textos menys estables.
  - Útil en màquines de desenvolupament o administració manual.

- apt-get (scripts/CI/CD, entorns automatitzats)
  - Interfície estable en el temps (output i codis d’eixida previsibles).
  - Ideal per a playbooks, Dockerfiles i pipelines.
  - Combina’l amb banderes per evitar prompts i recomanats.

Exemple interactiu:
```{code-block} bash
sudo apt update
sudo apt install curl
```

Exemple en scripts/CI:
```{code-block} bash
export DEBIAN_FRONTEND=noninteractive
sudo apt-get update
sudo apt-get install -y --no-install-recommends curl ca-certificates
sudo apt-get clean
```
:::

:::{tip}
En entorns de prova pots usar `apt` en lloc d’`apt-get`. Per a scripts o CI/CD és preferible `apt-get`.
:::

### 2) Usuari de servei

:::{warning}
Executar Odoo com a `root` és una mala pràctica de seguretat, ja que el procés tindria accés complet al sistema i podria provocar vulnerabilitats greus si es produïra algun atac o error. Per això, és recomanable crear un usuari de servei específic amb permisos limitats, que només puga accedir als recursos estrictament necessaris per a Odoo. D’aquesta manera, s’aplica el principi de mínims privilegis i es protegeix millor el servidor i les dades.

<!-- La comanda següent crea un usuari de sistema anomenat `odoo` al servidor Linux. L’opció `--system` indica que és un compte especial per a serveis, no per a ús interactiu. Amb `--quiet` es minimitza la informació mostrada durant la creació. L’opció `--shell=/bin/bash` assigna la shell Bash a l’usuari, útil per a tasques de manteniment. `--home=/opt/odoo` defineix la carpeta personal de l’usuari, on s’instal·larà Odoo i es guardaran els seus fitxers. Finalment, `--group odoo` crea un grup amb el mateix nom i l’assigna a l’usuari, facilitant la gestió de permisos sobre els fitxers del servei. Aquesta configuració ajuda a aïllar Odoo i aplicar el principi de mínims privilegis. -->

```{code-block} bash
:caption: Crear usuari de sistema per a Odoo i preparar permisos
sudo adduser --system --quiet --shell=/bin/bash --home=/opt/odoo --group odoo

# Opcional: bloqueja la contrasenya per evitar login interactiu
sudo passwd -l odoo

# Assegura propietats i permisos del directori de treball
sudo mkdir -p /opt/odoo
sudo chown -R odoo:odoo /opt/odoo
```
:::



:::{admonition} Per què un usuari de sistema?
:class: note
Aïlla el procés d’Odoo, aplica el principi de mínims privilegis i simplifica permisos i propietats de fitxers. Els usuaris de sistema (servei) no són comptes d’ús interactiu.
:::

:::{admonition} Què fan les opcions d’adduser?
:class: tip


--system
: crea un compte de servei (UID de sistema) i el seu directori.

--quiet
: minimitza la sortida.

--shell /bin/bash
: permet shell per a manteniment (pots usar `/usr/sbin/nologin` per a més restricció).

--home /opt/odoo
: carpeta on deixarem codi, virtualenv i dades pròpies del servei.

--group odoo
: crea el grup homònim i l’assigna a l’usuari.
:::



### Comprovar l’usuari de servei i permisos

Després de crear l’usuari de sistema `odoo`, és important verificar que tot està correcte abans de continuar amb la instal·lació. Aquestes ordres et permeten comprovar que l’usuari existeix, que el seu directori personal és el que toca, i que té els permisos adequats.

```{code-block} bash
:caption: Executar ordres com l’usuari odoo
sudo -u odoo -H bash -c 'whoami && echo $HOME'
```
Aquesta comanda executa una shell com l’usuari `odoo` i mostra el nom d’usuari i el seu directori personal. Si tot està bé, hauria d’aparéixer `odoo` i `/opt/odoo`.

```{code-block} bash
:caption: Verificacions útils
id odoo
ls -ld /opt/odoo
```
- `id odoo` mostra l’identificador d’usuari, grup i altres detalls del compte `odoo`.
- `ls -ld /opt/odoo` mostra els permisos i propietari del directori de treball d’Odoo. El propietari ha de ser `odoo` i el grup també.

:::{admonition} Bona pràctica
:class: important
No dones privilegis `sudo` a l’usuari `odoo`. Mantín-lo limitat al seu directori i fitxers. Això redueix el risc que un atac o error en Odoo puga afectar la resta del sistema. L’usuari de servei ha de tindre només els permisos estrictament necessaris per a executar Odoo i gestionar els seus fitxers.
:::

### 3) Instal·lació de la base de dades PostgreSQL

Abans d’instal·lar Odoo, necessitem un gestor de base de dades per guardar tota la informació de l’empresa: usuaris, factures, productes, configuració, etc. Odoo utilitza PostgreSQL perquè és robust, segur i compatible amb totes les funcionalitats del sistema. Per això, el primer pas és instal·lar PostgreSQL al servidor. Així podrem crear la base de dades que Odoo utilitzarà per funcionar correctament.

```{code-block} bash
:caption: Instal·lar PostgreSQL
sudo apt-get install -y postgresql
```

:::{tip}
Pots crear l’usuari per a Odoo de dues maneres, segons preferisques una opció més ràpida o una més interactiva. Aquest usuari serà el propietari de la base de dades i permetrà que Odoo gestione les seues dades de forma segura.

- **Forma 1 (recomanada i ràpida):**  
Utilitza una sola comanda des de root o qualsevol usuari amb permisos sudo. Aquesta opció és ideal si vols automatitzar el procés o fer-lo directament des del teu usuari d’administració.

```{code-block} bash
sudo -u postgres createuser -s odoo
```
Aquesta comanda crea l’usuari `odoo` amb privilegis de superusuari a PostgreSQL, necessari per a la gestió de bases de dades des d’Odoo.

- **Forma 2 (interactiva):**  
Accedeix com a usuari `postgres` i executa la creació de l’usuari de manera més guiada. Aquesta opció et permet definir contrasenya i altres paràmetres manualment.

```{code-block} bash
su - postgres
createuser -sdP odoo
```
Amb aquesta comanda, el sistema et demanarà la contrasenya per a l’usuari `odoo` i podràs ajustar opcions addicionals si ho necessites.

:::

### 4) Descàrrega d’Odoo 16.0

```{code-block} bash
:caption: Clonar Odoo 16
:linenos:
sudo -u odoo -H bash -c 'cd /opt/odoo && \
  git clone https://www.github.com/odoo/odoo --depth 1 --branch 16.0 --single-branch'
```

### 5) Dependències del sistema

```{code-block} bash
:caption: Paquets necessaris
:linenos:
sudo apt-get install -y \
  build-essential python3-pillow python3-lxml python3-dev python3-pip python3-setuptools \
  libpq-dev npm nodejs git libldap2-dev libsasl2-dev libxml2-dev libxslt1-dev libjpeg-dev \
  apache2 xfonts-75dpi xfonts-base libffi-dev fontconfig
```

:::{important}
Assegura’t que tots els paquets s’instal·len sense errors. Si falta alguna llibreria, Odoo pot no arrancar correctament.
:::

### 6) Entorn Python i requisits

```{code-block} bash
:caption: Actualitzar pip/setuptools
pip3 install --upgrade wheel setuptools pip
```

```{code-block} bash
:caption: Requeriments d’Odoo
pip3 install -r /opt/odoo/odoo/requirements.txt
```

:::{warning}
Amb Python 3.12 poden aparéixer incompatibilitats. Es recomana usar un entorn virtual.
:::

```{code-block} bash
:caption: Crear i usar un entorn virtual (opcional però recomanat)
:linenos:
sudo -u odoo -H bash -c '
  cd /opt/odoo
  python3 -m venv odoo-venv16
  source odoo-venv16/bin/activate
  pip3 install --upgrade wheel setuptools pip
  pip3 install -r /opt/odoo/odoo/requirements.txt
  deactivate
'
```

## Arrancant Odoo (prova ràpida)

Inicia Odoo i comprova que no hi ha errors:

```{code-block} bash
:caption: Execució directa (prova)
:linenos:
sudo -u odoo -H bash -c '
  cd /opt/odoo/odoo
  ./odoo-bin
'
```
```{image} /_static/assets/img/Tema2/img1_T2.png
:alt: Arranc d’Odoo correcte
:width: 100%
:align: center
```

:::{hint}
Prem {kbd}`Ctrl` + {kbd}`C` per aturar l’execució.
:::



:::{caution}
Si apareixen errors per dependències:
```bash
sudo pip3 install -r /opt/odoo/odoo/requirements.txt
# o instal·la la llibreria concreta que falte:
sudo pip3 install <nom_llibreria>
```
:::

## Configuració d’Odoo

En aquesta secció es detalla com preparar Odoo perquè funcione correctament en el servidor, incloent la generació d’informes PDF, la gestió de logs, la configuració del fitxer principal i la posada en marxa com a servei amb systemd.

### Llibreria PDF (wkhtmltopdf)

Odoo utilitza la llibreria **wkhtmltopdf** per convertir informes i documents a format PDF. Sense aquesta eina, moltes funcionalitats d’impressió i exportació no funcionaran. Cal instal·lar la versió adequada per al teu sistema operatiu i crear els enllaços necessaris perquè Odoo la trobe fàcilment.

```{code-block} bash
:caption: Instal·lar wkhtmltopdf per a informes PDF
:linenos:
wget https://github.com/wkhtmltopdf/packaging/releases/download/0.12.6.1-2/wkhtmltox_0.12.6.1-2.jammy_amd64.deb
sudo dpkg -i wkhtmltox_0.12.6.1-2.jammy_amd64.deb
rm wkhtmltox_0.12.6.1-2.jammy_amd64.deb
sudo ln -s /usr/local/bin/wkhtmltopdf /usr/bin/
sudo ln -s /usr/local/bin/wkhtmltoimage /usr/bin/
```

:::{warning}
Si falten fonts, Odoo pot mostrar errors o generar PDFs sense el format correcte. Instal·la les fonts bàsiques amb:
```bash
sudo apt-get install -y xfonts-75dpi xfonts-base
```
:::

### Fitxers de log

Els fitxers de log són essencials per monitoritzar el funcionament d’Odoo, detectar errors i fer seguiment de l’activitat. Es recomana crear una carpeta específica per als logs i assignar-li els permisos correctes perquè només l’usuari de servei puga escriure-hi.

```{code-block} bash
:caption: Carpeta de logs
:linenos:
sudo mkdir -p /var/log/odoo/
sudo chown odoo:root /var/log/odoo
```

### Fitxer de configuració

El fitxer de configuració d’Odoo (`/etc/odoo.conf`) defineix els paràmetres principals del sistema: usuari de la base de dades, contrasenya, rutes als mòduls (addons) i ubicació del log. Cal copiar el fitxer base, ajustar permisos i editar-lo segons les necessitats del teu entorn.

```{code-block} bash
:caption: Preparar /etc/odoo.conf
:linenos:
sudo cp /opt/odoo/odoo/debian/odoo.conf /etc/odoo.conf
sudo chown odoo: /etc/odoo.conf
sudo chmod 640 /etc/odoo.conf
sudo nano /etc/odoo.conf
```

Contingut mínim recomanat:

```{code-block} ini
:caption: /etc/odoo.conf
[options]
db_user = odoo
db_password = false
addons_path = /opt/odoo/odoo/addons
logfile = /var/log/odoo/odoo-server.log
```

:::{note}
Si tens mòduls personalitzats, pots afegir altres rutes a `addons_path` separades per comes.
:::

### Arrancada com a servei (systemd)

Perquè Odoo s’inicie automàticament i es gestione com un servei del sistema, cal crear una unitat de servei amb systemd. Això facilita l’arrancada, parada i monitoratge d’Odoo, i permet que el sistema el recupere automàticament en cas de fallada.

```{code-block} bash
:caption: Service unit
:linenos:
sudo cp /opt/odoo/odoo/debian/odoo.service /etc/systemd/system/odoo.service
sudo nano /etc/systemd/system/odoo.service
```

Contingut bàsic del fitxer de servei:

```{code-block} ini
:caption: /etc/systemd/system/odoo.service
[Unit]
Description=Odoo ERP
After=network.target postgresql.service

[Service]
Type=simple
User=odoo
Group=odoo
ExecStart=/opt/odoo/odoo/odoo-bin --config /etc/odoo.conf
Restart=on-failure

[Install]
WantedBy=multi-user.target
```

:::{important}
Si has instal·lat Odoo en un entorn virtual, adapta la línia `ExecStart` per utilitzar el Python de l’entorn:
```ini
ExecStart=/opt/odoo/odoo-venv16/bin/python /opt/odoo/odoo/odoo-bin --config /etc/odoo.conf
```
Aquesta modificació és necessària perquè, en un entorn virtual, les llibreries i dependències de Python estan aïllades del sistema principal. Així, Odoo s’executarà amb la versió de Python i els paquets que has preparat específicament per a ell, evitant conflictes amb altres aplicacions o versions del sistema. D’aquesta manera, garantixes que el servei utilitza exactament l’entorn que has configurat i millores la seguretat i estabilitat de la instal·lació.
:::

Finalment, cal activar el servei, iniciar-lo i comprovar que funciona correctament:

```{code-block} bash
:caption: systemctl
:linenos:
sudo systemctl daemon-reload
sudo systemctl enable odoo.service
sudo systemctl start odoo
sudo systemctl status odoo
```
- **sudo systemctl daemon-reload**: Actualitza la configuració de systemd. És necessari després de crear o modificar fitxers de servei perquè el sistema reconega els canvis.
- **sudo systemctl enable odoo.service**: Fa que el servei d’Odoo s’inicie automàticament cada vegada que arranca el sistema.
- **sudo systemctl start odoo**: Inicia manualment el servei d’Odoo en aquest moment.
- **sudo systemctl status odoo**: Mostra l’estat actual del servei, incloent si està actiu, errors recents i informació de logs útil per a diagnòstic.

Aquestes ordres són fonamentals per gestionar Odoo com a servei i assegurar que funcione de manera estable i controlada pel sistema operatiu.

## Accés des del navegador

Obri el navegador i visita:

```
http://IP_DEL_SERVIDOR:8069
```

```{image} /_static/assets/img/Tema2/img2_T2_1.png
:alt: Pantalla d’inici d’Odoo
:width: 65%
:align: center
```

👉 La clau que et dona (“Master Password”) és fonamental perquè:

- **Protegeix el Database Manager:** és la contrasenya mestra que controla totes les operacions de gestió de bases de dades (crear, eliminar, fer còpies, restaurar, canviar noms…).
- **No és la mateixa que l’usuari administrador (admin) dins de la base de dades:** aquesta contrasenya només serveix per accedir a la pantalla de gestió de BDs (`/web/database/manager`).
- **Es pot canviar:** pots posar-ne una pròpia al camp Master Password de la pantalla que has vist. També pots modificar-la després al fitxer de configuració d’Odoo (`/etc/odoo/odoo.conf`), en la línia `admin_passwd = ...`.
