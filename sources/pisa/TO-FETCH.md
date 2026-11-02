# PISA: URLs to retrieve from an unrestricted machine

All hosts below were blocked from the research sandbox (only github.com /
raw.githubusercontent.com / api.github.com / pypi.org were reachable). Titles
and URLs come from web-search result listings on 2026-11-02; none of the
pages themselves was opened. Fetch, and check the numbers in
`pisa_country_year.csv` / `pisa_norway_levels.csv` against the originals.

## 1. Primary OECD tables (highest priority)

| What | URL | Why |
|---|---|---|
| PISA 2025 Results (Volume I): Future-Ready Students, full PDF | https://www.oecd.org/content/dam/oecd/en/publications/reports/2026/09/pisa-2025-results-volume-i_5265bfb1/73451bc5-en.pdf | Authoritative 2000-2025 trend tables (Annex B1, Tables I.B1.2a.36 science, I.B1.2a.37 reading, I.B1.2a.38 mathematics) that our CSV is transcribed from. Also Annex A2 (coverage, exclusion rates). |
| PISA 2025 Results (Volume I), landing page | https://www.oecd.org/de/publications/2026/09/pisa-2025-results-volume-i_5265bfb1.html | Links to the Excel annex workbook (the uygarcatal6 repo cites it as `mrq53f.xlsx`); download the workbook and verify cells quoted in the CSV `note` column (e.g. Norway maths 2025 = Table I.B1.2a.38!P76). |
| "Student performance in PISA 2025" chapter (web book) | https://www.oecd.org/en/publications/pisa-2025-results-volume-i_73451bc5-en/full-report/student-performance-in-pisa-2025_23e075c2.html | Proficiency-level shares by country for 2025 (Norway top performers in maths not found in snippets). |
| OECD press release, 8 Sep 2026 | https://www.oecd.org/en/about/news/press-releases/2026/09/pisa-2025-students-reading-and-mathematics-performance-declined-sharply-across-the-oecd.html | Quotable OECD-wide statement: reading -14, maths -9 points 2022-2025; 2015-2025 reading -28, maths -22; 2025 OECD averages 463/461/482. |
| PISA 2022 Results (Volume I): The State of Learning and Equity in Education | https://www.oecd.org/en/publications/pisa-2022-results-volume-i_53f23881-en.html | Tables I.B1.2.1-I.B1.2.3 (mean, SE, 2022), I.B1.3.1-I.B1.3.3 (proficiency levels), I.B1.5.4-I.B1.5.6 (trend means 2000-2022, the second transcription we cross-checked against). |
| PISA 2022 Vol I, chapter "Changes in performance and equity between 2018 and 2022" | https://www.oecd.org/en/publications/pisa-2022-results-volume-i_53f23881-en/full-report/changes-in-performance-and-equity-in-education-between-2018-and-2022_036321c5 | Country list of significant 2018-2022 changes; Norway maths decline > 30 points, among the four largest. |
| PISA 2022 Vol I, chapter "What can students do in mathematics, reading and science" | https://www.oecd.org/en/publications/pisa-2022-results-volume-i_53f23881-en/full-report/what-can-students-do-in-mathematics-reading-and-science_6b45422e.html | Below-Level-2 and Level-5/6 shares, 2022 and trends. |
| PISA Data Explorer | https://pisadataexplorer.oecd.org/ide/idepisa/ | Interactive extraction of means, SEs and proficiency levels for any country/cycle (UNVERIFIED URL from model memory; confirm). |
| OECD Education and Skills dashboard, "Performance trends" | https://www.oecd.org/en/data/dashboards/pisa-education-and-skills/performance-trends.html | Source of the OECD wording "20 points is roughly the amount of learning that 15-year-olds typically gain in one school year across OECD countries". |
| Avvisati & Givord (2021), "How much do 15-year-olds learn over one year of schooling?", OECD Education Working Paper EDU/WKP(2021)14 | https://one.oecd.org/document/EDU/WKP(2021)14/en/pdf (also https://oecd-ilibrary.org/education/how-much-do-15-year-olds-learn-over-one-year-of-schooling-an-international-comparison-based-on-pisa_a28ed097-en) | Academic basis for the "about one-fifth of a standard deviation (~20 points) per school year" rule; use instead of the older 40-point rule. |
| OECD Education GPS, Norway student performance (PISA 2025) | https://gpseducation.oecd.org/CountryProfile?primaryCountry=NOR&treshold=5&topic=PI | Quick country profile with 2022-2025 changes and significance flags. |

## 2. OECD country notes for Norway

| What | URL |
|---|---|
| PISA 2025 Results (Volume I) - Country Notes: Norway | https://www.oecd.org/en/publications/pisa-2025-results-volume-i-country-notes_2d4ff9ea-en/norway_77d5f84b-en.html |
| PISA 2022 Results (Volume I and II) - Country Notes: Norway (HTML) | https://www.oecd.org/en/publications/pisa-2022-results-volume-i-and-ii-country-notes_ed6fbcc5-en/norway_9410c758-en.html |
| PISA 2022 Country Note: Norway (PDF) | https://oecd.org/publication/pisa-2022-results/webbooks/dynamic/pisa-country-notes/9410c758/pdf/norway.pdf |
| PISA 2022 Insights and Interpretations (Schleicher) | https://search.oecd.org/pisa/PISA%202022%20Insights%20and%20Interpretations.pdf |
| PISA 2025 Insights and Interpretations (copy hosted by Estonian ministry) | https://hm.ee/sites/default/files/documents/2026-09/PISA2025%20Insights%20and%20interpretations_FINAL_v2.pdf |

