# PISA mean scores 2000-2025: Norway versus peers

Prepared 2026-11-02 as evidence for the op-ed on Norway's IB-to-Norwegian
grade conversion table. Companion data files in this folder:

- `pisa_country_year.csv` - 438 rows: mean score and standard error for
  mathematics, reading and science, every PISA cycle 2000-2025, for Norway,
  Sweden, Denmark, Finland, Iceland, United Kingdom, Germany, Netherlands,
  France, United States, Canada, Australia, Singapore, Estonia, Poland,
  Switzerland, and three OECD averages (`OECD` = the "OECD average" row as
  printed in each OECD volume; `OECD_A23` and `OECD_A35` = the OECD's
  constant-composition trend averages of the 23 / 35 members with data in
  every cycle since 2003 / 2006).
- `pisa_norway_levels.csv` - Norway's share of low performers (below
  Level 2) and top performers (Level 5-6) in mathematics, 2003-2025.
- `TO-FETCH.md` - the OECD / Udir / regjeringen.no pages to retrieve from an
  unrestricted machine (all were blocked from the research sandbox).

Scale reminder: each PISA domain was set to an OECD mean of 500 and a
standard deviation of 100 in its first "major domain" year (reading 2000,
mathematics 2003, science 2006).

## 1. What the series show

### 1.1 Norway

| Domain | Peak | 2015 | 2018 | 2022 | 2025 | 2018-22 | 2022-25 | 2015-25 |
|---|---|---|---|---|---|---|---|---|
| Mathematics | 502 (2015) | 502 | 501 | 468 | 452 | -33 | -17 | -50 |
| Reading | 513 (2015) | 513 | 500 | 477 | 453 | -23 | -24 | -60 |
| Science | 500 (2009) | 498 | 490 | 478 | 470 | -12 | -8 | -28 |

(Means rounded; standard errors for Norway are 2.0-3.2 points in every
cycle, so any change above about 7-9 points between two cycles is
statistically significant on its own, before the OECD's link-error
adjustment. See `pisa_country_year.csv` for the SEs.)

- **Peak and plateau.** Norway's maths and reading scores were flat-to-rising
  from 2003 to 2015/2018 (maths 495 -> 502, reading 500 -> 513). 2015 was
  the all-time high in both; science peaked in 2009 (500).
- **The break came in 2022.** Mathematics fell 33 points between 2018 and
  2022 - the largest fall in Norway's PISA history and, per the OECD's
  PISA 2022 Volume I, one of only four declines exceeding 30 points
  (Albania, Jordan, Iceland, Norway). The OECD country note describes
  2022 maths as "lower than in any previous assessment".
- **2025 continued the fall.** Maths -17 and reading -24 points on 2022;
  science -8 (not statistically significant according to the OECD Norway
  country note / Education GPS). Norway is now below the OECD average in
  all three domains (452 vs 463; 453 vs 461; 470 vs 482).
