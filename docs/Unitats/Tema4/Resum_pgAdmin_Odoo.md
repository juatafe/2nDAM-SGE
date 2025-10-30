## 🧠 Resum

En aquesta pràctica hem aprés a:

- Configurar **PostgreSQL per a connexions remotes persistents**.  
- Utilitzar **pgAdmin** per explorar i administrar la base de dades d’Odoo.  
- Reconéixer les **taules, camps i usuaris principals** del sistema.  
- Entendre la relació entre **models Python i taules SQL** dins d’Odoo.  

Amb tot això, ja pots **analitzar i comprendre les dades internes d’Odoo** tant des del client web com des d’una eina professional com *pgAdmin*.

---

```{admonition} 💡 Recomanació de xarxa (entorn d’aula — NAT + port forwarding)
:class: note
- Accedeix des del teu ordinador a: `localhost:8069`, `localhost:5050`, `localhost:5432` o `localhost:8025`.  
- En el gestor de la màquina virtual, configura les regles de *port forwarding* amb **Host IP = 127.0.0.1** per a limitar l’accés al teu propi equip.  
- Dins la VM, els serveis poden escoltar a `0.0.0.0` (necessari perquè el trànsit redirigit arribe), però **restringeix l’origen** amb `UFW` i `pg_hba.conf` (per exemple, permetent només `10.0.2.2` en VirtualBox).  
- En entorns externs o de producció, **no uses 0.0.0.0** si no és imprescindible: especifica IPs concretes o utilitza túnels SSH o reverse proxies amb HTTPS i llistes d’IP segures.
```

```{admonition} ℹ️ Què és la IP 10.0.2.2 en NAT de VirtualBox?
:class: note
- El mode NAT de VirtualBox crea una xarxa virtual `10.0.2.0/24` amb:
  - **VM (guest):** 10.0.2.15 (per defecte)  
  - **Gateway/NAT virtual:** 10.0.2.2  
  - **DNS virtual:** 10.0.2.3  
- Quan redirigeixes ports (p. ex. `127.0.0.1:5432 → 10.0.2.15:5432`), el trànsit que arriba a la VM **té origen 10.0.2.2**.  
- Per això, si configures `pg_hba.conf` o `UFW` dins la VM, **té sentit permetre només 10.0.2.2**, ja que és el “pont” pel qual entra la connexió des del teu host.  
- En canvi, al teu ordinador (host), mantín els serveis limitats a **127.0.0.1**. En xarxes bridged o de producció, ignora 10.0.2.2 i utilitza IPs reals o canals segurs (SSH, HTTPS).
```

### ✅ Configuració recomanada (resum)

**1. Regles de port forwarding (VirtualBox/VMware):**  
| Servei | Host IP | Host Port | Guest IP | Guest Port |
|---------|----------|-----------|-----------|-------------|
| Odoo | 127.0.0.1 | 8069 | <IP_VM> | 8069 |
| pgAdmin | 127.0.0.1 | 5050 | <IP_VM> | 5050 |
| PostgreSQL | 127.0.0.1 | 5432 | <IP_VM> | 5432 |
| MailHog | 127.0.0.1 | 8025 | <IP_VM> | 8025 |

**2. PostgreSQL dins la VM:**
```bash
# postgresql.conf
listen_addresses = '*'

# pg_hba.conf
host  all  all  127.0.0.1/32    md5
host  all  all  10.0.2.2/32     md5   # IP del NAT de VirtualBox
```

**3. Tallafoc (UFW) dins la VM (opcional però recomanat):**
```bash
sudo ufw allow from 10.0.2.2 to any port 5432 proto tcp
sudo ufw allow from 10.0.2.2 to any port 5050 proto tcp
sudo ufw enable
```

> 🧱 En xarxes bridged o producció, evita `0.0.0.0`: exposa només les IP necessàries i usa connexions segures (SSH, HTTPS, IP whitelists).

---

<p align="center">
  <img src="/_static/assets/img/Tema4/img1_T4.png" width="100%">
</p>

---

### 🔗 Creació de connexió a pgAdmin

Fem clic amb el botó dret sobre **Servers → Create → Server…** i completem els camps següents:

<p align="center">
  <img src="/_static/assets/img/Tema4/img2_T4.png" width="50%">
</p>

<p align="center">
  <img src="/_static/assets/img/Tema4/img3_T4.png" width="50%">
</p>

- **Nom:** “Odoo Docker” (o qualsevol identificatiu).  
- **Host:** `localhost` (si connectes des del teu equip).  
- **Port:** `5432`.  
- **Base de dades de manteniment:** `postgres`.  
- **Usuari:** `odoo`.  
- **Contrasenya:** `myodoo` (segons el `docker-compose.yml`).  

Guarda la connexió per a futures sessions i comprova que pots veure les bases de dades i taules d’Odoo.

---
