# ARGUSCAS AI
## TEHNIČKA ARHITEKTURA I SPECIFIKACIJA SOFTVERA
**Vrsta dela:** Računarski program (Softver) / AI Sistem za biometrijsku autentifikaciju  
**Oblast primene:** Upravljanje radnom snagom (WFM) i bezbednost u uživo kazinima (Live Casino)  

---

### 1. SAŽETAK I SVRHA SOFTVERA
ArgusCas AI je softverski sistem poslovne klase za **pasivnu biometrijsku verifikaciju i eliminaciju lažnih alarma**, dizajniran za okruženja sa visokom gustinom prenosa uživo (npr. Live Casino). Funkcionišući u potpunosti kao "Headless" (nevidljivi) softverski sloj, eliminiše potrebu za hardverom za fizičku autentifikaciju (RFID, PIN tastature ili ekrani okrenuti krupijeima). Softver premošćava sirove podatke o rasporedu radne snage (WFM) sa mrežnim CCTV kamerama uživo, autonomno verifikujući identitet krupijea na stotinama stolova i omogućavajući neometan rad bez prekidanja toka igre.

### 2. OSNOVNA ARHITEKTURA I MODULI
Softver se oslanja na dinamički skalabilnu mikroservisnu arhitekturu (Python, FastAPI, React, Redis, DeepFace/InsightFace) podeljenu u četiri vlasnička mehanizma:

#### A. Mehanizam za dinamičku WFM sinhronizaciju i predviđanje rotacije
- **Funkcija:** Autonomno parsiranje rasporeda smena ljudskih resursa (Excel/CSV).
- **Algoritamska logika:** Koristi vlasničku matricu baziranu na regularnim izrazima (regex) za dinamičko generisanje "Digitalnog blizanca" (Digital Twin) kazina. Pored trenutnog krupijea, sistem automatski identifikuje i mapira:
  1. *Narednog krupijea za sledeću smenu (Next-Dealer Schedule)* za svaki pojedinačni sto.
  2. *Dodeljene mešače karata po studiju (Studio Shufflers)*.
- **Upravljanje stanjem:** Zapisuje parsirane podatke u Redis in-memory bazu podataka ultra-niske latencije.

#### B. Headless AI Vision & RTSP jezgro
- **Funkcija:** Autonomna pozadinska vizuelna autentifikacija sa mrežnih kamera.
- **Algoritamska logika:** 
  1. *Automatsko mrežno hvatanje:* Povezuje se direktno sa postojećim mrežnim IP kamerama (putem RTSP protokola) bez ikakvog ručnog unosa.
  2. *Ekstrakcija okvira:* Pozadinski demon u optimizovanim intervalima izdvaja ključne kadrove čuvajući mrežni i hardverski protok.
  3. *Biometrijsko ugrađivanje:* Ekstrahuje 512-dimenzionalne vektore lica pomoću dubokih konvolucionih neuronskih mreža.

#### C. Mehanizam hijerarhijske bele liste i vremenske tolerancije (Anti-False-Positive Engine)
- **Funkcija:** Sprečavanje lažnih bezbednosnih alarma prilikom prisustva više lica u kadru (operativne situacije uživo).
- **Algoritamska logika:** Svako detektovano lice prolazi kroz četvorostepeni hijerarhijski filter:
  1. *Primarni krupije:* Da li odgovara trenutno zakazanom krupijeu za dati sto?
  2. *Tolerancija primopredaje smene (Grace Period):* Da li odgovara narednom krupijeu unutar vremenskog prozora od +/- 2 minuta od početka nove smene? (Omogućava nesmetano stajanje iza kamere i rotaciju).
  3. *Stüdyo mešač karata:* Da li odgovara autorizovanom osoblju za mešanje karata (Shuffler) u tom studiju?
  4. *Globalni supervizor:* Da li odgovara autorizovanom rukovodiocu sale (Floor Supervisor) koji obilazi stolove?
- **Odluka:** Alarm se aktivira samo ukoliko lice u kadru ne prođe nijedan od ova 4 nivoa provere.

#### D. Centralizovana CCTV sigurnosna matrica (Dashboard)
- **Funkcija:** Interfejs za nadzor namenjen isključivo obezbeđenju i menadžmentu (Pitboss).
- **Algoritamska logika:** React matrica sa WebSocket ažuriranjem u realnom vremenu. Prikazuje sve aktivne stolove sa statusom "BEZBEDNO" (Zeleno) ili "OPASNOST/NEOVLAŠĆENO" (Crveno), uz detaljan prikaz uloga prisutnih lica (npr. *Krupije + Supervizor*).

### 3. INOVACIJA I ORIGINALNOST (PRAVO INTELEKTUALNE SVOJINE)
Osnovna intelektualna svojina ArgusCas AI leži u njegovoj **"Zero-Hardware, Hierarchical Multi-Face Enforcement"** logici. Za razliku od rigidnih sistema koji prijavljuju grešku čim se pojavi drugo lice u kadru, ArgusCas AI autonomno razlikuje legitimne operativne procese (rotacija krupijea, kontrola supervizora, rad mešača karata) od stvarnih bezbednosnih proboja putem kontekstualne vremenske i prostorne matrice.

### 4. DIJAGRAM TOKA PODATAKA (TEKSTUALNI)
1. `WFM_TABELA` -> `DINAMIČKI_PARSER` -> `REDIS (Krupije + Naredni Krupije + Mešači + Supervizori)`
2. `RTSP_KAMERE` -> `AI_DETEKCIJA_VIŠE_LICA` -> `VEKTORSKA_EKSTRAKCIJA`
3. `HIJERARHIJSKI_FILTER` (Krupije -> Rotacija +/-2min -> Mešač -> Supervizor)
4. `REZULTAT` -> `CCTV_SIGURNOSNA_MATRICA`

---
**AUTOR / KREATOR:** [Tvoje Ime / Kompanija]
**DATUM ZAVRŠETKA:** Avgust 2026.
**OKRUŽENJE ZA IMPLEMENTACIJU:** Bezbedna Docker kontejnerizacija
