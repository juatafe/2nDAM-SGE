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

Durant la instal·lació se’ns oferirà l’opció de configurar el servidor web automàticament.  Podem fer-ho després amb la següent ordre:

```bash
sudo /usr/pgadmin4/bin/setup-web.sh
```

Ens demanarà:
- Crear un **usuari administrador** (adreça de correu i contrasenya)
- Confirmar l’activació del servidor Apache integrat

---

### 4️⃣ Accedir a pgAdmin4 des del navegador

Una vegada finalitzada la configuració, podem obrir pgAdmin4 des del navegador web dins de la màquina virtual (si té entorn gràfic) o des d’un altre equip que tinga accés a la IP de la màquina:

```
http://<IP_MAQUINA>:5050
```

Per exemple, si la màquina virtual està en xarxa NAT i la IP és `192.168.56.10`, accedirem a:

👉 [http://192.168.56.10:5050](http://192.168.56.10:5050)

Autentica’t amb l’usuari creat durant la configuració (`setup-web.sh`).

---

### 5️⃣ Connexió amb el contenidor de PostgreSQL

Una vegada dins de pgAdmin4, creem una nova connexió amb el servidor Docker:

- **Nom:** Odoo Docker  
- **Host:** `localhost` o la IP de la màquina virtual  
- **Port:** `5432`  
- **Usuari:** `odoo`  
- **Contrasenya:** `myodoo`

Amb això, ja podem explorar la base de dades `cpa` creada per Odoo dins del contenidor PostgreSQL.

---

> 💡 **Avantatge:** la versió web de pgAdmin és molt més lleugera i permet treballar en màquines sense entorn gràfic, accedint-hi fàcilment des d’un navegador o des d’una altra màquina de la mateixa xarxa.

> ⚠️ Nota important sobre la xarxa (NAT + port forwarding)
> - Estem en una màquina virtual amb NAT i redirecció de ports. Des del teu ordinador accedeixes sempre per localhost (host), i el hipervisor redirigeix cap a la VM.
> - Perquè la redirecció funcione, dins de la VM els serveis han d’escoltar a 0.0.0.0 (o a la IP de la interfície), no només a 127.0.0.1.
> - La millor recomanació de seguretat en aquest escenari és limitar la redirecció del costat host a 127.0.0.1 perquè només el teu equip puga entrar, i dins de la VM restringir l’origen amb UFW i pg_hba.conf.

### ✅ Configuració recomanada (resum)
- VirtualBox/VMware (regla de port forwarding):
  - Host IP: 127.0.0.1
  - Host Port → Guest IP (IP de la VM) → Guest Port
  - Exemples: 127.0.0.1:8069 → <IP_VM>:8069; 127.0.0.1:5050 → <IP_VM>:5050; 127.0.0.1:5432 → <IP_VM>:5432; 127.0.0.1:8025 → <IP_VM>:8025
- PostgreSQL dins la VM:
  - postgresql.conf → listen_addresses = '*'
  - pg_hba.conf (afegix):  
    host  all  all  127.0.0.1/32    md5  
    host  all  all  10.0.2.2/32     md5   # IP host en NAT de VirtualBox (ajusta segons hipervisor)
- Tallafoc (UFW) dins la VM (opcional però recomanat):
  ```bash
  sudo ufw allow from 10.0.2.2 to any port 5432 proto tcp
  sudo ufw allow from 10.0.2.2 to any port 5050 proto tcp
  sudo ufw enable
  ```

> En entorns de xarxa diferent (bridged/producció), evita 0.0.0.0: exposa només IPs necessàries, usa túnel SSH o reverse proxy amb HTTPS i llistes d’IP permeses.
