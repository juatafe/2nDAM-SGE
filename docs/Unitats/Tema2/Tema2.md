# Tema 2 - Instal·lació i configuració d’Odoo

Més o menys les tasques són aquestes, encara que depén del sistema operatiu i del tipus d’instal·lació triada:

* Disseny de la instal·lació: Abans d’instal·lar cal fer un estudi de les necessitats de l’empresa i com seran resoltes per l’aplicació ERP: taules que cal adaptar, dades, formularis i informes que es requereixen, etc.
* Instal·lació d’equips servidors i clients: Caldrà la instal·lació, revisió i/o actualització del hardware de l’empresa, de manera que complisca els requisits mínims necessaris. De vegades, l’empresa pot optar per contractar serveis SaaS d’una empresa externa i accedir als recursos remots que aquesta li proporciona.
* Instal·lació del programari: Instal·lació tant de l’aplicació ERP com del programari necessari per al seu correcte funcionament.
* Adaptació i configuració del programa: Una vegada instal·lada, caldrà la configuració del programari i la seua adaptació a l’empresa client.
* Migració de dades: Aquest procés és molt important per a l’empresa, ja que les dades són imprescindibles per al seu bon funcionament: clients i proveïdors, comptabilitat, facturació... són dades molt importants i de gran volum.
* Realització de proves: Caldrà verificar mitjançant les proves necessàries que la solució ERP funciona correctament i els resultats obtinguts són satisfactoris.
* Documentació del sistema: En aquesta fase s’han de realitzar els documents i manuals necessaris.
* Formació d’usuaris: Aquesta etapa comprén la formació dels usuaris sobre la utilització de l’ERP, que podrà comportar una formació inicial per als responsables del projecte i una formació per als usuaris finals.

## Instal·lació, comprovació i configuració:
Instal·lació sobre Ubuntu 22.04

### Preparació del sistema i instal·lació:
Configurar la xarxa en Ubuntu Server 22.04

1. Actualització del sistema:
Abans de començar el procés d’instal·lació hem de tindre el sistema actualitzat, per a no tindre problemes posteriors i poder descarregar i instal·lar tots els paquets necessaris per a Odoo.


```
sudo apt-get update
sudo apt-get dist-upgrade
```

2. Creació de l’usuari base:
Anem a crear l’usuari bàsic de Linux per a fer funcionar Odoo, ja que per seguretat no es recomana executar Odoo com a root.
Aquest usuari tindrà com a home el directori /opt/odoo i com a intèrpret de comandes /bin/bash, i li posarem contrasenya.
```
sudo adduser --system --quiet --shell=/bin/bash --home=/opt/odoo --group odoo
```
Opció –group per a posar el grup de l’usuari, el paràmetre -shell /bin/bash definint el terminal d’aquest usuari i --home=/opt/odoo per a definir on estarà el home de l’usuari. Li posem contrasenya per a poder accedir.
```
sudo passwd odoo
```

3. Instal·lació del gestor de base de dades i configuració:
```
sudo apt-get install postgresql
```

Anem a crear un usuari a la base de dades per a treballar des d’Odoo:

Forma 1:

Creem l’usuari Odoo PostgreSQL i li assignem una contrasenya, aquest usuari i clau hem de tindre’ls presents perquè els usarem per a la configuració d’OdooERP amb PostgreSQL.
```
sudo su - postgres -c "createuser -s odoo"
```

Forma 2:

Iniciem sessió amb l’usuari postgres:
```
su postgres
```
amb contrasenya postgres. Si l’usuari postgres no tinguera contrasenya, la posem amb:
```
sudo passwd postgres
```
Creem l’usuari:
 ```
createuser -sdP odoo
```
4. Descàrrega d’Odoo 16.0: (Per a descarregar qualsevol altra versió d’Odoo cal indicar-la amb l’opció --branch)
Com que el propietari de la ruta /opt/odoo és l’usuari de sistema odoo, accedim amb aquest usuari per a poder fer el procés d’instal·lació sense problemes i posteriorment poder utilitzar l’ERP.

Entrem al directori /opt/odoo amb l’usuari odoo.
```
su odoo
cd /opt/odoo
git clone https://www.github.com/odoo/odoo --depth 1 --branch 16.0 --single-branch
```

