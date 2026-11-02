# TO-FETCH: endpoints, tables and reports to retrieve from an unrestricted machine

Everything below was identified during this session but could not be downloaded here
(only github.com / raw.githubusercontent.com / api.github.com / pypi.org were reachable).
Items are ordered by expected value for the op-ed chart (Norwegian grade means over time).

## A. Udir - Statistikkportalen (the engine behind udir.no "statistikkbanken")

Documented (reverse-engineered) in two GitHub repos: `VirtualAiCorp/NMBU-sammenligning`
(`scripts/fetch-udir.py`) and `terchris/atlas` (`atlas-data/ingest/src/sources/udir-gsi/README.md`).
Udir's own description of the API: "Dette APIet tilgjengeliggjør statistikkdata for
utdanningsdirektoratet. APIet er ikke ment for ekstern bruk i dag, og vil endres uten varsel."
No login, returns the same suppressed/prikkede numbers as udir.no.

- Swagger: `https://statistikkportalen.udir.no/api/rapportering/swagger` (json at `.../swagger/v1/swagger.json`)
- Base: `https://statistikkportalen.udir.no/api/rapportering/rest/v1/Statistikk/{skjema}/{tabell}/{rapportNr}/{rapportVersjon}/data`
- Helpers per table: `.../{...}/filterSpec`, `.../filterVerdier`, `.../filterStatus`, `.../sideData`;
  `GET .../rest/v1/Rapportside/{rapportside-id}` resolves the *current* report version.
