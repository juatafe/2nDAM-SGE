# Tema 4. Organització i consulta de la informació

```{toctree}
:maxdepth: 2
:caption: Continguts del Tema 4
:hidden:

```

## Introducció

En el **Tema 3** hem automatitzat completament la instal·lació d’Odoo en una màquina virtual mitjançant Docker.  A hores d’ara ja disposem d’un servidor amb tres contenidors principals:

- **Odoo** (aplicació web)  
- **PostgreSQL** (base de dades)  
- **MailHog** (servidor de correu de proves)

Ara anem un pas més enllà: aprendrem a **consultar directament la base de dades d’Odoo** utilitzant un client gràfic anomenat **pgAdmin**, i també veurem com identificar les taules i camps on Odoo desa la informació.

---

## 🎯 Objectius

- Entendre com es connecta Odoo a la seua base de dades PostgreSQL.  
- Configurar un accés remot **persistent** al contenidor de base de dades.  
- Instal·lar i configurar **pgAdmin** a la màquina virtual.  
- Visualitzar taules, dades i usuaris de PostgreSQL.  
- Comprendre la correspondència entre models d’Odoo i taules SQL.

---

## 🧩 Accés a la base de dades amb pgAdmin

Odoo utilitza **PostgreSQL** com a sistema gestor de base de dades (SGBD).  
Les dades de clients, productes, factures, etc., s’emmagatzemen en **centenars de taules** dins del contenidor `db`.  Podem accedir-hi amb dos tipus d’eines:

- **psql** — client de línia d’ordres per a usuaris avançats.  
- **pgAdmin** — client gràfic multiplataforma amb interfície visual.

---

### 🔧 Configuració persistent per a la connexió remota

Per defecte, PostgreSQL només accepta connexions locals.  A més, si modifiquem els fitxers de configuració **dins del contenidor**, aquests canvis **no són persistents**: es perden cada vegada que es recrea el contenidor. Per això, en el nostre **script d’automatització (`setup_odoo.sh`)** hem afegit un pas per crear una carpeta amb els fitxers de configuració de PostgreSQL i incloure-la com a volum en el directori especial `/docker-entrypoint-initdb.d`.  
D’aquesta manera, els fitxers s’apliquen automàticament **la primera vegada que s’inicialitza la base de dades** i es conserven després, sense interferir amb el volum de dades (`/var/lib/postgresql/data`).

#### Just abans de la línia on es crea el docker-compose.yml, afegeix aquest bloc:
```bash
# Carpeta de configuració persistent per a PostgreSQL
mkdir -p "$PROJECT_DIR/db_config"

# Crear fitxers de configuració per defecte si no existeixen
if [ ! -f "$PROJECT_DIR/db_config/pg_hba.conf" ]; then
cat > "$PROJECT_DIR/db_config/pg_hba.conf" <<'EOF'
# TYPE  DATABASE        USER            ADDRESS                 METHOD
local   all             all                                     peer
host    all             all             127.0.0.1/32            md5
host    all             all             ::1/128                 md5
# Connexions des de qualsevol IP amb contrasenya
host    all             all             0.0.0.0/0               md5
EOF
fi

if [ ! -f "$PROJECT_DIR/db_config/postgresql.conf" ]; then
cat > "$PROJECT_DIR/db_config/postgresql.conf" <<'EOF'
listen_addresses = '*'
max_connections = 100
shared_buffers = 128MB
logging_collector = on
log_directory = '/var/lib/postgresql/data/logs'
log_filename = 'postgresql.log'
EOF
fi
```

---

#### 1️⃣ Creació automàtica de la carpeta `db_config`

L’script crea aquesta estructura dins del projecte:

```
~/odoo_server/db_config/
```

I genera automàticament dos fitxers si no existeixen:  
`pg_hba.conf` i `postgresql.conf` (vegeu el contingut anterior).

> 🧠 **Per què és necessari?**  
> Sense aquesta carpeta externa, els fitxers de configuració estarien dins del contenidor i es perdrien en qualsevol reconstrucció. Amb aquest volum, Docker pot reaplicar la configuració i permet conservar-la entre reinicis.

---

#### 2️⃣ Modificació del `docker-compose.yml`

En el servei `db`, s’ha afegit el muntatge de la carpeta `db_config` com a volum:

```yaml
  db:
    image: postgres:latest
    environment:
      - POSTGRES_DB=postgres
      - POSTGRES_PASSWORD=myodoo
      - POSTGRES_USER=odoo
      - PGDATA=/var/lib/postgresql/data/pgdata
    ports:
      - "5432:5432"
    volumes:
      # Carpeta de dades (persistent)
      - odoo-db-data:/var/lib/postgresql/data/pgdata
      # Fitxers de configuració inicials (s'apliquen només en la primera inicialització)
      - ./db_config:/docker-entrypoint-initdb.d
    restart: always
```


:::{admonition} Com funciona `/docker-entrypoint-initdb.d` en PostgreSQL (Docker)
:class: tip

Quan s’utilitza la **imatge oficial de PostgreSQL** en Docker, aquesta incorpora un script d’entrada que s’executa automàticament cada vegada que arranca el contenidor.  Aquest script comprova si el volum de dades (📂 `/var/lib/postgresql/data`) està **buit** — és a dir, si la base de dades encara no existeix.

Si és la **primera inicialització**, PostgreSQL:

1️⃣ Llig tots els fitxers que hi haja al directori especial `/docker-entrypoint-initdb.d`.  
2️⃣ Executa automàticament:
   - Els `.sh` com a scripts de shell.  
   - Els `.sql` amb el client `psql`.  
   - I **copia** els fitxers `.conf` (com `postgresql.conf` o `pg_hba.conf`) al seu lloc dins `/var/lib/postgresql/data/`. 
 
3️⃣ Una vegada inicialitzada la base de dades, aquest procés **no es torna a repetir** fins que s’esborre el volum.

📦 **Això vol dir que:**
- Pots inicialitzar PostgreSQL amb configuracions pròpies sense tocar la imatge base.  
- Els canvis dins `db_config/` només s’apliquen en la **primera execució** (quan encara no hi ha dades).  
- Si vols reaplicar-los, pots eliminar el volum de dades amb:
  ```bash
  docker compose down -v
  docker compose up -d
  ```


>💡 Resum:
>El directori `/docker-entrypoint-initdb.d` és com una “carpeta de scripts d’inicialització”. Només actua la primera vegada, abans que PostgreSQL cree la seua base de dades interna, i et permet automatitzar la configuració sense tocar el contenidor manualment.


:::


> ⚠️ Si edites els fitxers dins del contenidor (i no al volum `db_config`), aquests canvis es perdran.  
> Per això sempre és recomanable mantindre `pg_hba.conf` i `postgresql.conf` **fora del contenidor** (a `~/odoo_server/db_config/`).  


```{dropdown} 🔧  **Si necessites modificar-los temporalment des de dins del contenidor**, pots seguir aquests passos:
:icon: wrench
:class: dropdown

> 1️⃣ **Accedeix al contenidor de PostgreSQL:**
> ```bash
> docker exec -it odoo_server-db-1 bash
> ```
> 2️⃣ **Edita els fitxers de configuració** a `/var/lib/postgresql/data/`:
> - `pg_hba.conf`
> - `postgresql.conf`
>
> 3️⃣ **Afegeix al fitxer `pg_hba.conf`:**
> ```bash
> host all all 0.0.0.0/0 md5
> ```
> (Permet connexions remotes autenticades amb contrasenya.)
>
> 4️⃣ **Modifica `postgresql.conf`** i assegura’t que conté:
> ```bash
> listen_addresses = '*'
> ```
> (El servidor escoltarà peticions des de qualsevol IP.)
>
> 5️⃣ **Reinicia el contenidor per aplicar els canvis:**
> ```bash
> exit
> docker restart odoo_server-db-1
> ```
> 🔁 Recorda: aquests canvis **no són persistents** — es perdran si el contenidor es recrea.  
> Per fer-los permanents, cal aplicar-los als fitxers del volum `~/odoo_server/db_config/`.

```

Ara el contenidor `db` acceptarà connexions externes pel port **5432**, i la configuració es mantindrà fins i tot després de reinicis o reconstruccions.



---

#### 3️⃣ Reinici del servei PostgreSQL

Hi ha dues situacions possibles:

- **Recreació completa:**  
  Si has modificat `setup_odoo.sh` o vols reiniciar completament la configuració:
  ```bash
  cd ~/odoo_server
  docker compose down -v
  ./setup_odoo.sh
  ```
  Això eliminarà el volum persistent i generarà una base de dades neta amb la nova configuració.

