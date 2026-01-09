# Pla General Comptable aplicat a un club de patinatge
El Pla General Comptable (PGC) és un sistema de classificació dels moviments econòmics. Per al cas de l'entitat club de platinatge i la comptabilitat en Odoo en general en lloc de centrar-nos en com fer balanços o declaracions fiscals, el PGC ajuda a organitzar i categoritzar els ingressos i despeses de manera clara i estructurada. A més incorpora comptes específics per a diferents tipus de transaccions, facilitant la gestió financera i el seguiment dels fluxos de diners. Així com, enviar models de declaracions fiscals a Hisenda.

## Entendre el Pla General Comptable 
El pla general comptable és com un gran llibre d’arxius on cada calaix té un número i un nom. Cada moviment econòmic del club (una factura, una quota, una subvenció…) s’ha de posar en el calaix correcte perquè la comptabilitat tinga sentit. A més, quan una patinadora paga la quota, no només és important saber que ha entrat diners, sinó també d’on ve eixos diners (quotes) i on estan ara (banc). El balanç final depèn de classificar bé cada moviment. 

:::{admonition} No confondre's
:class: warning
 Molta gent pensa que quan entra o ixen diners del banc, això és un ingrés o una despesa. Però no és així. El banc només ens diu on estan els diners físicament. La comptabilitat va de classificar cada moviment en dos comptes diferents: un per a l’origen o destí dels diners (ingrés o despesa) i un altre per a on estan ara (banc o caixa).
Aquest tema no va de fer assentaments, va de prendre decisions bones.
:::

Pensem per un moment, si una patinadora paga la quota mensual de 30 € per transferència bancària. Aquest moviment té dos aspectes importants:
1. **Ingressos**: El club ha rebut 30 € com a quota mensual, que és un ingrés per al club.
2. **Diners**: Aquests 30 € ara estan físicament al compte bancari del club.

Perquè la comptabilitat tinga sentit, hem de classificar aquest moviment en dos comptes diferents. Pera fer-ho s'utilitzen codis i noms específics del Pla General Comptable (PGC). Aquestos codis els vorem amb detall més endavant. En aquest cas, els comptes serien:
- **Compte d'Ingressos (700 - Prestació de serveis)**: Aquí registrem l'ingrés de 30 € com a quota mensual.
- **Compte de Diners (572 - Banc)**: Aquí registrem l'entrada de 30 € al compte bancari del club

Però açò són sols registres comptables. No estem parlant de moure diners físicament dues vegades. El que fem és classificar correctament el moviment en dos comptes diferents per reflectir tant l'origen dels diners (ingressos) com la ubicació actual dels diners (banc).

Si només registrem l'ingrés en el compte de diners (572), no sabrem d'on ve aquest diners. I si només registrem l'ingrés en el compte d'ingressos (700), no sabrem on estan aquests diners físicament. Per tant, és crucial classificar correctament cada moviment per mantenir una comptabilitat clara i precisa.

Si pel contrari fem un pagament de 50 € a la federació per una competició, també hem de classificar-ho en dos comptes:
1. **Compte de Despeses (623 - Serveis professionals)**: El club ha pagat 50 € a la federació, que és una despesa per al club. Aquí registrem la despesa de 50 € pagada a la federació.
2. **Compte de Diners (572 - Banc)**: Aquests 50 € han sortit físicament del compte bancari del club. Aquí registrem la sortida de 50 € del compte bancari del club.

Si només registrem la despesa en el compte de diners (572), no sabrem a què s'ha destinat aquest diners. I si només registrem la despesa en el compte de despeses (623), no sabrem d'on han sortit aquests diners físicament. Per tant, és crucial classificar correctament cada moviment per mantenir una comptabilitat clara i precisa.


::: {admonition} 🧠 Idea clau (abans de començar)
:class: note
La comptabilitat no és sumar i restar. És classificar.  Cada moviment del club (una factura, una quota, una subvenció…) va a un calaix concret. Eixos calaixos són els comptes.

Afortunadament, Odoo ens ajuda molt en aquesta tasca tècnica. Quan importem l’extracte bancari, només cal que classifiquem cada línia al compte correcte (700, 623, 628…) i Odoo s’encarrega de la resta. Així podem centrar-nos en gestionar el club sense perdre’ns en números i balanços complexos. Anem a estudiar com funciona el PGC i quins són els comptes més importants per a un club de patinatge.
:::


---

## 📚 Estructura bàsica del Pla General Comptable (PGC)

Pla General Comptable funciona com una caixa d’arxius amb nivells. Com més llarg el número, més concret és i en Odoo es solen reservar 8 dígits per a diferents nivells d'especificitat.


::: {imatge} /_static/assets/img/Tema9/estructura-pgc.png
:alt: Estructura PGC
:width: 40%
:class: center-img
:::


### Els 7 grans GRUPS (visió global)
El PGC està dividit en 7 grans grups. Cada grup té un número i un nom que indica què representa. A continuació tens una taula amb els 7 grups i el seu significat en un club de patinatge:
| Grup | Què representa | Al club de patinatge |
|------|----------------|----------------------|
| 1    | Capital propi  | Fons inicials del club |
| 2    | Béns duradors  | Patins, equips, ordinadors |
| 3    | Existències    | Material per vendre (si n’hi ha) |
| 4    | A cobrar / a pagar | Quotes pendents, factures |
| 5    | Diners         | Banc i caixa |
| 6    | Despeses       | Lloguer, llum, entrenadores |
| 7    | Ingressos      | Quotes, subvencions, patrocinis |

::: {admonition} Regla d’or
:class: important
- 6 = ixen diners  
- 7 = entren diners

Si dubtes, pensa: “açò em costa diners o me’n dona?”
:::

#### 🟩 GRUP 7 · INGRESSOS (el que entra al club)
Tot allò que el club cobra.

| Compte | Nom                  | Exemple                 |
|--------|----------------------|-------------------------|
| 700    | Prestació de serveis | Quotes mensuals         |
| 705    | Ingressos diversos   | Campus, activitats      |
| 740    | Subvencions          | Ajuntament              |
| 752    | Donacions            | Aportacions puntuals    |

🧠 Exemple:
- Una patinadora paga la quota mensual → _700 – Prestació de serveis_

#### 🟦 GRUP 6 · DESPESES (el que costa mantindre el club)
Tot allò que el club paga.

Subgrups més habituals en un club de patinatge:
| Compte | Nom                 | Exemple real          |
|--------|---------------------|-----------------------|
| 600    | Compres             | Material esportiu     |
| 621    | Lloguer             | Pavelló, local        |
| 622    | Reparacions         | Arreglar material     |
| 623    | Serveis professionals | Gestoria           |
| 624    | Transport           | Desplaçaments         |
| 628    | Subministraments    | Llum, aigua           |
| 629    | Altres serveis      | Web, assegurances     |
| 640    | Sous                | Entrenadores          |
| 642    | Seguretat Social    | Quotes SS             |

🧠 Exemple clar:
- Pagues 120 € de llum del pavelló → _628 – Subministraments_


#### 🟨 GRUP 5 · DINERS (on estan els diners)
Aquest grup no és ni gasto ni ingrés. És on estan els diners físicament.

| Compte | Què és              |
|--------|---------------------|
| 570    | Caixa (efectiu)     |
| 572    | Banc                |

🧠 Exemple:
- Et paguen una quota per transferència → entra a _572 – Banc_. Quan el banc t’ingressa els diners, ix de 572 i entra a _700 – Prestació de serveis_.
- Traus diners per pagar llum en efectiu → ix de 572 i entra a 570 - Caixa. Quan aportes la factura de la llum i la pagues en efectiu, ix de 570 i entra a _628 – Subministraments_.

#### 🟧 GRUP 4 · A cobrar i a pagar
Quan encara no s’ha cobrat o pagat.

| Compte | Significat     |
|--------|----------------|
| 430    | Clients        |
| 410    | Proveïdors     |
| 475    | Hisenda        |
| 476    | Seguretat Social |

👉 Aquest grup és clau per no perdre el control.

🧠 Exemple :
- Emets una factura de quota a una patinadora → entra a _430 – Clients_. Quan la patinadora paga, ix de 430 i entra a 572 – Banc i en _700 – Prestació de serveis_. Però si no paga, el deute queda registrat a 430. 
- Rep una factura de la federació → entra a _410 – Proveïdors_. Quan la pagues, ix de 410 i ix de _572 – Banc_ i entra en _623 – Serveis professionals_. Si no la pagues, el deute queda registrat a 410.


#### 🟪 GRUP 3 · Existències (material per vendre)
Si el club ven material (patins, roba…), es controla ací. Per exemple si montes una barra i vens begudes o menjar per a un event.  Si el club no ven material, no cal usar aquest grup.
| Compte | Exemple               |
|--------|-----------------------|
| 300    | Mercaderies           |

🧠 Exemple: 
- Compres begudes per a vendre → 300, quan les vens ix de 300 i entra en 700. Però si es vol mesclar-ho amb ingressos de quotes, es pot crear un compte específic dins de 700 com per exemple _701 – Vendes begudes_. Si encara no has venut res, el cost de les begudes queda registrat a 300 i els diners que has pagat ixen de _572 – Banc_.
- Compres patins per a vendre → 300
- Vens patins → ix de 300
- Benefici de la venda → _702 – Benefici venda patins_
  
🧠 Exemple de càlcul de benefici:
- Cost dels patins venuts → 600 
- Guany total = 701 - 600

:::{admonition} ⚠️ El benefici no és un moviment de banc.
:class: warning
El benefici és una diferència comptable entre ingressos (701) i despeses (600). No és un moviment físic de diners. Els diners ja han entrat al banc quan vas vendre els patins (572). El benefici només serveix per a saber si has guanyat o perdut diners en la venda.
:::

#### 🟥 GRUP 2 · Béns duradors (immobilitzat)
Coses que duren anys, no mesos. La màquina de muntar i extraure rodaments dels patins o la carpa per a events són exemples típics. També els equips informàtics del club.

| Compte | Exemple               |
|--------|-----------------------|
| 216    | Equipament esportiu   |
| 217    | Informàtica           |
| 218    | Altres equips         |

🧠 Exemple:
- Compres patins per a ús del club (no per vendre) → 216. 
- Equipament esportiu i ixen de _572 – Banc_ quan es paga.

:::{dropdown} 🧠 Comprendre l'Amortització: De la Inversió a la Despesa
Quan el club compra un bé durador (com uns patins o una màquina), no es considera una “despesa total” el primer dia, sinó una inversió. El cost es reparteix durant la vida útil de l’objecte.

### 1) El Moment de la Compra (Any 0)
Registrem que tenim un bé nou i que els diners han eixit del banc.

| Compte | Concepte                       | Deure (Entra) | Haver (Surt) |
|--------|--------------------------------|---------------|--------------|
| 216    | Mobiliari / Equipament esportiu| 1.000 €       |              |
| 572    | Bancs                          |               | 1.000 €      |

Nota: En aquest moment, el club no ha “perdut” diners; simplement ha canviat diners per una màquina del mateix valor.

### 2) El Procés d’Amortització (Anual)
Si la màquina de 1.000 € dura 5 anys, la quota anual és: 1.000 € / 5 anys = 200 €/any.

Cada any, durant 5 anys, farem aquest assentament per reflectir que la màquina és més vella i val menys:

| Compte | Concepte                         | Import | Funció                                      |
|--------|----------------------------------|--------|---------------------------------------------|
| 681    | Amortització de l’immobilitzat   | 200 €  | Despesa: apareix al resultat de l’any       |
| 281    | Amortització acumulada           | 200 €  | Correcció: redueix el valor del bé al balanç|

### 3) Resum Visual del Cicle de Vida
| Any   | Valor al Balanç (216) | Despesa a l’any (681) | Valor Real (Net)     |
|-------|------------------------|------------------------|----------------------|
| Any 0 | 1.000 €                | 0 €                    | 1.000 €              |
| Any 1 | 1.000 €                | 200 €                  | 800 €                |
| Any 2 | 1.000 €                | 200 €                  | 600 €                |
| Any 3 | 1.000 €                | 200 €                  | 400 €                |
| Any 4 | 1.000 €                | 200 €                  | 200 €                |
| Any 5 | 1.000 €                | 200 €                  | 0 € (Amortitzat)     |

En resum:
- El compte 216 ens diu què ens va costar.
- El compte 681 és la “factura” anual que ens enviem a nosaltres mateixos per l’ús de la màquina.
- El compte 572 només es mou el primer dia quan paguem.
:::