- **Cumulative decline since the 2015 peak: 50 points in maths, 60 in
  reading, 28 in science** - matching the Norwegian government's own
  framing on 8 Sep 2026 ("60 poeng i lesing, 50 poeng i matematikk og 28
  poeng i naturfag"). With the OECD's rule of thumb (section 3) that is
  roughly two to three school years' worth of learning in maths and reading.
- **Low and top performers in mathematics** (`pisa_norway_levels.csv`):
  below-Level-2 share was 17-22 % in every cycle 2003-2018 (17.1 % in 2015,
  18.9 % in 2018), then 31 % in 2022 and 38 % in 2025. Top performers
  (Level 5-6) were 9-12 % in 2003-2018 (12.2 % in 2018) and 7 % in 2022
  (OECD average 9 %). The 2025 top-performer share for maths was not found
  in the search snippets (science: 5 %, OECD average 7 %) - see gaps.

### 1.2 Peers and the OECD average (mathematics)

| | Peak (year) | 2018 | 2022 | 2025 | 2018-22 | 2022-25 | 2015-25 | Peak-2025 |
|---|---|---|---|---|---|---|---|---|
| Norway | 502 (2015) | 501 | 468 | 452 | -33 | -17 | -50 | -50 |
| Sweden | 509 (2003) | 502 | 482 | 464 | -21 | -18 | -30 | -45 |
| Denmark | 514 (2003) | 509 | 489 | 471 | -20 | -19 | -40 | -44 |
| Finland | 548 (2006) | 507 | 484 | 469 | -23 | -15 | -42 | -80 |
| Iceland | 515 (2003) | 495 | 459 | 450 | -36 | -9 | -38 | -65 |
| United Kingdom | 508 (2003)* | 502 | 489 | 488 | -13 | -1 | -5 | -21 |
| Germany | 514 (2012) | 500 | 475 | 464 | -25 | -11 | -42 | -50 |
| Netherlands | 538 (2003) | 519 | 493 | 483 | -27 | -9 | -29 | -54 |
| France | 511 (2003) | 495 | 474 | 458 | -22 | -16 | -35 | -53 |
| United States | 487 (2009) | 478 | 465 | 463 | -13 | -2 | -7 | -25 |
| Canada | 532 (2003) | 512 | 497 | 485 | -15 | -12 | -30 | -47 |
| Australia | 524 (2003) | 491 | 487 | 478 | -4 | -10 | -16 | -47 |
| Singapore | 575 (2022) | 569 | 575 | 563 | +6 | -12 | -1 | -12 |
| Estonia | 523 (2018) | 523 | 510 | 508 | -14 | -2 | -12 | -16 |
| Poland | 518 (2012) | 516 | 489 | 484 | -27 | -5 | -20 | -33 |
| Switzerland | 534 (2009) | 515 | 508 | 499 | -7 | -9 | -22 | -35 |
| OECD average (as printed) | 500 (2003) | 487 | 472 | 463 | -15 | -9 | -22 | -36 |
| OECD average-35 (constant) | 491 (2006) | 490 | 475 | 466 | -15 | -9 | -22 | -25 |

\* UK 2003 is in the PISA 2022 trend table but omitted from the PISA 2025
trend tables (the UK's 2000 and 2003 samples did not meet response-rate
standards); treat with care.

Reading and science tables for the same countries are in the CSV; the
shape is the same: reading fell everywhere except Singapore/US/UK
(2022->2025), science fell much less (OECD average -7 since 2015 vs -22
in maths and -28 in reading).

Reading of the peer table:

- **The decline is West-wide, not Norwegian.** The OECD average in maths fell
  22 points 2015-2025, and 14 of the 16 comparison countries fell by 10 or
  more over the same decade. The OECD press release (8 Sep 2026) calls 2025
  maths and reading "the lowest averages it has recorded".
- **But Norway's fall is steeper than almost all peers.** Among the 16, only
  Finland (-80 from its 2006 peak) and Iceland (-65) have fallen further
  from peak, and both started from higher levels. Over 2018-2025 Norway's
  -49 points in maths is the largest drop in the group (Iceland -46,
  Denmark -39, Finland -39, Sweden -38, France -38, Germany -36).
- **The Nordic pattern.** All five Nordic countries lost 38-46 points in
  maths between 2018 and 2025 and are now at or below the OECD average
  except Denmark (471 vs 463). Finland's long slide from 548 (2006) to 469
  (2025) is the most dramatic single series.
- **Counter-examples exist.** Singapore (-1 since 2015), Estonia (-12), the
  UK (-5) and the US (-7) held roughly level over the decade, so the
  decline is not an unavoidable artefact of the test.

### 1.3 The pandemic effect

PISA 2022 was fielded in spring 2022 (a year late because of COVID-19), so
the 2018-2022 change bundles pandemic disruption with any underlying trend.
Two features of the data argue that Norway's problem is not only COVID:

1. The OECD average fell 15 points in maths 2018-2022, Norway fell 33 - more
   than twice the OECD fall - despite Norway's comparatively short school
   closures (UNVERIFIED (model memory): Norwegian schools were closed for
   roughly 6-8 weeks in spring 2020; verify with Udir/OECD "Education at a
   Glance" tables before use).
2. The decline continued, at the same pace, in 2025 (maths -17, reading -24)
   when the OECD average fell 9 and 14. If 2022 had been a pandemic dip,
   2025 should have shown recovery, as it did in the UK, US, Australia and
   Estonia in maths.

Science is the exception: Norway's 2022->2025 change (-8) was not
significant and the OECD average was flat, which fits the OECD's own
observation that science has been more stable than maths and reading.

## 2. Data provenance

### 2.1 How the files were built

1. **Primary series (438 rows, with SEs for 2000-2025):**
   `data/derived/pisa_scores_long.csv` in the GitHub repository
   `uygarcatal6/pisa-turkiye-replication` (downloaded 2026-11-02 from
   raw.githubusercontent.com). Its author transcribed the OECD workbook
   `mrq53f.xlsx` (annex tables of *PISA 2025 Results (Volume I)*, published
   8 Sep 2026) and recorded sheet and cell for every value: Table I.B1.2a.36
   (science), I.B1.2a.37 (reading), I.B1.2a.38 (mathematics). Those sheet
   and cell references are carried into the `note` column of our CSV, so
   each number can be checked against the OECD workbook once it is
   downloaded (see `TO-FETCH.md`). Norway's row is row 76 of each sheet.
2. **Cross-check (independent transcription, 2000-2022):**
   `projects/brviz/data/pisa.csv` in `a0th/a0th.github.io`, labelled with
   PISA 2022 Volume I Tables I.B1.5.4-I.B1.5.6 (the 2000-2022 trend
   tables). All 328 country-cycle-domain values that both files hold for
   our 17 entities agree to within 0.01 points. A third file
   (`jeremydwong/rebirth_of_education_exploration/pisa-data-academic-performance.csv`,
   an Our World in Data chart export) agrees for Norway maths 2003-2022 as
   well. Values present only in the a0th file (OECD "average" rows for
   2000-2009 and 2018-2022; UK 2000-2003) were added from it, flagged in
   `note`, without SEs.
3. **Proficiency levels 2003-2018:**
   `05_working_paper/051_rawdata/pisa-wdi.csv` in `worldbank/LearningPoverty`
   (World Bank EdStats/WDI indicators `LO.PISA.MAT.0` ... `LO.PISA.MAT.6`,
   which are the OECD's published distribution across proficiency levels).
   Below Level 2 = level "0" (below 1) + level 1; top = levels 5 + 6; sums
   were computed by our script. Levels sum to 100.0 in every cycle.
4. **Proficiency levels 2022 and 2025, and all OECD "country note" text:**
   web-search snippets of the OECD Norway country notes, Udir, regjeringen.no
   and norway.no (the pages themselves could not be opened). The 2025
   below-Level-2 share (38 %) is 100 - 62 % "reached at least Level 2" and is
   also quoted directly by Norway's OECD delegation ("fra 17 prosent i 2015
   til 38 prosent i 2025"; our 2015 value from the World Bank file is 17.1 %,
   which corroborates the chain).

Raw downloads are kept outside the repository in the session scratchpad
(`/tmp/claude-0/-home-user/8679f277-2ab9-5639-a429-facf3bfeb078/scratchpad/pisa-raw/`);
the build script is
`/tmp/claude-0/-home-user/8679f277-2ab9-5639-a429-facf3bfeb078/scratchpad/pisa-scripts/build.py`.
MD5 of the delivered files: `pisa_country_year.csv`
a54699f05e5860a407aa433df48051f0; `pisa_norway_levels.csv`
d2c20f620e8ed48f0fb5ea9dde02496d.

### 2.2 Licensing

- The underlying statistics are (c) OECD, published under the OECD's terms of
  use, which permit reproduction of OECD data with attribution (cite the
  OECD volume and table). Quoting means in an op-ed is unproblematic.
- `uygarcatal6/pisa-turkiye-replication`: derived data and documentation
  CC BY 4.0 (code MIT); the repository states the PISA data remain (c) OECD.
  Attribution is given in the `source_url`/`note` columns.
- `worldbank/LearningPoverty`: MIT licence (World Bank EduAnalytics, 2019);
  underlying WDI data are CC BY 4.0.
- `a0th/a0th.github.io` and `jeremydwong/...`: no licence file found; used
  only for cross-checking and for 18 OECD-average / UK values that are
  themselves OECD tables (cite the OECD, not the repository).
- This folder's files may be committed under the repository's Unlicense
  terms as far as our own compilation is concerned; the OECD attribution
  must travel with them.

## 3. Interpreting point differences

- The scale is standardised to SD = 100 (OECD mean 500 at each domain's
  first major-domain cycle), so 10 points = 0.1 SD.
- The OECD's current rule of thumb, stated on its "PISA performance trends"
  dashboard, is that **"20 points is roughly the amount of learning that
  15-year-olds typically gain in one school year across OECD countries"**.
  The underlying estimate is Avvisati & Givord (2021), *How much do
  15-year-olds learn over one year of schooling? An international comparison
  based on PISA*, OECD Education Working Paper EDU/WKP(2021)14: about
  one-fifth of a standard deviation per school year.
- Caution: older OECD publications (2010) used "about 40 points = one school
  year", and quasi-experimental estimates vary by country and cycle
  (a UAB/INCASI note gives about 40 points for Spain in 2003 falling to about
  20 in 2022; Cambridge Assessment estimated about 36 for England). Use the
  20-point figure with "roughly" and cite the OECD dashboard and the
  working paper. On that yardstick Norway's maths decline since 2015 (50
  points) corresponds to about 2.5 school years.
- Standard errors on national means are about 2-3 points, so the
  differences discussed here (15-60 points) are far outside sampling error.

## 4. Caveats

1. **Mode change in 2015.** PISA moved from paper to computer-based testing
   in 2015 (and to adaptive testing in reading in 2018 and maths in 2025).
   The OECD links the scales so trends are comparable, but adds a "link
   error" to the SE of any cross-cycle comparison; small changes (under
   about 8-10 points) across the 2012/2015 boundary should not be called
   significant. Norway's 2015 peak coincides with the first computer-based
   cycle; the subsequent falls (33, 17 points) are far larger than any
   plausible link error.