- Query style: `?radSti=<rowpath>&filter=EierformID(-10)_KaraktertypeID(1_3)_KjoennID(-10)_TidID(201516_201617)_VisAntallPersoner(1)&inkluderKoder=true`
  (`-10` = Udir's "alle" sentinel; `*` = suppressed cell; numbers come as Norwegian strings "3,9", "1 677").
- Tables that will yield the op-ed series:
  - `VGO/ResultatFagV/2/5` - **Karakterer i videregående skole** (= udir.no/tall-og-forskning/statistikk/statistikk-videregaende-skole/karakterer-vgs/). Row hierarchy Fag -> Nasjonalt -> Fylke -> Enhet. `KaraktertypeID`: 1 = standpunkt, 3 = skriftlig eksamen (2 = muntlig, to confirm). Gives mean grade, n, and (in the web view) the grade distribution 1-6 per subject per school year 2007-08 -> 2025-26. Fagkoder (LK06/LK20): R1 REA3022/REA3056, R2 REA3024/REA3058, S1 REA3026/REA3060, S2 REA3028/REA3062; 1T MAT1013/MAT1017?, norsk hovedmål skriftlig Vg3 NOR1211/NOR1267?, engelsk Vg1 ENG1002/ENG1007?, fysikk 1 REA3004/REA3038?, kjemi 1 REA3011/REA3045? (codes with "?" are UNVERIFIED (model memory) - take them from `.../filterVerdier`). This is the single most valuable fetch: it gives standpunkt AND eksamen means plus share of 5/6 for every subject.
  - `GSK/ResultatFagG/...` - grunnskole karakterer per fag (standpunkt/eksamen 10. trinn).
  - `GSK/NasjonaleProever/...` - nasjonale prøver skalapoeng (5., 8., 9. trinn).
  - Grunnskolepoeng: table name not captured; look under schema `GSK` in swagger (likely `GrunnskolepoengG` or inside `ResultatFagG`). Web page: udir.no/tall-og-forskning/statistikk/statistikk-grunnskole/karakterer-grunnskolen/ (also "grunnskolepoeng" analysebrett).
- The *official* open API `api.statistikkbanken.udir.no/api/rest/v2/Eksport/{tabell}/data` (console: apikonsoll.statistikkbanken.udir.no) covers only Elevundersøkelsen (8 tables) - not useful for grades.

## B. Udir analyses / articles (PDF print endpoints found in search results)

`https://udir.no/api/PdfApi/PrintPageAsPdfDocument/<id>` renders a udir.no page as PDF. IDs seen, with best guess of content:
- 156295, 156134 - "Analyse av karakterstatistikk for videregående/grunnskolen 2018-19" (gap standpunkt-eksamen since 2011-12; "nesten halvparten får dårligere eksamenskarakter").
- 174390 - probably karakterstatistikk 2019-20 (first no-exam year).
- 182979, 183686 - karakterer 2020-21 (grunnskole / vgs).
- 198765, 199013, 199025 - karakterer 2021-22 (grunnskolepoeng 43,4; "de siste 15 årene ... stadig bedre karakterer" quote lives in one of these).
- 216116, 216111, 216297 - karakterer 2022-23 / 2023-24 (grunnskolepoeng 42,4 and 42,2; S1 eksamen 2,9 -> 2,4).
- 222156 - most likely "Karakterer i videregående skole 2024-25" (not seen in snippets; fetch).
- 145864, 105254, 105863, 114945, 170113 - older (2016-2018) analyses incl. Udir summary of SSB 2011/4 and NIFU 2014 (private vs public gap).
- Udir report 2026: `https://www.udir.no/tall-og-forskning/finn-forskning/rapporter/2026/kvalitet-i-standpunktvurderingen-krever-system-og-profesjonsfellesskap/`
- Udir nasjonale prøver trend pages: PDF ids 169350, 189337, 201672, 219217.

## C. SSB StatBank (api: `https://data.ssb.no/api/v0/no/table/<nr>` POST JSON-stat; or `.../table/<nr>?lang=no` CSV via web)

- **07497** Gjennomsnittlig grunnskolepoeng etter kjønn (0 poeng ikke medregnet) - 2009 ->. The authoritative grunnskolepoeng series (fills 2010, 2017, 2024-25 gaps).
- **07495** Karakterer og nasjonale prøver i grunnskolen (standpunkt/eksamen per fag, 10. trinn, 2009 ->).
- **07501**, **13715**, **13717** - related grunnskole karakter tables (fag x karakter distribution; by parental education).
- **06410** Elever i grunnskolen (denominators).
- Statistics pages: `ssb.no/kargrs` (Karakterer ved avsluttet grunnskole) archive releases 2009-12-03, 2010-12-17, 2011-11-17, 2012-11-01, 2013-11-06, 2015-10-08, 2016-10-06 (each states the national mean).
- `ssb.no/utdanning/statistikker/nasjprov` (nasjonale prøver) and article "Korrigerte tall for nasjonale prøveresultater over tid" (rescaling table).
- For VGS: SSB "Karakterer ved avsluttet videregående" (search StatBank for "standpunktkarakter videregående", tables 11xxx/12xxx - numbers not captured here).

## D. Samordna opptak / HK-dir

- Tableau data warehouse: `https://rapport-dv.educloud.no/` report "Poenggrenser og ventelistetall hovedopptak/suppleringsopptak" - append `.csv` to the view URL, filter `År` and `Opptaksrunde`; yields every programme x quota x year 2020-2026 (73 424 rows). Already mirrored in GitHub (`VirtualAiCorp/NMBU-sammenligning/data/nmbu/kilder/so_poenggrenser_venteliste.csv`) - **the medicine series in samordna_opptak.csv comes from there**. Check whether the view accepts years before 2020.
- Søker- og tilbudstall til nedlasting: `https://sokertallrapport.samordnaopptak.no/2026/figurer/side_0_grunntabeller_hoved/tabeller/` (static HTML with embedded JSON `allData`; tables `grunndata_tabell_2_uhg_hoved_26` etc., 2021-2026).
- Historical poenggrenser pages: `https://www.samordnaopptak.no/info/om/sokertall/` and `.../poenggrenser/` (hovedopptak 2005 ->; older years as PDF "Poenggrenser hovedopptak <year>"). Needed for UiO/UiB/NTNU/UiT medisin 2005-2019 (only UiO høst ORD 2011-2019 found via third-party site).
- Search API (undocumented): `POST https://sok.samordnaopptak.no/api/v1/search` (admission.id per year; programme fields incl. cut-offs for last 6 years).
- DBH/HK-dir table **571** "Opptakspoeng" (sum karakterpoeng and n per programme -> mean karakterpoeng of admitted/applicants) and 379 (søkere/kvalifiserte/tilbud). `https://dbh.hkdir.no/` -> API `https://dbh.hkdir.no/api/Tabeller/hentJSONTabellData` (POST, tabell_id 571).
- HK-dir statistics for the IB hearing: distribution of applicants' karakterpoeng/snitt by year, share with 6,0 (0,08 % vs 2,8 %) - ask HK-dir (post@hkdir.no) for the table behind the hoyringsnotat, or Innsyn.

## E. Reports / documents to download

- KD hoyringsnotat "Forslag om endring i forskrift om opptak til høgare utdanning - ny omrekningstabell for IB": `https://www.regjeringen.no/contentassets/315531d605f3405cac8dc90700b75b63/hoyringsnotat-forslag-om-endring-i-forskrift-om-opptak-til-hogare-utdanning-ny-omrekningstabell-for-ib.pdf` and annex `.../1-framlegg-til-ny-omrekningstabell-for-international-baccalaureate-ib.pdf`; hearing page `https://www.regjeringen.no/id3183537`; press release `https://www.regjeringen.no/no/aktuelt/ny-omregningstabell-for-ib-karakterer-sendes-pa-horing/id3184606/`.
- Stortinget: skriftlig spørsmål 15:571 (2024-25) `?qnid=99754` (30x statement), `?qnid=98049`, Dok 8:76 S (2024-2025) representantforslag on IB, Innst. 154 S (2025-2026).
- SSB Rapporter 2011/4 Galloway, Kirkebøen, Rønning "Karakterpraksis i grunnskoler": `https://www.ssb.no/emner/04/02/20/rapp_201104/rapp_201104.pdf`.
- SSB notater on standpunkt vs eksamen: 2005/31, 2006/35, 2007/29, 2008/24 (`statbank.ssb.no/emner/04/02/notat_2005xx/...`).
- SSB article "Større forskjeller mellom standpunkt- og eksamenskarakterer blant innvandrerelever" (vgs, 2016-2019 data; cites Udir 2020b: 4 av 10 får lavere eksamenskarakter).
- NOU 2019:3 Stoltenberg-utvalget: `https://www.regjeringen.no/contentassets/8b06e9565c9e403497cc79b9fdf5e177/no/pdfs/nou201920190003000dddpdfs.pdf` (ch. on karakterer; proposes timetall-weighted points). NOU 2019:25 Lied-utvalget: `https://cms12.regjeringen.no/contentassets/efa97f020331439a8adbb84dd90ab426/no/pdfs/nou201920190019000dddpdfs.pdf` (check: this id may be NOU 2019:19).
- Rambøll for KS (June 2021) "Undervisnings- og vurderingssituasjonen i videregående skole våren 2020" (effect on standpunkt): `https://www.nfk.no/_f/p1/id6a3bb16-0dc6-41bc-a74f-a3f790896b8a/070621_rapport_ks_standpunktkarakterer.pdf`.
- KD-commissioned PROMENTA report 2026 (realfag "grade penalty", uses standpunkt+eksamen): `https://www.universitetsavisa.no/files/2026/08/25/260821kdrapport.pdf`.
- KD FoU-oppdrag "kvalitet, karakterinflasjon og segregering i private og offentlige videregående skoler" (in process 2026) - listed in Statsforvalteren Innlandet slides `https://www.statsforvalteren.no/siteassets/innlandet/barnehage-og-opplaring/dokumenter/frokostmote-23.09.2026-presentasjon.pdf`; ask KD/Udir for status.
- kudos.dfo.no documents 10177/files/10142.pdf and 12924/files/13059.pdf (KD-archived reports on standpunkt/eksamen - titles not captured).
- NIFU: 2014 report on standpunkt vs eksamen in private vs public schools; NIFU-rapport 2020:4 (kvote/poeng for medisin og psykologi) `https://nifu.brage.unit.no/nifu-xmlui/bitstream/handle/11250/2648860/NIFUrapport2020-4.pdf`; NIFU analysis of university grade rise (forskning.no/NTB "Karakterene til norske studenter har blitt bedre").
- Civita notat 02/2024 "Oppvask i opptakssystemet": `https://civita.no/content/uploads/2024/02/Notat_02_2024_Oppvask-i-opptakssystemet.pdf`.
- Acta Didactica Norge (Dec 2018) article on standpunkt/eksamen: `https://www.doaj.org/article/7b7c224663b448fb85a9b5a4a84917c5`.
- Statsforvalteren Vestland yearly "Karakterstatistikk for grunnskulen" (tabulates Udir national grunnskolepoeng per year 2013-14 ->).
- UiO Det medisinske fakultet "Studier og opptakskrav <year>" pages 2022-2026 (official UiO cut-offs); Uniforum 2025 "Medisinstudiet ved UiO har den høyeste poenggrensen".
- hvatrengerjeg.no and karakterportalen.no (third-party tables of SO cut-offs 2011 ->; verify against SO).
