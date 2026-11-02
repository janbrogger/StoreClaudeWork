# IB -> Norwegian karakterpoeng: conversion tables and method (research notes)

Prepared 2026-11-02 for an op-ed on Kunnskapsdepartementet's hearing of 29 Oct 2026
("Høyring - forslag om endring i forskrift om opptak til høgare utdanning - ny
omrekningstabell for International Baccalaureate", ref. 26/5123, deadline 10.12.2026).

**How this was researched.** Only WebSearch snippets were available (regjeringen.no,
lovdata.no, samordnaopptak.no, stortinget.no, ibo.org etc. are blocked for fetching from
this machine). The shared search budget ran out after ~30 queries, before the foreign
precedents (Sweden, Finland, Netherlands, Germany, UK, Australia) could be searched.
Every number below is traced to a search-result snippet; items from model memory are
marked **UNVERIFIED (model memory)** and were deliberately kept out of the CSV files.
Values given by sources as an average grade (e.g. 4,04) are also shown as karakterpoeng
(x10) because karakterpoeng are by definition the vitnemål average times 10.

---

## 1. The conversion tables

### Overview of versions

| Version | Status | Data basis | Where it is written down |
|---|---|---|---|
| (a) Long-standing table ("dagens tabell") | In force for admission 2025 and 2026 (new table postponed Feb 2025) | Fixed by the department decades ago; "Gjeldende omregningstabell for IB har vært uendret i flere tiår" (regjeringen.no press release 29.10.2026) | FOR-1999-12-14-1505 Vedlegg 2A (Lovdata, last corrected 1 March 2004); samordnaopptak.no "IB - poengberegning", Table 1 |
| (b) HK-dir table of 15 Dec 2022 | Announced for admission 2025-2026; postponed by minister Sigrun Aasland in Feb 2025 (Khrono) | "offisiell karakterstatistikk fra International Baccalaureate Organization (IBO)" i.e. global IB statistics; method reviewed by Norsk Regnesentral | familieportalen.mfa.no/?p=912; HK-dir press release (NTB 17950602); bergenkatedralskole.vgs.no |
| (c) Hearing of 18 March 2025 (new opptaksforskrift, id3090858) | Proposed from admission 2026/2027; not adopted - the new forskrift of 11 Sept 2025 (in force 1 Jan 2027) does not contain the new IB table | Vedlegg "Omrekningstabell for IB-diplom" shows "ny tabell (innføring 2026)" next to "opphavleg tabell"; values match the 2022 table where both are visible | regjeringen.no/contentassets/7168f1dffed04771888d4e653de692a0/vedlegg-omrekningstabell-for-ib.pdf |
| (d) Hearing of 29 Oct 2026 (id3183537) | On hearing; proposed from admission 2030-2031 | HK-dir table built on data from IB lines in Norway ("berre ... data frå IB-liner i Noreg"), starting at 20 IB points; the HK-dir note of 26.10.2026 also contains a global-statistics variant (columns "2026a"/"2026b" in the vedlegg) | regjeringen.no/contentassets/315531d605f3405cac8dc90700b75b63/ (høyringsnotat + "1-framlegg-til-ny-omrekningstabell...") |

### (a) The long-standing table (in force today)

Rows recovered from snippets (IB total -> Norwegian average grade / karakterpoeng):

| IB points | Norwegian average | Karakterpoeng | Source |
|---|---|---|---|
| 20 | 2,6 | 26,0 | 2026 høyringsnotat vedlegg ("dagens tabell"); elev.no snippet |
| 21 | 2,8 | 28,0 | 2026 høyringsnotat vedlegg |
| 24 | 3,43 | 34,3 | 2025 vedlegg, column "opphavleg tabell" |
| 30 | 4,29 | 42,9 | 2025 vedlegg, "opphavleg" |
| 32 | 4,57 | 45,7 | Lovdata Vedlegg 2A; school page citing samordnaopptak.no |
| 35 | 5,00 | 50,0 | Lovdata Vedlegg 2A; samordnaopptak.no example; 2025 vedlegg |
| 40 | 5,71 | 57,1 | 2025 vedlegg, "opphavleg" |
| 42 | 6,0 | 60,0 | Lovdata Vedlegg 2A |
| 43-45 | 6,0 | 60,0 | elev.no / utdanningsnytt snippet ("tidligere ble 43-45 poeng regnet som snitt 6,0") |

Observation (my arithmetic on the recovered rows, not a sourced statement): from 24 to 42
points the old table is linear with slope 1/7 grade per IB point (3,43 + (IB-24)/7
reproduces 4,29 / 4,57 / 5,00 / 5,71 / 6,0 exactly). In other words it maps an IB
subject average of 4 (24/6) to 3,43 and an average of 7 (42/6) to 6,0, and then caps:
42, 43, 44 and 45 all give 6,0. Below 24 the slope is steeper (20 -> 2,6; 21 -> 2,8).
Bonus points for TOK/EE: the older ranking regulation said that "bonuspoeng" are not
counted when IB points are converted (§ 7-11(2), snippet of Lovdata); the current
samordnaopptak.no page says diploma holders have their "Total points" converted with
Table 1 - whether the 2024+ practice includes the up-to-3 core points was not
resolvable from snippets (see "Unknown").

### (b) The HK-dir table of December 2022

HK-dir press release (NTB, Dec 2022, Norwegian): "Samordna opptak har mottatt offisiell
karakterstatistikk fra International Baccalaureate Organization (IBO), og har utarbeidet
en omregningstabell." Rows recovered:

| IB points | Norwegian average (2022 table) | Karakterpoeng | Compare old table |
|---|---|---|---|
| 20 | 2,0 | 20,0 | 2,6 |
| 24 | 2,90 (Abelia: "4 ... devaluere[s] ... til norsk 2,9"; Dok8:76 S: "karakteren 2 i alle fag") | 29,0 | 3,43 |
| 30 | 4,04 | 40,4 | 4,29 |
| 35 | 4,74 | 47,4 | 5,00 |
| 40 | 5,36 | 53,6 | 5,71 |
| 45 | 6,00 ("bare 45 poeng gir 6,0") | 60,0 | 6,0 (from 42) |

So the 2022 table lowers every recovered row except the maximum, and removes the
plateau at the top: only 45/45 gives 6,0. The loss is largest at the bottom (-0,6 at
20 points, -0,53 at 24) and shrinks towards the top (-0,25 at 30, -0,26 at 35, -0,35 at
40, 0 at 45). Abelia's hearing reply: the table "vil ha negative konsekvenser for
IB-elever i den nedre halvdelen av karakterskalaen".

Verbatim (Representantforslag 76 S (2024-2025), Dok8:202425:076s): "Den nye
konverteringstabellen synes ikke å ta hensyn til forskjellen i relativ karakterfordeling
mellom IB og norske elever. Et eksempel er at en elev som får 24 poeng i IB, vil regnes
om til å få karakteren 2 i alle fag i det norske systemet."

### (c) The hearing of March 2025

The vedlegg "Omrekningstabell for IB-diplom" (regjeringen.no, contentassets/7168f1df...)
has two columns, "ny tabell (innføring 2026)" and "opphavleg tabell"; all recovered
"ny tabell" values (24 -> 2,90; 30 -> 4,04; 35 -> 4,74; 40 -> 5,36; 45 -> 6,00) coincide
with the 2022 table. Khrono (Feb 2025, "Aasland utsetter omstridt omregning"): the
minister confirmed in a written answer to Stortinget that the change is postponed one
year, to admission 2026, because the new table would give IB pupils lower Norwegian
grades than before. Uniforum (March 2025): the proposal was first meant to apply from
2026/2027. Ung.no later answered that no new table would come in 2026. The press release
of 29.10.2026: "Forslaget til ny omregningstabell for IB ble sist sendt på høring
vinteren 2025. Der kom det flere innspill, som regjeringen har lyttet til."

### (d) The hearing of 29 October 2026

Verbatim from the høyringsnotat (Nynorsk): "Departementet foreslår å innføre ein ny
omrekningstabell for International Baccalaureate frå og med opptak til studieåret
2030-2031." - "Departementet foreslår at ein ny omrekningstabell for IB skal starte på 20
IB-poeng og berre vere utarbeida med data frå IB-liner i Noreg." - "sjå vedlegg for tabell
som er utvikla av HK-dir". Press release: "Blant annet skal tabellen nå bruke
datagrunnlag fra IB-skoler i Norge, og ikke global statistikk som opprinnelig
foreslått." Rationale: "omregningsmetoden i dagens tabell har vist seg å gi elever med
IB-diplom et fortrinn sammenlignet med andre elever."

Rows recovered from the vedlegg "IBs poengskala, dagens tabell og forslag til ny tabell":

| IB points | Dagens tabell | Forslag 2026 |
|---|---|---|
| 20 | 26,0 | 29,5 |
| 21 | 28,0 | 31,7 |

The HK-dir note dated 26.10.2026 ("1-framlegg-til-ny-omrekningstabell...") gives the
same figures on the 1-6 scale (2,95 for 20 points in the version built on Norwegian
data) and contains two variants labelled "2026a" and "2026b"; the snippet quotes
HK-dir's own preference: "HK-dir meiner at det er mest tenleg å utarbeide éin felles
omrekningstabell for alle IB-søkjarar ved å bruke global statistikk for IB." The
department nevertheless chose the Norwegian-data variant. No rows above 21 were visible
in snippets, so **it is not yet known from this research what 40-45 IB points become
under the 2026 proposal** - this is the single most important item on TO-FETCH.md.
Note the direction at the bottom: the 2026 proposal is *more* generous than today at 20
and 21 points (29,5 vs 26,0), unlike the 2022 table (20,0). Combined with the
department's complaint that 2,8 % of IB applicants reach 6,0, the implication (my
inference, not a sourced statement) is that the compression happens at the top.

