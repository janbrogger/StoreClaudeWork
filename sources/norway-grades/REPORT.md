# Norwegian grade data and grade-inflation research - what was found

Prepared 2026-11-02 for the IB-conversion op-ed. Network was restricted to web-search
snippets plus GitHub; no Udir/SSB/SO page could be opened directly. Every number below
traces to a search snippet or a GitHub file (cited inline); anything from memory is marked
UNVERIFIED (model memory). Data files: `grunnskolepoeng.csv`, `vgs_grades.csv`,
`samordna_opptak.csv`, `applicant_distribution.csv`; retrieval list: `TO-FETCH.md`.

## 1. Grunnskolepoeng (mean at end of 10th grade), national

| Cohort (spring) | Mean | Source type |
|---|---|---|
| 2009 | 39,5 | SSB |
| 2010 | gap | - |
| 2011 | 39,9 | SSB |
| 2012 | "40" (rounded) | SSB |
| 2013 | 40,0 | SSB table |
| 2014 | 40,4 | SSB table (year label to verify) |
| 2015 | 40,8 | SSB |
| 2016 | 41,2 | SSB |
| 2017 | gap | - |
| 2018 (2017-18) | 41,8 | Udir via Statsforvalteren Vestland |
| 2019 (2018-19) | 42,0 | Udir via Statsforvalteren Vestland / KD |
| 2020 (2019-20) | 43,2 | KD press release - **no exams** |
| 2021 (2020-21) | 43,3 | Udir - **no exams** |
| 2022 (2021-22) | 43,4 | Udir - **no exams**, all-time high |
| 2023 (2022-23) | 42,4 | Udir - exams back |
| 2024 (2023-24) | 42,2 | Udir |
| 2025 (2024-25) | 42,0 (derived: 42,2 - 0,2) | Statsforvalteren Vestland 2026 |
| 2026 (2025-26) | 42,2 | Statsforvalteren Vestland 2026 |

So the thesis holds in broad strokes: +2,5 points from 2009 (39,5) to 2019 (42,0) with exams
in place, a +1,2 jump when exams were cancelled, and a partial fall-back to ~42,2 - still
about 2,7 above 2009 - after exams returned.

Verbatim:
- SSB 2009: "Gjennomsnittet for alle elever er 39,5 poeng."
- SSB 2011: "For alle elevene som gikk ut i 2011 var snittet 39,9 grunnskolepoeng." "I gjennomsnitt fikk jentene 42,0 grunnskolepoeng, mens guttene fikk 37,9."
- SSB 2015: "Gjennomsnittlig grunnskolepoeng har økt fra 39,5 til 40,8 poeng på seks år."
- SSB 2016: "Siden 2009 har de gjennomsnittlige grunnskolepoengene gått fra 39,5 til årets snitt på 41,2 på landsbasis."
- Statsforvalteren Vestland (Udir figures): "41,8 for 2017-2018 og 42,0 for 2018-2019"; 2019-20 increase "1,2 grunnskulepoeng".
- KD 25.08.2020 ("Høyeste karaktersnitt noensinne for årets tiendeklassinger"): avgangselevene fikk 43,2 grunnskolepoeng, over ett poeng mer enn året før; the ministry attributed part of the rise to cancelled exams and to the postponed deadline for standpunkt.
- Udir 2021-22: "Skoleåret 2021-2022 hadde avgangselevene i grunnskolen i gjennomsnitt 43,4 grunnskolepoeng" (jenter 45,6, gutter 41,3).
- Udir 2022-23: 42,4, "1 grunnskolepoeng mindre enn for 2022-kullet".
- Udir 2023-24: "Årets avgangselever fikk i snitt 42,2 grunnskolepoeng. Jentenes snitt, på 44,3 grunnskolepoeng, ligger for 2023-2024 4 poeng over guttenes snitt på 40,3."
- SSB on comparability: grunnskolepoeng for 2020-2022 "er kun basert på standpunktkarakterer, og er derfor ikke sammenlignbare med grunnskolepoeng fra andre skoleår."
- SSB vs Udir: "Det er noe avvik mellom tallene i denne statistikken og tallene som UDIR publiserer fordi utvalgskriteriene er annerledes." (The 2009-2016 rows are SSB, 2018+ are Udir; expect ~0,1-0,2 offsets.)

