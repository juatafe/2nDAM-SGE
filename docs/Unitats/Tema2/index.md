# Tema 2 - Instal·lació i configuració d'Odoo

## Introducció

En aquest tema aprendrem les diferents metodologies per desplegar **Odoo 16**, un dels sistemes de gestió empresarial (ERP) més populars i utilitzats actualment. Explorarem tant la instal·lació tradicional en servidors Linux com les solucions modernes amb contenidors Docker, analitzant els avantatges i inconvenients de cada aproximació.

Odoo és un sistema modular que permet administrar diferents aspectes d'una organització: vendes, compres, inventari, comptabilitat, recursos humans, projectes, etc. El seu desplegament adequat és fonamental per garantir el rendiment, la seguretat i la maintibilitat del sistema.

**Components clau que estudiarem:**
- **Servidor Linux** optimitzat per a aplicacions empresarials
- **PostgreSQL** com a sistema gestor de base de dades
- **Redis** com a sistema de cache i coordinació 
- **Docker** per a desplegaments moderns i escalables
- **Apache/Nginx** com a reverse proxy amb SSL
- **Automatització** de desplegaments amb CI/CD (Continuous Integration and Continuous Delivery/Deployment)

### Per què estudiem Odoo?

Com a futur tècnic superior en **Desenvolupament d'Aplicacions Multiplataforma**, és essencial que conegues aquestes eines perquè:

- **Moltes empreses** utilitzen ERPs per gestionar els seus processos de negoci
- **Treballaràs amb tecnologies clau**: Linux, bases de dades PostgreSQL, aplicacions web, Docker
- **Desenvoluparàs competències** en administració de sistemes i DevOps
- **Aprendràs metodologies modernes** de desplegament i automatització

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

**Consideracions addicionals:**
- **PostgreSQL**: Consumeix 25-30% de la RAM total
- **Usuaris concurrents**: +1 GB RAM per cada 50 usuaris concurrents
- **Mòduls pesats**: Comptabilitat i fabricació requereixen més recursos
:::

### Requisits del sistema per a producció

| Component | Mínim | Recomanat | Òptim |
|-----------|-------|-----------|-------|
| **CPU** | 2 cores | 4 cores | 8+ cores |
| **RAM** | 4GB | 8GB | 16GB+ |
| **Disc** | 50GB SSD | 200GB SSD | 500GB+ NVMe |
| **Xarxa** | 100Mbps | 1Gbps | 10Gbps |
| **Redis** | - | 1GB RAM | 2-4GB RAM |

:::{admonition} Consideracions per Redis
:class: tip
Redis és **opcional** per a entorns de desenvolupament amb 1-2 usuaris, però esdevé **imprescindible** en entorns de producció amb més de 10 usuaris concurrents. 

Consulta l'**[Annex E: Redis](Annex_Redis.md)** per a una guia completa sobre quan i com implementar-lo.
:::

## Metodologies de desplegament

### Visió general de les opcions

Aquest tema cobreix tres aproximacions principals per desplegar Odoo, cadascuna amb els seus avantatges específics:

```{mermaid}
graph TD
    A[Desplegament d'Odoo] --> B[Instal·lació Tradicional]
    A --> C[Docker/Contenidors]
    A --> D[SaaS Cloud]
    
    B --> B1[Control Total]
    B --> B2[Rendiment Òptim]
    B --> B3[Personalització Màxima]
    
    C --> C1[Portabilitat]
    C --> C2[Desplegament Ràpid]
    C --> C3[Escalabilitat]
    
    D --> D1[Zero Manteniment]
    D --> D2[Inici Immediat]
    D --> D3[Suport Inclòs]
```

### Comparativa detallada de metodologies

| **Aspecte** | **Instal·lació Tradicional** | **Docker** | **SaaS (Odoo.com)** |
|-------------|------------------------------|------------|-----------------|
| **🎯 Control** | Complet | Alt | Limitat |
| **🔧 Personalització** | Total | Total | Limitada |
| **📈 Complexitat** | Alta | Mitjana | Baixa |
| **🛠️ Manteniment** | Manual | Automatitzable | Inclòs |
| **⚡ Escalabilitat** | Manual | Fàcil | Automàtica |
| **💰 Costos inicials** | Alts | Mitjans | Baixos |
| **📊 Costos operacionals** | Variables | Previsibles | Previsibles |
| **⏱️ Temps desplegament** | 2-4 hores | 30 minuts | Immediat |
| **🎓 Corba aprenentatge** | Alta | Mitjana | Baixa |