### IB subject grades -> Norwegian subject grades (spesielle opptakskrav)

- samordnaopptak.no (IB - dekke spesielle opptakskrav): the requirement "4 i Matematikk
  R2" is met with grade **5** in a qualifying IB mathematics course (Analysis and
  approaches SL or HL, Applications and interpretation HL, older Mathematics SL /
  Mathematical Methods SL). Applications and interpretation SL does not appear in the
  list (snippet; verify).
- samordnaopptak.no (IB - poengberegning): IB subjects taken in addition to the diploma
  can cover special requirements or give language/science points if they appear on the
  IB certificate or DP course results; several IB mathematics courses (SL and HL, AA and
  AI) give 1,5 realfagspoeng.
- Course-result (non-diploma) applicants: course grades, plus TOK/EE points (1-5), are
  converted with "Table 2 (5-2)" on the samordnaopptak.no page. The IB 7 -> Norwegian 6
  etc. mapping of that table was not visible in snippets.
- IB subjects must be passed with grade 3 or better to count; general study competence
  requires 20 IB points or more (inn.no / samordnaopptak.no snippet - check whether this
  refers to the diploma threshold of 24).
- Chemistry/Physics mapping (Kjemi 1+2, Fysikk 1): not found in snippets.

---

## 2. How Norwegian karakterpoeng work, and how IB compares