## 2. Upper secondary (videregående, studieforberedende)

### 2a. Programme-subject maths, standpunkt means 2007-08 -> 2025-26 (Udir Statistikkportalen via GitHub mirror)

A GitHub repo (`VirtualAiCorp/NMBU-sammenligning`) pulled table `VGO/ResultatFagV/2/5`
(the table behind udir.no "Karakterer i videregående skole") on 2026-09-24 and committed the
national series; the repo states it cross-checked the 2025-26 values against Udir's own
article. Full rows (with n) in `vgs_grades.csv`.

| Year | R1 | R2 | S1 | S2 |
|---|---|---|---|---|
| 2007-08 | 3,9 | - | 3,5 | - |
| 2008-09 | 3,9 | 3,8 | 3,7 | 3,6 |
| 2009-10 | 3,9 | 3,8 | 3,7 | 3,5 |
| 2010-11 | 4,0 | 3,9 | 3,7 | 3,6 |
| 2011-12 | 4,0 | 3,9 | 3,7 | 3,6 |
| 2012-13 | 3,9 | 3,9 | 3,6 | 3,5 |
| 2013-14 | 4,0 | 3,9 | 3,6 | 3,6 |
| 2014-15 | 3,9 | 3,9 | 3,6 | 3,5 |
| 2015-16 | 4,0 | 4,0 | 3,7 | 3,6 |
| 2016-17 | 4,1 | 4,1 | 3,8 | 3,8 |
| 2017-18 | 4,2 | 4,3 | 3,8 | 3,8 |
| 2018-19 | 4,2 | 4,2 | 3,9 | 3,8 |
| 2019-20 | 4,2 | 4,3 | 3,9 | 3,9 |
| 2020-21 | 4,2 | 4,2 | 3,8 | 3,8 |
| 2021-22 | (3,8; n=61 - bad row) | 4,3 | (3,0; n=55 - bad row) | 3,8 |
| 2022-23 | 4,1 | 4,2 | 3,5 | 3,8 |
| 2023-24 | 4,0 | 4,2 | 3,6 | 3,7 |
| 2024-25 | 4,0 | 4,1 | 3,5 | 3,8 |
| 2025-26 | 4,0 | 4,2 | 3,5 | 3,8 |

Reading: R1/R2 standpunkt rose ~0,3 between 2015-16 and 2017-18 and have stayed ~0,2-0,3
above the 2008-2015 plateau; S1/S2 rose similarly to 2019-20 and then fell back (but the
S-cohort shrank from ~7 500 to ~1 500 after LK20, so composition changed). The 2021-22 R1
and S1 rows have implausibly small n (the mirror evidently missed a fagkode that year) and
must be re-fetched. These are teacher-set grades; the matching eksamen series exists in the
same table (KaraktertypeID=3) but was not mirrored - see TO-FETCH.

### 2b. Standpunkt vs eksamen gap, and the long-run statement from Udir

- Udir (karakterer i vgs, 2021-22 or 2023-24 article, exact page to confirm): "I løpet av de
  siste 15 årene har elevene i de fleste fellesfagene i videregående opplæring fått stadig
  bedre karakterer. Undersøkelser viser imidlertid ikke den samme utviklingen i elevenes
  kompetanse" - Udir calls this an "unaturlig utvikling". **This is the strongest single
  quote for the op-ed: the regulator itself says grades rose while measured competence did not.**
- Udir analysis (series back to 2011-12): "nesten halvparten av elevene i videregående har
  fått dårligere karakter til skriftlig eksamen enn standpunktkarakteren i samme fag"
  (snippet paraphrase; original in PDF id 156295).
- SSB (citing Udir 2020b, data 2016-2019): "fire av ti elever får en lavere karakter på
  skriftlig eksamen enn de fikk i standpunkt", largest difference in Norwegian.
- Grunnskole: "41 prosent av elevene får en lavere karakter til skriftlig eksamen enn det
  de fikk i standpunkt."