### Quan utilitzar cada metodologia

:::{admonition} 🏗️ Instal·lació tradicional (On-Premise)
:class: tip
**Recomanada per a:**
- Organitzacions amb equips tècnics especialitzats
- Requisits específics de seguretat o compliment normatiu
- Integració complexa amb sistemes existents
- Control total sobre dades i infraestructura
- Pressupost per a infraestructura pròpia

**✅ Avantatges:**
- Màxim control sobre la configuració
- Personalització completa
- Millor rendiment optimitzat
- Propietat total de les dades
- Compliment de normatives estrictes

**❌ Inconvenients:**
- Requereix expertesa tècnica elevada
- Manteniment i actualitzacions manuals
- Inversió inicial en infraestructura
- Responsabilitat sobre seguretat i backups
- Escalabilitat manual complexa
:::

:::{admonition} 🐳 Docker i contenidors
:class: note
**Recomanada per a:**
- Entorns de desenvolupament i proves
- Desplegaments ràpids i replicables
- Arquitectures de microserveis
- Equips amb coneixements de DevOps
- Projectes que requereixen múltiples entorns

**✅ Avantatges:**
- Desplegament ràpid i consistent
- Aïllament d'aplicacions
- Facilita CI/CD i automatització
- Escalabilitat horitzontal
- Menor overhead de sistema
- Portabilitat entre entorns

**❌ Inconvenients:**
- Corba d'aprenentatge de Docker
- Gestió de volums i xarxes
- Monitoratge més complex
- Requereix orquestració per a producció
- Debugging inicial més complicat
:::

:::{admonition} ☁️ SaaS (Odoo.com)
:class: important
**Recomanada per a:**
- Petites i mitjanes empreses
- Accés ràpid sense inversió tècnica
- Equips sense recursos IT especialitzats
- Projectes amb pressupost limitat
- Necessitat d'inici immediat

**✅ Avantatges:**
- Implementació immediata
- Actualitzacions automàtiques
- Suport tècnic inclòs
- Escalabilitat automàtica
- Reducció de costos operacionals
- Zero responsabilitat tècnica

**❌ Inconvenients:**
- Dependència del proveïdor
- Personalització limitada
- Menys control sobre dades
- Costos recurrents permanents
- Possibles limitacions de rendiment
- Menor flexibilitat d'integració
:::

## Metodologia d'aprenentatge d'aquest tema

### Aproximació pràctica i progressiva

En aquest tema seguirem una aproximació pràctica i progressiva que et permetrà comprendre profundament cada metodologia:

**🎯 Objectius d'aprenentatge:**

Al final d'aquest tema hauràs après a:

- **Analitzar** les diferents opcions de desplegament d'Odoo segons les necessitats
- **Implementar** una instal·lació tradicional completa en Linux
- **Desplegar** Odoo utilitzant Docker i Docker Compose
- **Configurar** aspectes de seguretat, rendiment i manteniment
- **Comparar** avantatges i inconvenients de cada metodologia
- **Documentar** processos de desplegament de manera professional
- **Comprendre** conceptes avançats com CI/CD per a automatització

### Estructura del tema

```{mermaid}
graph LR
    A[Part 1: Tradicional] --> B[Part 2: Docker]
    B --> C[Annexos Especialitzats]
    
    A --> A1[Ubuntu Server]
    A --> A2[PostgreSQL]
    A --> A3[Odoo Manual]
    
    B --> B1[Docker Install]
    B --> B2[Docker Compose]
    B --> B3[Automatització]
    
    C --> C1[Apache Proxy]
    C --> C2[Operacions Docker]
    C --> C3[Producció Avançada]
    C --> C4[CI/CD Pipeline]
```

**📚 Continguts del tema:**