## 3. Norwegian official sources (Udir, regjeringen.no, UiO/ILS)

| What | URL | Why |
|---|---|---|
| Udir, PISA 2022 summary (print-as-PDF endpoints found by search) | https://udir.no/api/PdfApi/PrintPageAsPdfDocument/214861 and https://udir.no/api/PdfApi/PrintPageAsPdfDocument/202354 | Udir's Norwegian framing; "andelen lavtpresterende økte fra 19 til 31 prosent" 2018-2022; sample 8 500 pupils / 260 schools. |
| Regjeringen, PISA 2022 press release (5 Dec 2023) | https://www.regjeringen.no/no/aktuelt/stor-nedgang-i-15-aringers-ferdigheter-i-lesing-matematikk-og-naturfag/id3016910/ | |
| Regjeringen, PISA 2025 press release (8 Sep 2026) "Fortsatt kraftig nedgang for norske elever i lesing og matematikk" | https://www.regjeringen.no/no/aktuelt/fortsatt-kraftig-nedgang-for-norske-elever-i-lesing-og-matematikk/id3172084/ | 2015-2025 drops quoted as 60 (reading) / 50 (maths) / 28 (science) points; 6 469 pupils, 281 schools. |
| Regjeringen, ministerial comment on PISA 2025 | https://www.regjeringen.no/no/aktuelt/fremleggelse-av-pisa-2025/id3172096/ | |
| Norway's OECD delegation, PISA 2025 summary | https://www.norway.no/no/missions/oecd-unesco/norge-oecd-unesco/nyheter-arr/pisa-2025-fortsatt-tilbakegang-i-elevenes-ferdigheter-i-lesing-og-matematikk/ | "lavpresterende i matematikk fra 17 prosent i 2015 til 38 prosent i 2025". |
| UiO ILS PISA project page (national report publisher) | https://uv.uio.no/ils/english/research/projects/pisa | Norwegian national PISA 2022 report (open access at OAPEN: https://library.oapen.org/handle/20.500.12657/86988) and "Matematisk kompetanse" (https://library.oapen.org/handle/20.500.12657/93959). Need: Norway's below-Level-2 and Level-5/6 shares for every cycle incl. 2022/2025 (top performers 2025 missing). |
| Udir PISA 2025 pages | https://www.udir.no/ (search "PISA 2025") | Not surfaced by search; find the Udir/ILS national report for 2025. |

## 4. Nordic comparison

| What | URL |
|---|---|
| Dansk Industri, "Historisk tilbagegang i danske elevers PISA-resultater" (Sep 2026) | https://www.danskindustri.dk/arkiv/analyser/2026/09/historisk-tilbagegang-i-danske-elevers-pisa-resultater/ |
| VIVE (Denmark) PISA 2025 report | https://www.vive.dk/media/pure/bxq12bbz/31540448 |
| Skolkoll (Sweden), international statistics | https://skolkoll.se/en/statistics/international/ |
| Nordic Council, "Nordisk fokus på fallende PISA-resultater" | https://www.norden.org/no/node/99262 |
| The Northern Voices, "PISA 2025 Nordic-Baltic results" (blog; secondary) | https://www.thenorthernvoices.com/post/pisa-2025-nordic-baltic-results-estonia-latvia |

## 5. Open-data mirrors (reachable from the sandbox; already downloaded)

| What | URL |
|---|---|
| uygarcatal6/pisa-turkiye-replication, `data/derived/pisa_scores_long.csv` and `pisa_scores_wide.csv` (CC BY 4.0) | https://github.com/uygarcatal6/pisa-turkiye-replication |
| a0th/a0th.github.io `projects/brviz/data/pisa.csv` (PISA 2022 Vol I Tables I.B1.5.4-6; no licence file found) | https://github.com/a0th/a0th.github.io |
| worldbank/LearningPoverty `05_working_paper/051_rawdata/pisa-wdi.csv` (MIT; WDI/EdStats `LO.PISA.MAT.*` indicators, 2000-2018) | https://github.com/worldbank/LearningPoverty |
| Our World in Data ETL, OECD PISA snapshot 2023-12-06 (`snapshots/oecd/2023-12-06/pisa_*_all.xls.dvc`, garden step `etl/steps/data/garden/oecd/2023-12-06/pisa.py`) | https://github.com/owid/etl | DVC pointers only; the data itself sits on OWID's S3/catalog (not reachable). The OWID grapher chart "Average performance of 15-year-olds in mathematics" is what `jeremydwong/.../pisa-data-academic-performance.csv` exported. |
| learningtower R package (student-level subset 2000-2022, .rda) | https://github.com/kevinwang09/learningtower | Not needed for country means; useful if student-level re-analysis is wanted. |
