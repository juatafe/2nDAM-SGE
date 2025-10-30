# 🗂️ Tema 4. Organització i consulta de la informació

```{toctree}
:maxdepth: 2
:caption: Continguts del Tema 4
:hidden:

```

## Introducció

En el **Tema 3** hem automatitzat completament la instal·lació d’Odoo en una màquina virtual mitjançant Docker.  
A hores d’ara ja disposem d’un servidor amb tres contenidors principals:

- **Odoo** (aplicació web)
- **PostgreSQL** (base de dades)
- **MailHog** (servidor de correu de proves)

Ara anem un pas més enllà: aprendrem a **consultar directament la base de dades d’Odoo** utilitzant un client gràfic anomenat **pgAdmin**, i també veurem com identificar les taules i camps on Odoo desa la informació.

---

## 🎯 Objectius

- Entendre com es connecta Odoo a la seua base de dades PostgreSQL.  
- Configurar l’accés remot al contenidor de base de dades.  
- Instal·lar i configurar **pgAdmin** a la màquina virtual.  
- Visualitzar taules, dades i usuaris de PostgreSQL.  
- Comprendre la correspondència entre models d’Odoo i taules SQL.

---

## 🧩 Accés a la base de dades amb pgAdmin

Odoo utilitza **PostgreSQL** com a sistema gestor de base de dades (SGBD).  
Les dades de clients, productes, factures, etc., s’emmagatzemen en **centenars de taules** dins del contenidor `db`.  
Podem accedir-hi amb dos tipus d’eines:

- **psql** — client de línia d’ordres per a usuaris avançats.  
- **pgAdmin** — client gràfic multiplataforma amb interfície visual.

---

### 🔧 Preparació de la connexió remota

Per defecte, PostgreSQL només accepta connexions locals.  
Com que el nostre servidor d’Odoo està dins d’un contenidor Docker, hem d’habilitar la connexió externa des del nostre ordinador o màquina host.

1️⃣ **Accedim al contenidor de PostgreSQL**:

```
docker exec -it odoo_server-db-1 bash
```

2️⃣ **Editem els fitxers de configuració** que es troben a `/var/lib/postgresql/data/`:

- `pg_hba.conf`
- `postgresql.conf`

3️⃣ **Afegim al fitxer `pg_hba.conf`:**

```
host all all 0.0.0.0/0 md5
```

Amb això permetem connexions remotes autenticades amb contrasenya.

4️⃣ **Editem `postgresql.conf`** i busquem la línia:

```
listen_addresses = '*'
```

Això indica que el servidor escoltarà peticions de qualsevol IP.

5️⃣ **Reiniciem el contenidor:**

```
exit
docker restart odoo_server-db-1
```

Ara el contenidor `db` acceptarà connexions externes pel port **5432** (que ja exposem en el `docker-compose.yml`).

---

## 💻 Instal·lació de pgAdmin

Descarrega **pgAdmin** des de la pàgina oficial:  
👉 [https://www.pgadmin.org/download/](https://www.pgadmin.org/download/)

Selecciona la versió per al teu sistema (Windows, Linux o macOS) i instal·la-la.  
Quan s’inicie, apareixerà la finestra principal:

<p align="center">
  <img src="img/Tema4/img1_T4.png" width="100%">
</p>

---

### Connexió amb el servidor de PostgreSQL

Fem clic amb el botó dret a “Servers → Create → Server…” i configurem els camps següents:

<p align="center">
  <img src="img/Tema4/img2_T4.png" width="50%">
</p>

<p align="center">
  <img src="img/Tema4/img3_T4.png" width="50%">
</p>

- **Nom:** “Odoo Docker” (o qualsevol altre identificatiu).  
- **Host:** `localhost` (si connectem a la màquina virtual) o la IP del servidor.  
- **Port:** `5432`.  
- **Base de dades de manteniment:** `postgres`.  
- **Usuari:** `odoo`.  
- **Contrasenya:** `myodoo` (segons el `docker-compose.yml`).

Guarda la connexió per a futures sessions.

---

## 📋 Exploració de la base de dades d’Odoo

Una vegada connectats, veurem totes les bases de dades disponibles.  
Seleccionem la que hem creat (per exemple, `cpa`) per explorar-ne les taules:

<p align="center">
  <img src="img/Tema4/img4_T4.png" width="50%">
</p>

Odoo utilitza un esquema per a cada mòdul instal·lat:  
- Les taules del mòdul *website* comencen per `website_`.  
- Les del mòdul *sale* per `sale_`.  
- Les del mòdul *crm* per `crm_`, etc.

<p align="center">
  <img src="img/Tema4/img5_T4.png" width="50%">
</p>

Podem veure els **camps de cada taula**:

<p align="center">
  <img src="img/Tema4/img6_T4.png" width="40%">
</p>

I també **consultar les dades** prement la pestanya *Data*:

<p align="center">
  <img src="img/Tema4/img8_T4.png" width="100%">
</p>

Així visualitzem, per exemple, els productes registrats a Odoo.

---

## 👥 Gestió d’usuaris de PostgreSQL

També podem veure i modificar els usuaris existents des del menú lateral:

<p align="center">
  <img src="img/Tema4/img9_T4.png" width="25%">
</p>

L’usuari per defecte amb el qual Odoo es connecta és **odoo**.

<p align="center">
  <img src="img/Tema4/img10_T4.png" width="70%">
</p>

Des de *Properties* podem revisar permisos i contrasenyes:

<p align="center">
  <img src="img/Tema4/img11_T4.png" width="50%">
</p>

---

## 🌐 Consulta des del client web d’Odoo

Finalment, recorda que podem accedir a les mateixes dades també des del **client web d’Odoo**, però de manera estructurada i segura, mitjançant les seues vistes i models.

Odoo segueix el patró **MVC (Model–Vista–Controlador):**

- **Model** → taules SQL (classes Python)  
- **Vista** → fitxers XML que defineixen formularis, llistes o cerques  
- **Controlador** → lògica Python que gestiona les accions de l’usuari

Aquesta arquitectura permet mantenir separats les dades i el disseny de la interfície.

---

## 🧠 Resum

Amb aquesta pràctica hem aprés a:

- Configurar PostgreSQL per a connexions remotes.  
- Utilitzar **pgAdmin** per explorar la base de dades d’Odoo.  
- Identificar les taules, camps i usuaris principals.  
- Relacionar els models Python amb les taules SQL.

A partir d’ara ja pots **analitzar i comprendre les dades internes d’Odoo** tant des del client web com des d’una eina de base de dades professional.