1. **[Part 1: Instal·lació tradicional](Part1.md)** - Fonaments sòlids
2. **[Part 2: Desplegament amb Docker](Part2.md)** - Metodologia moderna
3. **[Annexos especialitzats](#recursos-addicionals)** - Configuracions avançades
4. **[Pràctiques guiades](#pràctiques-del-tema)** - Aplicació pràctica

## Conceptes fonamentals

### Arquitectura d'Odoo

Abans de procedir amb qualsevol instal·lació, és important entendre l'arquitectura de components d'Odoo:

```{mermaid}
graph TD
    A[Client Web/Mòbil] --> B[Reverse Proxy]
    B --> C[Servidor Odoo]
    C --> D[Base de Dades PostgreSQL]
    
    E[Load Balancer] --> C
    F[Sistema de Fitxers] --> C
    G[Cache Redis] --> C
    
    H[Mòduls Core] --> C
    I[Mòduls Personalitzats] --> C
    J[Mòduls Comunitat] --> C
```

**Components principals:**

1. **Servidor web (Apache/Nginx)**: Gestió de peticions HTTP, SSL, load balancing
2. **Servidor d'aplicacions (Odoo)**: Lògica de negoci, API, renderització
3. **Base de dades (PostgreSQL)**: Emmagatzematge persistent de dades
4. **Sistema de fitxers**: Documents, imatges, adjunts
5. **Cache (Redis)**: Sessions, cache de consultes, tasques asíncrones

### Consideracions per a entorns de producció

:::{admonition} Factors clau per a entorns professionals
:class: warning
**🔒 Seguretat:**
- Autenticació multi-factor i autorització granular
- Xifratge de dades en trànsit i en repòs
- Auditoria completa d'accions
- Compliment de normatives (RGPD, ISO 27001)

**⚡ Rendiment:**
- Optimització de consultes de base de dades
- Cache estratègic de contingut
- Load balancing per distribució de càrrega
- Monitoratge proactiu de recursos

**📈 Escalabilitat:**
- Capacitat de créixer amb la demanda
- Arquitectura horitzontal
- Gestió automàtica de recursos
- Planificació de capacitat

**🛠️ Manteniment:**
- Actualitzacions planificades i automàtiques
- Backups regulars i verificats
- Monitoratge 24/7 amb alertes
- Documentació completa de processos

**📋 Compliment:**
- Logs detallats per auditoria
- Traçabilitat completa d'operacions
- Gestió de permisos granular
- Polítiques de retenció de dades
:::

### Evolució tecnològica: De tradicional a DevOps

```{mermaid}
timeline
    title Evolució del desplegament d'aplicacions
    
    section Tradicional
        2000-2010 : Servidor físic
                  : Instal·lació manual
                  : Configuració específica
                  
    section Virtualització
        2010-2015 : Màquines virtuals
                  : Millor utilització recursos
                  : Aïllament bàsic
                  
    section Contenidors
        2015-2020 : Docker i contenidors
                  : Portabilitat completa
                  : Microserveis
                  
    section DevOps/Cloud
        2020-2025 : CI/CD automàtic
                  : Orquestració Kubernetes
                  : Cloud nativo
```

## Pràctiques del tema

### Pràctica 1: Instal·lació tradicional

**📋 [Pràctica 1: Instal·lació tradicional d'Odoo](Tema2_prac1.md)**

**🎯 Objectius:**
- Configurar una màquina virtual amb Ubuntu Server
- Instal·lar PostgreSQL i configurar usuaris
- Descarregar i configurar Odoo des del codi font
- Crear serveis systemd per a automatització
- Verificar funcionament i documentar el procés

**⏱️ Durada estimada:** 4-6 hores
**🎓 Nivell:** Intermedi

### Pràctica 2: Desplegament amb Docker

**📋 [Pràctica 2: Docker i automatització](Tema2_prac2.md)**

**🎯 Objectius:**
- Configurar Docker i Docker Compose
- Crear contenidors personalitzats d'Odoo
- Implementar scripts d'automatització
- Configurar volumes i xarxes Docker
- Explorar conceptes de CI/CD

**⏱️ Durada estimada:** 3-4 hores
**🎓 Nivell:** Intermedi-Avançat

## Recursos addicionals

### Documentació especialitzada

Els següents annexos proporcionen configuracions avançades per a entorns professionals:

- **📖 [Part 1: Instal·lació tradicional pas a pas](Part1.md)**
  - Configuració completa d'Ubuntu Server per a Odoo
  - Instal·lació de PostgreSQL i dependències
  - Configuració de seguretat i optimització del sistema

- **📖 [Part 2: Desplegament amb Docker](Part2.md)**
  - Configuració de contenidors per a desenvolupament i producció
  - Docker Compose amb múltiples serveis
  - Gestió de volums i xarxes

- **📖 [Annex A: Configuració d'Apache com a Reverse Proxy](Apache_ReverseProxy.md)**
  - SSL/TLS amb certificats Let's Encrypt
  - Load balancing i alta disponibilitat
  - Configuració de seguretat avançada

- **📖 [Annex B: Operacions avançades amb Docker](Docker_Operations.md)**
  - Monitoratge de contenidors i recursos
  - Backup i restauració automatitzada
  - Scaling i optimització de rendiment

- **📖 [Annex C: Configuració avançada i producció d'Odoo](Configuracio_Avancada.md)**
  - Optimització de PostgreSQL per a grans volums de dades
  - Configuració de workers i balanceig de càrrega
  - Diagnòstic i resolució de problemes comuns

- **📖 [Annex D: Integració i Desplegament Continu (CI/CD)](Annex_CICD.md)**
  - Automatització de desplegaments
  - Testing automàtic i integració contínua
  - DevOps per a entorns Odoo

- **📖 [Annex E: Redis com a Cache i Broker de Missatges](Annex_Redis.md)**
  - Implementació de Redis per a acceleració d'Odoo
  - Configuració optimitzada per a producció
  - Scripts de monitoratge i manteniment automàtic
  - Resolució de problemes i optimització de rendiment

### Progressió d'aprenentatge recomanada

```{mermaid}
graph LR
    A[Fonaments Linux] --> B[Instal·lació Tradicional]
    B --> C[Conceptes Docker]
    C --> D[Desplegament Docker]
    D --> E[Reverse Proxy]
    E --> F[Producció Avançada]
    F --> G[CI/CD i Automatització]
    
    classDef essential fill:#e1f5fe
    classDef intermediate fill:#fff3e0
    classDef advanced fill:#f3e5f5
    
    class A,B essential
    class C,D,E intermediate
    class F,G advanced
```

**🟦 Nivell essencial** (obligatori per tots):
- Part 1: Instal·lació tradicional
- Pràctica 1: Implementació pas a pas

**🟨 Nivell intermedi** :
- Part 2: Desplegament amb Docker (recomanat)
- Annexos A i B: Configuració professional (NO PER AL CURS)

**🟣 Nivell avançat** (per a especialització):
- Annexos C i D: Producció i CI/CD (NO PER AL CURS)
- Implementació completa en entorn real (NO PER AL CURS)

### Bibliografia i referències

**📚 Documentació oficial:**
- [Documentació oficial d'Odoo 16](https://www.odoo.com/documentation/16.0/)
- [Docker Documentation](https://docs.docker.com/)
- [PostgreSQL Performance Tuning](https://wiki.postgresql.org/wiki/Performance_Optimization)
- [Redis Documentation](https://redis.io/documentation)

**🔧 Configuració i seguretat:**
- [Apache Configuration for Odoo](https://httpd.apache.org/docs/2.4/howto/reverse_proxy.html)
- [Let's Encrypt with Apache](https://certbot.eff.org)
- [OWASP Application Security Guidelines](https://owasp.org/)

**🚀 DevOps i automatització:**
- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [GitLab CI/CD Documentation](https://docs.gitlab.com/ee/ci/)
- [Docker Compose Best Practices](https://docs.docker.com/compose/production/)

**⚡ Optimització de rendiment:**
- [Redis Best Practices](https://redis.io/docs/manual/patterns/)
- [Odoo Performance Guidelines](https://www.odoo.com/documentation/16.0/administration/performance.html)
- **[Annex E: Implementació Redis](Annex_Redis.md)** - Guia completa específica del curs

Aquest tema et proporciona una base sòlida per desenvolupar una carrera exitosa en l'àmbit de la tecnologia empresarial moderna! 🎯✨


```{toctree}
:maxdepth: 2
:caption: Continguts del Tema 2
:hidden:

Part1
Tema2_prac1
Part2
Tema2_prac2
Apache_ReverseProxy
Docker_Operations
Configuracio_Avancada
Annex_CICD
Annex_Redis
```