**Karakterpoeng** = the average of all numeric grades on the vitnemål, with two decimals,
multiplied by 10 (ung.no / dn.no / uia.no snippets: "Karakterpoeng er gjennomsnitt av
tallkarakterene på vitnemålet, med to desimaler, multiplisert med 10"; a 4,5 average
gives 45 karakterpoeng; maximum 60,0).

**Skolepoeng** (used in førstegangsvitnemålskvoten) = karakterpoeng + realfagspoeng and
språkpoeng (joint cap 4,0; Matematikk R2 and Fysikk 2 give 1,0 each, other 140-hour
science programme subjects 0,5; max 1,5 språkpoeng per language, only for programme
subjects) + kjønnspoeng (+ points for admission tests where used).

**Konkurransepoeng** (ordinary quota) adds alderspoeng (up to 8) and tilleggspoeng
(up to 2, for folkehøgskole/military service/higher education). So the theoretical
maximum is 60 + 4 + 2 + 8 (+ kjønnspoeng) in the ordinary quota, 64 (+ kjønnspoeng) in
the first-time quota. Reform: from admission 2027 (one snippet says 2028) språkpoeng,
alderspoeng and tilleggspoeng are removed and realfagspoeng halved (ung.no snippets
citing the new opptaksforskrift; verify the exact year on samordnaopptak.no).