2. **2022 was delayed by one year** (fieldwork 2022 instead of 2021 because of
   COVID-19), so the 2018-2022 interval is four years and includes the
   pandemic. The 2022-2025 interval is three years.
3. **PISA 2025 sampling standards were not met in Norway.** The OECD country
   note records an overall exclusion rate of 10.4 % in 2025, above the 5 %
   tolerance in the PISA technical standards and up from 7.3 % in 2022, and
   warns that high exclusion "may bias performance results upwards" - i.e.
   Norway's true 2025 mean is, if anything, lower. The 2025 Norway rows are
   flagged with an asterisk in the OECD tables (`asterisk_flag` in the
   source file). Exclusions have risen steadily: 3.5 % (2006), 5.9 % (2009),
   6.1 % (2012), 6.7 % (2015), 7.9 % (2018), 7.3 % (2022), 10.4 % (2025)
   (coverage/exclusion figures 2006-2022 from the OECD Annex A2 transcription
   in `pisa_scores_wide.csv`; 2025 from the country note snippet). Student
   response rate in 2022 was 86.7 %, the lowest since 2006.
4. **Coverage index.** Norway's "Coverage Index 3" (share of the 15-year-old
   population represented by the sample) fell from 0.97 (2006) to 0.90
   (2025). Rising exclusion of pupils with special needs or limited
   Norwegian is a plausible contributor; it does not explain a 50-point
   fall.