- Udir: norsk hovedmål skriftlig eksamen Vg3 averaged "3,6 i de to årene før pandemien";
  a Udir table shows norsk hovedmål Vg3 SF standpunkt "about 4,0-4,2" across the years shown
  (exact per-year values not captured) - i.e. a standpunkt-eksamen gap of ~0,5.
- SSB 2019 (level likely 10. trinn; verify): norsk hovedmål standpunkt gutter 3,6 / jenter
  4,3 vs eksamen 3,1 / 3,7 - the gender gap is largest in standpunkt.
- Udir 2023-24: "tendensen er at karakteren i mange av fagene er litt høyere enn de var før
  pandemien, med unntak av matematikkfagene"; "i flertallet av fagene er karakteren uendret
  fra skoleåret 2022-2023 til 2023-2024"; English and Norwegian common-subject means are
  slightly higher in 2023-24 than in 2018-19. Eksamen S1: "gikk ned fra 2,9 i fjor til 2,4
  i år"; S2 "fra 3,0 i fjor til 2,8".
- Udir 2022-23: "3 av 4 elever annullerte sin skriftlige eksamen i norsk hovedmål" (the
  2023 cancellation rule) - exam means for 2022-23 are selection-biased.
- Udir 2021-22: standpunkt in fellesfag "hovedsakelig på nivå med 2020 og 2021"; "pandemien
  gjør at 2019-20, 2020-21 og 2021-22 skiller seg fra tallene fra tidligere årganger".