- **Només reiniciar el contenidor:**  
  Si només has canviat els fitxers `db_config`:
  ```bash
  cd ~/odoo_server
  docker compose restart db
  # o, si cal, força la recreació:
  docker compose up -d --force-recreate db
  ```

---

## 💻 Instal·lació de pgAdmin en Ubuntu (sense entorn gràfic)

Com que treballem dins d’una **màquina virtual Ubuntu 24.04** sense interfície gràfica, no podem instal·lar la versió d’escriptori de pgAdmin.  En el seu lloc, instal·larem la **versió web (pgAdmin4)**, que es gestiona des del navegador.

### 1️⃣ Instal·lar dependències bàsiques

Actualitzem els paquets i instal·lem les dependències necessàries:

```bash
sudo apt update
sudo apt install -y curl ca-certificates gnupg
```

---

### 2️⃣ Afegir el repositori oficial de pgAdmin

Descarreguem i registrem la clau pública del repositori de PostgreSQL:

```bash
curl https://www.pgadmin.org/static/packages_pgadmin_org.pub | sudo gpg --dearmor -o /usr/share/keyrings/pgadmin-keyring.gpg
```

Afegim el repositori a la nostra llista d’orígens:

```bash
echo "deb [signed-by=/usr/share/keyrings/pgadmin-keyring.gpg] https://ftp.postgresql.org/pub/pgadmin/pgadmin4/apt/noble pgadmin4 main" | sudo tee /etc/apt/sources.list.d/pgadmin4.list > /dev/null
```

> 🧩 *Nota:* en Ubuntu 24.04 el nom en clau és **noble**, per això usem aquest valor.

---

### 3️⃣ Instal·lar pgAdmin4 en mode servidor

```bash
sudo apt update
sudo apt install -y pgadmin4-web
```

>💡 Nota important (Ubuntu 24.04 “noble”):
>La instal·lació del paquet no llança automàticament l’assistent de configuració del servidor web. Cal executar-lo manualment amb la següent ordre:

```bash
sudo /usr/pgadmin4/bin/setup-web.sh
```

Durant aquest procés:
  - Se’t demanarà crear un usuari administrador (adreça de correu i contrasenya).
  - Es configurarà automàticament Apache i el mòdul wsgi per a servir pgAdmin4.
  - El sistema et preguntarà si vols reiniciar Apache per aplicar els canvis.

Quan tot acabe correctament, apareixerà un missatge com aquest:

```bash
Apache successfully restarted. You can now start using pgAdmin 4 in web mode at http://127.0.0.1/pgadmin4
```


:::{dropdown}  💾 Espai esgotat en la màquina virtual: com ampliar el disc LVM (Ubuntu)
:icon: wrench
:class: dropdown
:class: tip

És molt habitual que aparega l’error:

  ```bash
  sqlite3.OperationalError: database or disk is full
  ``` 

encara que el disc virtual (.vdi) tinga molts GB disponibles.  
Això passa perquè **Ubuntu instal·la per defecte amb LVM**, i el volum lògic del sistema (`ubuntu-lv`) només ocupa una part del disc virtual.

---

### 🧩 1️⃣ Comprovació inicial

Mostra l’espai real utilitzat dins la màquina virtual:

```bash
df -h
```

Si veus alguna línia com:

```bash
/dev/mapper/ubuntu--vg-ubuntu--lv   11G   11G     0 100% /
```

vol dir que el volum lògic només té 11 GB encara que el `.vdi` siga més gran (p. ex. 25 GB).

---

### ⚙️ 2️⃣ Ampliar el volum lògic per utilitzar tot l’espai del disc

Executa aquestes ordres dins de la màquina virtual:

```bash
sudo lvextend -l +100%FREE /dev/ubuntu-vg/ubuntu-lv
sudo resize2fs /dev/ubuntu-vg/ubuntu-lv
```

- `lvextend` assigna tot l’espai lliure del disc al volum lògic.  
- `resize2fs` expandeix el sistema de fitxers per aprofitar-lo.

---

### ✅ 3️⃣ Verifica l’expansió

Torna a comprovar l’espai amb:

```bash
df -h
```