**IB total**: six subjects graded 1-7 (max 42) plus up to 3 core points from Theory of
Knowledge and the Extended Essay, max 45; diploma requires 24 (UNVERIFIED (model memory)
for the 24/42/45 structure - the snippets only confirm "max 45" and that "24 points
corresponds to an average of 4" (Abelia)). Under the old table an IB subject average of
7 (42 points) = Norwegian 6,0, average 4 (24) = 3,43; under the 2022 table average 4 =
2,90 and only 45 = 6,0.

**Norwegian grade-point distribution vs IB**: the only comparative statistic found is
the one the department itself uses (press release 29.10.2026, from HK-dir applicant
statistics): "0,08 % av søkerne med norsk videregående opplæring (studieforberedende)
fikk snitt 6,0 i opptaket, mens 2,8 % av IB-søkerne fikk dette" - 35 times as many.
Shares with average 5,5+ etc. were not found. Context from Udir (Karakterer i
videregående skole 2023-2024; 2025 analysis): "elevenes snittkarakterer i mange av
fagene er litt høyere i skoleåret 2023-2024 enn de var i årene før pandemien"; the last
three years the averages in most common-core subjects have been "ganske stabile"; pupils
"får som regel lavere karakterer til skriftlig eksamen enn til standpunkt"; Udir also
writes that small margins on the vitnemål have large effects on study opportunities.
(The parallel research folder `norway-grades/` should hold the inflation time series.)

---

## 3. The statistical method

**Legal basis (new opptaksforskrift FOR-2025-09-11-1850, kap. 9-1 "Omrekning av
utanlandske karakterar", Lovdata snippet):** the tables are made "etter statistiske
metodar"; "Tabellane skal lagast ved å finne prosentilar i det utanlandske
datagrunnlaget"; where no table exists a linear formula is used. Vedlegg II of the
regulation lists the tables; "Departementet har overført mynde og ansvar for fastsetjing
av dei fleste omrekningstabellar til Direktoratet for høgare utdanning og kompetanse ved
tenesta Samordna opptak" (but the IB table is fixed by the department - the 2026
hearing amends Vedlegg II).

**2022 method (HK-dir / Norsk Regnesentral):** HK-dir press release Dec 2022: "I 2022
fikk Samordna opptak ekstern bistand av Norsk Regnesentral til å vurdere metodene som
brukes for å lage omregningstabeller. Norsk Regnesentral foreslo at omregningstabellene
kan ta utgangspunkt i den empiriske kumulative fordelingsfunksjonen («ecdf») for en
utenlandsk karakterstatistikk, sett opp mot ecdf for norsk karakterstatistikk." The NR
discussion paper (samordnaopptak.no, "En diskusjon av noen statistiske metoder brukt
for å lage omregningstabeller for utenlandske karakterer", 04.11.2022) finds the ecdf
method best on calibration, with an interpolated variant second. In short this is
equipercentile matching: an IB score is mapped to the Norwegian average that sits at the
same percentile of the Norwegian studiespesialiserende vitnemål distribution. Minister's
written answers (Stortinget, qnid 98049 and 100321): the comparison is "en ren statistisk
sammenligning av populasjonene"; "den nye tabellen bygger på IBOs offisielle
karakterstatistikk, og ... den statistiske metoden er vurdert av Norsk Regnesentral";
"omregningstabellene er en objektiv statistisk metode for rettferdig konkurranse om
studieplasser, ikke en devaluering av noens kvalifikasjoner". HK-dir's general method
description (regjeringen.no Vedlegg II PDF): "Metoden går i korte trekk ut på å
sammenligne karakterfordelingen i det utenlandske systemet med den norske"; the IB
average-grade data "ble gitt til HK-dir av IB-stiftelsen og statistisk sammenlignet med
karaktergjennomsnitt fra norske vitnemål fra studiespesialiserende".

**2026 method:** same percentile approach but with the IB distribution of Norwegian IB
lines only, starting at 20 points (høyringsnotat; HK-dir note 26.10.2026 with variants
2026a/2026b). The notat's own phrase "etablert statistisk metode" was not visible in a
snippet and should be confirmed in the PDF.

**Assumptions embedded in the method (as the critics and the documents frame them):**
1. The two applicant populations have the same ability distribution, so equal percentiles
   mean equal merit - NIBS (letter 3 May 2023): "its basic assumptions may not be valid",
   "sampling bias which disfavours IB students may occur"; Dok8:76 S: ignores "forskjellen
   i relativ karakterfordeling mellom IB og norske elever".
2. The Norwegian vitnemål distribution is the reference ("gold standard"); any inflation
   in Norwegian standpunkt grades propagates into a stricter IB table.
3. The 2022/2025 version used the *global* IB distribution, i.e. assumed Norwegian IB
   applicants are drawn from the world population; the 2026 version drops this.
4. Ceiling: the 2026 rationale is explicitly about the 6,0 ceiling (2,8 % vs 0,08 %).
   Under percentile matching the top IB score can only reach 6,0 if its share is at
   most the Norwegian share at 6,0 - which mechanically pushes 6,0 to 45/45 or beyond.
5. Process critique: HK-dir "chose to disregard national statistics on admission points,
   completion and expectation indicators for Norwegian IB students" (Jønnes, Stortinget
   qnid 98049); NIBS was informed only shortly before the Dec 2022 announcement and
   neither IB schools nor the IBO were involved; "over 500 høringssvar uttrykte bekymring
   for IB-programmets fremtid" (Jønnes). An.no debate piece: "Elever som velger et
   krevende utdanningsløp får devaluert sine karakterer".
6. IB's criterion-referenced, exam-based grading (grade boundaries fixed against
   standards, not quotas) vs Norwegian norm-drifting standpunkt grades - argued in the
   op-ed context; the snippets do not contain a Norwegian source making this point
   explicitly (NIBS letter may; fetch it).

