# Synthesis: what the evidence base says (first pass, 2 Nov 2026)

This note pulls the key findings of the seven evidence folders together for the
op-ed. Every number below is traced in the folder named in brackets; most come
from search-engine snippets of primary documents, because the cloud session
could not open the source websites. **Verify against the primary documents in
each folder's `TO-FETCH.md` before quoting verbatim.**

## 1. The case in one chart

`charts/grade_inflation_vs_ib.png` (small multiples, same relative y-scale)
and `charts/grade_inflation_vs_ib_indexed.png` (one panel, 2012 = 100):

| Yardstick | Start | End | Change | Folder |
|---|---|---|---|---|
| Norwegian grunnskolepoeng, national mean | 39.5 (2009) | 42.2 (2026); peak 43.4 (2022, no exams) | +2.7 points (+7 %) | norway-grades |
| IB Diploma mean total points, May, worldwide | 30.4 (2004); 29.65 (2019) | 30.9 (2026, provisional); 30.24 (2023) | about +0.5 since 2004, +0.6 since the 2023 reset | ib-statistics |
| PISA mathematics, Norway | 495 (2003); 502 (2015 peak) | 452 (2025) | -50 since 2015, about 2.5 school years by the OECD's 20-points rule | pisa |

The pandemic band is the natural experiment: when ordinary exams disappeared,
*both* systems inflated (grunnskolepoeng +1.2 in one year; IB mean 29.65 to
33.02). The IB then deliberately "set the distribution of awarded grades to
the pre-pandemic levels of May 2019" in 2023 (mean back to 30.24). Norwegian
grades came only part of the way down and have settled about 2.7 points above
2009. An externally anchored system corrects; a teacher-set system ratchets.

## 2. Norwegian grade inflation is documented by the authorities themselves

- Udir on upper secondary: "I løpet av de siste 15 årene har elevene i de
  fleste fellesfagene i videregående opplæring fått stadig bedre karakterer.
  Undersøkelser viser imidlertid ikke den samme utviklingen i elevenes
  kompetanse" (norway-grades).
- Nearly half of upper-secondary pupils get a lower grade on the written exam
  than their standpunkt grade; 41 % in lower secondary (Udir, SSB).
- National tests (nasjonale prøver): no change in mean scale points 2014-2021
  while grunnskolepoeng rose; declines in 2023 and 2024 (norway-grades).
- The ministry itself commissioned research in 2026 on "kvalitet,
  karakterinflasjon og segregering" in upper secondary (norway-grades).
- Upper-secondary maths programme subjects (R1, R2, S1, S2) show the same
  ratchet: R1 standpunkt 3.9 (2007-2015) to 4.2 (2017-2021) to 4.0 (2023-2026)
  (norway-grades, `vgs_grades.csv`).
- PISA: Norway's maths decline 2018-2025 (-49) is the largest among the 16
  comparison countries; 38 % of 15-year-olds are now below Level 2 in maths,
  against 17-22 % in every cycle 2003-2018 (pisa).

## 3. The IB is built to hold its standard; Norwegian standpunkt grades are not

- IB: externally marked exams, moderated internal assessment, grade boundaries
  set at a grade-award meeting from judgement plus statistics, with the chief
  examiner guide stating "the grade standard from previous sessions must be
  carried forward". The statistical anchor (Statistically Recommended
  Boundaries) was reviewed independently by AlphaPlus in 2021-2022
  (ib-assessment-design).
- Norwegian standpunkt grades are set by the teacher's "faglige skjønn" against
  kompetansemål with no external anchoring; only a few exams are drawn by lot;
  all exams were cancelled in 2020 and 2022 (ib-assessment-design, norway-grades).
- Honest caveats to keep in the op-ed: the IB calls its own model "weak
  criterion referencing"; it visibly inflated in 2020-2022 before correcting;
  the mean has drifted up about 0.6 points since 2023 without an IB
  explanation; nearly all predictive-validity studies are IB-commissioned, and
  an independent Cambridge Assessment study (Green and Vignoles 2012) found the
  UK tariff *over*-valued the IB (ib-assessment-design).
