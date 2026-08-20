# WATCHDOG AI
## TEHNIČKA ARHITEKTURA I SPECIFIKACIJA SOFTVERA
**Vrsta dela:** Računarski program (Softver) / AI Sistem za biometrijsku autentifikaciju  
**Oblast primene:** Upravljanje radnom snagom (WFM) i bezbednost u uživo kazinima (Live Casino)  

---

### 1. SAŽETAK I SVRHA SOFTVERA
Watchdog AI je softverski sistem poslovne klase za **pasivnu biometrijsku verifikaciju**, dizajniran za okruženja sa visokom gustinom prenosa uživo (npr. Live Casino). Funkcionišući u potpunosti kao "Headless" (nevidljivi) softverski sloj, eliminiše potrebu za hardverom za fizičku autentifikaciju (RFID, PIN tastature ili ekrani okrenuti krupijeima). Softver premošćava sirove podatke o rasporedu radne snage (WFM) sa mrežnim kamerama (uživo), autonomno verifikujući identitet krupijea na stotinama stolova i upozoravajući bezbednosno osoblje preko centralizovane kontrolne table.

### 2. OSNOVNA ARHITEKTURA I MODULI
Softver se oslanja na dinamički skalabilnu mikroservisnu arhitekturu (Python, FastAPI, React, Redis, DeepFace/InsightFace) podeljenu u tri vlasnička mehanizma:

#### A. Mehanizam za dinamičku WFM sinhronizaciju
- **Funkcija:** Autonomno parsiranje rasporeda smena ljudskih resursa (Excel/CSV).
- **Algoritamska logika:** Za razliku od statičkih sistema, ovaj mehanizam koristi vlasničku matricu baziranu na regularnim izrazima (regex) za dinamičko generisanje "Digitalnog blizanca" (Digital Twin) kazina. Bilo da studio ima 10 ili 1.000 stolova, mehanizam automatski popunjava strukturu baze podataka na osnovu učitanog WFM fajla.
- **Upravljanje stanjem:** Zapisuje parsirano stanje u Redis in-memory bazu podataka ultra-niske latencije, mapirajući očekivane ID-ove zaposlenih sa prostornim koordinatama (npr. Sto 8.1 očekuje zaposlenog sa ID 43286 u 22:30).

#### B. Headless AI Vision & RTSP jezgro
- **Funkcija:** Autonomna pozadinska vizuelna autentifikacija sa mrežnih kamera.
- **Algoritamska logika:** 
  1. *Automatsko mrežno hvatanje:* Sistem se direktno povezuje sa postojećim mrežnim IP kamerama studija (putem RTSP protokola) ili karticama za snimanje (Capture cards). Ne zahteva manuelni video unos ili interakciju krupijea.
  2. *Ekstrakcija okvira (Edge Frame Extraction):* Pozadinski demon u optimizovanim intervalima izdvaja ključne kadrove kako bi sačuvao CPU/GPU propusni opseg.
  3. *Biometrijsko ugrađivanje i L2 distanca:* Ekstrahuje 512-dimenzionalne karakteristike lica pomoću dubokih neuronskih mreža, poredeći snimak uživo sa HR referentnom slikom u manje od 100 milisekundi.

#### C. Centralizovana CCTV sigurnosna matrica (Dashboard)
- **Funkcija:** Jedini interfejs između čoveka i mašine, dizajniran isključivo za nadzor (Obezbeđenje / Pitboss).
- **Algoritamska logika:** React mreža vođena WebSocket tehnologijom u realnom vremenu. Umesto praćenja jednog stola, korisnički interfejs prikazuje ogromnu matricu svih aktivnih stolova. Stolovi pasivno održavaju status "BEZBEDNO" (SAFE - Zeleno). Prilikom biometrijskog neslaganja, specifični čvor trenutno aktivira "OPASNOST/NEOVLAŠĆENO" (DANGER - Crveno) upozorenje, omogućavajući trenutnu intervenciju.

### 3. INOVACIJA I ORIGINALNOST (PRAVO INTELEKTUALNE SVOJINE)
Osnovna intelektualna svojina Watchdog AI leži u njegovoj **"Zero-Hardware, Headless" petlji za sprovođenje provere**. Tradicionalni sistemi zahtevaju aktivni unos (skeniranje bedža) što ometa operacije. Watchdog AI je visoko originalan u svojoj metodi uzimanja dva potpuno različita, nestrukturirana izvora podataka — statičkih HR Excel rasporeda i sirovih mrežnih CCTV tokova — i njihovog autonomnog premošćavanja putem AI petlje za unakrsno referenciranje. Sposobnost dinamičkog skaliranja ove verifikacije na stotine čvorova bez uvođenja ijednog komada fizičkog hardvera predstavlja jedinstvenu poslovnu tajnu (trade secret) i arhitektonski novitet ovog softvera.

### 4. DIJAGRAM TOKA PODATAKA (TEKSTUALNI)
1. `WFM_TABELA` -> `DINAMICKI_PARSER` -> `REDIS_DIGITALNI_BLIZANAC`
2. `MREŽNI_RTSP_TOKOVI` -> `HEADLESS_WATCHDOG_DEMON` -> `EKSTRAKTOR_KARAKTERISTIKA_LICA`
3. `MEHANIZAM_ZA_POREDJENJE` (Upoređuje `REDIS_DIGITALNI_BLIZANAC` sa `SNIMKOM_UZIVO`)
4. `REZULTAT` -> `CCTV_SIGURNOSNA_MATRICA`

---
**AUTOR / KREATOR:** [Tvoje Ime / Kompanija]
**DATUM ZAVRŠETKA:** Avgust 2026.
**OKRUŽENJE ZA IMPLEMENTACIJU:** Bezbedna Docker kontejnerizacija
