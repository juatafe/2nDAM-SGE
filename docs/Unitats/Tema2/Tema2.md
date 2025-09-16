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
Per seguretat, no executes Odoo com a `root`.
:::

```{code-block} bash
:caption: Crear usuari de sistema per a Odoo i preparar permisos
sudo adduser --system --quiet --shell=/bin/bash --home=/opt/odoo --group odoo

# Opcional: bloqueja la contrasenya per evitar login interactiu
sudo passwd -l odoo

# Assegura propietats i permisos del directori de treball
sudo mkdir -p /opt/odoo
sudo chown -R odoo:odoo /opt/odoo
```

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



```{code-block} bash
:caption: Executar ordres com l’usuari odoo
sudo -u odoo -H bash -c 'whoami && echo $HOME'
```

```{code-block} bash
:caption: Verificacions útils
id odoo
ls -ld /opt/odoo
```

:::{admonition} Bona pràctica
:class: important
No dones privilegis `sudo` a l’usuari `odoo`. Mantín-lo limitat al seu directori i fitxers.
```


```{code-block} bash
:caption: Instal·lar PostgreSQL
:linenos:
sudo apt-get install -y postgresql
```

:::{tip}
Pots crear l’usuari per a Odoo de dues maneres:
:::

- Forma 1 (recomanada i ràpida):
```{code-block} bash
sudo -u postgres createuser -s odoo
```

- Forma 2 (interactiva):
```{code-block} bash
su - postgres
createuser -sdP odoo
```

### 4) Descàrrega d’Odoo 16.0

```{code-block} bash
:caption: Clonar Odoo 16
:linenos:
sudo -u odoo -H bash -c '
  cd /opt/odoo && \
  git clone https://www.github.com/odoo/odoo --depth 1 --branch 16.0 --single-branch
'
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
:linenos:
pip3 install --upgrade wheel setuptools pip
```

```{code-block} bash
:caption: Requeriments d’Odoo
:linenos:
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

:::{hint}
Prem :kbd:`Ctrl` + :kbd:`C` per aturar l’execució.
:::

```{image} /_static/assets/img/Tema2/img1_T2.png
:alt: Arranc d’Odoo correcte
:width: 65%
:align: center
```

:::{caution}
Si apareixen errors per dependències:
```bash
sudo pip3 install -r /opt/odoo/odoo/requirements.txt
# o instal·la la llibreria concreta que falte:
sudo pip3 install <nom_llibreria>
```
:::

## Configuració d’Odoo

### Llibreria PDF (wkhtmltopdf)

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
Si falten fonts, instal·la-les:
```bash
sudo apt-get install -y xfonts-75dpi xfonts-base
```
:::

### Fitxers de log

```{code-block} bash
:caption: Carpeta de logs
:linenos:
sudo mkdir -p /var/log/odoo/
sudo chown odoo:root /var/log/odoo
```

### Fitxer de configuració

Còpia i edita el fitxer de configuració d’Odoo:

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
Pots afegir altres rutes a `addons_path` separades per comes si tens mòduls personalitzats.
:::

### Arrancada com a servei (systemd)

Crea el servei:

```{code-block} bash
:caption: Service unit
:linenos:
sudo cp /opt/odoo/odoo/debian/odoo.service /etc/systemd/system/odoo.service
sudo nano /etc/systemd/system/odoo.service
```

Contingut bàsic:

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
Si uses entorn virtual, adapta `ExecStart`:
```ini
ExecStart=/opt/odoo/odoo-venv16/bin/python /opt/odoo/odoo/odoo-bin --config /etc/odoo.conf
```
:::

Activa i gestiona el servei:

```{code-block} bash
:caption: systemctl
:linenos:
sudo systemctl daemon-reload
sudo systemctl enable odoo.service
sudo systemctl start odoo
sudo systemctl status odoo
```

## Accés des del navegador

Obri el navegador i visita:

```
http://IP_DEL_SERVIDOR:8069
```

```{image} /_static/assets/img/Tema2/img2_T2.png
:alt: Pantalla d’inici d’Odoo
:width: 65%
:align: center
```

:::{tip}
Si no carrega, comprova:
- Estat del servei: `systemctl status odoo`
- Logs: :file:`/var/log/odoo/odoo-server.log`
- Port obert al firewall
