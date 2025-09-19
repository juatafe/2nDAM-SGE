# Tema 2 - Instal·lació i configuració d'Odoo

## Introducció

En aquest tema aprendrem les diferents metodologies per desplegar Odoo 16 en entorns professionals. Explorarem tant la instal·lació tradicional en servidors Linux com les solucions modernes amb contenidors Docker, analitzant els avantatges i inconvenients de cada aproximació.

Odoo és un sistema de gestió empresarial (ERP) modular que permet administrar diferents aspectes d'una organització: vendes, compres, inventari, comptabilitat, recursos humans, projectes, etc. El seu desplegament adequat és fonamental per garantir el rendiment, la seguretat i la maintibilitat del sistema.

### Requisits del sistema

:::{admonition} Requisits de hardware per a Odoo 16
:class: note
**Requisits mínims (entorn de proves):**
- **CPU**: 2 cores (2 GHz)
- **RAM**: 4 GB
- **Disc**: 20 GB d'espai lliure
- **Sistema**: Ubuntu 20.04 LTS o superior

**Requisits recomanats (producció petita-mitjana):**
- **CPU**: 4+ cores (2.5+ GHz)
- **RAM**: 8+ GB
- **Disc**: 50+ GB SSD
- **Xarxa**: Connexió estable a Internet

**Consideracions adicionals:**
- **PostgreSQL**: Consumeix 25-30% de la RAM total
- **Concurrent users**: +1 GB RAM per cada 50 usuaris concurrents
- **Mòduls pesats**: Comptabilitat i fabricació requereixen més recursos
:::

## Opcions de desplegament d'Odoo

### Comparativa de metodologies

| Aspecte | Instal·lació tradicional | Docker | SaaS (Odoo.com) |
|---------|--------------------------|--------|-----------------|
| **Control** | Complet | Alt | Limitat |
| **Personalització** | Total | Total | Limitada |
| **Complexitat** | Alta | Mitjana | Baixa |
| **Manteniment** | Manual | Automatitzable | Inclòs |
| **Escalabilitat** | Manual | Fàcil | Automàtica |
| **Costos inicials** | Alts | Mitjans | Baixos |
| **Costos operacionals** | Variables | Previsibles | Previsibles |

### Quan utilitzar cada opció

:::{admonition} Instal·lació tradicional (On-Premise)
:class: tip
**Recomanada per a:**
- Organitzacions amb equips tècnics especialitzats
- Requisits específics de seguretat o compliment normatiu
- Integració complexa amb sistemes existents
- Control total sobre dades i infraestructura

**Avantatges:**
- Màxim control sobre la configuració
- Personalització completa
- Millor rendiment optimitzat
- Propietat total de les dades

**Inconvenients:**
- Requereix expertesa tècnica elevada
- Manteniment i actualitzacions manuals
- Inversió inicial en infraestructura
- Responsabilitat sobre seguretat i backups
:::

:::{admonition} Docker i contenidors
:class: note
**Recomanada per a:**
- Entorns de desenvolupament i proves
- Desplegaments ràpids i replicables
- Arquitectures de microserveis
- Equips amb coneixements de DevOps

**Avantatges:**
- Desplegament ràpid i consistent
- Aïllament d'aplicacions
- Facilita CI/CD
- Escalabilitat horitzontal
- Menor overhead de sistema

**Inconvenients:**
- Corba d'aprenentatge de Docker
- Gestió de volums i xarxes
- Monitoratge més complex
- Requereix orquestració per a producció
:::

:::{admonition} SaaS (Odoo.com)
:class: important
**Recomanada per a:**
- Petites i mitjanes empreses
- Accés ràpid sense inversió tècnica
- Equips sense recursos IT especialitzats
- Projectes amb pressupost limitat

**Avantatges:**
- Implementació immediata
- Actualitzacions automàtiques
- Suport inclòs
- Escalabilitat automàtica
- Reducció de costos operacionals