---

## 4. Foreign precedents

Only Denmark was reached before the search budget ran out. Everything else below is
**UNVERIFIED (model memory)** and is excluded from tables_foreign.csv.

- **Denmark**: IB points are converted to the 7-trins-skala by a ministry table; EUC Syd's
  page (snippet) gives 24 -> 4,4 and 45 -> 12,7 (the latter exceeds the scale maximum
  of 12 and must be checked in the official table). Folketinget documents to fetch:
  BUU alm. del bilag 79 (2015-16, ft.dk/samling/20151/almdel/BUU/bilag/79/1582938.pdf)
  and spm. 162 (2014-15). UNVERIFIED (model memory): the Danish table was recalibrated
  around 2015-16 after IB pupils complained that the conversion was too harsh.
- **Sweden**: UHR converts IB to meritvärde (max 20,00). Found: IFN/Jonas Vlachos 2016
  op-ed "På tok för lätt för IB-elever att få toppbetyg" (ifn.se PDF) arguing the Swedish
  conversion was too generous; Riksdag motions HE0253, HA02133, HB02737 and written
  question "En rättvis bedömning för elever som går IB-program" (h411174) on the
  fairness of the IB conversion. UNVERIFIED (model memory): a new conversion applied from
  autumn 2014 when the Swedish grade scale changed (A-F), with linear mapping from IB
  points; values not retrieved.