Ara hauries de veure alguna cosa semblant a:

```bash
/dev/mapper/ubuntu--vg-ubuntu--lv   25G   11G   14G   45% /
```

A partir d’aquest moment el sistema ja disposa de tot l’espai del disc virtual.

---

### 💡 4️⃣ En cas de no tindre més espai assignat al disc virtual

Si continues al 100 %, pots **augmentar la mida del `.vdi`** des de VirtualBox:

1. Apaga la màquina virtual.  
2. En **Configuració → Emmagatzematge → Dispositiu SATA → OdooServer-Docker.vdi**, augmenta la mida (p. ex. de 25 GB a 40 GB).  
3. Torna a iniciar la VM i repeteix els passos anteriors (`lvextend` i `resize2fs`).

---

Amb això, el teu Ubuntu aprofitarà tot l’espai disponible i deixarà d’aparéixer l’error `database or disk is full` en pgAdmin4 o altres aplicacions.
:::
---

## 4️⃣ Accedir a pgAdmin4 des del navegador

Una vegada finalitzada la configuració amb `sudo /usr/pgadmin4/bin/setup-web.sh`, podem obrir pgAdmin4 des del navegador web dins de la màquina virtual (si té entorn gràfic) o des del nostre ordinador amfitrió mitjançant **redirecció de ports**.

---

### 🧭 Cas 1: Xarxa NAT amb redirecció de ports (VirtualBox)

Com que la màquina virtual està configurada en **mode NAT**, cal crear una regla de redirecció per permetre l’accés al port `8080` (pgAdmin4) des del nostre ordinador host.

A VirtualBox:
1️⃣ Obri la configuració de la màquina virtual → **Xarxa → Avançat → Redirecció de ports**  
2️⃣ Afig una nova regla:

| Nom         | Protocol | IP de l’amfitrió | Port de l’amfitrió | IP del client | Port del client |
|--------------|-----------|-----------------|--------------------|----------------|-----------------|
| pgadmin4     | TCP       | 127.0.0.1       | 8080               | 10.0.2.15      | 80           |

> 💡 Això permet que quan accedim a `http://127.0.0.1:8080` al nostre navegador, el trànsit es redirigisca al port `80` de la màquina virtual (10.0.2.15).

```{image} /_static/assets/img/Tema4/pgadmin-4.png
:alt: pgadmin-4
:width: 80%
:align: center
```

---

### 🧭 Cas 2: Xarxa pont (bridged)

Si la màquina virtual està en xarxa **bridged (pont)**, simplement accedim directament a la seua IP dins de la xarxa local.

👉 Exemple:
:::bash
http://192.168.56.10:8080/pgadmin4
:::

---

### 🔐 Autenticació

Autentica’t amb l’usuari creat durant el procés de configuració (`setup-web.sh`):

- **Usuari (email):** el que vas introduir durant la configuració  
- **Contrasenya:** la que vas definir

Després d’iniciar sessió, ja podràs afegir una connexió al servidor PostgreSQL del teu entorn Docker (contenidor `db`).

---

### ⚙️ Exemple d’accés des del host

Amb la redirecció de ports configurada com a dalt, des del teu navegador (al teu ordinador host) pots accedir-hi amb:

:::bash
http://127.0.0.1:8080/pgadmin4
:::

Això obrirà la interfície web de pgAdmin4, servida per la màquina virtual Ubuntu mitjançant Apache i WSGI.

---

### 5️⃣ Connexió amb el contenidor de PostgreSQL

```{image} /_static/assets/img/Tema4/pgadminnuevo.png
:alt: pgadminnuevo
:width: 80%
:align: center
```

Una vegada dins de pgAdmin4, creem una nova connexió amb el servidor Docker:

- **Nom:** Odoo Docker  
- **Host:** `localhost` o la IP de la màquina virtual  
- **Port:** `5432`  
- **Usuari:** `odoo`  
- **Contrasenya:** `myodoo` (segons el `docker-compose.yml`).

Amb això, ja podem explorar la base de dades `cpa` creada per Odoo dins del contenidor PostgreSQL.


```{image} /_static/assets/img/Tema4/pgadminnuevoconfig.png
:alt: pgadminnuevoconfig
:width: 80%
:align: center
```

---
### 🧭 Interfície de pgAdmin4

