# Tema 2 - Pràctica 1  
## Instal·lació i configuració d’Odoo

:::{admonition} Objectiu de la pràctica
:class: note
Preparar una màquina amb Ubuntu Server 22.04, instal·lar Odoo 16, configurar-lo i verificar-ne el funcionament. S’avaluarà tant la part tècnica com la documentació del procés.
:::

:::{admonition} Requisits previs
:class: important
- ISO d’Ubuntu Server 22.04 i un hipervisor (VirtualBox).  
- Connexió a Internet a la VM i accés des de la màquina host.  
- Espai lliure: mínim 20 GB i 2 GB de RAM (recomanat 4 GB).  
- Coneixements bàsics de terminal i xarxes.
:::


+++ Abans de començar: VirtualBox i xarxa (NAT + port forwarding)

:::{admonition} Requisits de VirtualBox
:class: note
- VT-x/AMD‑V activat al BIOS/UEFI.  
- Host amb 4 GB RAM (mínim) i 20+ GB lliures.  
- VirtualBox 7.x o superior.
:::

```{code-block} bash
# Instal·lació ràpida de VirtualBox en Ubuntu (host)
sudo apt-get update
sudo apt-get install -y virtualbox
```

:::{admonition} Configuració de xarxa (NAT + ports)
:class: tip
- Adapter 1: NAT  
- Advanced → Port Forwarding:
  - SSH: Host Port 2222 → Guest Port 22 (TCP)
  - Odoo: Host Port 8069 → Guest Port 8069 (TCP)
:::

Alternativa per línia d’ordres (substitueix "Odoo-VM" pel nom real de la teua VM):

```{code-block} bash
VBoxManage modifyvm "Odoo-VM" --natpf1 "ssh,tcp,,2222,,22"
VBoxManage modifyvm "Odoo-VM" --natpf1 "odoo,tcp,,8069,,8069"
```

Verificació des de l’host (després d’instal·lar la VM):

```{code-block} bash
# Accés SSH (usuari d'Ubuntu de la VM)
ssh -p 2222 usuari@127.0.0.1

# Quan Odoo estiga arrencat:
curl -I http://127.0.0.1:8069
```

:::{admonition} Compte
:class: warning
- Si el port 8069 o 2222 ja està en ús al host, tria altres (p. ex. 18069 i 2223).  
- A la VM revisa el tallafoc: `sudo ufw status` i obri el 22 i 8069 si cal.
:::


:::{admonition} Recomanació: Visual Studio Code Insiders
:class: tip
Editor lleuger i extensible. La versió Insiders rep novetats abans i és útil per a Markdown/MyST i treball remot.

Instal·lació (repo oficial a Ubuntu/Debian):
```{code-block} bash
sudo apt-get update && sudo apt-get install -y wget gpg apt-transport-https
wget -qO- https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor | sudo tee /etc/apt/trusted.gpg.d/microsoft.gpg >/dev/null
echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/trusted.gpg.d/microsoft.gpg] https://packages.microsoft.com/repos/code stable main" | sudo tee /etc/apt/sources.list.d/vscode.list
sudo apt-get update
sudo apt-get install -y code-insiders
```

Alternativa amb Snap:
```{code-block} bash
sudo snap install code-insiders --classic
```
:::

:::{admonition} Connexió remota a la VM amb Remote - SSH
:class: tip
Per a què serveix
- Editar fitxers de la VM com si estigueres dins (p. ex. /opt/odoo).
- Tindre terminal integrat que executa directament en la VM.
- Instal·lar extensions al servidor remot (Python, Docker, etc.).

Què necessites
- Visual Studio Code Insiders (o VS Code estable).
- Extensió: Remote - SSH.

Instal·lar l’extensió:
```{code-block} bash
# amb Insiders
code-insiders --install-extension ms-vscode-remote.remote-ssh
# amb VS Code estable (si no uses Insiders)
code --install-extension ms-vscode-remote.remote-ssh
```

Configura l’accés SSH (NAT amb port 2222):
```{code-block} text
# ~/.ssh/config
Host odoo-vm
  HostName 127.0.0.1
  Port 2222
  User usuari
```

Com connectar
1) Ctrl+Shift+P → “Remote-SSH: Connect to Host…” → odoo-vm  
2) Accepta la clau i tria “Linux”.  
3) File → Open Folder… → /opt/odoo  
4) Terminal → New Terminal (veuràs [SSH: odoo-vm] a la barra inferior).

:::{admonition} Problemes habituals
:class: warning
- “Permission denied (publickey)”: genera una clau amb `ssh-keygen` i copia-la amb `ssh-copy-id -p 2222 usuari@127.0.0.1`.  
- El port 2222 està ocupat: canvia’l a 2223 al Port Forwarding i a `~/.ssh/config`.  
- No apareix el prefix [SSH: …]: comprova que has obert la carpeta després de connectar.
:::


:::{admonition} Instal·lació en Windows (host)
:class: tip
VirtualBox i VS Code Insiders es poden instal·lar amb winget:

```{code-block} powershell
# VirtualBox
winget install -e --id Oracle.VirtualBox

# Visual Studio Code Insiders
winget install -e --id Microsoft.VisualStudioCode.Insiders
```

Si no tens winget:
- VirtualBox: https://www.virtualbox.org/wiki/Downloads
- VS Code Insiders: https://code.visualstudio.com/insiders/

NAT + Port Forwarding (GUI de VirtualBox):
1) Selecciona la VM → Settings → Network → Adapter 1 → Attached to: NAT  
2) Advanced → Port Forwarding…  
   - Name: ssh | Protocol: TCP | Host Port: 2222 | Guest Port: 22  
   - Name: odoo | Protocol: TCP | Host Port: 8069 | Guest Port: 8069
:::

:::{admonition} Instal·lació en macOS (host)
:class: note
Intel vs Apple Silicon (M1/M2/M3)
- Intel: VirtualBox funciona amb normalitat.  
- Apple Silicon: el suport de VirtualBox és limitat; si tens problemes, usa UTM o VMware Fusion Player (gratuït per a ús personal).

Instal·lació amb Homebrew (recomanat):
```{code-block} bash
# Homebrew (si no el tens): /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
brew update

# VirtualBox (millor en Mac Intel)
brew install --cask virtualbox

# VS Code Insiders (Intel o Apple Silicon)
brew install --cask visual-studio-code-insiders
```

Notes macOS:
- En instal·lar VirtualBox pot demanar autoritzar l’extensió a Settings → Privacy & Security → Allow.  
- Pot requerir reiniciar.  
- Configura NAT + Port Forwarding igual que en Windows (ssh: 2222→22, odoo: 8069→8069).
:::

:::{admonition} Resum de connexió des de l’host
:class: important
- SSH: `ssh -p 2222 usuari@127.0.0.1`  
- Odoo (navegador): `http://127.0.0.1:8069`  
- VS Code Insiders + Remote‑SSH: instal·la l’extensió i connecta a l’host `odoo-vm` definit a `~/.ssh/config`.
```