- **Finland**: UNVERIFIED (model memory): IB results are scored directly in
  todistusvalinta point tables published by universities (IB 7 ~ laudatur equivalent).
- **Netherlands**: UNVERIFIED (model memory): IB diploma (24+) = VWO; for numerus fixus
  selection institutions set their own conversions.
- **Germany**: a KMK agreement converts IB total points to an Abitur average
  (scribd document "ib_points_to_abitur_grade_conversion_table" exists). UNVERIFIED
  (model memory): formula N = 1 + 3 x (42 - P) / 18 for P between 24 and 42, i.e. 42 ->
  1,0, 24 -> 4,0; core points not counted.
- **UK (UCAS)**: UNVERIFIED (model memory): the tariff is per component, not per total:
  HL 7 = 56, 6 = 48, 5 = 32 ...; SL 7 = 28; EE/TOK bonus small; 45 points therefore
  does not equal a single tariff figure like 720.
- **Australia**: UAC document "Determining ranks for IB students"
  (uac.edu.au/assets/documents/international-baccalaureate/determining-ranks-for-IB-students.pdf)
  found. UNVERIFIED (model memory): until 2021 a 45 converted to 99.95 ATAR-equivalent
  for all 45-scorers; from the 2022 intake a fine-grained "IB admission score" using
  HL/SL grade detail and the Australian IB cohort distribution was introduced after
  universities complained the old schedule was too generous at the top.

---

## 5. What is still unknown

1. Full row set of all four Norwegian tables (only 9-11 rows of (a), 6 of (b)/(c), 2 of
   (d) recovered). In particular (d) at 35-45 points - the heart of the op-ed thesis.
2. Whether (c) is exactly (b) (it appears so), and whether the 2026 "2026a" (global) and
   "2026b" (Norwegian data) columns differ at the top.
3. Whether TOK/EE core points are included in "Total points" today.
4. Table 2 (IB course grades -> Norwegian grades) and the Kjemi/Fysikk mapping.
5. The exact wording of the 2026 method section ("etablert statistisk metode"), the
   sizes of the samples (how many Norwegian IB candidates per year), and which Norwegian
   reference population (all studieforberedende applicants? vitnemål holders?).
6. Norwegian distribution shares at 5,5+, 5,0+ etc.; IB Norway distribution.
7. All foreign values except the two Danish points.

---

## Sources

(All accessed 2026-11-02 via WebSearch snippets only; the hosts themselves could not be
fetched from this machine.)