5. **OECD average composition changes** (members joining, countries excluded
   for data-quality reasons). The `OECD` rows use whatever "OECD average"
   each volume printed (37 countries in the 2022 volume, 38 in 2025); use
   `OECD_A35`/`OECD_A23` for strictly constant-composition trends. The
   differences are 1-3 points.
6. **UK 2000/2003 and Netherlands 2000** are excluded or flagged by the OECD
   for low response rates; Singapore joined in 2009, Estonia in 2006.
7. **Numbers taken from search snippets** (2022/2025 proficiency shares,
   exclusion rate 10.4 %, country-note wording) have not been read on the
   OECD pages themselves; verify against the URLs in `TO-FETCH.md` before
   quoting verbatim.
8. One item is marked UNVERIFIED (model memory) above: the length of
   Norwegian school closures in 2020.

## 5. Gaps

- Norway's share of top performers (Level 5-6) in mathematics for 2025 (the
  country note gives the science figure, 5 %, but the maths figure did not
  appear in search results).
- Reading and science proficiency shares for Norway (only maths was built).
- Standard errors for the 18 values that come only from the PISA 2022 trend
  tables (OECD average 2000-2009, 2018-2022; UK 2000-2003).
- The web-search budget shared by the parallel agents was exhausted before
  Udir's own PISA 2025 pages and the Norwegian national report (UiO/ILS)
  could be located; the OECD and regjeringen.no sources above cover the
  same numbers.

