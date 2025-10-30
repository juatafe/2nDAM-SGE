```{dropdown}  💾 Espai esgotat en la màquina virtual: com ampliar el disc LVM (Ubuntu)
:icon: wrench
:class: dropdown
:class: tip

És molt habitual que aparega l’error:

:::bash
sqlite3.OperationalError: database or disk is full
:::

encara que el disc virtual (.vdi) tinga molts GB disponibles.  
Això passa perquè **Ubuntu instal·la per defecte amb LVM**, i el volum lògic del sistema (`ubuntu-lv`) només ocupa una part del disc virtual.

---

### 🧩 1️⃣ Comprovació inicial

Mostra l’espai real utilitzat dins la màquina virtual:

:::bash
df -h
:::

Si veus alguna línia com:

:::bash
/dev/mapper/ubuntu--vg-ubuntu--lv   11G   11G     0 100% /
:::

vol dir que el volum lògic només té 11 GB encara que el `.vdi` siga més gran (p. ex. 25 GB).

---

### ⚙️ 2️⃣ Ampliar el volum lògic per utilitzar tot l’espai del disc

Executa aquestes ordres dins de la màquina virtual:

:::bash
sudo lvextend -l +100%FREE /dev/ubuntu-vg/ubuntu-lv
sudo resize2fs /dev/ubuntu-vg/ubuntu-lv
:::

- `lvextend` assigna tot l’espai lliure del disc al volum lògic.  
- `resize2fs` expandeix el sistema de fitxers per aprofitar-lo.

---

### ✅ 3️⃣ Verifica l’expansió

Torna a comprovar l’espai amb:

:::bash
df -h
:::

Ara hauries de veure alguna cosa semblant a:

:::bash
/dev/mapper/ubuntu--vg-ubuntu--lv   25G   11G   14G   45% /
:::

A partir d’aquest moment el sistema ja disposa de tot l’espai del disc virtual.

---

### 💡 4️⃣ En cas de no tindre més espai assignat al disc virtual

Si continues al 100 %, pots **augmentar la mida del `.vdi`** des de VirtualBox:

1. Apaga la màquina virtual.  
2. En **Configuració → Emmagatzematge → Dispositiu SATA → OdooServer-Docker.vdi**, augmenta la mida (p. ex. de 25 GB a 40 GB).  
3. Torna a iniciar la VM i repeteix els passos anteriors (`lvextend` i `resize2fs`).

---

Amb això, el teu Ubuntu aprofitarà tot l’espai disponible i deixarà d’aparéixer l’error `database or disk is full` en pgAdmin4 o altres aplicacions.
```