1. https://www.regjeringen.no/no/dokumenter/holring-om/id3183537/ - "Høyring - forslag om endring i forskrift om opptak til høgare utdanning - ny omrekningstabell for International Baccalaureate", Kunnskapsdepartementet, 29.10.2026 (deadline 10.12.2026).
2. https://www.regjeringen.no/contentassets/315531d605f3405cac8dc90700b75b63/hoyringsnotat-forslag-om-endring-i-forskrift-om-opptak-til-hogare-utdanning-ny-omrekningstabell-for-ib.pdf - Høyringsnotat, KD, Oct 2026.
3. https://www.regjeringen.no/contentassets/315531d605f3405cac8dc90700b75b63/1-framlegg-til-ny-omrekningstabell-for-international-baccalaureate-ib.pdf - HK-dir, "Framlegg til ny omrekningstabell for IB", dated 26.10.2026.
4. https://www.regjeringen.no/no/aktuelt/ny-omregningstabell-for-ib-karakterer-sendes-pa-horing/id3184606/ - Press release, KD, 29.10.2026.
5. https://www.regjeringen.no/contentassets/7168f1dffed04771888d4e653de692a0/vedlegg-omrekningstabell-for-ib.pdf - "Vedlegg: Omrekningstabell for IB-diplom" (ny tabell innføring 2026 vs opphavleg tabell), KD, March 2025 hearing.
6. https://www.regjeringen.no/no/dokumenter/hoyring-forslag-til-ny-forskrift-om-hogare-utdanning-opptaksforskrift/id3090858/ - Hearing of 18.03.2025 on the new opptaksforskrift (deadline 18.06.2025).
7. https://www.regjeringen.no/contentassets/3ec2f4e6590445f8994720962f8f1400/hoyringsnotat2519275-002.pdf - Høyringsnotat for the 2025 hearing.
8. https://www.regjeringen.no/contentassets/a16ceedba555472d86172a8fb73192ff/vedlegg-ii.-liste-over-tabellar-for-omrekning-av-karakterer-fra-utenlandsk-vidaregaande-opplaring.pdf - Vedlegg II with HK-dir method description.
9. https://www.regjeringen.no/contentassets/a0bf31cb0ef1411481211e542cd9389c/vedlegg-ii-liste-over-alle-omregningstabeller-per-2023.pdf - Vedlegg II list of all tables per 2023 (2023 hearing).
10. https://www.regjeringen.no/no/dokumenter/hoyring-av-forslag-om-endringar-i-forskrift-om-opptak-til-hogare-utdanning-for-opptaksaret-2025-2026/id3041173/Download/?vedleggId=fd7e89aa-284b-4581-a5fd-3dff8536040d - Abelia's hearing reply (2024).
11. https://lovdata.no/dokument/SFO/forskrift/1999-12-14-1505/KAPITTEL_6 - FOR-1999-12-14-1505 Vedlegg 2A "Tabell for omregning av karakterpoeng for søkere med International Baccalaureate (IB)", Lovdata.
12. https://lovdata.no/dokument/SF/forskrift/2025-09-11-1850/KAPITTEL_9-1 - Opptaksforskrifta 2025, "Omrekning av utanlandske karakterar", Lovdata.
13. https://lovdata.no/dokument/SF/forskrift/2017-01-06-13/vedleggII - Opptaksforskrift 2017 Vedlegg II, Lovdata.
14. https://www.samordnaopptak.no/universitet-og-hogskole/utdanning-fra-utlandet/land/ib/poengberegning.html - Samordna opptak, "IB - poengberegning".
15. https://www.samordnaopptak.no/universitet-og-hogskole/utdanning-fra-utlandet/land/ib/dekke-spesielle-opptakskrav.html - Samordna opptak, "IB - dekke spesielle opptakskrav".
16. https://www.samordnaopptak.no/universitet-og-hogskole/utdanning-fra-utlandet/pdfer/omregningstabeller-for-utenlandske-karakterer-041122.pdf - Norsk Regnesentral, "En diskusjon av noen statistiske metoder brukt for å lage omregningstabeller for utenlandske karakterer", 04.11.2022.
17. https://familieportalen.mfa.no/?p=912 and https://nettsteder.regjeringen.no/familieportalen/aktuelt/samordna-opptak-tabell-som-skal-gjelde-fra-studiearet-2025-2026/ - "Samordna opptak - Tabell som skal gjelde fra studieåret 2025/2026", UD familieportal.
18. https://kommunikasjon.ntb.no/pressemelding/17950602/ny-omregning-for-ib-diplom-vil-gi-likebehandling-ved-opptak-til-hoyere-utdanning?publisherId=9361272 - HK-dir press release, Dec 2022.
19. https://www.bergenkatedralskole.vgs.no/nyheiter/new-conversion-table-for-ib-diploma-grades - Bergen katedralskole news.
20. https://www.bergenkatedralskole.vgs.no/contentassets/a90efe96a9fa4e28b943d1f14c552789/nibs-brev-til-foresatte-og-alumni-mai-2023.pdf and https://afk.no/aas-vgs/_f/p74/if6f690c9-c039-4ae3-9089-c525b4563ab7/nibs-letter-to-parents-guardians-alumni.pdf - NIBS letter, 3 May 2023 (NO/EN).
21. https://www.stortinget.no/no/Saker-og-publikasjoner/Publikasjoner/Representantforslag/2024-2025/dok8-202425-076s - Representantforslag 76 S (2024-2025) on postponing the IB tables.
22. https://www.stortinget.no/no/Saker-og-publikasjoner/Sporsmal/Skriftlige-sporsmal-og-svar/Skriftlig-sporsmal/?qnid=98049 - Written question, Kari-Anne Jønnes (H), with minister's answer.
23. https://www.stortinget.no/no/Saker-og-publikasjoner/Sporsmal/Skriftlige-sporsmal-og-svar/Skriftlig-sporsmal/?qnid=100321 - Written question, Himanshu Gulati (FrP), with answer.
24. https://www.stortinget.no/globalassets/pdf/dokumentserien/2024-2025/dokument-15-1_202425.pdf, .../dokument-15-8-202425.pdf, .../2025-2026/dokument-15-7-202526.pdf - Dokument 15 collections with IB questions (Astrup, Jønnes, Velle).
25. https://www.khrono.no/aasland-utsetter-omstridt-omregning/944452 - Khrono, Feb 2025.
26. https://www.abelia.no/nyheter/2025/februar/utsetter-urettferdig-omregningstabell/ - Abelia, Feb 2025.
27. https://www.utdanningsnytt.no/elevorganisasjonen-internasjonalt-international-baccalaureate/elevene-ble-hort-ny-poengberegning-pa-ib-linja-innfores-ikke-likevel/432473 - Utdanningsnytt.
28. https://elev.no/likemuligheter/ - Elevorganisasjonen campaign page.
29. https://www.uniforum.uio.no/nyheter/2025/03/slik-kan-de-nye-opptaksreglene-for-hoyere-utdannin.html - Uniforum, March 2025.
30. https://www.ung.no/oss/jt7FgVybmpTdJNWTZGpcif - Ung.no, "Kommer det en ny omregningstabell for IB?".
31. https://www.an.no/elever-som-velger-et-krevende-utdanningslop-far-devaluert-sine-karakterer/o/5-4-1779449 - Avisa Nordland debate piece.
32. https://www.udir.no/tall-og-forskning/statistikk/statistikk-videregaende-skole/analyser/2024/karakterer-i-videregaende-skole-20232024/ and .../2025/karakterer-i-videregaende-skole-2025/ - Udir grade analyses.
33. https://www.dn.no/samordna-opptak/slik-beregnes-poengene/1-1-5421790 ; https://www.uia.no/studier/soknad-og-opptak/poengberegning.html ; ung.no answers - karakterpoeng rules.
34. https://www.eucsyd.dk/ib-diploma/konvertering-mellem-karakterer/ - EUC Syd, Danish IB conversion.
35. https://www.ft.dk/samling/20151/almdel/BUU/bilag/79/1582938.pdf - Folketinget BUU bilag 79 (2015-16).
36. https://www.ifn.se/media/f5dhzht1/2016-vlachos-på-tok-för-lätt-för-ib-elever-att-få-toppbetyg-förlaga.pdf - Vlachos (IFN), 2016.
37. https://www.riksdagen.se/sv/dokument-och-lagar/dokument/skriftlig-fraga/en-rattvis-bedomning-for-elever-som-gar-ib-program_h411174/ ; https://data.riksdagen.se/dokument/HE0253 ; HA02133 ; HB02737 - Riksdag items on IB conversion.
38. https://www.uac.edu.au/assets/documents/international-baccalaureate/determining-ranks-for-IB-students.pdf - UAC (Australia).
39. https://www.ibo.org/globalassets/new-structure/about-the-ib/pdfs/dp-cp-final-statistical-bulletin-may-2023.pdf - IB statistical bulletin May 2023 (points distribution).