#### 🟫 GRUP 1 · Capital propi (Patrimoni Net)
Aquest grup representa la base econòmica permanent del club. Són diners que no estan destinats a ser gastats en el dia a dia, sinó que formen l'estructura que permet al club existir i créixer. Reflecteix els fons que els socis han posat per a crear l'entitat i serveix per a saber la solidesa del club. Eixos diners no es gasten, són el patrimoni. El patrimoni no és una guardiola, és un termòmetre.

Aquest grup és més rellevant en la creació del club que en la gestió diària.

| Compte | Exemple               |  Ús al club            |
|--------|-----------------------|------------------------|
| 101    | Fons social           |Diners aportats pels fundadors el dia que es va crear el club.
| 110    | Reserves              |Beneficis d'anys anteriors que el club decideix no gastar per tenir un "matalàs".|

🧠 Exemple
- Els socis aporten 1.000 € cadascun per crear el club → _101 – Fons Social_.

:::{admonition} ⚠️ Nota important sobre les Inscripcions
:class: warning
Tot i que sembla una "aportació inicial", la inscripció d'un nou soci en un club que ja funciona no es registra aquí. Eixos diners s'utilitzen per a la gestió de l'exercici actual (assegurances, fitxes, lloguer de pista).
Així que la inscripció s'ha de registrar com a ingrés normal en el compte 700 – Prestació de serveis, igual que les quotes mensuals.
:::

Gràcies a aquesta separació, si el club té 10.000 € al banc però 8.000 € són del Fons Social (Grup 1), la directiva sap que només pot disposar realment de 2.000 € per a gastar en patins nous, perquè la resta és el patrimoni sagrat del club.


:::{dropdown} 💡 Com es "gasten" els diners del Patrimoni? 
:class: tip

Tot i que el Grup 1 és el "patrimoni sagrat", de vegades el club necessita utilitzar aquests fons. Per exemple, si el club vol comprar una furgoneta nova per a transportar les patinadores a les competicions, pot decidir utilitzar part del Fons Social per a aquesta inversió. Però aquest procés ha de seguir unes regles clares:

- L'aprovació: Per a tocar aquests diners, normalment cal una **reunió de la Junta Directiva** o una **Assemblea de Socis** que aprove la despesa (per exemple, comprar una furgoneta pel club).

- El mecanisme comptable: Els diners no "ixen" directament del compte 101 cap a la botiga. El procés és:

    - Es registra la compra o despesa (Grup 2 amortització o Grup 6 gastos).

    - Els diners ixen del Banc (Compte 572).

    - Al final de l'any, si el club ha gastat més del que ha ingressat, el valor del Grup 1 disminuirà automàticament per compensar la pèrdua.

- Inversió vs. Despesa:

    - Si compres patins nous (Actiu), el teu patrimoni no baixa, només canvia de forma: abans tenies diners, ara tens patins.

    - Si fas servir el fons per pagar la llum perquè no hi ha socis, el teu patrimoni sí que es fa petit.

Consell de gestió: Un club ben gestionat només "toca" el Grup 1 per a inversions que milloren l'entitat a llarg termini. 
:::


::: {admonition} 🎓 Recorda: en cada moviment hi ha sempre dos preguntes:
:class: tip
- per què entra o ix els diners? (ingrés o despesa)
- i on estan ara? (banc o caixa).
Odoo fa la resta.
:::

:::{dropdown} 🧠 Decidir QUÈ és cada moviment (classificar bé)
:class: tip
## Decidir QUÈ és cada moviment (classificar bé)
Aquest apartat **no és un pas del procés**.
És la manera correcta de pensar **abans** de registrar res al programa.

El banc no diu què és el moviment. Només diu que els diners s’han mogut.

### Moviments típics del club (mapa directe)
- Pagaments grans i repetits (federació)
  - 👉 GASTO → 623 – Serveis professionals  
  - Alternativa: 629 – Altres serveis (“Federació”) si vols afinar

- Entrenadores (pagament a Irene Zuleme)
  - Si factura → 623 – Serveis professionals  
  - Si és nòmina → 640 – Sous

``` {admonition} Idea clau
:class: note
“No mirem el banc, mirem què estem pagant.” El banc és l’origen, el compte és la classificació. En el club ho simplificarem tot a 623 o 629, però el més important no és el número exacte, sinó no posar-ho mai en 572 com si fora un gasto.
```

- Assegurances (Allianz)
  - 👉 625 – Primes d’assegurances

- Material / logística (Disvall Logistic)
  - 👉 600 – Compres

- Quotes xicotetes (10, 35, 80, 100 €) de patinadores
  - 👉 INGRESSOS → 700 – Prestació de serveis  
  - Client = la patinadora

- Imports grans agrupats (ab.rem.2025…)
  - Normalment remeses de quotes o campus/activitats  
  - 👉 700 (quotes / activitats)  
  - Si és subvenció → 740 – Subvencions

- Ajuntament (500 / 2000 €)
  - 👉 740 – Subvencions

``` {admonition} No són donacions
:class: warning
Les quotes de patinadores no són donacions; són ingressos per servei → 700.
```

---

## Els comptes “estrella” del club (per començar)
Domina aquests i ja cobriràs el 80% dels casos:

| Compte | Ús pràctic                                    |
|--------|-----------------------------------------------|
| 572    | Banc (diari central)                          |
| 700    | Quotes / ingressos                            |
| 623    | Federació, gestoria, serveis professionals    |
| 628    | Subministraments (llum, aigua)                |
| 625    | Assegurances                                  |
| 640    | Entrenadores (si és nòmina)                   |

``` {admonition} Bonus de rigor
:class: tip
- Grup 7 (Ingressos) → entra diners  
- Grup 6 (Despeses) → ix diners  
- Grup 5 (Diners) → on estan (caixa/banc)  
- Grup 4 (Clients/Proveïdors) → a cobrar/pagar  
```

:::

---
## 🥇 PAS 1 · Definir en Odoo el BANC com a centre de tot
El club té un únic compte bancari (572001). Tots els moviments passen per ací: és el “fil conductor”.

### 1.1 Crear el diari de banc (tornem a Odoo)
- Compte: _572 – Banc_
- Nom: “Banc Club de Patinatge”
- Tipus: Banc
- (Opcional) IBAN i mètodes de pagament si fas remeses
Si vas a _Facturació → Configuració → Diaris_ pots observar que ja hi han diaris creats per defecte. Anem a reutilitzar el diari de banc que ja està creat per defecte i només cal que l’editem per posar-li un nom més clar.
:::{image} /_static/assets/img/Tema9/diaris.png
:alt: Diaris Odoo
:class: center-img
:width: 100%
:::

:::{admonition} Reutilitzar diari existent
:class: tip
**Reutilitzar el diari existent**

A la llista de diaris es veu clarament un diari anomenat "Banc" amb el tipus "Banc". Aquest és el diari que Odoo ha creat per defecte per gestionar els moviments bancaris:

    Nom diari: Banc

    Codi curt: BNK1

    Compte per defecte: 572001 Banc

Què has de fer? Simplement clica a sobre de la línia on diu "Banc" per editar-lo i posa-hi les dades reals del club:

- **Canvia el nom**: Si vols, posa-hi el nom del banc real (ex: "Banc Sabadell" o "CaixaBank Club") per identificar-lo millor.

- **Configura l'IBAN**: Dins del diari, veuràs un camp per al número de compte. Posa-hi l'IBAN del club, per exemple `ES1600816723126557549777` i dona-li a Crea. Això és vital per a les futures remeses SEPA (Single Euro Payments Area). Aquest sistema permet agrupar múltiples pagaments o cobraments en un únic fitxer que es puja al banc, facilitant la gestió financera del club. Són remeses que Odoo generarà per cobrar les quotes als socis automàticament.

**Per què no crear-ne un de nou?**

  Evites confusions: Si en crees un de nou, tindràs dos diaris de banc i podries acabar fent assentaments en un i conciliant en l'altre.

  Comptes comptables: El diari actual ja està enllaçat al compte 572001. Si en creares un de nou, hauries de crear el compte 572002, fent la teva llista de comptes més llarga innecessàriament.

:::

:::{image} /_static/assets/img/Tema9/caixabanck.png
:alt: Editar diari banc Odoo
:class: center-img
:width: 100% 
:::


#### El Codi curt: 
Pots mantenir BNK1 o canviar-lo per un de més descriptiu si vols (per exemple, CABK per CaixaBank).



#### Comptes de Guanys i Pèrdues per Diferències

Dins de la configuració del Diari de Banc (ex: CaixaBank Club), trobem els camps de Compte de guanys (778000) i Compte de pèrdues (678000). La seua funció és purament tècnica:

**Per a què serveixen?**

  S'utilitzen per a registrar automàticament xicotetes diferències de cèntims durant la conciliació.

  Exemple pràctic: Si una quota d'un alumne és de 50,01 € però el banc rep exactament 50,00 €, Odoo assignarà eixe cèntim de diferència al compte de pèrdues per a poder "tancar" l'operació sense haver de reclamar eixe cèntim a l'alumne.

**On van aquests diners?**

  - _Guanys (778)_: Ingressos excepcionals (has cobrat un poquet de més).

  - _Pèrdues (678)_: Despeses excepcionals (has cobrat un poquet de menys o hi ha hagut un arredoniment).

Són els "comptes de seguretat" que permeten que el banc sempre quadre a zero, absorbint les diferències d'arredoniment de manera automàtica.


### 1.2 El compte bancari 💳 (IBAN) i les Remeses SEPA

Dins de la fitxa del Banc, el camp Número de compte és on s'ha d'introduir l'IBAN (el codi internacional que identifica el compte del club). Configurar-lo correctament és fonamental per a automatitzar el cobrament de les quotes.

**Què és l'IBAN?** 
És el "DNI" del compte bancari. Odoo el necessita per a saber d'on surten els diners o on s'han d'ingressar.

**Per a què serveix en un club?**
 La funció principal és generar Remeses SEPA:

  - En lloc de cobrar als 200 alumnes d'un en un, Odoo genera un fitxer XML amb totes les ordres de cobrament.

  - Tu puges eixe fitxer a la web del teu banc i, automàticament, es giren els rebuts a tots els pares i mares.
    - **Avantatges del SEPA:**
      - Estalvi de temps: No cal picar les dades al banc manualment.
      - Control de morositat: Odoo sap exactament qui ha pagat i qui no en importar l'extracte posteriorment.
      - Seguretat: El sistema valida que el format de l'IBAN siga correcte gràcies als mòduls de dades bancàries que hem instal·lat.

Sense l'IBAN correctament configurat, no podem fer remeses. És la peça que connecta la llista d'alumnes amb els diners reals que entren al banc.


#### Pagaments i cobraments SEPA amb Odoo
Per a automatitzar el cobrament de quotes i el pagament a proveïdors, Odoo utilitza el sistema de remeses SEPA. Recorda cal tenir instal·lat el mòdul de dades bancàries per a que Odoo valide els IBANs i puga generar dites remeses SEPA.

:::{imatge} /_static/assets/img/Tema9/pagamentes-entrants.png
:alt: Pagaments entrants SEPA
:class: center-img
:width: 100%
::: 

##### Activar mòdul SEPA Odoo
Per a generar remeses SEPA entrants, cal activar el mòdul específic d’Odoo. S'anomena `account_banking_sepa_direct_debit` i cal activar-lo des d'Apps.
:::{imatge} /_static/assets/img/Tema9/activar-sepa.png
:alt: Activar mòdul SEPA Odoo
:class: center-img
:width: 100%
:::
Per a generar remeses SEPA sortints, cal activar el mòdul específic d’Odoo. S'anomena `account_banking_sepa_credit_transfer` i cal activar-lo des d'Apps.
:::{imatge} /_static/assets/img/Tema9/activar-sepa-sortint.png
:alt: Activar remeses SEPA Odoo
:class: center-img
:width: 100%
:::

Amb aquestos mòduls activats, ja apareixeran les opcions per a generar remeses SEPA de pagaments i cobraments.
:::{imatge} /_static/assets/img/Tema9/pagamentes-sortints.png
:alt: Pagaments sortints SEPA
:class: center-img
:width: 100%

:::
---

::: {admonition} Per què comencem pel banc?
:class: tip
- El banc et diu “què ha passat de veritat”.  
- Després classifiques cada moviment al compte correcte (700, 623, 628…).  
- Així Odoo pot quadrar la comptabilitat sense sorpreses.
:::

---