- The ACER / ISA belief is not supported: ACER has only been a research
  contractor to the IB; DP assessment is designed and run by the IB's own
  Assessment Centre in Cardiff. ACER did lead the PISA consortium 2000-2012 and
  is back as a PISA 2025 contractor (ib-assessment-design).

## 4. The conversion table: what changed and what the method assumes

| IB points | Table in force (1999 regulation) | 2022 HK-dir table | 2026 proposal |
|---|---|---|---|
| 20 | 26.0 | 20.0 | 29.5 |
| 24 | 34.3 | 29.0 | ? |
| 30 | 42.9 | 40.4 | ? |
| 35 | 50.0 | 47.4 | ? |
| 40 | 57.1 | 53.6 | ? |
| 42-45 | 60.0 (plateau from 42) | 45 only = 60.0 | ? (Legeforeningen's annex: 45 = 60.0) |

(conversion-table, `tables_norway.csv`; rows 22-45 of the 2026 proposal were
not visible in any snippet and are the top fetch priority.)

- Method: the admission regulation says tables "skal lagast ved å finne
  prosentilar i det utanlandske datagrunnlaget"; HK-dir / Norsk Regnesentral
  match the empirical cumulative distribution (ecdf) of IB totals to the
  distribution of Norwegian vitnemål averages. The minister called it "en ren
  statistisk sammenligning av populasjonene" (conversion-table).
- The only quantitative justification found: "0,08 % av søkerne med norsk
  videregående opplæring (studieforberedende) fikk snitt 6,0 i opptaket, mens
  2,8 % av IB-søkerne fikk dette" (press release 29 Oct 2026). The method
  therefore assumes IB and Norwegian applicants have the same ability
  distribution and treats the Norwegian distribution, inflation included, as
  the reference. Nobody has published Norwegian outcome data on how IB
  graduates actually perform at university (media-and-policy,
  ib-assessment-design).
- Medicine, UiO autumn, ordinary quota: cut-off 68.0 (2011) to 70.2 (2023) to
  69.0 (2026); first-time-diploma quota 61.6 (2020) to 60.0 (2026). A 45-point
  diploma converts to 60.0 under every table, so the fight is over 38-44 points
  (media-and-policy, norway-grades).
- Timeline: old table since the 1990s; HK-dir table 15 Dec 2022 for the
  2025/26 intake; NIBS letter May 2023; Storting questions autumn 2024 and
  Dok 8:76 S (Feb 2025, H, FrP, SV, V, KrF); minister Aasland postponed and
  re-heard in winter 2025; new hearing 29 Oct 2026 (deadline 10 Dec 2026,
  effective from the 2030-31 intake, built only on Norwegian IB-line data)
  (media-and-policy, `timeline.csv`).

## 5. The Western record: teacher grades rise, external measures do not

- UK A-level A*/A share: 25.4 % (2019), 38.1 % (2020, teacher grades),
  44.8 % (2021), back to 27.2 % (2023) under Ofqual's "comparable outcomes".
  Regulators anchor school grades to external evidence, never the reverse.
- US: mean high-school GPA 2.68 (1990) to 3.11 (2019) while SAT and NAEP fell.
- Germany: share of 1.0-1.9 Abitur 20.1 % (2006) to 30.7 % (2024).
- Denmark: STX average 6.9 (2010) to 7.7 (2022); exam grades 0.8 below teacher
  year grades. Sweden: decades of betygsinflation research and a 2023 inquiry
  "för att stoppa betygsinflationen".
- Every earlier IB-conversion dispute (UK tariff, Australia ATAR 2021-2023,
  Sweden 2016, Denmark 2018) was about top-end resolution and the choice of
  comparison group, the same two design questions as Norway's
  (grade-inflation-international).

## 6. Gaps to close before publication

1. Full 2026 proposal table (rows 22-45) and the HK-dir "2026a/2026b" variants.
2. Per-subject upper-secondary standpunkt and exam series (one Udir API fetch).
3. Norwegian applicants' grade-average distribution over time (DBH / HK-dir).
4. IB bulletins: 2009 mean, 2017 pass rate, 45-point counts 2014-2015, Norway
   has no country breakdown (regional only).
5. Foreign conversion tables beyond Denmark; Storting committee outcome on
   Dok 8:76 S; any VG, BT, Aftenposten, NRK coverage (none surfaced in search).