5. Instal·lació de les llibreries necessàries per a la posterior instal·lació d’Odoo:
* python3-pip: instal·lador de llibreries Python (s’utilitza com pip3)
* gdebi-core: permet instal·lar paquets deb locals resolent i instal·lant les seues dependències.
* libxml2-dev: arxius de desenvolupament per a la llibreria XML de GNOME.
* libjpeg-dev: llibreria C per a llegir i escriure fitxers d’imatge JPEG.
* libxslt-dev: llibreria per a transformacions XSLT.
* libldap2-dev: llibreries d’OpenLDAP.
* libsasl2-dev: arxius de desenvolupament per a la llibreria d’autenticació Cyrus SASL.
* build-essential: paquets essencials per a la creació de paquets Debian.
* python3-pillow: llibreria de processament d’imatges de Python.
* python3-lxml: llibreria de Python per a manejar fitxers XML i HTML.
* python3-dev: arxius de capçalera per a crear extensions de Python.
* python3-setuptools: permet instal·lar un paquet sense copiar arxius al directori de l’intèrpret.
* libpq-dev: binaris i capçaleres mínimes de PostgreSQL.
* npm: gestor de paquets de Node.js.
* nodejs: entorn d’execució per a JavaScript.
* apache2: servidor web.

```
sudo apt-get install build-essential python3-pillow python3-lxml python3-dev python3-pip python3-setuptools libpq-dev npm nodejs git libldap2-dev libsasl2-dev libxml2-dev libxslt1-dev libjpeg-dev apache2 xfonts-75dpi xfonts-base libpq-dev libffi-dev fontconfig -y
```

Assegura’t que tot s’ha instal·lat correctament, ja que si falla alguna instal·lació, Odoo podria no arrancar.

6. Instal·lació de dependències amb PIP3

Actualitzem pip:

```
pip3 install wheel setuptools pip --upgrade
```

Instal·lem: 
```
pip3 install -r /opt/odoo/odoo/requirements.txt

```

Per veure les llibreries instal·lades:
```
pip freeze
```
(mostra el llistat instal·lat, que hauria de coincidir amb el requirements.txt)

NOTA:

Si es presenten errors d’entorn de virtualització (python 3.12), convé fer la instal·lació en un entorn virtual:

Canvia a l’usuari odoo i accedeix a la carpeta /opt/odoo, crea l’entorn:
```
python3 -m venv odoo-venv16
source odoo-venv16/bin/activate
```
Ara, instal·la els requeriments pip d’Odoo 16 a l’entorn creat:
```
pip3 install wheel setuptools pip --upgrade
pip3 install -r /opt/odoo/odoo/requirements.txt
```
Amb la instrucció deactivate ixes de l’entorn virtual:
```
deactivate

```

### Arrancant Odoo
Arranca Odoo com a usuari odoo i comprova que no hi ha errors. Per a això, inicia sessió amb l’usuari odoo, entra a la carpeta on està instal·lat (/opt/odoo/odoo/) i executa odoo-bin.
Comprova que no dona errors: hauria d’aparéixer alguna cosa semblant a això si tot funciona correctament:

```{image} /_static/assets/img/Tema2/img1_T2.png
:alt: Amb ctrl+C pares l’execució d’Odoo.
:width: 65%
:align: center
```

a) Possibles errors:
Si hi ha algun error perquè falten llibreries, pot ser que haja fallat la instal·lació (potser per problemes de connexió). Pots tornar a executar la instal·lació de les llibreries amb:


```
sudo pip3 install -r /opt/odoo/odoo/requirements.txt 

```
o instal·lar la llibreria que falta amb:

```
sudo pip3 install libreria.

```

### Configuració d’Odoo: /opt/odoo/odoo (substitueix per la ruta on tens Odoo)

#### Instal·lació de la llibreria de PDF

Per a poder generar informes en PDF des d’Odoo necessitem una llibreria que ho permeta. Instal·lem la llibreria de PDF per a la generació d’informes en aquest format.
Descarreguem el fitxer wkhtmltox_0.12.6.1-2.jammy_amd64.deb i l’instal·lem. Una vegada instal·lat, creem els enllaços necessaris des de /usr/local/bin a /usr/bin tant del PDF com de la imatge.
```
wget  https://github.com/wkhtmltopdf/packaging/releases/download/0.12.6.1-2/wkhtmltox_0.12.6.1-2.jammy_amd64.deb
sudo dpkg -i wkhtmltox_0.12.6.1-2.jammy_amd64.deb
rm wkhtmltox_0.12.6.1-2 .jammy_amd64.deb
sudo ln -s /usr/local/bin/wkhtmltopdf /usr/bin/
sudo ln -s /usr/local/bin/wkhtmltoimage /usr/bin/
```
Problema amb les fonts: Si en el procés anterior fallen les dependències de les fonts, ho solucionarem instal·lant-les:


```
sudo apt install xfonts-75dpi xfonts-base
```

#### Fitxers de log

Quan s’arranca, es para o es produeixen errors en els sistemes i serveis, la informació que es genera es pot guardar en fitxers de log per a la seua consulta, la qual cosa ens permetrà solucionar problemes i errors.
Anem a crear la carpeta on es guardarà l’arxiu log d’Odoo, per a això crearem una carpeta anomenada odoo dins de la ruta predeterminada de logs d’Ubuntu, és a dir, /var/log/odoo/.
Recorda que aquest procés només el podràs fer amb un usuari administrador, que pot ser root o l’usuari creat en el procés d’instal·lació.
Modifiquem el propietari de la carpeta perquè l’usuari propietari siga odoo, però el grup propietari continue sent l’usuari que la va crear, així ens assegurem que es puguen guardar els arxius generats des d’Odoo.
```
mkdir /var/log/odoo/
chown odoo:root /var/log/odoo
```

#### Fitxer de configuració d’Odoo

El fitxer de configuració és un fitxer amb extensió .conf, on es guarda tota la configuració necessària perquè en arrancar Odoo puga llegir les dades i funcionar correctament.
El fitxer de configuració d’Odoo es troba a la ruta d’instal·lació, que és /opt/odoo/odoo/debian/odoo.conf. Aquest fitxer el copiarem al directori de sistema on es troben tots els fitxers .conf, és a dir, el copiarem a /etc. Modifiquem el propietari de la carpeta perquè l’usuari propietari siga odoo, però el grup propietari continue sent l’usuari que el va crear.

Modifiquem els permisos del fitxer perquè el propietari tinga tots els permisos, el grup només lectura i la resta cap permís. Així no tindrem problemes en executar-lo i llegir-lo des d’Odoo.
Editem el fitxer de configuració i modifiquem les dades perquè l’usuari de la base de dades siga odoo, sense contrasenya, així en treballar des d’Odoo podem accedir a la base de dades sense problemes. Indiquem la ruta d’addons, si apareix comentada la descomentem i posem la ruta on guardarà els logs.


```
cp /opt/odoo/odoo/debian/odoo.conf /etc/odoo.conf
chown odoo: /etc/odoo.conf
chmod 640 /etc/odoo.conf
nano /etc/odoo.conf
```
Contingut mínim del fitxer:

db_user = odoo

db_password = false

addons_path = /opt/odoo/odoo/addons

logfile = /var/log/odoo/odoo-server.log

#### Arrancada automàtica d’Odoo

Per a no haver d’arrancar manualment Odoo i poder gestionar-lo com un servei, cal crear aquest servei i configurar-lo. Per tant, copiem el fitxer odoo.service de la ruta d’instal·lació a la carpeta de serveis del sistema:
copiem odoo.service de la ruta /opt/odoo/odoo/debian/ a la ruta /etc/systemd/system/. Editem el fitxer i modifiquem el contingut perquè l’usuari siga odoo i el grup també odoo, que és l’usuari creat per a gestionar Odoo sense problemes. També hem d’indicar-li la ruta d’arrancada d’Odoo i la ruta del fitxer de configuració.
Activem el servei i ja està disponible per a ser parat, arrancat, veure el seu estat com a servei i comprovem que està correcte veient l’estat.


```
sudo cp /opt/odoo/odoo/debian/odoo.service /etc/systemd/system/odoo.service
sudo nano /etc/systemd/system/odoo.service
```
Posem el següent contingut:

[Service]

Type= simple

User=odoo

Group= odoo

ExecStart=/opt/odoo/odoo/odoo-bin --config /etc/odoo.conf

::: important
Si hem creat un entorn virtual per a instal·lar Odoo, el fitxer odoo.service ha de tindre una estructura diferent:

ExecStart=/opt/odoo/odoo-venv16/bin/python /opt/odoo/odoo/odoo-bin --config /etc/odoo.conf
:::

Activar servei:
```
sudo systemctl enable odoo.service
```
Arrancar, parar i veure l’estat del servei:
```
sudo systemctl start odoo
sudo systemctl stop odoo
sudo systemctl status odoo
```
Accés a Odoo des del client web: Ja podem accedir des del navegador a Odoo:

http://IP_server:8069

Ens apareix una web amb la imatge d’Odoo i comprovem que efectivament Odoo està correctament.

```{image} /_static/assets/img/Tema2/img2_T2.png
:alt: Imatge d’Odoo
:width: 65%
:align: center
```