## 🥈 PAS 2 · Definir QUI són les persones i entitats
Cal saber QUI és qui per a classificar bé els moviments. Per exemple, si veus un pagament a “Federació de Patinatge”, has de saber que és una despesa de llicències (623). Si veus un ingrés de “Ajuntament Local”, has de saber que és una subvenció (740). Això només ho pot saber una persona que coneix el club i té accés a l’extracte bancari.

### 2.1 Entendre l'extracte bancari
A continuació tens un extracte bancari fictici, amb el mateix format que un extracte real del banc.
No està “netejat”, ni resumit, ni explicat a propòsit. Sols s'ha introduït la columna del tipus d'operació per a que entengues què és cada moviment.

```text
Tipus moviment                   Import     Saldo        Nro. Apunt   Tipus d'operació
trf. entitat esportiva          -3.593,00   14.082,67     854           Despesa: Llicències Federació (Grup 6)
chq: 82-0000XXX                 -3.500,00   10.575,00     857           Despesa: Compra material pesant (Grup 2 o 6)
trf. monitor/a 01                 -765,00    8.402,78     787           Despesa: Serveis professionals (623)
rcbo. logística sl               -422,61   12.369,67     844           Despesa: Compra subministraments
rcbo. assegurances sa            -224,41   12.831,79     779           Despesa: Assegurança responsabilitat civil
bel-liq.rem.devol. 2025           -35,00   12.796,79     782           Devolució: Rebut de quota retornat pel banc
trf. alumne/a anoním 01             10,00   12.087,67     866           Ingrés: Quota individual (Grup 7)
trf. club patinatge convidat       150,00   16.442,28     837           Ingrés: Inscripció en trofeig organitzat
ab.rem. 2025/001                  770,00   15.257,78     826           Remesa: Cobrament grupal de quotes (SEPA)
trf. ajuntament local           2.000,00   11.917,67     863           Ingrés: Subvenció anual (Grup 7)

```
Mira l’extracte i identifica actors: federacions, ajuntament, entrenadores, asseguradora, clubs, famílies etc.

👉 Açò no són “comptes comptables”, són PERSONES i ENTITATS. Després d'analitzar els tipus de moviments caldrà definir qui és qui.


:::{dropdown} 🔎 Diccionari de “Tipus de moviment” més habituals
:class: tip

##### 🔁 trf. → Transferència
Algú envia diners o el club envia diners per transferència.

Exemples reals:
- trf. federacio patinatge → pagament a la federació
- trf. irene zuleme → pagament a entrenadora
- trf. alumne/a → quota o activitat

👉 En Odoo: contacte + ingrés o despesa, segons el signe.

##### 🧾 rcbo. → Rebut domiciliat
Un proveïdor ha passat un rebut automàticament pel banc.

Exemples:
- rcbo.allianz seguros → assegurança
- rcbo.disvall logistic → material / subministraments

👉 Normalment:
- Proveïdor
- Despesa periòdica
- Molt típic d’assegurances, material etc.

##### 💳 chq: → Xec
Pagament fet amb xec (encara es veu en clubs antics).

Exemples:
- chq:82-0904841
- chq:42-9351715

👉 El banc no diu a qui, només diu que has pagat amb xec.  
➡️ Ací és on el cap humà és imprescindible: entrenadora? compra gran? material?  
Odoo no ho sap, algú ho sabrà.

##### 📦 ab.rem. → Abonament per remesa
Entrada de diners agrupada (normalment SEPA).

Exemples:
- ab.rem.20250072818
- ab.rem.20250102958

👉 Açò no és una persona, són moltes quotes juntes


En Odoo:
- vindrà d’una remesa SEPA
- després es reparteix entre socis

##### ↩️ bel-liq.rem.devol → Devolució de rebut
Un rebut ha sigut retornat pel banc.

Exemples:
- bel-liq.rem.devol20250102958

👉 Importantíssim:
- No és una despesa
- És un ingrés que ha fallat

En Odoo:
- Indica morositat, el soci torna a deure els diners.

##### 🏛️ trf. ajuntament de… → Subvenció
Ingressos públics.

Exemples:
- trf. ayuntamiento de tavernes de la valldigna

👉 En comptabilitat:
- Ingrés
- No és quota
- No és donació
- És subvenció

##### 👤 Noms propis (persones o clubs)
Entrades o eixides xicotetes, molt repetides.

Exemples:
- trf. marta
- trf. carolina sala ayuso
- trf. cpa alginet
- imports de 10 €, 35 €, 80 €, 100 €…

👉 Normalment:
- Quotes
- Activitats puntuals
- Campus
- Inscripcions
:::

::: {admonition} 🧠 Traducció mental obligatòria
:class: tip
El banc no diu què és el moviment.  
Només diu què ha passat amb els diners.

El treball real és, identificar qui hi ha darrere, decidir què representa eixe moviment i després classificar-ho.
:::

---



### 2.2 Crear contactes (abans de parlar de factures)
Quan mires un extracte bancari com el de dalt, el primer que has de fer no és pensar en números, sinó en qui hi ha darrere de cada moviment. Abans de parlar d’ingressos, despeses o comptes (700, 623, 572…), Odoo necessita saber qui és cadascú. Per això, el primer pas sempre és crear els contactes.

#### Actors habituals en un club de patinatge (per crear contactes)
A partir d’un extracte bancari realista, en un club de patinatge apareixen sempre els mateixos tipus d’actors:
- Sòcia / Patinadora
  - Persones que paguen quotes o activitats.
  - Exemples: Maria, Zulema, Marta…

- Entrenadora / Monitor
  - Persones que cobren pel seu treball.
  - Exemple: Irene Zuleme

- Proveïdors
  - Empreses que passen rebuts o factures.
  - Exemples: Allianz, Disvall Logistic, empresa de material esportiu…

- Entitats esportives
  - Federacions o altres clubs.
  - Exemples: Federació de Patinatge, club convidat…

- Administració pública
  - Organismes que poden ingressar subvencions.
  - Exemple: Ajuntament de Tavernes

::: {admonition} Per què definir-los com a contactes?
:class: tip
Aquests actors no són comptes comptables: són CONTACTES que Odoo usarà per emetre factures, registrar cobraments, controlar deutes i generar remeses SEPA.
:::
---




#### Importació massiva socis

Una bona gestió comença per no picar les dades a mà. Una vegada configurat el diari de Banc (CaixaBank Club), farem servir la funció d'importació per a carregar-los juntament amb el seu IBAN. 