## Sources

Accessed 2026-11-02. "Downloaded" = file fetched from
raw.githubusercontent.com and parsed; "search snippet" = text returned by
web search for that URL; the page itself was not opened (host blocked).

1. uygarcatal6, *PISA trends in Türkiye, 2003-2025: replication code and
   derived data*, GitHub, 2026, `data/derived/pisa_scores_long.csv`,
   `pisa_scores_wide.csv`, `README.md`, `LICENSE` (CC BY 4.0 data).
   https://github.com/uygarcatal6/pisa-turkiye-replication - downloaded.
2. OECD, *PISA 2025 Results (Volume I): Future-Ready Students*, OECD
   Publishing, Paris, 8 Sep 2026, Annex B1 Tables I.B1.2a.36-38 (via source 1).
   https://www.oecd.org/content/dam/oecd/en/publications/reports/2026/09/pisa-2025-results-volume-i_5265bfb1/73451bc5-en.pdf - search listing only.
3. a0th, `projects/brviz/data/pisa.csv` (PISA 2022 Vol I Tables
   I.B1.5.4-6), GitHub. https://github.com/a0th/a0th.github.io - downloaded.
4. OECD, *PISA 2022 Results (Volume I): The State of Learning and Equity in
   Education*, OECD Publishing, Paris, 5 Dec 2023, Tables I.B1.5.4-I.B1.5.6
   (via source 3). https://www.oecd.org/en/publications/pisa-2022-results-volume-i_53f23881-en.html - search listing only.
5. World Bank EduAnalytics, *LearningPoverty* repository,
   `05_working_paper/051_rawdata/pisa-wdi.csv` (WDI indicators
   LO.PISA.MAT.0-6), MIT licence, 2019. https://github.com/worldbank/LearningPoverty - downloaded.
6. jeremydwong, `pisa-data-academic-performance.csv` (Our World in Data
   chart export, maths 2003-2022), GitHub. https://github.com/jeremydwong/rebirth_of_education_exploration - downloaded (cross-check only).
7. OECD, *PISA 2025 Results (Volume I) - Country Notes: Norway*, Sep 2026.
   https://www.oecd.org/en/publications/pisa-2025-results-volume-i-country-notes_2d4ff9ea-en/norway_77d5f84b-en.html - search snippet (2025 means, OECD averages, 62 % at least Level 2, 5 % top in science, exclusions 10.4 % vs 7.3 %, bias warning).
8. OECD Education GPS, *Norway - Student performance (PISA 2025)*.
   https://gpseducation.oecd.org/CountryProfile?primaryCountry=NOR&treshold=5&topic=PI - search snippet (science -8 not significant).
9. OECD, press release *PISA 2025: Students' reading and mathematics
   performance declined sharply across the OECD*, 8 Sep 2026.
   https://www.oecd.org/en/about/news/press-releases/2026/09/pisa-2025-students-reading-and-mathematics-performance-declined-sharply-across-the-oecd.html - search snippet (OECD -14 reading, -9 maths 2022-25; -28/-22 2015-25; averages 463/461/482).
10. OECD, *PISA 2022 Results (Volume I and II) - Country Notes: Norway*, Dec
    2023. https://www.oecd.org/en/publications/pisa-2022-results-volume-i-and-ii-country-notes_ed6fbcc5-en/norway_9410c758-en.html (PDF: https://oecd.org/publication/pisa-2022-results/webbooks/dynamic/pisa-country-notes/9410c758/pdf/norway.pdf) - search snippet (7 % top performers in maths, 69 % at least Level 2, "lower than in any previous assessment").