Quan accedim a pgAdmin4, podem vore totes les bases de dades disponibles dins del servidor PostgreSQL.  
Per defecte, apareixen dues:

| Nom de la base de dades | Origen | Funció | Pots esborrar-la? |
|--------------------------|---------|--------|-------------------|
| **postgres** | Base de dades creada automàticament per PostgreSQL | S’utilitza per a connexions administratives o proves. No conté dades d’Odoo. | ❌ No recomanat |
| **cpa** | Base de dades creada per Odoo en la instal·lació inicial | Conté totes les taules, esquemes i dades reals del projecte Odoo. | ✅ És la base principal |

> ⚠️ **Atenció:** no confongues la base `postgres` amb la base del projecte Odoo.  
> Totes les dades útils es troben dins de la base **`cpa`**.

---

### 📊 Panell de control de pgAdmin

Des de la pestanya **Tablero** (Dashboard), pgAdmin mostra informació en temps real sobre l’activitat de la base de dades:

- **Sessions actives** i connexions obertes.  
- **Transaccions per segon** (cometre/retrocedir).  
- **Lectures i escriptures** de blocs de dades.  
- **Insercions, actualitzacions i esborrats** recents.

```{image} /_static/assets/img/Tema4/pgadmintablero.png
:alt: pgadmintablero
:width: 100%
:align: center
```

> 💡 Aquesta vista és molt útil per comprovar si Odoo està interactuant correctament amb la base de dades: cada vegada que un usuari inicia sessió o crea un registre, veuràs activitat al gràfic.


> 💡 **Avantatge:** la versió web de pgAdmin és molt més lleugera i permet treballar en màquines sense entorn gràfic, accedint-hi fàcilment des d’un navegador o des d’una altra màquina de la mateixa xarxa.

> ⚠️ Nota important sobre la xarxa (NAT + port forwarding)
> - Estem en una màquina virtual amb NAT i redirecció de ports. Des del teu ordinador accedeixes sempre per localhost (host), i el hipervisor redirigeix cap a la VM.
> - Perquè la redirecció funcione, dins de la VM els serveis han d’escoltar a 0.0.0.0 (o a la IP de la interfície), no només a 127.0.0.1.
> - La millor recomanació de seguretat en aquest escenari és limitar la redirecció del costat host a 127.0.0.1 perquè només el teu equip puga entrar, i dins de la VM restringir l’origen amb UFW i pg_hba.conf.

### 📋 Exploració de la base de dades d’Odoo

Una vegada connectats, veurem totes les bases de dades disponibles.  
Seleccionem la que hem creat (per exemple, `cpa`) per explorar-ne les taules:

```{image} /_static/assets/img/Tema4/img4-T4.png
:alt: img4-T4
:width: 100%
:align: center
```

Odoo utilitza un esquema per a cada mòdul instal·lat:  
- Les taules del mòdul *website* comencen per `website_`.  
- Les del mòdul *sale* per `sale_`.  
- Les del mòdul *crm* per `crm_`, etc.

```{image} /_static/assets/img/Tema4/img5-T4.png
:alt: img5-T4
:width: 100%
:align: center
```

Podem veure els **camps de cada taula**:

```{image} /_static/assets/img/Tema4/img6-T4.png
:alt: img6-T4
:width: 100%
:align: center
```

I també **consultar les dades** fent la consulta corresponent:

```{image} /_static/assets/img/Tema4/img8-T4.png
:alt: img8-T4
:width: 100%
:align: center
```

Així visualitzem, per exemple, els productes registrats a Odoo.

---

### 👥 Gestió d’usuaris de PostgreSQL

També podem veure i modificar els usuaris existents des del menú lateral:

```{image} /_static/assets/img/Tema4/img9_T4.png
:alt: img9_T4
:width: 25%
:align: center
```

L’usuari per defecte amb el qual Odoo es connecta és **odoo**.

```{image} /_static/assets/img/Tema4/img10_T4.png
:alt: img10_T4
:width: 70%
:align: center
```

Des de *Propietats* podem revisar permisos i contrasenyes:

```{image} /_static/assets/img/Tema4/img11-T4.png
:alt: img11-T4
:width: 100%
:align: center
```

---

### 🌐 Consulta des del client web d’Odoo