- Exams: cancelled for all grunnskole pupils spring 2020, 2021, 2022; "de fleste eksamener
  for elever i videregående skole [ble] avlyst våren 2022"; 2020 and 2021 vitnemål in vgs
  were standpunkt-only ("I 2020 fikk elever i videregående vitnemål basert kun på
  standpunktkarakterer" - Stortinget written question).
- Not found: share of standpunkt grades 5-6 per year, 1T/engelsk/fysikk/kjemi series,
  per-year norsk hovedmål standpunkt/eksamen means. All are in table VGO/ResultatFagV
  (TO-FETCH A).

## 3. Samordna opptak

### 3a. Medicine cut-offs (hovedopptak), from the SO Tableau export mirrored on GitHub

| Year | UiO høst ORD / ORDF | UiB ORD / ORDF | NTNU ORD / ORDF | UiT ORD / ORDF |
|---|---|---|---|---|
| 2020 | 69,0 / 61,6 | 67,7 / 60,1 | 67,9 / 62,0 | 67,6 / 60,0 |
| 2021 | 69,5 / 62,0 | 68,1 / 60,5 | 68,6 / 62,0 | 68,0 / 60,3 |
| 2022 | 69,6 / 62,4 | 68,3 / 60,8 | 69,2 / 62,5 | 68,2 / 60,4 |
| 2023 | 70,2 / 61,2 | 68,6 / 60,1 | 69,6 / 62,2 | 68,2 / 59,8 |
| 2024 | 69,7 / 60,7 | 67,8 / 59,4 | 69,4 / 61,7 | 66,8 / 57,8 |
| 2025 | 69,6 / 60,5 | 67,2 / 58,5 | 68,5 / 61,0 | 66,0 / 57,1 |
| 2026 | 69,0 / 60,0 | 67,2 / 59,0 | 68,2 / 60,8 | 65,8 / 56,5 |

The 2020-2021 UiO values match the KD table (regjeringen.no uio.pdf: "Medisin, høst | UIO |
61,6 | 62,0" and "69,0 | 69,5"), validating the mirror. UiO høst ORD earlier years
(third-party hvatrengerjeg.no, SO-derived; 2017-19 confirmed by UiO): 2011 68,0; 2012 67,7;
2013 68,0; 2014 67,9; 2015 68,1; 2016 68,3; 2017-2019 68,5. UiO notat 2009: høst 68,0 / vår
66,9. Tidsskriftet 2003: "Hele 70,2 studiepoeng må til" (old point system, not comparable).
Pattern: the ORD cut-off climbed from ~68,0 (2011-2015) to a 70,2 peak in 2023 (the cohorts
with no-exam vitnemål), then eased; the førstegangsvitnemål cut-off peaked 2022 (62,4) and
has fallen to 60,0 in 2026 (fewer applicants: UiO høst ORD waiting list 1 836 in 2020 -> 670
in 2026). Note ORD includes tilleggspoeng/alderspoeng and forbedrede fag, so it is a worse
index of school-grade levels than ORDF.

### 3b. Distribution of applicants' average

- KD hearing document on the new IB table: "0,08 % av søkerne med norsk videregående
  opplæring (studieforberedende) fikk snitt 6,0 i opptaket, mens 2,8 % av IB-søkerne fikk
  dette" (year of opptak to confirm in the PDF; the Stortinget answer below refers to 2024).
- Stortinget, skriftlig spørsmål 15:571 (2024-25), answered 13.12.2024 by Oddmund Hoel: "Tal
  frå HK-dir viser at antal IB-søkjarar som blei rekna om til å ha eit gjennomsnitt på 6,0
  (høgaste karaktergjennomsnitt i norsk skule) var 30 gongar høgare enn for søkjarar med
  norsk vidaregåande skule, i årets opptak."
- Hearing notes: HK-dir's first table (2024 hearing) used IB-foundation data from all IB
  schools worldwide; the newer proposal (based on the forskrift of 11.09.2025, in force
  01.01.2027) would start the table at 20 IB points and be built only from Norwegian IB
  lines, to apply from the 2030-31 intake. The 2025 table was set in December 2022 and
  applied from the 2025 intake. NIBS: "unfair towards IB students and devaluates the IB
  Diploma".
- No national time series of the share of Norwegian applicants with snitt >= 5,5 / 6,0 was
  found in snippets. DBH table 571 (sum of karakterpoeng and n) or an HK-dir request is the
  route (TO-FETCH D).

## 4. Research and policy documents on Norwegian grade inflation

- **Udir** (statistics notes, yearly "Analyse av karakterstatistikk"): the 15-year "stadig
  bedre karakterer ... ikke den samme utviklingen i elevenes kompetanse" statement (above);
  yearly standpunkt-eksamen gap analyses; 2026 report "Kvalitet i standpunktvurderingen
  krever system og profesjonsfellesskap".
- **KD FoU-oppdrag (2026, in process)**: "kvalitet, karakterinflasjon og segregering i ulike
  private og offentlige videregående skoler" (listed in Statsforvalteren Innlandet slides,
  23.09.2026). The ministry itself uses the word karakterinflasjon.
- **SSB Rapporter 2011/4**, Galloway, Kirkebøen, Rønning, "Karakterpraksis i grunnskoler:
  Sammenheng mellom standpunkt- og eksamenskarakterer": the standpunkt-eksamen gap is similar
  at every exam-grade level; Udir's summary adds that small schools with low exam means give
  relatively higher standpunkt than large high-performing schools. Earlier SSB notater
  2005/31, 2006/35, 2007/29, 2008/24 test whether the gap follows family background/school.
- **NIFU 2014** (Udir summary): the standpunkt-eksamen gap is larger in private than public
  schools, "men dette gjelder ikke alle private skoler". **NIFU** on higher education
  (forskning.no/NTB): university grades rose over 20 years, ~two-thirds "structural causes"
  incl. upper-secondary grades - "little evidence of grade inflation" at university level.
- **NOU 2019:3 Stoltenberg-utvalget**: girls lead in all subjects, most in standpunkt; proposes
  timetall-weighted points. **NOU 2019:25 Lied-utvalget** (not reached in snippets).
- **Rambøll/KS June 2021** "Undervisnings- og vurderingssituasjonen i videregående skole våren
  2020": quantitative analysis of standpunkt in the first no-exam spring.
- **PROMENTA/KD 2026** (universitetsavisa PDF): realfag "grade penalty", uses standpunkt and
  eksamen. **Civita 02/2024** "Oppvask i opptakssystemet". **Acta Didactica Norge 2018**
  article on standpunkt/eksamen (DOAJ id 7b7c2246...).
- Media: no 2025 "snillere lærere"/"karakterinflasjon" articles surfaced in snippets
  (Dagbladet "Unødvendig inflasjon" op-ed exists; content not captured).

## 5. Nasjonale prøver as stability check

- Udir: no change in mean skalapoeng in lesing, regning and engelsk from the start of the
  trend measurement (2014 for engelsk/regning, 2016 for lesing) until 2021 - i.e. flat test
  scores while grunnskolepoeng rose 40,4 -> 42,0 (2014-2019). Caveat (SSB): the 2014-2021
  model "ga en underestimering av endring mellom årene" (SSB rescaling article).
- 2022: break - tests re-based on LK20, "resultatene er ikke direkte sammenlignbare".
  2023: 8th/9th grade weaker in lesing and regning, >3 pp more 8th-graders at lowest level.
  2024: regning down for second year, 8th grade "to skalapoeng svakere enn 2022-kullet";
  lesing "om lag uendret sammenlignet med 2018".

## Caveats

1. **Kunnskapsløftet 2006 (LK06)**: new subject codes; R1/R2/S1/S2 series start 2007-08.
   **LK20 (fagfornyelsen)**: new codes from 2020-21 (Vg1), 2021-22 (Vg2), 2022-23 (Vg3);
   2020-21 "var første året med nye fag". The mirrored maths series stitches LK06/LK20
   codes; the 2021-22 R1 and S1 rows are broken (n=61/55) and must be refetched.
2. **Exam cancellations**: grunnskole 2020, 2021, 2022; vgs 2020, 2021 and most of 2022.
   Grunnskolepoeng 2020-2022 are standpunkt-only (SSB: "ikke sammenlignbare"). 2023 exams:
   pupils could annul; "3 av 4" annulled norsk hovedmål skriftlig, biasing 2022-23 exam means.
   The 2020-2022 vitnemål cohorts drove medicine cut-offs to their 2023 peak.
3. **Grunnskolepoeng definition**: average of standpunkt+eksamen grades x10, pupils with
   fewer than half the grades excluded (SSB "0 poeng ikke medberegnet"); SSB and Udir use
   different selections (small offsets); Udir figures from 2017-18 come via Statsforvalteren
   Vestland tabulation and the 2024-25 value is derived, not read directly.
4. **Scale**: 1-6 unchanged since before 2006, but the share of grade 6 and the 5/6 share
   per subject - the quantity most comparable to IB 7s - was not obtained.
5. **Samordna opptak points**: ORD = karakterpoeng (snitt x10) + realfag/språkpoeng +
   alderspoeng + tilleggspoeng; ORDF excludes age/other points. Pre-2009 "studiepoeng"
   (2003 value) used a different system. New opptaksforskrift from 2027 changes points again
   ("Poenggrensene før og etter 2028 blir ikke direkte sammenlignbare").
6. **Composition**: S1/S2 enrolment collapsed after LK20 (S1 7 536 in 2019-20 -> 1 461 in
   2025-26), Vg3 SF cohort ~45-49 000; subject means are not cohort-adjusted.
7. **Third-party mirrors**: the maths and medicine series come from GitHub copies of Udir/SO
   exports; spot-checks (2025-26 maths vs Udir article; 2020-21 UiO cut-offs vs KD table)
   passed, but re-pull from source before publication.

## Gaps (not found in this session)

Grunnskolepoeng 2010, 2017, 2024-25 (direct); per-subject vgs standpunkt and eksamen means
for norsk hovedmål, engelsk, 1T, fysikk, kjemi by year; share of 5/6; medicine cut-offs
2005-2019 for UiB/NTNU/UiT and ORDF before 2020; applicant snitt distribution over time;
text of Lied-utvalget and Eksamensutvalget/ekspertgruppe on karakterer; recent newspaper
debate. Search budget (shared 200-query limit) ran out before these could be targeted.

## Sources

(How accessed: WS = web-search snippet; GH = raw file from github.com.)

- SSB, "Karakterer ved avsluttet grunnskole" releases: https://www.ssb.no/utdanning/statistikker/kargrs/arkiv/2009-12-03 (2009); .../kargrs/aar/2011-11-17 (2011); .../kargrs/aar/2012-11-01 (2012); .../kargrs/aar/2015-10-08 (2015); .../kargrs/aar/2016-10-06 (2016); table https://www.ssb.no/146119/gjennomsnittlig-grunnskolepoeng... (2013/2014); StatBank 07497, 07495 - SSB, 2009-2016, WS.
- SSB, "Ingen tegn til mindre kjønnsforskjeller i grunnskolepoeng" https://www.ssb.no/utdanning/artikler-og-publikasjoner/ingen-tegn-til-mindre-kjonnsforskjeller-i-grunnskolepoeng - SSB, 2019/2020, WS.
- SSB, "Større forskjeller mellom standpunkt- og eksamenskarakterer blant innvandrerelever" https://www.ssb.no/utdanning/videregaende-utdanning/artikler/storre-forskjeller-mellom-standpunkt-og-eksamenskarakterer-blant-innvandrerelever - SSB, c. 2021, WS.
- SSB, "Flere elever på lavere nivå i lesing og regning" https://www.ssb.no/utdanning/grunnskoler/statistikk/karakterer-ved-avsluttet-grunnskole/artikler/flere-elever-pa-lavere-niva-i-lesing-og-regning and "Korrigerte tall for nasjonale prøveresultater over tid" - SSB, 2023-2024, WS.
- SSB Rapporter 2011/4, Galloway, Kirkebøen, Rønning, "Karakterpraksis i grunnskoler" https://www.ssb.no/utdanning/artikler-og-publikasjoner/karakterpraksis-i-grunnskoler (PDF https://www.ssb.no/emner/04/02/20/rapp_201104/rapp_201104.pdf) - SSB, 2011, WS.
- Udir, karakterstatistikk pages rendered as PDF: https://udir.no/api/PdfApi/PrintPageAsPdfDocument/156295 (analyse 2018-19), /198765 and /199013 (2021-22), /216116, /216111, /216297 (2022-23 and 2023-24), /182979, /183686 (2020-21), /222156 (likely 2024-25) - Udir, 2019-2025, WS.
- Udir, nasjonale prøver trend pages /169350, /189337, /201672, /219217 - Udir, 2018-2024, WS.
- Udir report 2026 "Kvalitet i standpunktvurderingen krever system og profesjonsfellesskap" https://www.udir.no/tall-og-forskning/finn-forskning/rapporter/2026/kvalitet-i-standpunktvurderingen-krever-system-og-profesjonsfellesskap/ - Udir, 2026, WS (via Statsforvalteren slides).
- Udir Statistikkportalen table VGO/ResultatFagV/2/5 (Karakterer i videregående skole), mirrored in https://github.com/VirtualAiCorp/NMBU-sammenligning/blob/main/kilde/public/sokergrunnlag/udir.json (fetched by repo 2026-09-24; script scripts/fetch-udir.py) - Udir via GitHub, GH.
- Samordna opptak datavarehus (Tableau "Poenggrenser og ventelistetall", rapport-dv.educloud.no), mirrored in https://github.com/VirtualAiCorp/NMBU-sammenligning/blob/main/data/nmbu/kilder/so_poenggrenser_venteliste.csv (73 424 rows, 2020-2026) - SO/HK-dir via GitHub, GH.
- Kunnskapsdepartementet, "Høyeste karaktersnitt noensinne for årets tiendeklassinger" https://www.regjeringen.no/no/aktuelt/hoyeste-karaktersnitt-noensinne-for-arets-tiendeklassinger/id2736529/ - KD, 25.08.2020, WS; "Rekordhøgt snitt for årets avgangskull" .../id2740015/ - KD, 2020, WS.
- Kunnskapsdepartementet, poenggrenser table https://www.regjeringen.no/contentassets/8a06aa3520624c5daf5131f37e21b383/uio.pdf?uid=UIO - KD, 2021, WS.
- Kunnskapsdepartementet, høyringsnotat ny omrekningstabell for IB https://www.regjeringen.no/contentassets/315531d605f3405cac8dc90700b75b63/hoyringsnotat-forslag-om-endring-i-forskrift-om-opptak-til-hogare-utdanning-ny-omrekningstabell-for-ib.pdf; hearing https://www.regjeringen.no/id3183537; press release https://www.regjeringen.no/no/aktuelt/ny-omregningstabell-for-ib-karakterer-sendes-pa-horing/id3184606/ - KD, 2025-2026, WS.
- Stortinget, skriftlig spørsmål 15:571 (2024-2025) https://www.stortinget.no/no/Saker-og-publikasjoner/Sporsmal/Skriftlige-sporsmal-og-svar/Skriftlig-sporsmal/?qnid=99754 - Stortinget, 13.12.2024, WS; Dok 8:76 S (2024-2025) https://www.stortinget.no/no/Saker-og-publikasjoner/Publikasjoner/Representantforslag/2024-2025/dok8-202425-076s/ - WS; Innst. 180 S (2021-2022) on exams - WS.
- Statsforvalteren i Vestland, "Karakterstatistikk for grunnskulen 2018-19" https://www.statsforvalteren.no/vestland/barnehage-og-opplaring/grunnskule-og-vidaregaande-opplaring/karakterstatistikk-for-grunnskulen-2018-19/ and "Liten karakteroppgang i grunnskulen" (Aug 2026) https://www.statsforvalteren.no/vestland/kommune-og-tenesteaktor/barnehage-og-skule--for-eigarar-og-tilsette/nyhende/2026/08/liten-karakteroppgang-i-grunnskulen/ - Statsforvalteren, 2019 and 2026, WS.
- Statsforvalteren i Innlandet, slides "Frokostmøte om klager på standpunktkarakter" 23.09.2026 https://www.statsforvalteren.no/siteassets/innlandet/barnehage-og-opplaring/dokumenter/frokostmote-23.09.2026-presentasjon.pdf - 2026, WS.
- NOU 2019:3 "Nye sjanser - bedre læring" https://www.regjeringen.no/no/dokumenter/id2627718/ - KD, 2019, WS.
- Rambøll for KS, "Undervisnings- og vurderingssituasjonen i videregående skole våren 2020" https://www.nfk.no/_f/p1/id6a3bb16-0dc6-41bc-a74f-a3f790896b8a/070621_rapport_ks_standpunktkarakterer.pdf - KS, June 2021, WS.
- NIFU-rapport 2020:4 https://nifu.brage.unit.no/nifu-xmlui/bitstream/handle/11250/2648860/NIFUrapport2020-4.pdf - NIFU, 2020, WS; forskning.no/NTB "Karakterene til norske studenter har blitt bedre" https://www.forskning.no/ntb-skole-og-utdanning/karakterene-til-norske-studenter-har-blitt-bedre/2665940 - WS.
- Civita notat 02/2024 https://civita.no/content/uploads/2024/02/Notat_02_2024_Oppvask-i-opptakssystemet.pdf - Civita, 2024, WS.
- KD-commissioned report (PROMENTA) https://www.universitetsavisa.no/files/2026/08/25/260821kdrapport.pdf - 2026, WS.
- UiO Det medisinske fakultet, "Studier og opptakskrav 2022/2023/2024/2025/2026" https://www.med.uio.no/studier/aktuelt/aktuelle-saker/2025/studier-og-opptakskrav-2025 (and sibling pages); UiO notat til studiekomiteen Sept 2009 https://uio.no/om/organisasjon/utvalg/utdanningskomiteen/moter/2009/170909/notat%20til%20studiekomiteen%20sept09_Osak1.pdf - UiO, WS.
- hvatrengerjeg.no "Medisin, Oslo, høst" https://www.hvatrengerjeg.no/studier/medisin-oslo-host-universitetet-i-oslo-185740 - third party, 2026, WS.
- Tidsskriftet, "Vanskeligst å bli lege i Oslo" https://tidsskriftet.no/2003/08/nytt-fra-nett/vanskeligst-bli-lege-i-oslo - 2003, WS.
- Bergen katedralskole / NIBS letters on the IB table https://www.bergenkatedralskole.vgs.no/nyheiter/new-conversion-table-for-ib-diploma-grades - 2023-2025, WS.
- GitHub repos documenting Udir/SO endpoints: https://github.com/VirtualAiCorp/NMBU-sammenligning, https://github.com/terchris/atlas (udir-gsi README), https://github.com/enraarne/Alternativ-statistikkbank, https://github.com/Jowiam/PBI-API (docs/udir-vurdering.md), https://github.com/trymhaak/open-apis - GH.