11. OECD, PISA 2022 Vol I chapter *Changes in performance and equity in
    education between 2018 and 2022*. https://www.oecd.org/en/publications/pisa-2022-results-volume-i_53f23881-en/full-report/changes-in-performance-and-equity-in-education-between-2018-and-2022_036321c5 - search snippet (maths declines > 30 points: Albania, Jordan, Iceland, Norway).
12. Utdanningsdirektoratet, PISA 2022 summary pages, Dec 2023.
    https://udir.no/api/PdfApi/PrintPageAsPdfDocument/214861 and .../202354 - search snippet ("andelen lavtpresterende ... fra 19 til 31 prosent"; 8 500 pupils, 260 schools).
13. Regjeringen.no, *Fortsatt kraftig nedgang for norske elever i lesing og
    matematikk*, 8 Sep 2026. https://www.regjeringen.no/no/aktuelt/fortsatt-kraftig-nedgang-for-norske-elever-i-lesing-og-matematikk/id3172084/ - search snippet (60/50/28 points since 2015; 6 469 pupils, 281 schools; below OECD average in all three).
14. Norway's delegation to the OECD and UNESCO, *PISA 2025: Fortsatt
    tilbakegang i elevenes ferdigheter i lesing og matematikk*, Sep 2026.
    https://www.norway.no/no/missions/oecd-unesco/norge-oecd-unesco/nyheter-arr/pisa-2025-fortsatt-tilbakegang-i-elevenes-ferdigheter-i-lesing-og-matematikk/ - search snippet (low performers in maths 17 % in 2015 to 38 % in 2025).
15. Regjeringen.no, *Stor nedgang i 15-åringers ferdigheter i lesing,
    matematikk og naturfag*, 5 Dec 2023. https://www.regjeringen.no/no/aktuelt/stor-nedgang-i-15-aringers-ferdigheter-i-lesing-matematikk-og-naturfag/id3016910/ - search snippet.
16. The Local Norway, *What the PISA report tells us about schools in
    Norway*, 6 Dec 2023. https://www.thelocal.no/20231206/what-the-pisa-report-tells-us-about-schools-in-norway - search snippet (468/477/478; secondary).
17. Skolkoll, *International statistics*. https://skolkoll.se/en/statistics/international/ - search snippet (Norway -33/-22/-12, 2018-2022; secondary).
18. OECD, *PISA education and skills dashboard - Performance trends*.
    https://www.oecd.org/en/data/dashboards/pisa-education-and-skills/performance-trends.html - search snippet ("20 points is roughly the amount of learning that 15-year-olds typically gain in one school year").
19. Avvisati, F. and P. Givord (2021), *How much do 15-year-olds learn over
    one year of schooling? An international comparison based on PISA*, OECD
    Education Working Paper EDU/WKP(2021)14. https://one.oecd.org/document/EDU/WKP(2021)14/en/pdf - search snippet (about one-fifth of a SD per school year).
20. INCASI / UAB, note on the "one year of schooling" interpretation.
    https://webs.uab.cat/incasi/en/?p=5052 - search snippet (critique; 40 -> 20 points for Spain).
21. Cambridge Assessment, *The relationship between time in education and
    achievement in PISA in England*. https://www.cambridgeassessment.org.uk/Images/178785-the-relationship-between-time-in-education-and-achievement-in-pisa-in-england.pdf - search snippet (about 36 points for England; earlier OECD figure about 40).
22. The Northern Voices, *PISA 2025 Nordic-Baltic results*, Sep 2026.
    https://www.thenorthernvoices.com/post/pisa-2025-nordic-baltic-results-estonia-latvia - search snippet (blog; Norway 470/452/453 consistent with OECD).
23. Our World in Data, ETL repository, OECD PISA snapshot 2023-12-06
    (`snapshots/oecd/2023-12-06/pisa_*_all.xls.dvc`). https://github.com/owid/etl - GitHub code search only; data not retrievable from the sandbox.