Finalment, recorda que podem accedir a les mateixes dades també des del **client web d’Odoo**, però de manera estructurada i segura, mitjançant les seues vistes i models.

Odoo segueix el patró **MVC (Model–Vista–Controlador):**

- **Model** → taules SQL (classes Python)  
- **Vista** → fitxers XML que defineixen formularis, llistes o cerques  
- **Controlador** → lògica Python que gestiona les accions de l’usuari

Aquesta arquitectura permet mantenir separats les dades i el disseny de la interfície.

---

## 🧠 Resum

En aquest tema hem aprés a:

- Configurar **PostgreSQL per a connexions remotes persistents**.  
- Utilitzar **pgAdmin** per explorar i administrar la base de dades d’Odoo.  
- Reconéixer les **taules, camps i usuaris principals** del sistema.  
- Entendre la relació entre **models Python i taules SQL** dins d’Odoo.  

Amb tot això, ja pots **analitzar i comprendre les dades internes d’Odoo** tant des del client web com des d’una eina professional com *pgAdmin*.

---
:::{dropdown}  ✅ Configuració recomanada (resum)
:icon: wrench
:class: dropdown
:class: tip 


**1. Regles de port forwarding (VirtualBox/VMware):**  

```{admonition} 💡 Recomanació de xarxa (entorn d’aula — NAT + port forwarding)
:class: note
- Accedeix des del teu ordinador a: `localhost:8069`, `localhost:5050`, `localhost:5432` o `localhost:8025`.  
- En el gestor de la màquina virtual, configura les regles de *port forwarding* amb **Host IP = 127.0.0.1** per a limitar l’accés al teu propi equip.  
- Dins la VM, els serveis poden escoltar a `0.0.0.0` (necessari perquè el trànsit redirigit arribe), però **restringeix l’origen** amb `UFW` i `pg_hba.conf` (per exemple, permetent només `10.0.2.2` en VirtualBox).  
- En entorns externs o de producció, **no uses 0.0.0.0** si no és imprescindible: especifica IPs concretes o utilitza túnels SSH o reverse proxies amb HTTPS i llistes d’IP segures.
```
| Servei | Host IP | Host Port | Guest IP | Guest Port |
|---------|----------|-----------|-----------|-------------|
| Odoo | 127.0.0.1 | 8069 | <IP_VM> | 8069 |
| pgAdmin | 127.0.0.1 | 5050 | <IP_VM> | 5050 |
| PostgreSQL | 127.0.0.1 | 5432 | <IP_VM> | 5432 |
| MailHog | 127.0.0.1 | 8025 | <IP_VM> | 8025 |


```{admonition} ℹ️ Què és la IP 10.0.2.2 en NAT de VirtualBox?
:class: note
- El mode NAT de VirtualBox crea una xarxa virtual `10.0.2.0/24` amb:
  - **VM (guest):** 10.0.2.15 (per defecte)  
  - **Gateway/NAT virtual:** 10.0.2.2  
  - **DNS virtual:** 10.0.2.3  
- Quan redirigeixes ports (p. ex. `127.0.0.1:5432 → 10.0.2.15:5432`), el trànsit que arriba a la VM **té origen 10.0.2.2**.  
- Per això, si configures `pg_hba.conf` o `UFW` dins la VM, **té sentit permetre només 10.0.2.2**, ja que és el “pont” pel qual entra la connexió des del teu host.  
- En canvi, al teu ordinador (host), mantín els serveis limitats a **127.0.0.1**. En xarxes bridged o de producció, ignora 10.0.2.2 i utilitza IPs reals o canals segurs (SSH, HTTPS, IP whitelists).
```


**2. PostgreSQL dins la VM:**
```bash
# postgresql.conf
listen_addresses = '*'

# pg_hba.conf
host  all  all  127.0.0.1/32    md5
host  all  all  10.0.2.2/32     md5   # IP del NAT de VirtualBox
```

**3. Tallafoc (UFW) dins la VM (opcional però recomanat en producció):**

```bash
sudo ufw allow from 10.0.2.2 to any port 5432 proto tcp
sudo ufw allow from 10.0.2.2 to any port 5050 proto tcp
sudo ufw enable
```

> 🧱 En xarxes bridged o producció, evita `0.0.0.0`: exposa només les IP necessàries i usa connexions segures (SSH, HTTPS, IP whitelists).
:::
---