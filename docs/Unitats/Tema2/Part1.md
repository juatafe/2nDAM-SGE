# 📌 Part 1: Instal·lació tradicional d'Odoo en Ubuntu Server

Aquest document cobreix la instal·lació completa d'Odoo 16 utilitzant el mètode tradicional en Ubuntu Server. Aquest enfocament proporciona el màxim control sobre l'entorn i permet entendre profundament tots els components del sistema.

## Introducció

La instal·lació tradicional d'Odoo implica configurar manualment tots els components: sistema operatiu, base de dades, aplicació i serveis. Aquesta metodologia és ideal per a:

- **Entorns de producció** que requereixen personalització avançada
- **Aprenentatge** dels components i la seva interacció
- **Control total** sobre la configuració i seguretat
- **Optimització específica** segons les necessitats del negoci

### Arquitectura del sistema

```{mermaid}
graph TD
    A[Cliente Web] --> B[Apache Reverse Proxy]
    B --> C[Odoo Application Server]
    C --> D[PostgreSQL Database]
    
    E[Systemd] --> C
    F[Entorn Virtual Python] --> C
    G[Mòduls/Addons] --> C
```

### Avantatges vs inconvenients

| ✅ **Avantatges** | ❌ **Inconvenients** |
|------------------|---------------------|
| Control complet sobre la configuració | Configuració més complexa |
| Millor rendiment (sense overhead) | Més temps d'instal·lació |
| Facilitat per al debugging | Requereix més coneixements |
| Personalització avançada | Gestió manual de dependències |
| Integració nativa amb el sistema | Actualitzacions més complexes |

### Requisits previs

:::{admonition} Requisits del sistema
:class: important
**Hardware mínim:**
- CPU: 2 cores (2.5 GHz)
- RAM: 4 GB (8 GB recomanat)
- Disc: 20 GB d'espai lliure (SSD preferible)
- Xarxa: Connexió estable a Internet

**Software:**
- Ubuntu Server 22.04 LTS (o posterior)
- Accés sudo al sistema
- Connexió SSH configurada (si és remot)

**Coneixements tècnics:**
- Línia d'ordres de Linux
- Conceptes bàsics de xarxa i permisos
- Gestió de serveis amb systemd
:::

:::{note}
Les instruccions d'aquest document han estat provades en Ubuntu 22.04 LTS. En altres versions o distribucions poden variar els noms de paquets o ordres específiques.
:::

## Visió general del procés

La instal·lació tradicional segueix aquests passos principals:

1. **[Preparació del sistema](#1-preparació-del-sistema)**: Actualització i dependències base
2. **[Usuari de servei](#2-usuari-de-servei)**: Creació d'usuari dedicat per seguretat
3. **[PostgreSQL](#3-instal·lació-de-postgresql)**: Instal·lació i configuració de la base de dades
4. **[Odoo](#4-descàrrega-i-configuració-dodoo)**: Descàrrega del codi font i dependències
5. **[Configuració](#5-configuració-dodoo)**: Fitxers de configuració personalitzats
6. **[Servei systemd](#6-servei-systemd)**: Automatització i gestió del servei
7. **[Verificació](#checklist-de-verificació-de-la-instal·lació)**: Tests de funcionament
8. **[Apache (opcional)](#7-configuració-dapache-com-a-reverse-proxy-opcional)**: Reverse proxy per a producció

**Temps estimat:** 45-90 minuts (depenent de l'experiència i velocitat de connexió)

(1-preparació-del-sistema)=
## 1) Preparació del sistema

### Actualització completa del sistema

```bash
# Actualitzar llista de paquets
sudo apt-get update

# Actualització completa del sistema
sudo apt-get dist-upgrade -y

# Neteja de paquets orfes (opcional)
sudo apt-get autoremove -y
sudo apt-get autoclean
```

**Explicació de les ordres:**

| Ordre | Funció |
|-------|--------|
| `apt-get update` | Actualitza la llista de paquets disponibles des dels repositoris |
| `apt-get dist-upgrade` | Actualització intel·ligent que pot instal·lar/eliminar paquets per resoldre dependències |
| `autoremove` | Elimina paquets que es van instal·lar com a dependències i ja no són necessaris |
| `autoclean` | Elimina fitxers .deb descarregats que ja no estan disponibles als repositoris |

:::{admonition} apt vs apt-get: Quan usar cadascun
:class: tip
**apt** (recomanat per a ús interactiu):
- Interfície més amigable amb barres de progrés
- Millor experiència d'usuari
- Ideal per a administració manual

```bash
sudo apt update
sudo apt install curl
sudo apt upgrade
```

**apt-get** (per a scripts i automatització):
- Sortida més predictible i estable
- Ideal per a scripts, CI/CD i Dockerfiles
- Comportament consistent entre versions

```bash
export DEBIAN_FRONTEND=noninteractive
sudo apt-get update
sudo apt-get install -y --no-install-recommends curl
sudo apt-get clean
```
:::

### Instal·lació d'eines bàsiques

```bash
# Eines essencials per a l'administració
sudo apt-get install -y \
    curl \
    wget \
    git \
    nano \
    htop \
    unzip \
    software-properties-common \
    apt-transport-https \
    ca-certificates \
    gnupg \
    lsb-release
```

**Descripció de les eines:**

- **curl/wget**: Descàrrega de fitxers des d'Internet
- **git**: Control de versions per descarregar Odoo
- **nano**: Editor de text senzill per a configuracions
- **htop**: Monitor de processos millorat
- **unzip**: Descompressió de fitxers
- **software-properties-common**: Gestió de repositoris PPA
- **apt-transport-https**: Suport per a repositoris HTTPS
- **ca-certificates**: Certificats d'autoritats de certificació
- **gnupg**: Verificació de signatures GPG
- **lsb-release**: Informació de la distribució Linux

(2-usuari-de-servei)=
## 2) Usuari de servei

### Creació de l'usuari dedicat

```bash
# Crear usuari de sistema per a Odoo
sudo adduser --system --quiet --shell=/bin/bash --home=/opt/odoo --group odoo

# Verificar la creació
id odoo
```

**Explicació detallada dels paràmetres:**

| Paràmetre | Funció |
|-----------|--------|
| `--system` | Crea un usuari de sistema (UID < 1000) |
| `--quiet` | Suprimeix missatges verbosos durant la creació |
| `--shell=/bin/bash` | Assigna bash com a shell per permetre execució d'scripts |
| `--home=/opt/odoo` | Estableix el directori home personalitzat |
| `--group odoo` | Crea un grup amb el mateix nom que l'usuari |

### Configuració de seguretat

```bash
# Bloquejar la contrasenya per evitar logins interactius
sudo passwd -l odoo

# Preparar estructura de directoris
sudo mkdir -p /opt/odoo
sudo chown -R odoo:odoo /opt/odoo
sudo chmod 755 /opt/odoo

# Verificar permisos
ls -la /opt/ | grep odoo
```

:::{admonition} Per què un usuari de sistema dedicat?
:class: important
**Seguretat (Principi de mínims privilegis):**
- L'usuari `odoo` només té accés als recursos necessaris
- Si es compromet el servei, l'atacant no té privilegis d'administrador
- Aïllament del procés respecte a altres serveis del sistema

**Gestió:**
- Simplifica la gestió de permisos de fitxers
- Facilita l'auditoria de processos i recursos
- Permet polítiques de seguretat específiques per servei

**Manteniment:**
- Els fitxers d'Odoo estan clarament identificats per propietari
- Facilita backups i migracions
- Evita conflictes amb altres aplicacions
:::

### Verificació de l'usuari

```bash
# Informació de l'usuari creat
id odoo
getent passwd odoo

# Verificar que el directori home existeix
sudo -u odoo ls -la /opt/odoo

# Test d'execució com a usuari odoo
sudo -u odoo whoami
```

(3-instal·lació-de-postgresql)=
## 3) Instal·lació de PostgreSQL

### Instal·lació del servidor de base de dades

```bash
# Instal·lar PostgreSQL i extensions
sudo apt-get install -y postgresql postgresql-contrib

# Verificar la instal·lació
sudo systemctl status postgresql
psql --version
```

**Explicació dels paquets:**

- **postgresql**: Servidor de base de dades principal
- **postgresql-contrib**: Mòduls addicionals amb funcionalitats extenses com:
  - Extensions per a tipus de dades especials
  - Funcions adicionals d'agregació
  - Utilitats per a backup i restauració
  - Mòduls de seguretat i auditoria

### Configuració de PostgreSQL per a Odoo

```bash
# Crear usuari PostgreSQL per a Odoo
sudo -u postgres createuser -s odoo

# Verificar la creació de l'usuari
sudo -u postgres psql -c "\du"

# Opcional: Crear una base de dades de prova
sudo -u postgres createdb odoo_test
```

**Explicació de la configuració:**

| Ordre | Funció |
|-------|--------|
| `sudo -u postgres` | Executa ordres com l'usuari postgres (propietari del servei) |
| `createuser -s odoo` | Crea un usuari amb privilegis de superusuari (`-s`) |
| `\du` | Ordre SQL per llistar tots els usuaris de PostgreSQL |
| `createdb odoo_test` | Crea una base de dades opcional per a proves |

:::{admonition} Per què superusuari PostgreSQL?
:class: note
Odoo necessita privilegis de superusuari a PostgreSQL per:

- **Crear i eliminar bases de dades** dinàmicament des de la interfície web
- **Instal·lar extensions** PostgreSQL necessàries (unaccent, pg_trgm, etc.)
- **Gestionar schemas** i estructures complexes de base de dades
- **Executar operacions de manteniment** com VACUUM i ANALYZE

En entorns de producció molt restrictius, es poden configurar privilegis més limitats, però requereix configuració manual adicional.
:::

### Optimització bàsica de PostgreSQL

```bash
# Backup de la configuració original
sudo cp /etc/postgresql/*/main/postgresql.conf /etc/postgresql/*/main/postgresql.conf.backup

# Configuració bàsica per a Odoo
sudo tee -a /etc/postgresql/*/main/postgresql.conf > /dev/null << EOF

# Configuració optimitzada per a Odoo
shared_buffers = 256MB
effective_cache_size = 1GB
work_mem = 32MB
maintenance_work_mem = 128MB
checkpoint_completion_target = 0.7
wal_buffers = 16MB
default_statistics_target = 100
EOF

# Reiniciar PostgreSQL per aplicar canvis
sudo systemctl restart postgresql
sudo systemctl status postgresql
```

(4-descàrrega-i-configuració-dodoo)=
## 4) Descàrrega i configuració d'Odoo

### Descàrrega del codi font

```bash
# Canviar a l'usuari odoo per a la descàrrega
sudo -u odoo -H bash -c '
    cd /opt/odoo
    git clone https://www.github.com/odoo/odoo --depth 1 --branch 16.0 --single-branch odoo16
'

# Verificar la descàrrega
sudo -u odoo ls -la /opt/odoo/
```

**Explicació de la clonació Git:**

| Paràmetre | Funció |
|-----------|--------|
| `-u odoo -H` | Executa com usuari odoo amb el seu entorn HOME |
| `--depth 1` | Clonació superficial (només l'última revisió) per estalviar espai |
| `--branch 16.0` | Especifica la branca de la versió 16.0 d'Odoo |
| `--single-branch` | Només descarrega la branca especificada |
| `odoo16` | Nom del directori destí |

### Instal·lació de dependències del sistema

```bash
# Dependències essencials per a Odoo
sudo apt-get install -y \
    build-essential \
    python3-dev \
    python3-pip \
    python3-venv \
    python3-wheel \
    python3-setuptools \
    libpq-dev \
    libxml2-dev \
    libxslt1-dev \
    libldap2-dev \
    libsasl2-dev \
    libjpeg-dev \
    libpng-dev \
    libfreetype6-dev \
    libffi-dev \
    libssl-dev \
    npm \
    nodejs \
    fontconfig \
    xfonts-75dpi \
    xfonts-base
```

**Categorització de les dependències:**

**Eines de compilació:**
- `build-essential`: Compiladors GCC i eines de construcció
- `python3-dev`: Headers per compilar extensions Python amb codi C

**Processament de dades:**
- `libxml2-dev`, `libxslt1-dev`: Manipulació i transformació XML/HTML
- `libpq-dev`: Connectors per a PostgreSQL
- `libldap2-dev`, `libsasl2-dev`: Autenticació LDAP/Active Directory

**Processament d'imatges:**
- `libjpeg-dev`, `libpng-dev`: Formats d'imatge JPEG i PNG
- `libfreetype6-dev`: Renderització de fonts en imatges
- `python3-pillow` (instal·lat amb pip): Biblioteca de processament d'imatges

**Eines web i PDF:**
- `npm`, `nodejs`: Gestió de paquets JavaScript
- `fontconfig`, `xfonts-*`: Fonts per a generació de PDFs
- `wkhtmltopdf` (instal·lat posteriorment): Conversió HTML a PDF

### Creació de l'entorn virtual Python

```none
# Crear i configurar entorn virtual
sudo -u odoo -H bash -c '
    cd /opt/odoo
    python3 -m venv odoo-venv
    source odoo-venv/bin/activate
    
    # Actualitzar eines base
    pip install --upgrade pip wheel setuptools
    
    # Instal·lar dependències d'Odoo
    pip install -r odoo16/requirements.txt
    
    deactivate
'

# Verificar la instal·lació
sudo -u odoo /opt/odoo/odoo-venv/bin/pip list | grep -E "(psycopg2|lxml|Pillow)"
```

**Explicació de l'entorn virtual:**

Els entorns virtuals Python proporcionen:

- **Aïllament de dependències**: Evita conflictes entre versions de paquets
- **Gestió neta**: Fàcil actualització i eliminació sense afectar el sistema
- **Reproducibilitat**: Mateixes versions en desenvolupament i producció
- **Seguretat**: Dependències específiques per aplicació

**Contingut de requirements.txt:**

El fitxer `/opt/odoo/odoo16/requirements.txt` conté dependències com:

```text
Babel>=2.6.0               # Internacionalització
chardet                    # Detecció de codificació de text
cryptography               # Criptografia i certificates
decorator                  # Decoradors Python
ebaysdk                    # Integració amb eBay
feedparser                 # Parsing de feeds RSS/Atom
gevent                     # Concurrència asíncrona
idna                       # Internacionalització de noms de domini
Jinja2                     # Motor de plantilles
lxml                       # Processament XML/HTML
Pillow                     # Processament d'imatges
psutil                     # Informació del sistema
psycopg2                   # Connector PostgreSQL
python-dateutil            # Manipulació de dates
qrcode                     # Generació de codis QR
reportlab                  # Generació de PDFs
requests                   # Client HTTP
Werkzeug                   # Utilitats web WSGI
```

### Instal·lació de wkhtmltopdf

```bash
# Descarregar i instal·lar wkhtmltopdf
cd /tmp
wget https://github.com/wkhtmltopdf/packaging/releases/download/0.12.6-1/wkhtmltox_0.12.6-1.focal_amd64.deb
sudo dpkg -i wkhtmltox_0.12.6-1.focal_amd64.deb

# Si hi ha errors de dependències
sudo apt-get install -f

# Verificar la instal·lació
wkhtmltopdf --version
which wkhtmltopdf
```

**Importància de wkhtmltopdf:**

- **Generació de PDFs**: Converteix vistes HTML d'Odoo a documents PDF
- **Informes**: Essencial per a factures, albarans, nòmines, etc.
- **Qualitat**: Proporciona millor qualitat que altres biblioteques Python
- **Compatibilitat**: Versió específica requerida per compatibilitat amb Odoo

(5-configuració-dodoo)=
## 5) Configuració d'Odoo

### Estructura de directoris

```bash
# Crear estructura de directoris per a Odoo
sudo mkdir -p /etc/odoo
sudo mkdir -p /var/log/odoo
sudo mkdir -p /var/lib/odoo/filestore
sudo mkdir -p /opt/odoo/custom-addons

# Assignar permisos
sudo chown -R odoo:odoo /var/log/odoo
sudo chown -R odoo:odoo /var/lib/odoo
sudo chown -R odoo:odoo /opt/odoo/custom-addons
```

**Explicació de l'estructura:**

| Directori | Funció |
|-----------|--------|
| `/etc/odoo/` | Fitxers de configuració del sistema |
| `/var/log/odoo/` | Logs d'aplicació i debug |
| `/var/lib/odoo/filestore/` | Emmagatzematge de fitxers pujats |
| `/opt/odoo/custom-addons/` | Mòduls personalitzats i de tercers |

### Fitxer de configuració principal

```bash
# Crear fitxer de configuració d'Odoo
sudo tee /etc/odoo/odoo.conf > /dev/null <<'EOF'
[options]
# Configuració de base de dades
db_host = localhost
db_port = 5432
db_user = odoo
db_password = false

# Configuració de l'aplicació
admin_passwd = SuperAdminPassword2024!
xmlrpc_port = 8069
longpolling_port = 8072

# Rutes i addons
addons_path = /opt/odoo/odoo16/addons,/opt/odoo/custom-addons
data_dir = /var/lib/odoo

# Logging
logfile = /var/log/odoo/odoo.log
log_level = info
logrotate = True

# Rendiment
workers = 0
max_cron_threads = 2
limit_memory_hard = 2684354560
limit_memory_soft = 2147483648
limit_request = 8192
limit_time_cpu = 600
limit_time_real = 1200

# Seguretat
list_db = True
proxy_mode = False
EOF

# Configurar permisos del fitxer de configuració
sudo chown odoo:odoo /etc/odoo/odoo.conf
sudo chmod 640 /etc/odoo/odoo.conf
```

**Explicació detallada de la configuració:**

**Connexió a base de dades:**
- `db_host = localhost`: PostgreSQL al mateix servidor
- `db_user = odoo`: Usuari creat anteriorment
- `db_password = false`: Sense contrasenya (autenticació per usuari del sistema)

**Aplicació web:**
- `admin_passwd`: Contrasenya mestra per gestionar bases de dades
- `xmlrpc_port = 8069`: Port principal de la interfície web
- `longpolling_port = 8072`: Port per a notificacions en temps real

**Addons i dades:**
- `addons_path`: Rutes separades per comes on Odoo busca mòduls
- `data_dir`: Directori per a filestore, sessions i cache

**Logging:**
- `logfile`: Ubicació del fitxer de log
- `log_level = info`: Nivell de detall dels logs
- `logrotate = True`: Rotació automàtica de logs

**Rendiment:**
- `workers = 0`: Mode single-thread per a desenvolupament/proves
- `limit_memory_*`: Límits de memòria per procés
- `limit_time_*`: Timeouts per a operacions

### Configuració de logrotate

```bash
# Configurar rotació automàtica de logs
sudo tee /etc/logrotate.d/odoo > /dev/null <<'EOF'
/var/log/odoo/*.log {
    daily
    missingok
    rotate 14
    compress
    delaycompress
    notifempty
    create 0640 odoo odoo
    postrotate
        systemctl reload odoo
    endscript
}
EOF
```

**Explicació de logrotate:**

- `daily`: Rotació diària dels logs
- `rotate 14`: Mantenir 14 versions anteriors
- `compress`: Comprimir logs antics
- `create 0640 odoo odoo`: Crear nous logs amb permisos específics
- `postrotate`: Recarregar el servei després de la rotació

(6-servei-systemd)=
## 6) Servei systemd

### Creació del fitxer de servei

```bash
# Crear servei systemd per a Odoo
sudo tee /etc/systemd/system/odoo.service > /dev/null <<'EOF'
[Unit]
Description=Odoo ERP and CRM
Documentation=https://www.odoo.com/documentation/16.0/
After=network.target postgresql.service
Wants=postgresql.service

[Service]
Type=simple
User=odoo
Group=odoo
WorkingDirectory=/opt/odoo

Environment=PATH="/opt/odoo/odoo-venv/bin:$PATH"
ExecStart=/opt/odoo/odoo-venv/bin/python /opt/odoo/odoo16/odoo-bin -c /etc/odoo/odoo.conf

# Gestió de processos
Restart=on-failure
RestartSec=10
KillMode=mixed
KillSignal=SIGINT
TimeoutStopSec=60

# Seguretat
NoNewPrivileges=true
PrivateTmp=true
ProtectSystem=strict
ReadWritePaths=/var/log/odoo /var/lib/odoo /opt/odoo/custom-addons

# Recursos
LimitNOFILE=65535

[Install]
WantedBy=multi-user.target
EOF
```

**Explicació avançada del servei systemd:**

**Secció [Unit]:**
- `After=network.target postgresql.service`: Odoo s'inicia després de la xarxa i PostgreSQL
- `Wants=postgresql.service`: Prefereix que PostgreSQL estigui actiu, però no és obligatori

**Secció [Service]:**
- `WorkingDirectory`: Directori de treball per al procés
- `Environment=PATH`: Assegura que s'usa l'entorn virtual Python
- `ExecStart`: Comando complet d'inici amb intèrpret específic

**Gestió de processos:**
- `Restart=on-failure`: Reinicia automàticament si falla
- `RestartSec=10`: Espera 10 segons abans de reiniciar
- `KillMode=mixed`: Envia SIGTERM al procés principal i SIGKILL als fills
- `TimeoutStopSec=60`: Màxim 60 segons per aturar el servei

**Seguretat avançada:**
- `NoNewPrivileges=true`: Evita escalada de privilegis
- `PrivateTmp=true`: Directori /tmp privat per al servei
- `ProtectSystem=strict`: Sistema de fitxers de només lectura
- `ReadWritePaths`: Només aquestes rutes són escribibles

### Activació i gestió del servei

```bash
# Recarregar configuració de systemd
sudo systemctl daemon-reload

# Activar el servei per a inici automàtic
sudo systemctl enable odoo

# Iniciar el servei
sudo systemctl start odoo

# Verificar l'estat del servei
sudo systemctl status odoo

# Seguir logs en temps real
sudo journalctl -u odoo -f
```

### Ordres útils per a la gestió

```bash
# Operacions bàsiques del servei
sudo systemctl start odoo      # Iniciar
sudo systemctl stop odoo       # Aturar
sudo systemctl restart odoo    # Reiniciar
sudo systemctl reload odoo     # Recarregar configuració

# Informació i debugging
sudo systemctl status odoo     # Estat actual
sudo journalctl -u odoo        # Logs del servei
sudo journalctl -u odoo --since "1 hour ago"  # Logs recent

# Configuració d'inici
sudo systemctl enable odoo     # Activar inici automàtic
sudo systemctl disable odoo    # Desactivar inici automàtic
sudo systemctl is-enabled odoo # Verificar si està activat
```

(checklist-de-verificació-de-la-instal·lació)=
## Checklist de verificació de la instal·lació

:::{admonition} ✅ Verificació completa del sistema
:class: success
Abans de considerar la instal·lació completa, verifica tots aquests punts:

**🔧 Sistema base:**
```bash
# Verificacions del sistema
lsb_release -a                    # Versió d'Ubuntu
sudo apt list --upgradable        # Actualitzacions pendents
df -h                             # Espai en disc disponible
free -h                           # Memòria disponible
```

**👤 Usuari i permisos:**
```bash
id odoo                           # Informació de l'usuari
ls -la /opt/odoo                  # Permisos del directori
sudo -u odoo whoami               # Test d'execució com usuari odoo
```

**🐘 PostgreSQL:**
```bash
sudo systemctl status postgresql  # Estat del servei
sudo -u postgres psql -c "\du"   # Llistar usuaris PostgreSQL
sudo -u postgres psql -c "SELECT version();"  # Versió PostgreSQL
```

**🐍 Odoo:**
```bash
ls /opt/odoo/odoo16/odoo-bin      # Executable principal d'Odoo
/opt/odoo/odoo-venv/bin/python --version  # Versió Python de l'entorn virtual
/opt/odoo/odoo-venv/bin/pip list | grep psycopg2  # Dependències crítiques
cat /etc/odoo/odoo.conf           # Configuració d'Odoo
```

**⚙️ Servei systemd:**
```bash
sudo systemctl status odoo        # Estat del servei
sudo netstat -tlnp | grep 8069   # Port 8069 en escolta
sudo journalctl -u odoo --no-pager | tail -10  # Últims logs
```

**🌐 Accés web:**
```bash
curl -I http://localhost:8069     # Test de connexió HTTP
curl -s http://localhost:8069/web/database/selector | grep -i odoo  # Pàgina d'Odoo
```

**Si tots els punts anterior funcionen correctament, la instal·lació és exitosa! 🎉**
:::

### Tests específics de funcionament

```bash
#!/bin/bash
# test-odoo-installation.sh - Script de verificació automàtica

echo "🔍 Verificant instal·lació d'Odoo..."

# Test 1: Usuari i permisos
echo -n "👤 Usuari odoo: "
if id odoo >/dev/null 2>&1; then
    echo "✅ OK"
else
    echo "❌ FALLA"
    exit 1
fi

# Test 2: PostgreSQL
echo -n "🐘 PostgreSQL: "
if sudo systemctl is-active --quiet postgresql; then
    echo "✅ OK"
else
    echo "❌ FALLA"
    exit 1
fi

# Test 3: Usuari PostgreSQL
echo -n "🔑 Usuari PostgreSQL odoo: "
if sudo -u postgres psql -tAc "SELECT 1 FROM pg_roles WHERE rolname='odoo'" | grep -q 1; then
    echo "✅ OK"
else
    echo "❌ FALLA"
    exit 1
fi

# Test 4: Fitxers d'Odoo
echo -n "📁 Codi font Odoo: "
if [ -f "/opt/odoo/odoo16/odoo-bin" ]; then
    echo "✅ OK"
else
    echo "❌ FALLA"
    exit 1
fi

# Test 5: Entorn virtual
echo -n "🐍 Entorn virtual Python: "
if [ -f "/opt/odoo/odoo-venv/bin/python" ]; then
    echo "✅ OK"
else
    echo "❌ FALLA"
    exit 1
fi

# Test 6: Dependències Python
echo -n "📦 Dependències Python: "
if /opt/odoo/odoo-venv/bin/pip show psycopg2 >/dev/null 2>&1; then
    echo "✅ OK"
else
    echo "❌ FALLA"
    exit 1
fi

# Test 7: Configuració
echo -n "⚙️ Fitxer de configuració: "
if [ -f "/etc/odoo/odoo.conf" ] && [ -r "/etc/odoo/odoo.conf" ]; then
    echo "✅ OK"
else
    echo "❌ FALLA"
    exit 1
fi

# Test 8: Servei systemd
echo -n "🔧 Servei systemd: "
if systemctl is-enabled --quiet odoo; then
    echo "✅ OK"
else
    echo "❌ FALLA"
    exit 1
fi

# Test 9: Servei actiu
echo -n "🚀 Servei en execució: "
if sudo systemctl is-active --quiet odoo; then
    echo "✅ OK"
else
    echo "❌ FALLA - Intentant iniciar..."
    sudo systemctl start odoo
    sleep 5
    if sudo systemctl is_active --quiet odoo; then
        echo "✅ OK (iniciat)"
    else
        echo "❌ FALLA"
        echo "Logs del servei:"
        sudo journalctl -u odoo --no-pager -n 10
        exit 1
    fi
fi

# Test 10: Port accessible
echo -n "🌐 Port 8069 accessible: "
if ss -tlnp | grep -q ":8069"; then
    echo "✅ OK"
else
    echo "❌ FALLA"
    exit 1
fi

# Test 11: Resposta HTTP
echo -n "📡 Resposta HTTP: "
if curl -s -f http://localhost:8069/web/database/selector >/dev/null; then
    echo "✅ OK"
else
    echo "❌ FALLA"
    exit 1
fi

echo ""
echo "🎉 Instal·lació verificada correctament!"
echo "🔗 Accés: http://$(hostname -I | awk '{print $1}'):8069"
echo ""
echo "📋 Informació del sistema:"
echo "   - Usuari Odoo: $(id odoo)"
echo "   - Versió PostgreSQL: $(sudo -u postgres psql -tAc 'SELECT version()' | head -1)"
echo "   - Versió Python: $(/opt/odoo/odoo-venv/bin/python --version)"
echo "   - Estat del servei: $(sudo systemctl is-active odoo)"
```

### Primer accés a Odoo

1. **Obrir navegador** i accedir a: `http://IP_SERVIDOR:8069`

2. **Pantalla de gestió de bases de dades:**

```{image} /_static/assets/img/Tema2/img2_T2_1.png
:alt: Pantalla d'inici d'Odoo
:width: 70%
:align: center
```

3. **Crear primera base de dades:**
   - **Nom de la base de dades**: `production` o `test`
   - **Email**: Administrador principal
   - **Contrasenya**: Contrasenya de l'administrador
   - **Idioma**: Català/Castellà
   - **País**: Espanya
   - **Dades de demostració**: Desmarcada per entorns de producció

4. **Configuració inicial:**
   - Seleccionar aplicacions a instal·lar
   - Configurar informació de l'empresa
   - Personalitzar la interfície

(7-configuració-dapache-com-a-reverse-proxy-opcional)=
## 7) Configuració d'Apache com a reverse proxy (Opcional)

Per a entorns de producció, és altament recomanable utilitzar Apache com a reverse proxy davant d'Odoo. Aquesta configuració proporciona beneficis significatius en seguretat, rendiment i gestió.

:::{admonition} 📖 Configuració Apache detallada
:class: note
La configuració completa d'Apache com a reverse proxy és un tema extens que inclou:

- Instal·lació i configuració d'Apache
- Configuració SSL/TLS amb Let's Encrypt
- Capçaleres de seguretat per a compliment RGPD
- Optimització de rendiment i cache
- Load balancing per a alta disponibilitat
- Monitoratge i logging avançat
- Resolució de problemes habituals

**📋 Documentació completa:** [Annex A: Apache com a Reverse Proxy per a Odoo](Apache_ReverseProxy.md)
:::

### Avantatges del reverse proxy

| **Aspect** | **Benefici** |
|------------|-------------|
| **Seguretat** | Terminació SSL, ocultació del backend, filtratge de peticions |
| **Rendiment** | Cache de contingut estàtic, compressió, gestió eficient de connexions |
| **Escalabilitat** | Load balancing, gestió de múltiples instàncies |
| **Manteniment** | Logs centralitzats, certificats unificats, zero downtime |

### Configuració ràpida (resum)

```bash
# Instal·lació bàsica d'Apache
sudo apt-get install -y apache2

# Activar mòduls necessaris
sudo a2enmod proxy proxy_http ssl headers rewrite

# Configuració bàsica de VirtualHost
sudo tee /etc/apache2/sites-available/odoo.conf > /dev/null <<'EOF'
<VirtualHost *:80>
    ServerName odoo.empresa.com
    
    ProxyPreserveHost On
    ProxyRequests Off
    
    ProxyPass /longpolling/ http://127.0.0.1:8072/
    ProxyPassReverse /longpolling/ http://127.0.0.1:8072/
    
    ProxyPass / http://127.0.0.1:8069/
    ProxyPassReverse / http://127.0.0.1:8069/
    
    ErrorLog ${APACHE_LOG_DIR}/odoo_error.log
    CustomLog ${APACHE_LOG_DIR}/odoo_access.log combined
</VirtualHost>
EOF

# Activar site i reiniciar Apache
sudo a2ensite odoo
sudo systemctl restart apache2
```

## Resolució de problemes habituals

### Problemes amb el servei

**🔧 El servei no s'inicia:**

```bash
# Verificar logs detallats
sudo journalctl -u odoo -f

# Comprovar configuració
sudo -u odoo /opt/odoo/odoo-venv/bin/python /opt/odoo/odoo16/odoo-bin -c /etc/odoo/odoo.conf --test-enable

# Verificar permisos
ls -la /etc/odoo/odoo.conf
ls -la /var/log/odoo/
```

**🔧 Error de connexió a PostgreSQL:**

```bash
# Verificar estat de PostgreSQL
sudo systemctl status postgresql

# Test de connexió manual
sudo -u odoo psql -h localhost -U odoo -l

# Verificar configuració pg_hba.conf
sudo nano /etc/postgresql/*/main/pg_hba.conf
```

**🔧 Port 8069 no accessible:**

```bash
# Verificar que el servei escolta
sudo netstat -tlnp | grep 8069

# Comprovar firewall
sudo ufw status
sudo iptables -L

# Test local
curl -I http://localhost:8069
```

### Problemes de rendiment

**🔧 Odoo va lent:**

```bash
# Verificar recursos
htop
free -h
df -h

# Optimitzar PostgreSQL
sudo -u postgres psql -c "VACUUM ANALYZE;"

# Revisar configuració de workers
sudo nano /etc/odoo/odoo.conf
```

### Problemes de permisos

**🔧 Errors de permisos de fitxers:**

```bash
# Corregir permisos d'Odoo
sudo chown -R odoo:odoo /opt/odoo
sudo chown -R odoo:odoo /var/log/odoo
sudo chown -R odoo:odoo /var/lib/odoo

# Verificar permisos de configuració
sudo chown odoo:odoo /etc/odoo/odoo.conf
sudo chmod 640 /etc/odoo/odoo.conf
```

## Manteniment i actualitzacions

### Backups regulars

```bash
#!/bin/bash
# backup-odoo.sh - Script de backup bàsic

BACKUP_DIR="/backup/odoo"
DATE=$(date +%Y%m%d_%H%M%S)

mkdir -p $BACKUP_DIR

# Backup base de dades
sudo -u postgres pg_dump odoo_production > $BACKUP_DIR/db_$DATE.sql

# Backup filestore
tar czf $BACKUP_DIR/filestore_$DATE.tar.gz -C /var/lib/odoo filestore/

# Backup configuració
tar czf $BACKUP_DIR/config_$DATE.tar.gz /etc/odoo/ /opt/odoo/custom-addons/

echo "Backup completat: $DATE"
```

### Actualització d'Odoo

```bash
# Backup abans d'actualitzar
sudo systemctl stop odoo
sudo -u postgres pg_dump odoo_production > /backup/pre-update-$(date +%Y%m%d).sql

# Actualitzar codi
sudo -u odoo -H bash -c '
    cd /opt/odoo/odoo16
    git pull origin 16.0
'

# Actualitzar dependències
sudo -u odoo -H bash -c '
    source /opt/odoo/odoo-venv/bin/activate
    pip install --upgrade -r /opt/odoo/odoo16/requirements.txt
    deactivate
'

# Actualitzar base de dades
sudo -u odoo /opt/odoo/odoo-venv/bin/python /opt/odoo/odoo16/odoo-bin -c /etc/odoo/odoo.conf -u all -d odoo_production --stop-after-init

# Reiniciar servei
sudo systemctl start odoo
```

### Monitoratge bàsic

```bash
# Script de monitoratge simple
#!/bin/bash
# monitor-odoo.sh

echo "=== Monitor Odoo $(date) ==="

# Estat del servei
echo "Servei Odoo: $(sudo systemctl is-active odoo)"

# Ús de recursos
echo "CPU: $(top -bn1 | grep "Cpu(s)" | awk '{print $2}' | sed 's/%us,//')"
echo "RAM: $(free -h | grep Mem | awk '{print $3 "/" $2}')"

# Connexions actives
echo "Connexions HTTP: $(sudo netstat -an | grep ":8069" | grep ESTABLISHED | wc -l)"

# Logs recents d'error
echo "Errors recents:"
sudo tail -n 5 /var/log/odoo/odoo.log | grep ERROR || echo "Cap error recent"
```

## Conclusions

La instal·lació tradicional d'Odoo proporciona:

### ✅ Avantatges aconseguits

- **Control total** sobre la configuració i l'entorn
- **Rendiment òptim** sense overhead de contenidors
- **Flexibilitat màxima** per a personalitzacions
- **Integració nativa** amb el sistema operatiu
- **Debugging facilititat** amb accés directe als components

### 📚 Coneixements adquirits

Durant aquest procés has après:

- Gestió d'usuaris i permisos en Linux
- Configuració de PostgreSQL per a aplicacions web
- Entorns virtuals Python i gestió de dependències
- Serveis systemd i automatització
- Conceptes de reverse proxy i arquitectura web
- Estratègies de backup i manteniment

### 🚀 Pròxims passos recomanats

1. **Explorar l'Annex A** per configurar Apache com a reverse proxy
2. **Implementar SSL/TLS** per a connexions segures
3. **Configurar backups automàtics** amb programació cron
4. **Monitoritzar el rendiment** i optimitzar segons l'ús
5. **Documentar la configuració** específica del teu entorn

Aquesta base sòlida et permet desenvolupar i mantenir un sistema Odoo professional en entorns de producció. 🎯