**Inconvenients:**
- Dependència del proveïdor
- Personalització limitada
- Menys control sobre dades
- Costos recurrents
- Possibles limitacions de rendiment
:::

## Metodologia d'aquest tema

En aquest tema seguirem una aproximació pràctica i progressiva:

1. **Fonaments teòrics**: Conceptes clau sobre desplegament d'aplicacions empresarials
2. **Instal·lació tradicional**: Procés complet en Ubuntu Server (Pràctica 1)
3. **Desplegament amb Docker**: Alternativa moderna i eficient (Pràctica 2)
4. **Configuració avançada**: Optimització, seguretat i monitoratge
5. **Comparativa pràctica**: Anàlisi dels resultats obtinguts

### Objectius d'aprenentatge

Al final d'aquest tema hauràs après a:

- **Analitzar** les diferents opcions de desplegament d'Odoo
- **Implementar** una instal·lació tradicional completa en Linux
- **Desplegar** Odoo utilitzant Docker i Docker Compose
- **Configurar** aspectes de seguretat, rendiment i manteniment
- **Comparar** avantatges i inconvenients de cada metodologia
- **Documentar** processos de desplegament de manera professional

## Conceptes fonamentals

### Arquitectura d'Odoo

Abans de procedir amb la instal·lació, és important entendre l'arquitectura de components d'Odoo:

**Components principals:**

1. **Servidor web (Apache/Nginx)**: Gestió de peticions HTTP, SSL, load balancing
2. **Servidor d'aplicacions (Odoo)**: Lògica de negoci, API, renderització
3. **Base de dades (PostgreSQL)**: Emmagatzematge persistent de dades
4. **Sistema de fitxers**: Documents, imatges, adjunts
5. **Cache (Redis)**: Sessions, cache de consultes, tasques asíncrones

### Consideracions de producció

:::{admonition} Factors clau per a entorns de producció
:class: warning
- **Disponibilitat**: SLA/SLO, redundància, recuperació de desastres
- **Seguretat**: Autenticació, autorització, xifratge, auditoria
- **Rendiment**: Optimització de consultes, cache, load balancing
- **Escalabilitat**: Capacitat de créixer amb la demanda
- **Manteniment**: Actualitzacions, backups, monitoratge
- **Compliment**: RGPD, auditories, logs, traçabilitat
:::

```{toctree}
:maxdepth: 1
:caption: Continguts

Part1
Part2
Apache_ReverseProxy
Docker_Operations
Configuracio_Avancada
Annex_CICD
Tema2_prac1
Tema2_prac2
```
## Recursos addicionals

  - **📖 [Annex A: Apache com a Reverse Proxy per a Odoo](Apache_ReverseProxy.md)**
  - **📖 [Annex B: Operacions habituals amb Docker per a Odoo](Docker_Operations.md)**
  - **📖 [Annex C: Configuració avançada i producció d'Odoo](Configuracio_Avancada.md)**

### Bibliografia i referències

- [Documentació oficial d'Odoo](https://www.odoo.com/documentation/16.0/)
- [Docker Documentation](https://docs.docker.com/)
- [PostgreSQL Performance Tuning](https://wiki.postgresql.org/wiki/Performance_Optimization)
- [Apache Configuration for Odoo](https://httpd.apache.org/docs/2.4/howto/reverse_proxy.html)
- [Let's Encrypt with Apache](https://certbot.eff.org/instructions?ws=apache&os=ubuntu)

### Scripts i eines

Els scripts d'automatització desenvolupats en aquest tema es poden trobar al repositori del curs, incloent:

- **Script d'instal·lació tradicional**: Automatització completa del procés manual
- **Script de Docker avançat**: Desplegament professional amb mòduls personalitzats
- **Scripts de backup**: Estratègies per a ambdues metodologies
- **Monitoratge i alertes**: Eines de supervisió i manteniment