Com que calen IBANs vàlids per a les remeses SEPA, assegura’t que el fitxer d’importació estiga ben formatat. Per a proves pots generar IBANs ficticis amb eines com [RandomIBAN](https://randomiban.com/).


**Pas 1: Preparació del fitxer**

Perquè les remeses funcionen, el fitxer d'importació ha de tindre com a mínim:

- Nom (name): Persona que rep la factura (normalment el pare/mare).
- Email: Per a enviar el rebut automàticament.
- Número de compte (`bank_ids/acc_number`): L'IBAN on girarem el rebut.
- Permitir pagaments sortints (`allow_outbound_batch_payment`): S'ha de marcar com a True perquè Odoo sàpiga que aquest compte accepta remeses.

>> El fitxer d'importació ha de tenir una columna anomenada `bank_ids/acc_number`. Això indica a Odoo que eixa dada no és un text normal, sinó un Compte Bancari que s'ha de crear i assignar a la fitxa del contacte.

Exemple de fitxer CSV `importacio_patinatge.csv`:
```csv
name,email,street,city,zip,vat,is_company,bank_ids/acc_number,bank_ids/allow_outbound_batch_payment
"Joan Garcia (Pare d'Anna)","joan.garcia@example.com","Carrer de la Pau 10","Tavernes de la Valldigna","46760","12345678Z",False,"ES7401828551262155718716",True
"Marta Beltran","marta.b@example.com","Avinguda de la Marina 5","Gandia","46701","87654321X",False,"ES9501281533757351281254",True
"Pere Estruch","p.estruch@example.com","Carrer Major 22","Simat de la Valldigna","46750","11223344S",False,"ES8921003193472648111816",True
"Inés Zeleme","ines@example.com","Carrer Ample 1","Tavernes de la Valldigna","46760","99887766M",False,"ES6131908813697881432291",True
```

**Pas 2: Importació en Odoo**
Ves a _Contactes > Favorits > Importar registres_. Puja el fitxer CSV creat al pas anterior. Odoo aparellarà automàticament:

- `name` → Nom
- `vat` → NIF (DNI)
- `bank_ids/acc_number` → Compte bancari / Número de compte

:::{image} /_static/assets/img/Tema9/importar-contactes.png
:alt: Importació bank_ids Odoo
:class: center-img
:width: 100%
:::

::: {admonition} 🛠️ Ajust de la Importació (L'últim camp)
:class: tip
A la imatge d'importació, l'última fila diu:

- Columna del fitxer: `bank_ids/allow_outbound_batch_payment`
- Camp Odoo: "Per importar, seleccioneu un camp..."

**Què has de fer?**
 Clica en eixe desplegable i busca el camp: `Bancs / Enviar diners`. Això és el que activa el "check" intern perquè Odoo sàpiga que aquest compte bancari es pot fer servir per a remeses SEPA.

:::


:::{image} /_static/assets/img/Tema9/importar-contactes2.png
:alt: Importació bank_ids Odoo
:class: center-img
:width: 100%
:::

**Verificació:** Odoo aparellarà les columnes del teu fitxer amb els camps del sistema. Revisa que l'IBAN s'assigne a "Compte bancari / Número de compte". Clica a Test per a comprovar que no hi ha errors de format i després a Importa. Ara cada contacte tindrà el seu IBAN assignat.


:::{image} /_static/assets/img/Tema9/contacte-creat.png
:alt: Contacte amb IBAN Odoo
:class: center-img
:width: 100%
:::

---

**Pas 3: El Mandat SEPA (L'última peça)**

Encara que l'IBAN s'haja importat, estiga activat el booleà "Enviar diners", per a cobrar les quotes cal tenir el Mandat SEPA. Aquest mandat és l'autorització legal que dóna el titular del compte bancari (normalment el pare/mare) perquè el club puga girar rebuts al seu compte.

  Exercici per al discent: Entra a la fitxa d'un soci, ves a la pestanya de "Comptabilitat" i comprova que l'IBAN està correctament creat. Clica a "Mandats" i crea'n un de nou amb l'estat "Validat". Sense aquest pas, el fitxer de remesa que generarem més endavant ignorarà aquest soci.

:::{image} /_static/assets/img/Tema9/mandat1.png
:alt: Mandat SEPA Odoo
:class: center-img
:width: 100%
:::

Perquè un gir bancari siga legalment vàlid, el club ha de custodiar el document de mandat signat. Odoo ens permet gestionar això de dues maneres:
1. **Crear-lo i validar-lo dins d'Odoo:** Directament des de la fitxa del soci.

:::{image} /_static/assets/img/Tema9/mandat2.png
:alt: Mandat SEPA Odoo
:class: center-img
:width: 100%
:::{image} /_static/assets/img/Tema9/mandat3.png
:alt: Mandat SEPA Odoo
:class: center-img
:width: 100%
:::
:::{image} /_static/assets/img/Tema9/mandat4.png
:alt: Mandat SEPA Odoo
:class: center-img
:width: 100%
:::

2. **Pujar el document signat:** Per tenir la prova documental vinculada al registre.
::: {important}
Pots descarregar un model oficial del CPA Patinatge per a recollir els mandats signats pels socis i pujar-los a Odoo: 
[📄 Descarregar Exemple de Mandat SEPA (PDF)](/_static/assets/img/Tema9/exemple_de_mandat.pdf)
:::
En Odoo Community NO pots crear un mandat SEPA massiu. Cal anar d'un en un, bé pujant el fitxer del mandat signat pels socis i validar o bé crear-lo manualment. El permís legal és manual el que és automàtic és el cobrament. Altra cosa seria crear un mòdul específic que d'un formulari generara mandats signats i els pujara automàticament però això ja és un desenvolupament a mida.

:::{admonition} Mandat SEPA obligatori
:class: warning
Per llei, per a fer càrrecs directes SEPA (rebuts), cal que el titular del compte bancari haja signat un Mandat SEPA. Aquest mandat autoritza al club a girar rebuts al seu compte. L'importació crea el contacte i l'IBAN, però per llei cal activar el Mandat SEPA dins de la fitxa de cada contacte abans de fer la primera remesa. Sense mandat, el banc rebutjarà el cobrament.
:::


---
## 🥉 PAS 3 · Crear els productes de quotes 
Ara que ja tenim els contactes creats, el següent pas és generar els productes de quotes. Odoo necessita un producte per a cada tipus de quota que volem cobrar. Així, quan fem una factura o un rebut, només cal seleccionar el producte correcte i Odoo assigna automàticament el preu i el compte comptable adequat, necessitem un producte configurat.


:::{dropdown}  ⛸️ Gestió de Productes i Quotes: CPA Patinatge
:class: tip

L'estructura del club s'organitza en dos grans blocs segons l'experiència de l'atleta. 

**1. Estructura Organitzativa**

Per a la creació dels productes al sistema, cal seguir aquesta jerarquia:

* **Grup Iniciació**: Per a nous patinadors.
* **Grup Federats**:
    * **Modalitats**: Lliure o Dansa (o ambdues).
    * **Nivells de competició**:
        * **Nivells**: Nivells 1 al 6.
        * **Categories Territorials**: Aleví, Infantil, Cadet, Juvenil, Junior i Senior.

**2. Tarifes i Productes**

A continuació es detalla la graella de preus mensuals segons la modalitat i el nivell:

| Producte / Categoria | Tipus de Modalitat | Nivell de Competició | Quota Mensual |
| :--- | :--- | :--- | :--- |
| **Iniciació** | Única | - | **37 €** |
| **Nivells** | Simple (Lliure o Dansa) | Nivells 1-6 | **47 €** |
| **Territorial** | Simple (Lliure o Dansa) | Territorial (Aleví...) | **65 €** |
| **Doble Mixte** | Doble (Lliure + Dansa) | Lliure(Nivells) Territorial(Dansa) | **80 €** |
| **Doble Territorial** | Doble (Lliure + Dansa) | Territorial (Aleví...) | **100 €** |


**3. Identificació per SKU (Stock Keeping Unit)**

Per a professionalitzar la gestió, cada quota s'identifica amb un **SKU**. Un SKU és un codi alfanumèric únic que serveix per a "etiquetar" cada servei al programa de comptabilitat o gestió. Utilitza una estructura lògica per a facilitar la identificació ràpida. TIPO-MODEL-COLOR-TALLA és un exemple típic en comerç, però nosaltres adaptarem aquesta idea a les quotes amb una estructura pròpia. TIPUS-GRUP-ÀMBIT DE COMPETICIÓ-MODALITAT.

**Per què fem servir SKUs en lloc de noms llargs?**
* **Evita errors:** És més difícil equivocar-se escrivint `QUO-FED-TER-S` que escrivint a mà "Quota Federat Territorial Simple" cada vegada.
* **Agilitat en les cerques:** Permet filtrar ràpidament quants alumnes tenim en cada categoria per a fer estadístiques.
* **Automatització:** El sistema reconeix el codi i assigna automàticament el preu correcte (37€, 47€, etc.) sense haver d'introduir-lo manualment.

**Lògica dels nostres codis:**
L'estructura del codi segueix l'ordre: `TIPUS - GRUP - ÀMBIT DE COMPETICIÓ - MODALITAT`.
* `QUO`: Quota.
* `FED`: Federat.
* `NIV/TER`: Nivells o Territorial.
* `S/D`: Simple (1 modalitat) o Doble (2 modalitats).

| Codi (SKU) | Descripció | Quota |
| :--- | :--- | :--- |
| **QUO-INI** | Quota Iniciació | 37 € |
| **QUO-FED-NIV-S** | Quota Federat Nivells (Simple) | 47 € |
| **QUO-FED-MIX-D** | Quota Federat lliure nivells i dansa territorial (Doble) | 80 € |
| **QUO-FED-TER-S** | Quota Federat Territorial (Simple) | 65 € |
| **QUO-FED-TER-D** | Quota Federat Territorial (Doble) | 100 € |

::: 

Podem crear un producte per a cada tipus de quota seguint la graella de preus i els codis SKU definits.
**Creació del Producte "Quota Iniciació"**
- Ves a Facturació > Clients > Productes.
  - Crea un de nou: "Quota iniciació".
  - Tipus de producte: Servei.
  - Preu de venda: 37,00 € (per exemple).
  - Pestanya Comptabilitat: En el camp "Compte d'ingressos", selecciona el 700000 (Prestació de serveis). Això fa que, automàticament, cada venda sume a l'Haver del compte d'ingressos del club.

:::{image} /_static/assets/img/Tema9/crear-quotes.png
:alt: Producte Quota Odoo
:class: center-img
:width: 100%
:::

Pero també podem importar els productes massivament amb un fitxer CSV. Això és molt útil si tenim molts tipus de quotes diferents.

**Importació massiva de Productes (Quotes)**
Prepara un fitxer CSV amb les següents columnes mínimes:
- `name`: Nom del producte (ex: "Quota Iniciació").
- `type`: Tipus de producte (ex: "service" per a serveis).
- `list_price`: Preu de venda (ex: 37.00).
- `categ_id/name`: Categoria del producte (opcional, ex: "Quotes Patinatge").
- `property_account_income_id/name`: Compte d'ingressos (ex: "700000 - Prestació de serveis").
- `default_code`: Codi SKU (ex: "QUO-INI").
- `invoice_policy`: Política de facturació (ex: "order" per a facturar a la comanda).
- `sale_ok`: Permetre la venda (ex: True).
- `purchase_ok`: Permetre la compra (ex: False).
- `taxes_id`: Impostos del client. **Nota:** Deixem aquest camp buit (`""`) perquè les quotes estiguen exemptes d'IVA.

Exemple de fitxer CSV `importacio_quotes.csv`:
```csv
name,type,list_price,categ_id,property_account_income_id,default_code,invoice_policy,sale_ok,purchase_ok,taxes_id
"Quota Iniciació","service",37.00,"All / Quotes Patinatge","705000 Prestaciones de servicios en España","QUO-INI","order",True,False,""
"Quota Federat Nivells Simple","service",47.00,"All / Quotes Patinatge","705000 Prestaciones de servicios en España","QUO-FED-NIV-S","order",True,False,""
"Quota Federat Territorial Simple","service",65.00,"All / Quotes Patinatge","705000 Prestaciones de servicios en España","QUO-FED-TER-S","order",True,False,""
"Quota Federat Lliure Nivells i Dansa Territorial (Doble)","service",80.00,"All / Quotes Patinatge","705000 Prestaciones de servicios en España","QUO-FED-MIX-D","order",True,False,""
"Quota Federat Territorial Doble","service",100.00,"All / Quotes Patinatge","705000 Prestaciones de servicios en España","QUO-FED-TER-D","order",True,False,""
``` 
**Importació en Odoo**

Ves a _Facturació > Clients > Productes > Favorits > Importar registres_. Puja el fitxer CSV i Odoo aparellarà automàticament les columnes amb els camps corresponents. 

:::{image} /_static/assets/img/Tema9/crearcategoria.png
:alt: Importació productes Odoo
:class: center-img  
:width: 100%
:::

Com que hem inclòs la columna `categ_id/name`, al test es queixa i et demana què fer. Cal seleccionar "_crear nous valors_". Odoo crearà automàticament la categoria "Quotes Patinatge" i assignarà els productes a aquesta categoria. Revisa que la resta estiga correcte i clica a Importa.


:::{image} /_static/assets/img/Tema9/quotes-llistat2.png
:alt: Productes importats Odoo
:class: center-img
:width: 100%
:::


:::{admonition} 💡Consell d'usuari expert
:class: tip
Una vegada importats, pots agrupar els teus productes per la columna Categoria de producte (`categ_id`). Això et permetrà veure en un sol clic quants ingressos genera "Iniciació" vs "Federats" en els teus informes de vendes de final de mes.
:::


---

## 🥉 PAS 4 · Crear les FACTURES de quotes 
Ara que ja tenim els contactes creats i les quotes definides, el següent pas és generar les factures de quotes per a cada soci. 

Per poder cobrar una factura cal tenir configurat el diari de Banc (CaixaBank Club) i haver creat els contactes amb els seus IBANs i mandats SEPA. A més cal tenir creats els productes de quotes amb els seus preus i comptes comptables. Per últim, cal tenir el mòdul de remeses SEPA activat i crear un mode de pagament amb el mètode "ADEU DIRECTE SEPA".

### 1. Configurar el Mode de Pagament
Per a poder generar remeses SEPA de cobrament, cal crear un mode de pagament específic. Aquest mode de pagament s'assignarà a les factures per a indicar que es cobraran mitjançant domiciliació bancària SEPA. Vés a _Facturació > Configuració > Modes de pagament_. 
:::{image} /_static/assets/img/Tema9/modesdepagament.png
:alt: Mode de pagament SEPA Odoo
:class: center-img
:width: 30%
:::
- Crea un de nou amb les següents dades:
  - `Nom` Crea un de nou anomenat "ADEU DIRECTE SEPA".
  - `Mètode de pagament`: Selecciona "`[sepa_direct_debit] Càrrec directe SEPA per a clients (inbound)`" (aquest camp apareix gràcies al mòdul que vas instal·lar anteriorment).
  - `Enllaç al compte bancari`: "Fix" perquè el club sols té un compte.
  - `Diari de banc fix`: Selecciona el diari de Banc que has creat com per exemple "CaixaBank Club".
  - `Modalitat de pagament per a devolucions`: Deixa-ho buit per ara.
    - Aquest camp serveix per a indicar quin mètode s'ha d'utilitzar si el club ha de tornar diners a un soci (per exemple, si s'ha cobrat una quota per error).
      - **Per què no et deixa triar cap?** No apareixen opcions perquè encara no has creat un mode de pagament de tipus "Outbound" (eixida de diners) que siga compatible amb devolucions.
      - **Com actuar ara?**: De moment, pots deixar-ho buit. No és imprescindible per a generar les remeses de cobrament (ingrés) de les quotes. Si més endavant necessites fer devolucions massives, hauries de crear un mode de pagament per a "Transferència SEPA" (pagaments del club cap a fora) i llavors ja el podries seleccionar ací.
  - `Transfer journal on payment/debit orders`:
    - Aquest camp és una eina de control comptable per a situacions en què els diners no arriben immediatament al banc.
      - **Què vol dir?** Si el selecciones, quan generes la remesa, Odoo no portarà els diners directament al compte del banc (572), sinó que els deixarà en un "Diari de trànsit" fins que tu confirmis que els diners han arribat realment.
      - **Recomanació per al club:** 
        - **Si vols simplicitat:** Deixa-ho buit. D'aquesta manera, quan registres el pagament de la remesa, els diners aniran directament al diari de banc "CaixaBank Club".
        - **Si vols un control total (Professional):** Es podria crear un diari tipus "Efectiu/Transitoris". Això serveix per a reflectir que has enviat el fitxer al banc, però que el banc encara pot trigar 2-3 dies a fer-ho efectiu.
- Opcions de Ordres de pagament:
  - `No permetis el dèbit abans de la data de venciment`: Marca aquesta casella per a assegurar que els càrrecs no es facen abans de la data de venciment de la factura.
    - Aquesta casella (que sol aparèixer com a "Do not allow debit before maturity date") és una mesura de seguretat legal i de gestió.
      - **Què fa**: Si la marques, Odoo s'assegurarà que la data de cobrament que s'envia al banc en el fitxer XML mai siga anterior a la data de venciment que vas posar a la factura.
      - **Per què és important per al club**: Evita queixes de les famílies. Si la factura venç el dia 5, però tu generes la remesa el dia 1, el banc esperarà fins al dia 5 per a fer el càrrec si aquesta opció està activa.
      - **Recomanació**: Marca-la. Dóna serietat al club i garanteix que respecteu els terminis promesos als socis.
  - `Data d'execució de pagament per defecte`
    - Aquest camp defineix quina data portaran els rebuts de la remesa per defecte si no s'especifica una altra. Sol tindre tres opcions habituals:
      - **Data de venciment de la factura**: Cada rebut es cobrarà el dia que venç la seua factura corresponent. És la més precisa.
      - **Data actual**: El banc intentarà cobrar-ho tan prompte com reba el fitxer.
      - **Data fixa**: Una data que tu tries manualment cada vegada que fas la remesa.
      - **Recomanació per al club**: Selecciona "Data de venciment de la factura".
      - **El motiu**: Si el club factura totes les quotes el dia 1 amb venciment el dia 1, totes s'executaran el mateix dia. Si un soci té un acord especial i la seua factura venç el dia 15, el sistema ho respectarà automàticament dins del mateix fitxer.
  - `Agrupa les transaccions de les ordres de pagament`: Marca la casella "Agrupa les transaccions de les ordres de pagament" per a generar un sol assentament comptable per remesa.

- Seleccioneu apunts per pagar - Valors per defecte:
  - `Filtre de diaris`: Deixa-ho per defecte en Factures de client. Serveix per a limitar aquest mode de pagament a uns diaris de facturació concrets. En un club xicotet, normalment només tens un diari de "Factures de Client", així que no cal filtrar.
  - `Mode de pagament de la factura`: Selecciona "Igual". Això obliga el sistema a buscar només les factures on hages posat específicament "ADEU DIRECTE SEPA" com a mètode de cobrament. És la forma més segura d'evitar cobrar per banc a algú que t'ha dit que et pagarà en efectiu.
  - `Assentaments de destí`: Marca "Tots els assentaments assentats" (All posted entries). En el PGC, una factura només és vàlida i genera deute legal quan està "Assentada" (validada). No vols que el sistema intente cobrar factures que encara estan en estat "Esborrany", ja que podrien tindre errors o imports incorrectes.
  - `Enllaç amb una factura o abonament`: Deixa-ho desmarcat. Si ho marques, el sistema podria intentar compensar factures amb abonaments (factures rectificatives) automàticament. Per a la gestió del club, és millor tindre el control manual de quan es fa un descompte o devolució a un soci.
  - `Filtre de tipus de data`: Selecciona "venciment", Odoo filtrarà les factures segons la data límit que tenen per a ser pagades. Si generes les factures el dia 25 del mes anterior però el venciment (quan realment vols cobrar) és el dia 1, el sistema agafarà correctament el dia 1 com a referència per a la remesa. "Apunt" fa referència a la data en què es va registrar el moviment comptable al llibre diari. Si registres una factura avui amb una data de venciment a 15 dies, i filtres per "Apunt", el sistema podria intentar cobrar-la avui mateix, ignorant el termini de 15 dies acordat amb el soci.
- Mostra compte bancari a l'informe de factura
  - `Mostrar compte bancari`:  Selecciona "Complet". Encara que el pagament es faça per remesa SEPA, és una bona pràctica que a la factura aparega l'IBAN del club per a donar transparència i perquè, en cas que un rebut siga retornat, el soci sàpiga a quin compte ha de fer la transferència manual per regularitzar el deute.
  - `Compte bancari dels diaris`: Deixa-la desmarcada. El sistema utilitzarà el compte bancari que has definit en aquest Mode de Pagament (el que has posat a "Enllaç al compte bancari: CaixaBank Club"). Com que per al club hem definit que el banc és el centre de tot i ja l'hem enllaçat dalt, és més segur deixar-ho desmarcat per evitar confusions si en un futur creares un altre diari.


### 2. Crear les factures de quotes
Ara que ja tenim tot preparat, podem generar una factura de quotes. En Facturació > Clients > Factures de clients, clica a "Crear" i  afegeix el producte "Quota Iniciació". Ajusta la data i l'import si cal. Desa i envia la factura.

Un error comú és no definir l'empresa CPA Patinantge com a "Empresa per defecte" en la configuració d'Odoo. Això pot provocar que les factures no es puguen generar apareguent un missatge d'error. Assegura't que l'empresa està creada correctament abans de crear les factures.

Per a la creació de l'empresea caldra un CIF fictici (per exemple G98558232) i una adreça. Això només és necessari per a que Odoo funcione correctament. Pots generar un CIF fictici amb eines com [Generador de CIF](https://testingdatagenerator.com/doi.html).

:::{admonition} 📄 Logotip oficial CPA Patinatge
:class: tip
Per a donar un toc més professional a les factures, pots pujar el logotip oficial del CPA Patinatge a la configuració de l'empresa dins d'Odoo. Això farà que el logotip aparega automàticament a totes les factures i documents generats pel sistema.
[📄 Descarregar logotip CPA (jpeg)](/_static/assets/img/Tema9/cpa-logo.jpeg)

:::

Caldrà crear dos factures d'exemple per a veure com funciona el procés de cobrament massiu amb remeses SEPA. 

Quan creem la primera factura, escollim el client i el producte "Quota Iniciació". Odoo assigna automàticament el preu i el compte comptable. Desem la factura i la confirmem. Ara la factura està en estat "Oberta" i pendent de cobrament. En _Facturació > Clients > Factures_ podem seleccionar la factura i crear ordes de cobrament SEPA. En la pestanya de "Transaccions" veiem que Odoo ha creat una ordre de cobrament vinculada a aquesta factura, afegint una línia podem afegir més factures a la mateixa remesa.

:::{image} /_static/assets/img/Tema9/creartrransaccio.png
:alt: Crear transacció SEPA Odoo
:class: center-img
:width: 100%
:::

Amb aquest procediment podem crear ordes de cobrament SEPA per a tots els socis del club. 

:::{image} /_static/assets/img/Tema9/ordresdecobrament2.png
:alt: Ordres de cobrament SEPA Odoo
:class: center-img
:width: 100%
:::

Una vegada generades les ordes de cobrament, podem generar el fitxer SEPA (.xml) per a enviar-lo al banc. Primer cal confirmar pagaments i després generar fitxer de pagaments. 

:::{admonition} Cal que l'usuari tinga permisos
:class: warning
Per a poder generar ordes de cobrament SEPA i fitxers XML, l'usuari d'Odoo ha de tindre els permisos adequats. Assegura't que l'usuari té activada "SEPA/PAIN Identifiers on Payment Modes" en TECHNICAL FEATURES dins de la seua fitxa d'usuari. Una vegada activat, desat i reiniciada la sessió, l'usuari podrà veure les opcions de SEPA en els modes de pagament i introduir el camp "Identificador del creditor SEPA".
::: 

:::{image} /_static/assets/img/Tema9/identificadorSepa.png
:alt: Identificador SEPA Odoo
:class: center-img
:width: 100%
:::



:::{dropdown} 🏦 Identificador del creditor SEPA
:class: info

En configurar els cobraments per domiciliació SEPA, Odoo ens demana l'**Identificador del creditor SEPA**.
Aquest codi no és inventat ni “a ull”: es valida amb un algorisme matemàtic (**MOD 97**) que calcula el residu de la divisió per 97. Finalment es resta el resultat de 98 menys aquest residu. Si el càlcul no quadra, Odoo el rebutja directament.

En el nostre cas partíem de:
* **CIF de l'entitat:** G98558232
* **Identificador SEPA introduït:** ES41000G98558232

Inicialment no funcionava… fins que vam entendre com ho valida Odoo:

**🧮 Com es calcula (el que fa Odoo per darrere)**
1. **Partim del CIF**, sense espais ni guions: `G98558232`
2. **Afegim el codi de país i dos zeros**: `G98558232ES00`
3. **Convertim les lletres a números** segons la norma SEPA (G→16, E→14, S→28). El codi queda així: `1698558232142800`
4. **Apliquem el mòdul 97**: `1698558232142800 mod 97 = 57`
5. **Calculem els dígits de control**: `98 − 57 = 41`

**✅ Resultat correcte**
Amb el CIF G98558232, l’identificador SEPA correcte és: **ES41000G98558232**



Quan aquest valor és matemàticament vàlid:
* Odoo el dona per bo.
* El mètode de pagament SEPA es guarda.
* Ja es poden generar mandats i remeses.

:::{admonition} Idea clau
:class: tip
Odoo no comprova si el banc t’ha assignat l’identificador, només comprova que el càlcul siga correcte (MOD 97).
:::

:::{admonition} Atenció (vida real)
:class: warning
En producció, l’identificador del creditor SEPA l’ha de proporcionar el banc. Encara que el codi siga matemàticament correcte, si no és l’oficial, el banc rebutjarà la remesa.
:::

**🧠 Traducció a llenguatge humà**
La fórmula la podem calcular nosaltres. El segell final… eixe el té el banc.
O dit més clar: **Odoo sap matemàtiques, però no telefona a CaixaBank.** 😄
:::


#### Fitxer SEPA (.xml) de cobrament massiu
Una vegada confirmat el pagament vol dir que el soci ha autoritzat el cobrament mitjançant domiciliació SEPA. Ara podem generar el fitxer SEPA (.xml) per a enviar-lo al banc.

:::{image} /_static/assets/img/Tema9/fitxerdepagament.png
:alt: Fitxer SEPA Odoo
:class: center-img
:width: 100%
:::

:::{dropdown} Fitxer SEPA (.xml) de cobrament massiu
:class: code-block info
```xml
<?xml version='1.0' encoding='UTF-8'?>
<Document xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns="urn:iso:std:iso:20022:tech:xsd:pain.008.001.02">
  <CstmrDrctDbtInitn>
    <GrpHdr>
      <MsgId>PAY0001</MsgId>
      <CreDtTm>2026-01-07T21:01:49</CreDtTm>
      <NbOfTxs>2</NbOfTxs>
      <CtrlSum>137.00</CtrlSum>
      <InitgPty>
        <Nm>Clup de patinatge artistic Tavernes de la Valldigna</Nm>
      </InitgPty>
    </GrpHdr>
    <PmtInf>
      <PmtInfId>PAY0001-FRST-20260130-NORM-NOcateg</PmtInfId>
      <PmtMtd>DD</PmtMtd>
      <BtchBookg>true</BtchBookg>
      <NbOfTxs>1</NbOfTxs>
      <CtrlSum>37.00</CtrlSum>
      <PmtTpInf>
        <SvcLvl>
          <Cd>SEPA</Cd>
        </SvcLvl>
        <LclInstrm>
          <Cd>CORE</Cd>
        </LclInstrm>
        <SeqTp>FRST</SeqTp>
      </PmtTpInf>
      <ReqdColltnDt>2026-01-30</ReqdColltnDt>
      <Cdtr>
        <Nm>Clup de patinatge artistic Tavernes de la Valldigna</Nm>
      </Cdtr>
      <CdtrAcct>
        <Id>
          <IBAN>ES1600816723126557549777</IBAN>
        </Id>
      </CdtrAcct>
      <CdtrAgt>
        <FinInstnId>
          <Othr>
            <Id>NOTPROVIDED</Id>
          </Othr>
        </FinInstnId>
      </CdtrAgt>
      <ChrgBr>SLEV</ChrgBr>
      <CdtrSchmeId>
        <Id>
          <PrvtId>
            <Othr>
              <Id>ES41000G98558232</Id>
              <SchmeNm>
                <Prtry>SEPA</Prtry>
              </SchmeNm>
            </Othr>
          </PrvtId>
        </Id>
      </CdtrSchmeId>
      <DrctDbtTxInf>
        <PmtId>
          <InstrId>7</InstrId>
          <EndToEndId>7</EndToEndId>
        </PmtId>
        <InstdAmt Ccy="EUR">37.00</InstdAmt>
        <DrctDbtTx>
          <MndtRltdInf>
            <MndtId>BM0000004</MndtId>
            <DtOfSgntr>2026-01-07</DtOfSgntr>
          </MndtRltdInf>
        </DrctDbtTx>
        <DbtrAgt>
          <FinInstnId>
            <Othr>
              <Id>NOTPROVIDED</Id>
            </Othr>
          </FinInstnId>
        </DbtrAgt>
        <Dbtr>
          <Nm>Marta Beltran</Nm>
        </Dbtr>
        <DbtrAcct>
          <Id>
            <IBAN>ES9501281533757351281254</IBAN>
          </Id>
        </DbtrAcct>
        <Purp>
          <Cd>SUBS</Cd>
        </Purp>
        <RmtInf>
          <Strd>
            <CdtrRefInf>
              <Tp>
                <CdOrPrtry>
                  <Cd>SCOR</Cd>
                </CdOrPrtry>
                <Issr>structured</Issr>
              </Tp>
              <Ref>Esports CPA</Ref>
            </CdtrRefInf>
          </Strd>
        </RmtInf>
      </DrctDbtTxInf>
    </PmtInf>
    <PmtInf>
      <PmtInfId>PAY0001-FRST-20260129-NORM-NOcateg</PmtInfId>
      <PmtMtd>DD</PmtMtd>
      <BtchBookg>true</BtchBookg>
      <NbOfTxs>1</NbOfTxs>
      <CtrlSum>100.00</CtrlSum>
      <PmtTpInf>
        <SvcLvl>
          <Cd>SEPA</Cd>
        </SvcLvl>
        <LclInstrm>
          <Cd>CORE</Cd>
        </LclInstrm>
        <SeqTp>FRST</SeqTp>
      </PmtTpInf>
      <ReqdColltnDt>2026-01-29</ReqdColltnDt>
      <Cdtr>
        <Nm>Clup de patinatge artistic Tavernes de la Valldigna</Nm>
      </Cdtr>
      <CdtrAcct>
        <Id>
          <IBAN>ES1600816723126557549777</IBAN>
        </Id>
      </CdtrAcct>
      <CdtrAgt>
        <FinInstnId>
          <Othr>
            <Id>NOTPROVIDED</Id>
          </Othr>
        </FinInstnId>
      </CdtrAgt>
      <ChrgBr>SLEV</ChrgBr>
      <CdtrSchmeId>
        <Id>
          <PrvtId>
            <Othr>
              <Id>ES41000G98558232</Id>
              <SchmeNm>
                <Prtry>SEPA</Prtry>
              </SchmeNm>
            </Othr>
          </PrvtId>
        </Id>
      </CdtrSchmeId>
      <DrctDbtTxInf>
        <PmtId>
          <InstrId>8</InstrId>
          <EndToEndId>8</EndToEndId>
        </PmtId>
        <InstdAmt Ccy="EUR">100.00</InstdAmt>
        <DrctDbtTx>
          <MndtRltdInf>
            <MndtId>BM0000001</MndtId>
            <DtOfSgntr>2026-01-07</DtOfSgntr>
          </MndtRltdInf>
        </DrctDbtTx>
        <DbtrAgt>
          <FinInstnId>
            <Othr>
              <Id>NOTPROVIDED</Id>
            </Othr>
          </FinInstnId>
        </DbtrAgt>
        <Dbtr>
          <Nm>Pere Estruch</Nm>
        </Dbtr>
        <DbtrAcct>
          <Id>
            <IBAN>ES8921003193472648111816</IBAN>
          </Id>
        </DbtrAcct>
        <Purp>
          <Cd>SUBS</Cd>
        </Purp>
        <RmtInf>
          <Strd>
            <CdtrRefInf>
              <Tp>
                <CdOrPrtry>
                  <Cd>SCOR</Cd>
                </CdOrPrtry>
                <Issr>structured</Issr>
              </Tp>
              <Ref>Esports CPA</Ref>
            </CdtrRefInf>
          </Strd>
        </RmtInf>
      </DrctDbtTxInf>
    </PmtInf>
  </CstmrDrctDbtInitn>
</Document>
```
:::



## 🥉 PAS 5 · Rebre els diners al banc
Un cop enviat el fitxer SEPA al banc, cal esperar que els diners entren al compte. Quan això passe, descarregarem l’extracte bancari en format CSV i l’importarem a Odoo per a conciliar els moviments.
::: {admonition} 📥 Descarregar extracte bancari
:class: tip
Per a descarregar l’extracte bancari en format CSV, accedeix a la teua banca en línia de CaixaBank. Ves a la secció d’extractes o moviments del compte i busca l’opció per a exportar o descarregar l’extracte. Selecciona el format CSV i el període corresponent als moviments que vols importar a Odoo.
:::



### 📉 Simulació de l'extracte bancari (Noves Remeses)
Aquest seria l'escenari que et trobaràs al banc en uns dies per a aquestes noves remeses. Seguim el format que m'has passat anteriorment:

```text
Tipus moviment         Import      Saldo       Nro. Apunt   Tipus d'operació
ab.rem. PAY0001        +137,00 €   12.054,67   867          Ingrés: Remesa quotes (Marta + Pere)
bel-liq.rem.devol.     -100,00 €   11.954,67   868          Devolució: Rebut de Pere Estruch retornat
comis. devol.           -3,50 €    11.951,17   869          Despesa: Comissió bancària per devolució
```

Per importar l'extracte bancari a Odoo i completar el procés de conciliació per a la teva remesa PAY0001, has de seguir aquests passos tècnics:
1. Preparació de l'arxiu d'extracte

Tens dues opcions principals segons el que et proporcione CaixaBank:

  - Format Norma 43 (.n43): És el format estàndard bancari a Espanya. El format Norma 43 (.n43) és un fitxer de text pla (ASCII) amb una estructura molt rígida de columnes on no existeixen els decimals (els darrers dos dígits són sempre els cèntims)
    - Aquí tens la representació del fitxer que hauries d'importar a Odoo per simular aquest extracte. Pots copiar aquest contingut en un bloc de notes i guardar-lo amb l'extensió .n43. 


:::{dropdown} Exemple fitxer Norma 43 (.n43)
:class: code-block info
```plaintext
111001ES16008167231265575497770101260701261205467EUR2
221600816723126557549777070126070126040100000000137000000000000867AB.REM. PAY0001        
2301Ingres: Remesa quotes (Marta + Pere)                                        
2216008167231265575497770701260701260401000000001000000000000868BEL-LIQ.REM.DEVOL.      
2301Devolucio: Rebut de Pere Estruch retornat                                   
221600816723126557549777070126070126040100000000003500000000000869COMIS. DEVOL.         
2301Despesa: Comissio bancaria per devolucio                                    
3316008167231265575497770000010000000013700000000200000000103501195117          
88999999999999999999990000100000000000000000000000000000000000
```
🔍 Explicació de l'estructura generada:

- Registre 11 (Capçalera): Defineix el compte del club (acabat en 9777) i el saldo inicial de la sessió.
- Registre 22 (Moviments): Aquí és on es codifiquen els teus apunts:
  - L'import +137,00 € es posa com 0000000013700 (el codi 04 indica un abonament/ingrés).
  - L'import -100,00 € es posa com 0000000010000 (el codi 04 i la posició indiquen el càrrec en aquest context).
  - L'import -3,50 € es posa com 0000000000350.
- Registre 23 (Conceptes): Conté les descripcions que has facilitat ("Ingrés: Remesa...", etc.).

- Registre 33 (Totals): Suma els càrrecs i abonaments per verificar que el fitxer és correcte i calcula el saldo final de 11.951,17 €.
:::

  - Format CSV/Excel (.csv): En moltes ocasions el banc sols et proporciona l'extracte en format CSV o Excel. En aquest cas, hauràs de revisar que les columnes estiguen ben organitzades perquè Odoo puga interpretar-les correctament. En aquest exemple anem a utilitzar: date,ref,name i amount (amb signe positiu o negatiu).
:::{dropdown} Exemple fitxer CSV
:class: code-block info
```csv
date,ref,name,amount
07/01/2026,867,"ab.rem. PAY0001 - Ingrés: Remesa quotes (Marta + Pere)",137.00
07/01/2026,868,"bel-liq.rem.devol. - Devolució: Rebut de Pere Estruch retornat",-100.00
07/01/2026,869,"comis. devol. - Despesa: Comissió bancària per devolució",-3.50
```
:::

### Pas a pas per a la importació a Odoo

1. Vés al tauler de Facturació.
  - Localitza la targeta del diari CaixaBank Club. Aquest no és el diari de tipus banc que hem creat anteriorment, sinó el contacte bancari on es registren els moviments.

:::{dropdown} 🖼️ Ubicació del diari bancari a Odoo
:class: info
```{image} /_static/assets/img/Tema9/configurarcaixabank.png
:alt: Diari bancari Odoo
:class: center-img
:width: 50%
```
Cal tenir configurat un contacte bancari per al diari CaixaBank Club perquè Odoo puga associar correctament els moviments importats amb el compte bancari del club.
:::


Per importar l'extracte bancari en format n43 necessitem instalar el mòdul "Importació d'extractes bancaris" `l10n_es_account_statement_import_n43` si no està ja instal·lat. Aquest mòdul permet a Odoo llegir i processar fitxers d'extractes bancaris en diversos formats, facilitant la conciliació dels moviments amb les transaccions registrades al sistema.

:::{image} /_static/assets/img/Tema9/importacioExtractes.png
:alt: Mòdul importació extractes bancaris Odoo
:class: center-img
:width: 100%
:::

Aquest mòdul necessita el mòdul `account_statement_import_file` per a funcionar correctament. Assegura't que aquest mòdul també està instal·lat en el teu sistema Odoo.

Per a poder importar csvs cal també tenir el mòdul `account_statement_import_sheet_file` instal·lat i requereix la llibreria Python `chardet`. Si utilitzes Docker, pots afegir aquesta llibreria al teu fitxer Dockerfile.

:::{dropdown} 🛠️ Instal·lació dels mòduls afegint a l'script
:class: info
```bash
# --- PART 7: IMPORTACIÓ DE FITXERS BANCARIS (BASE + N43) ---
echo "--- Descarregant mòduls d'importació de l'OCA ---"

# 1. Mòdul Base de Reconciliació (Repositori: bank-statement-reconcile)
git clone --depth 1 --branch 16.0 https://github.com/OCA/bank-statement-reconcile.git /tmp/bs-rec
cp -r /tmp/bs-rec/account_statement_base ./dev_addons/

# 2. Mòduls d'Importació (Repositori: bank-statement-import)
git clone --depth 1 --branch 16.0 https://github.com/OCA/bank-statement-import.git /tmp/bs-imp
cp -r /tmp/bs-imp/account_statement_import_base ./dev_addons/
cp -r /tmp/bs-imp/account_statement_import_file ./dev_addons/

# 3. Mòdul Espanyol Norma 43 (Repositori: l10n-spain)
git clone --depth 1 --branch 16.0 https://github.com/OCA/l10n-spain.git /tmp/l10n-es
cp -r /tmp/l10n-es/l10n_es_account_statement_import_n43 ./dev_addons/
echo "--- Descarregant mòduls d'importació (Noms v16.0 Confirmats) ---"

# 1. Neteja previa
rm -rf /tmp/bs-imp

# 2. Clonar repositori (ja hem vist que aquest és el bo)
git clone --depth 1 --branch 16.0 https://github.com/OCA/bank-statement-import.git /tmp/bs-imp

# 3. Copiar els mòduls segons el teu 'ls'
# El motor base es diu: account_statement_import_base
cp -r /tmp/bs-imp/account_statement_import_base ./dev_addons/

# El motor de fitxers es diu: account_statement_import_file
cp -r /tmp/bs-imp/account_statement_import_file ./dev_addons/

# El que permet importar CSV/Excel es diu: account_statement_import_sheet_file
cp -r /tmp/bs-imp/account_statement_import_sheet_file ./dev_addons/

# Netegem temporals
rm -rf /tmp/bs-rec /tmp/bs-imp /tmp/l10n-es

echo "--- Mòduls d'importació de fitxers bancaris descarregats ---"
```
Podem afegir aquest codi a l'script d'instal·lació per automatitzar la descàrrega i instal·lació dels mòduls necessaris per a la importació d'extractes bancaris en el futur o bé símplement executar-lo manualment en el servidor on està instal·lat Odoo i després executar la instal·lació amb el codi:
```bash
# Pas A: La base (account_statement_base)
docker compose exec web odoo -d cpa -i account_statement_base --stop-after-init

# Pas B: Els connectors (import_base i import_file)
docker compose exec web odoo -d cpa -i account_statement_import_base,account_statement_import_file --stop-after-init

# Pas C: EL MÒDUL CSV (Sheet File) i la Norma 43
# Instal·lem els dos formats de fitxer alhora
docker compose exec web odoo -d cpa -i account_statement_import_sheet_file,l10n_es_account_statement_import_n43 --stop-after-init

docker compose restart web
```

Ara el diari bancari CaixaBank Club tindrà l'opció d'importar extractes en format Norma 43 i altres formats compatibles.
```{image} /_static/assets/img/Tema9/dirariavan2.png
:alt: Importar extracte bancari Odoo
:class: center-img
:width: 100%
``` 

1. Activa el canal correcte

  - Marca l'opció "OCA Import (N43, TXT/CSV/XSLX)".

  - Això enllaça directament el diari amb els mòduls de l'OCA que hem instal·lat per terminal.

2. Per què apareix això ara?

  - Aquest camp apareix perquè els mòduls instal·lats afegeixen aquesta opció específica per a la localització espanyola.

  - En seleccionar-ho, Odoo habilitarà els botons d'importació de fitxers al tauler principal per a aquest banc concret.



:::
---

### ⚙️ Configuració del Statement Sheet Mapping
Perquè Odoo puga interpretar el fitxer CSV, cal configurar el “traductor” de columnes. Si les capçaleres del fitxer no coincideixen exactament amb la configuració, el sistema donarà un error de lectura.
:::{image} /_static/assets/img/Tema9/statement-csv.png
:alt: Crear statement sheet mapping Odoo
:class: center-img
:width: 100%
:::
:::{image} /_static/assets/img/Tema9/seetmapping.png
:alt: Configuració statement sheet mapping Odoo
:class: center-img
:width: 100%
:::


#### 1) Formats i separadors
- Timestamp Format: `%d/%m/%Y` (per a dates com 07/01/2026)
- Delimiter: coma (,)
- Decimals Separator: punt (.)
- Thousands Separator: buit (sense separador)
- Encoding recomanat: UTF-8

#### 2) Mapeig de columnes (secció “Columns”)
Escriu el nom exacte de la capçalera del teu CSV al camp corresponent d’Odoo per a fer l’aparellament automàtic:

| Camp d’Odoo        | Valor a escriure (capçalera CSV) |
|--------------------|-----------------------------------|
| Timestamp Column   | date                              |
| Amount Column      | amount                            |
| Description Column | name                              |
| Reference Column   | ref                               |

::: {admonition} Important
:class: warning
Els ingressos (quotes) s’han de registrar en positiu i les despeses o devolucions en negatiu.  
Si el teu CSV porta els signes invertits, marca la casella “Inverse sign of amount”.
:::

::: {admonition} Consells anti-error
:class: tip
- Les capçaleres han de coincidir lletra per lletra (sense espais extres ni majúscules inesperades).  
- Revisa que la columna d’import no porta símbols (€) ni separadors de milers.  
- Si el CSV ve amb punt i coma (;), canvia el “Delimiter” a “;”.
:::

Ara cal tornar al dirari bancari i en la pestanya configuració avançada seleccionar el statement sheet mapping que acabes de crear. Ves a _Facturació > Configuració > Diaris Comptables > CaixaBank Club_ i selecciona'l. 

:::{image} /_static/assets/img/Tema9/triarcsvstatement.png
:alt: Importar extracte bancari Odoo
:class: center-img
:width: 100%

:::


### Tauler de comptabilitat bancària: Importar l'extracte
Ara ja estem preparats per a importar l'extracte bancari al diari CaixaBank Club.

1. Importació de l'extracte bancari
En el tauler del diari CaixaBank Club, clica a Importar extracte bancari.
:::{image} /_static/assets/img/Tema9/tarjetacaixabank.png
:alt: Importar extracte bancari Odoo
:class: center-img
:width: 100%
:::

  - Clica al botó Importar extracte 
  - Puja l'arxiu.
  - Selecciona el teu arxiu (.n43 o .csv).

:::{admonition} Recorda
:class: tip
Cal seleccionar el statement sheet mapping que has creat abans si és un CSV. 
:::

:::{image} /_static/assets/img/Tema9/seleccionarcsvstatement.png
:alt: Seleccionar mapeig extracte bancari Odoo
:class: center-img
:width: 100%
:::

:::{admonition} ⚠️ Evita duplicats
:class: warning
Si ja has importat aquest extracte abans, Odoo et mostrarà un avís de duplicats. Això és per evitar que carregues el mateix extracte dues vegades. Si estàs segur que és un extracte nou, pots ignorar l'avís.
:::
1. Revisió i confirmació
Odoo processarà l'arxiu i et mostrarà una vista prèvia dels moviments detectats.
  - Revisa que els imports i conceptes coincideixen amb els del banc.
  - Assegura't que els imports estan ben classificats (positius per a ingressos, negatius per a despeses).
  - Clica a Confirmar per a completar la importació.  
:::{admonition} ⚠️ Si és un CSV, Odoo et demanarà "aparellar" les columnes.
:class: warning
 Revisa que l'import de 137,00 € (remesa) i el de -100,00 € (devolució) estiguen ben identificats.
:::  

:::{image} /_static/assets/img/Tema9/extractebancari.png
:alt: Extracte bancari
:class: center-img
:width: 100%
:::

### 🛠️ Com gestionar-ho a Odoo segons el PGC

Si has seguit tots els passos anteriors, en aquest punt tens:
- ✔️ Les factures creades (Marta i Pere)
- ✔️ El fitxer SEPA enviat
- ✔️ L’extracte bancari importat amb els moviments:
    - +137 €
    - −100 €
    - −3,50 €
:::{admonition} ⚠️ Importar un extracte no paga factures.
:class: warning
En Odoo Community, les factures només es paguen quan registres un pagament.
Si has seguit tots els passos, ara tindràs l'extracte bancari importat a Odoo amb els moviments correctes. Pots tornar a ell mitjançant el tauler del diari CaixaBank Club, als tres puntets de la dreta i seleccionant "Extractes bancaris". També pots obrir més detalls com Referència  des de la vista de llista.
:::
:::{image} /_static/assets/img/Tema9/referenciesestracte.png
:alt: Extracte bancari Odoo
:class: center-img
:width: 100%
:::


### 📚 Flux comptable
Ara que tens el lot creat, el flux comptable és el següent:

:::{image} /_static/assets/img/Tema9/apuntscomptables.png
:alt: Flux comptable Odoo
:class: center-img
:width: 100%
:::


:::{dropdown} 📋 Llista d’apunts en l’ordre exacte que apareixen
:class: info
#### 🟢 1. PCABK/2026/00001 – 431200 Efectes comercials en gestió de cobrament – 37 € (DEURE)
👉 “La quota de Marta entra en la remesa SEPA”  
Els diners deixen d’estar en el client i passen a estar en tràmit (encara no al banc).

#### 🟢 2. PCABK/2026/00001 – 430000 Clients (euros) – 37 € (HAVER)
👉 “Marta ja no deu diners al club”  
La factura de Marta queda cobrada… però pendent de banc.

📌 Aquestes dues línies són la remesa, no el cobrament.

---

#### 🟢 3. INV/2026/00002 – 705000 Prestacions de serveis – Pere – 100 € (HAVER)
👉 “Ingressos per la quota de Pere”  
Açò és crear la factura, no cobrar res encara.

#### 🟢 4. INV/2026/00002 – 430000 Clients – Pere – 100 € (DEURE)
👉 “Pere deu 100 € al club”  
Factura emesa, client deutor.

#### 🟢 5. INV/2026/00001 – 705000 Prestacions de serveis – Marta – 37 € (HAVER)
👉 “Ingressos per la quota de Marta”  
És la factura de Marta (ingrés).

#### 🟢 6. INV/2026/00001 – 430000 Clients – Marta – 37 € (DEURE)
👉 “Marta deu 37 € (quan es crea la factura)”  
Aquesta línia després quedarà compensada amb la remesa.

---

### 💥 ARA ENTREM EN EL BANC (extracte importat)

#### 🔵 7. CABK/2026/00003 – 572001 Banc – 3,50 € (HAVER)
👉 “El banc et lleva 3,50 € de comissió”  
Eixos diners ixen del banc.

#### 🔵 8. CABK/2026/00003 – 572998 Compte transitori – 3,50 € (DEURE)
👉 “Registrem la comissió com a despesa”  
La despesa es compensa contra el banc.

📌 Aquest assentament és només la comissió, res a vore amb socis.

#### 🔴 9. CABK/2026/00002 – 572001 Banc – 100 € (HAVER)
👉 “El banc diu: aquest rebut NO”  
El cobrament de Pere no entra (retorn).

#### 🔴 10. CABK/2026/00002 – 572998 Compte transitori – 100 € (DEURE)
👉 “Desfem el cobrament que pensàvem que arribaria”  
Els diners no arriben al banc, tornen enrere.

#### 🟢 11. CABK/2026/00001 – 572001 Banc – 137 € (DEURE)
👉 “Ingressen els diners de la remesa”  
137 € = 37 € (Marta) + 100 € (Pere)  
(encara que després Pere es retornarà)

#### 🟢 12. CABK/2026/00001 – 572998 Compte transitori – 137 € (HAVER)
👉 “Buidem el compte transitori”  
El que estava “en tràmit” passa al banc.

---

### 🔁 CORRECCIÓ FINAL PEL REBUT RETORNAT (Pere)

#### 🔴 13. / – 431200 Efectes comercials en gestió de cobrament – Pere – 100 € (DEURE)
👉 “El rebut de Pere torna a estar pendent”  
Odoo diu: aquest client torna a deure diners.

#### 🔴 14. / – 430000 Clients – Pere – 100 € (HAVER)
👉 “Reobrim el deute del client”  
La factura de Pere torna a estar impagada.

---

### 🧠 RESUM CLAR (per a dir-ho a classe)

✔️ Marta: factura → remesa → banc → tot bé  
❌ Pere: factura → remesa → retorn → factura impagada  
🏦 Banc: comissió = despesa  
📦 Compte transitori: només és un pas intermedi

👉 No sobra cap apunt  
👉 Tots expliquen una cosa diferent que ha passat de veritat

:::



---

### 🧭 ORDRE REAL DELS FETS
En aquest apartat veiem l’ordre exacte en què Odoo crea els apunts comptables per a aquest cas concret de factures, remesa, cobrament i devolució.

#### 🟢 1️⃣ Es crea la factura de Marta
Apunts:
- `INV/2026/00001 – 430000 Clients (euros) – Marta Beltran – DEURE 37,00 € – ADEU DIRECTE SEPA`
- `INV/2026/00001 – 705000 Prestacions de serveis en Espanya – Marta Beltran – HAVER 37,00 €`

Què vol dir:
- Marta passa a deure 37 € al club (430). El compte _430 Clients_ és “gent que ens deu diners”.
- El club reconeix que ha fet un servei i ha guanyat 37 €. El compte _705000 Prestacions de serveis en Espanya_ és “ingressos per serveis”.

📌 Això passa abans de qualsevol remesa o banc. L’ingrés naix amb la factura, no amb el cobrament.

---

#### 🟢 2️⃣ Es crea la factura de Pere
Apunts:
- `INV/2026/00002 – 430000 Clients (euros) – Pere Estruch – DEURE 100,00 € – ADEU DIRECTE SEPA`
- `INV/2026/00002 – 705000 Prestacions de serveis en Espanya – Pere Estruch – HAVER 100,00 €`

Què vol dir:
- Pere passa a deure 100 € al club (430).
- Ingrés reconegut pel club (705/700). En estar a l’HAVER, indica que el club ha guanyat diners pel servei prestat, encara que encara no els haja cobrat.

📌 Fins ací:
- 2 factures
- 2 clients deutors
- 0 banc
- 0 remesa

:::{admonition} 🧠 Recorda
:class: tip
Amb la factura de Pere, el club guanya 100 €, però Pere encara els deu.
:::
---

#### 🟡 3️⃣ Es crea la remesa SEPA (PAY0001)
Apunts:
- `PCABK/2026/00001 – 431200 Efectes comercials en gestió de cobrament – Marta Beltran – PAY0001 – DEURE 37,00 €`
- `PCABK/2026/00001 – 430000 Clients (euros) – Marta Beltran – PAY0001 – HAVER 37,00 €`
- `/ – 431200 Efectes comercials en gestió de cobrament – Pere Estruch – PAY0001 – DEURE 100,00 €`
- `/ – 430000 Clients (euros) – Pere Estruch – PAY0001 – HAVER 100,00 €`

Què vol dir

  - Els rebuts de Marta i Pere passen a “gestió de cobrament”.
  El compte 431200 Efectes comercials en gestió de cobrament representa diners que encara no han arribat al banc.
  - Es tanca provisionalment el deute dels clients.
  El compte _430 Clients_ passa a l’HAVER perquè ja no deuen res (per ara) mentre el banc intenta cobrar els rebuts.
  - La barra / indica línies internes d’un procés que no tenen assentament propi, però sí efecte comptable.PAY0001 és un únic document, però té línies “sense número” perquè Odoo les enganxa al moviment principal.
  - Encara no hi ha cap moviment bancari real.
En aquest moment el banc no ha ingressat res, no sabem si algun rebut serà retornat, només sabem que els cobraments estan en tràmit.

:::{admonition} 📌 Clau important
:class: tip
**Crear la remesa NO és cobrar**, és dir-li al banc “intenta cobrar aquests rebuts”.
:::

---

#### 🔵 4️⃣ El banc abona la remesa
Apunts:
- `CABK/2026/00001 – 572001 Banc – ab.rem. PAY0001 – Ingrés: Remesa quotes (Marta + Pere) – DEURE 137,00 €`
- `CABK/2026/00001 – 572998 Compte transitori – ab.rem. PAY0001 – Ingrés: Remesa quotes (Marta + Pere) – HAVER 137,00 €`

Què vol dir:
- Entren diners al banc del club.
El compte 572001 Banc és el compte on està el diners reals del club.
  En estar **al DEURE**, vol dir que: 
    - El saldo del banc augmenta en 137 €.
- Es buida el compte “pont” de la remesa.
El compte 572998 Compte transitori (o compte pont) és un compte tècnic que Odoo utilitza per a guantar diners mentre estan en tràmit, fins que el banc confirma què ha passat.
  En estar **a l’HAVER**, indica que:
    - Els diners ixen del compte transitori i passen al banc.

Odoo dona per bona la remesa completa. En aquest moment, el sistema assumeix:
 -  Marta ha pagat ✔️
 -  Pere ha pagat ✔️
(encara que això després es corregirà)

:::{admonition} 📌 Importantíssim
:class: tip
El banc entra primer tot, encara que després (en un altre apunt) torne una part. És com funcionen els extractes reals.
:::
---

#### 🔴 5️⃣ El banc torna el rebut de Pere
Apunts:
- `CABK/2026/00002 – 572001 Banc – bel.liq.rem.devol. – Devolució: Rebut de Pere Estruch retornat – HAVER 100,00 €`
- `CABK/2026/00002 – 572998 Compte transitori – bel.liq.rem.devol. – Devolució: Rebut de Pere Estruch retornat – DEURE 100,00 €`

Què vol dir:
- El banc trau 100 € del compte del club.
El compte 572001 Banc **en HAVER** indica que:
  - El saldo real del banc baixa en 100 €.

Açò representa el **retorn del rebut de Pere**:
en altres paraules, el banc diu “aquests diners que t’havia ingressat… ara te’ls lleve”.

- Es desfà parcialment el cobrament anterior.
El compte 572998 Compte transitori **en DEURE** indica que:
  - Els diners tornen al circuit de tràmit, perquè aquest cobrament ja no és definitiu.

- Encara no es reobre la factura del client.
  En aquest punt:
    - Només s’ha corregit el moviment de banc,
    - Pere **encara no apareix com a deutor** en clients (això ve després).

:::{admonition} 📌 Important
:class: tip
Quan el banc retorna un rebut, trau els diners del banc i desfà el cobrament, però el client encara no torna a deure fins que Odoo ho reobri.”
:::
---

#### 🔁 6️⃣ Odoo reobri el deute de Pere
Apunts:
- `/ – 431200 Efectes comercials en gestió de cobrament – Pere Estruch – PAY0001 – DEURE 100,00 €`
- `/ – 430000 Clients (euros) – Pere Estruch – PAY0001 – HAVER 100,00 €`

Què vol dir:
- El cobrament de Pere deixa d’estar “en tràmit”.
El compte 431200 Efectes comercials en gestió de cobrament **en DEURE** indica que:
    - Aquest efecte ja no està sent gestionat pel banc, perquè el rebut ha sigut retornat.

- La factura de Pere torna a estar impagada.
El compte 430000 Clients (euros) **en HAVER** indica que:
    - el client torna a deure 100 € al club.

- Açò no és banc, és comptabilitat de clients.
En aquest moment:
    - El banc ja ha fet el seu moviment (retorn)
    - Odoo arregla els saldos perquè la realitat comptable siga coherent:
      - El client torna a aparéixer com a deutor,
      - La factura deixa d’estar cobrada.

::: {admonition} 📌 Clau important
:class: tip
Un retorn té dues parts:
1) El banc trau els diners.  
2) Odoo reobre el deute del client.

Si no es fera aquest segon pas, la factura quedaria “cobrada”... però sense diners. 😬
:::

---

#### 🏦 7️⃣ Comissió bancària
Apunts:
- `CABK/2026/00003 – 572998 Compte transitori – comis. devol. – Despesa: Comissió bancària per devolució – DEURE 3,50 €`
- `CABK/2026/00003 – 572001 Banc – comis. devol. – Despesa: Comissió bancària per devolució – HAVER 3,50 €`

Què vol dir:
- El banc cobra una comissió de 3,50 € al club.
El compte 572001 Banc **en HAVER** indica que:
  - Ixen diners reals del compte bancari.
- Es reconeix una despesa del club.
El compte 572998 Compte transitori (o el compte de despesa associat, segons configuració) **en DEURE** indica que:
  - El club assumeix un cost per la devolució del rebut.

- Aquesta despesa no té res a veure amb el client.
Importantíssim:
  - No s’imputa a Pere, no afecta la seua factura, és un cost que el club es menja.
:::{admonition} 📌 Important
:class: tip
Les comissions bancàries són despeses pròpies, no deutes del client (excepte si després les refactures, clar).
:::

### 🟢 CAS NORMAL (Marta – tot va bé)
```css
[ FACTURA ]
     │
     │  (es crea la factura)
     ▼
[ 430 CLIENTS ]
“Marta deu 37 €”
     │
     │  (es crea la remesa SEPA)
     ▼
[ 431 EFECTES EN GESTIÓ ]
“El banc està intentant cobrar”
     │
     │  (el banc abona la remesa)
     ▼
[ 572998 COMPTE TRANSITORI ]
“Diners en tràmit, pendents de confirmar”
     │
     │  (confirmació definitiva)
     ▼
[ 572 BANC ]
“Els diners ja estan al compte del club”
```

#### 🔴 CAS PROBLEMÀTIC (Pere – rebut retornat)
```css
[ FACTURA ]
     │
     │  (es crea la factura)
     ▼
[ 430 CLIENTS ]
“Pere deu 100 €”
     │
     │  (es crea la remesa SEPA)
     ▼
[ 431 EFECTES EN GESTIÓ ]
“El banc està intentant cobrar”
     │
     │  (el banc abona la remesa)
     ▼  
[ 572 BANC ]
“Els diners havien entrat…”
     ▲
     │  (el banc retorna el rebut)
     │
[ 572998 COMPTE TRANSITORI ]
“El cobrament deixa de ser vàlid”
     ▲
     │
[ 431 EFECTES EN GESTIÓ ]
“El banc ja no el gestiona”
     ▲
     │
[ 430 CLIENTS ]
“Pere torna a deure 100 €”
```


### 📦 Regla d’or 
Pensa els comptes com caixes. La regla depén del tipus de compte:

#### 🟩 Comptes d’ACTIU
- Exemples: banc, caixa, clients, existències…
- Regla:
  - DEURE → entra / augmenta
  - HAVER → ix / disminueix
- 🧠 Exemple claríssim:
  - Et lleven diners del banc → `572` a l’HAVER
  - T’ingressen diners → `572` al DEURE
  - 👉 Ací sí: HAVER = “llevar”

#### 🟥 Comptes de PASSIU i PATRIMONI
- Exemples: proveïdors, hisenda, capital…
- Regla:
  - DEURE → baixa el que deus
  - HAVER → puja el que deus
- 🧠 Exemple:
  - Deus més diners → HAVER
  - Pagues el deute → DEURE
  - 👉 Ací HAVER no és “llevar”, és “deure més”.

#### 🟦 Comptes d’INGRESSOS (7xx)
- Regla:
  - HAVER → reconeixes ingrés
  - DEURE → correcció o anul·lació
- 🧠 Quan factures:
  - `700` a l’HAVER → “he guanyat diners”
  - No entra cap banc encara, però el resultat puja.

#### 🟨 Comptes de DESPESES (6xx)
- Regla:
  - DEURE → reconeixes despesa
  - HAVER → anul·lació o ajust
- 🧠 Quan pagues llum:
  - `628` al DEURE → “açò m’ha costat diners”

---

### 📌 Taula màgica (què passa en cada tipus de compte)

| Tipus de compte                                 | DEURE (↑)                 | HAVER (↓)                  |
|-------------------------------------------------|---------------------------|----------------------------|
| Actiu (banc, caixa, clients, existències)       | puja · entra              | baixa · ix                 |
| Passiu (proveïdors, hisenda, préstecs, capital) | baixa · deus menys        | puja · deus més            |
| Ingressos (7xx)                                  | correcció/anul·lació      | puja · reconeixes ingrés   |
| Despeses (6xx)                                   | puja · reconeixes despesa | correcció/ajust            |

Nota ràpida: ↑ puja/entra · ↓ baixa/ix. En 6xx/7xx reconeixes resultat; el moviment real de diners es veu en Banc/Caixa (572/570), no en el mateix 7xx/6xx.



### 🧾 Conciliació bancària 
Ara que ja tenim l'extracte bancari importat, el següent pas és conciliar els moviments amb les factures i pagaments registrats a Odoo.
Però ens adonem que   ens faltava un mòdul `account_reconcile_oca` per a la conciliació bancària automàtica. El tenim descarregat sols cal anar a _Apps > Actualitza llista de mòduls_ i instal·lar-lo.
:::{image} /_static/assets/img/Tema9/accountreconcile.png
:alt: Conciliació bancària Odoo
:class: center-img    
:width: 100%
:::

A partir d'ací, quan anem al tauler del CaixaBanck Club, tindrem l'opció de conciliar els moviments bancaris amb les factures i pagaments registrats a Odoo.
:::{image} /_static/assets/img/Tema9/reconciliar.png
:alt: Conciliació bancària Odoo
:class: center-img
:width: 100%
:::
#### Pas a pas per a conciliar
En entrar al tauler de conciliació, veurem els moviments bancaris importats a la columna esquerre. Odoo intentarà automàticament trobar coincidències amb les factures i pagaments registrats. A la columna dreta, veurem les possibles coincidències suggerides per Odoo. A la part de baix, les factures i pagaments pendents de conciliació. 

:::{image} /_static/assets/img/Tema9/statementlines.png
:alt: Tauler de conciliació bancària Odoo
:class: center-img
:width: 100%
::: 

A la pestanya de conciliar seleccionem la factura de Marta i observarem que apareix dalt junt al pagament seleccionat.  
:::{image} /_static/assets/img/Tema9/statementlines2.png
:alt: Tauler de conciliació bancària Odoo
:class: center-img
:width: 100%
::: 
Si seleccionem ADD ALL afig totes les relacionades i ja es pot conciliar. Ara cal seleccionar Clicant a "Validar" Odoo farà l'assentament comptable necessari per a tancar la factura i registrar l'ingrés al banc.

:::{image} /_static/assets/img/Tema9/statementlines3.png
:alt: Validar conciliació bancària Odoo
:class: center-img    
:width: 100%
:::

El següent moviment de l'extracte és la devolució del rebut de Pere. El compte 572998 és un compte de banc i per poder conciliar-lo cal retornar al compte 430 de clients quedant així Pere com a deudor. Seleccionem la línia de compte transitori i a la part de baix triem la pestanya d'Operació manual. Aquí seleccionem el compte 430000 Clients i apliquem. Ara ja podem validar el moviment. 

:::{image} /_static/assets/img/Tema9/statementlines4.png
:alt: Validar conciliació bancària Odoo
:class: center-img    
:width: 100%
::: 

Finalment, l'últim moviment és la comissió bancària. Aquest moviment no té cap factura o pagament relacionat, per tant, cal seleccionar la pestanya d'Operació manual i assignar el compte 626000 Serveis bancaris i l'Empresa a CaixaBank. Ara ja podem validar el moviment.
:::{image} /_static/assets/img/Tema9/statementlines5.png
:alt: Validar conciliació bancària Odoo
:class: center-img
:width: 100%
:::

::: {admonition} ⚠️ Resumint
:class: warning
- La conciliació automàtica és una ajuda, però no sempre encerta. Revisa sempre les propostes.  
- Per a moviments sense factura/pagament associat, utilitza l'Operació manual per a assignar el compte correcte.  
- Assegura't que tots els moviments bancaris estan correctament classificats després de la conciliació.
:::

---

### 📊 Informes financers personalitzats
El mòdul `account_financial_report` permet generar informes financers personalitzats a Odoo, com ara balanços i comptes de pèrdues i guanys. Aquest mòdul és especialment útil per a organitzacions que necessiten complir amb requisits comptables específics o que volen adaptar els seus informes a les seves necessitats particulars.
:::{image} /_static/assets/img/Tema9/accountfinancialreport.png
:alt: Mòdul informes financers Odoo
:class: center-img
:width: 100%
:::

Una vegada instal·lat el mòdul, podem accedir a la configuració dels informes financers des de _Facturació > Informes_. Aquí podem crear nous informes o modificar els existents segons les nostres necessitats.

:::{image} /_static/assets/img/Tema9/accountfinancialreport1.png
:alt: Configuració informes financers Odoo
:class: center-img  
:width: 100%
::: 

