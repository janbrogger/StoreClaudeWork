# IB statistical bulletins to retrieve from an unrestricted machine

All ibo.org hosts were blocked from this session; every figure in
`ib_session_stats.csv` comes from search-engine snippets of these PDFs, IB
press releases, or secondary sites. Fetch the PDFs below and re-read the
tables named. Two URL families exist: the old `contentassets/bc850970f4e54b87828f83c7976a4db6/`
(2007-2021) and the new `globalassets/new-structure/about-the-ib/pdfs/`
(2022-). Index page: https://ibo.org/about-the-ib/facts-and-figures/statistical-bulletins/diploma-programme-and-career-related-programme-statistical-bulletin/

Old-format bulletins (2005-2019) are tabular. Tables to extract: "Number of
candidates registered" (by category: Diploma / Retake / Course / Anticipated),
"Pass rate worldwide" (5-year table), "Mean grade worldwide", "Mean points
score worldwide" (5-year), "Number/percentage of candidates scoring 45 points"
(5-year), "Distribution of points totals" (0-45, awarded / not awarded),
"Number of schools registering candidates", plus the per-region tables.
From ~2020 the bulletins are Power BI exports with 5-year charts: "Number of
Students and Pass Rate", "Mean Grade", "Mean Total Points", "Grouped Total
Points Distribution" (0-23 / 24-29 / 30-34 / 35-39 / 40-45) and "Mean Grade and
Mean Total Points of Candidates Awarded the Diploma". From May 2023 the
45-point count is no longer published (bulletin note).

| Session | URL | Status | Extract |
|---|---|---|---|
| May 2006 | listed on index page as "May 2006 (PDF, 1.8 MB)" - URL not captured | unknown | mean points/pass rate/45-pt tables 2002-2006 |
| May 2007 | https://www.ibo.org/contentassets/bc850970f4e54b87828f83c7976a4db6/ibdiplomaprogrammemay2007.pdf | confirmed by search | distribution of points totals; 5-year mean/pass tables |
| May 2008 | https://ibo.org/contentassets/bc850970f4e54b87828f83c7976a4db6/may2008statisticalbulletin.pdf | confirmed | "Mean grade worldwide" / "Pass rate worldwide" / mean points May 2004-2008 |
| 2008 data summary | https://www.ibo.org/contentassets/8711842fb1bf4aa88684c8f7769a508d/2008datasum.pdf | confirmed | summary |
| May 2009 | https://www.ibo.org/contentassets/bc850970f4e54b87828f83c7976a4db6/may2009statisticalbulletin.pdf | confirmed | pass rate 2005-2009 (81.40, 80.35, ...), mean grade, schools 2005-2009 (1,582 in 2009), 45-pt counts |
| Nov 2009 | https://www.ibo.org/contentassets/bc850970f4e54b87828f83c7976a4db6/nov2009statisticalbulletin.pdf | confirmed | |
| May 2010 | not surfaced (try `may2010statisticalbulletin.pdf` in the same folder - GUESS) | | |
| May 2011 | https://www.ibo.org/contentassets/bc850970f4e54b87828f83c7976a4db6/statistical_bulletin_may_2011.pdf | confirmed | "Mean points score worldwide", "% candidates scoring 45 points" |
| Nov 2011 | https://ibo.org/contentassets/bc850970f4e54b87828f83c7976a4db6/november2011statisticalbulletin.pdf | confirmed | |
| May 2012 | https://www.ibo.org/contentassets/bc850970f4e54b87828f83c7976a4db6/may_2012_statistical_bulletin.pdf | confirmed | "Mean points score worldwide May 2008-May 2012" |
| Nov 2012 | https://www.ibo.org/contentassets/bc850970f4e54b87828f83c7976a4db6/2012-novemberstatsbulletin.pdf | confirmed | |
| May 2013 | https://www.ibo.org/contentassets/bc850970f4e54b87828f83c7976a4db6/2013-maydpstatisticalbulletin.pdf | confirmed | mean 29.81 vs 29.96 discrepancy; 108 x 45 pts |
| May 2014 | https://highered.colorado.gov/sites/highered/files/2020-03/ib_statistical_bulletin_-_may_2014.pdf (mirror; ibo.org URL not captured) | confirmed mirror | 5-year chart 2010-2014 (29.7, 29.7, 29.9, 30.0, 30.1 / 78.1, 77.9, 78.5, 79.0, 79.3) - verify year mapping |
| May 2015 | https://ibo.org/contentassets/bc850970f4e54b87828f83c7976a4db6/dp-2015-may-stats-bulletin.pdf | confirmed | pass rate, 45-pt count (160 per press release) |
| Nov 2015 | https://www.ibo.org/contentassets/bc850970f4e54b87828f83c7976a4db6/dp-statistical-bulletin-november-2015.pdf | confirmed | |
| May 2016 | https://ibo.org/contentassets/bc850970f4e54b87828f83c7976a4db6/dp-statistical-bulletin-may-2016-en.pdf | confirmed | |
| Nov 2016 | https://ibo.org/contentassets/bc850970f4e54b87828f83c7976a4db6/dp-statistical-bulletin-november-2016-en.pdf | confirmed | |
| May 2017 | not surfaced (try `dp-statistical-bulletin-may-2017-en.pdf` - GUESS) | | pass rate, candidates, 218 x 45 pts |
| May 2018 | https://www.ibo.org/contentassets/bc850970f4e54b87828f83c7976a4db6/dp-statistical-bulletin-may-2018-en.pdf | confirmed | summary table: 29.76 / 259 x 45 / 78.18% |
| Nov 2018 | https://www.ibo.org/contentassets/bc850970f4e54b87828f83c7976a4db6/dp-statistical-bulletin-november-2018-en.pdf | confirmed | |
| May 2019 (final) | https://www.ibo.org/contentassets/bc850970f4e54b87828f83c7976a4db6/dp-statistical-bulletin-may-2019.pdf | confirmed | 166,465 cand.; 29.65; 275 x 45; 77.81%; 2,926 schools; 5-year tables 2015-2019 |
| Nov 2019 prov/final | https://www.ibo.org/contentassets/bc850970f4e54b87828f83c7976a4db6/dp-statistical-bulletin-november-2019.pdf ; ...-november-2019-final-en.pdf | confirmed | |
| May 2020 (provisional, Aug 2020) | https://www.ibo.org/contentassets/bc850970f4e54b87828f83c7976a4db6/dp-statistical-bulletin-may-2020-en.pdf | confirmed | 170,343 / 29.92 / 141 x 45; note on exclusion from time series. A FINAL May 2020 bulletin (174,360 / 31.34 / 339) must exist - URL not captured |
| May 2021 final | https://ibo.org/globalassets/new-structure/programmes/dp/pdfs/diploma-programme-final-statistical-bulletin-may-2021-assessment-session..pdf (double dot is real) | confirmed | 1,351 x 45; chart "mean of awarded" 2017-2021: 32.45, 34.49(?), 32.23, 32.30, 33.15 - verify |
| May 2021 results overview | https://www.ibo.org/globalassets/new-structure/assessment/pdfs/m21-results-overview-data-en.pdf | confirmed | 33.02 / 88.96 / 5.19 |
| Nov 2021 prov/final | https://www.ibo.org/contentassets/bc850970f4e54b87828f83c7976a4db6/dp-provisional-statistical-bulletin-november-2021-en.pdf ; https://www.ibo.org/globalassets/new-structure/about-the-ib/pdfs/final-statistical-bulletin-november-2021.pdf | confirmed | |
| May 2022 prov/final | https://www.ibo.org/globalassets/new-structure/about-the-ib/pdfs/provisional-statistical-bulletin-may-2022.pdf ; https://ibo.org/globalassets/new-structure/about-the-ib/pdfs/final-statistical-bulletin-dp-cp-may-2022.pdf | confirmed | 32.00 / 772 x 45 / 86.11 |
| Nov 2022 prov/final | https://www.ibo.org/globalassets/new-structure/about-the-ib/pdfs/provisional-statistical-bulletin-november-2022.pdf ; .../final-dp-statistical-bulletin-november-2022.pdf | confirmed | |
| May 2023 prov/final | https://www.ibo.org/globalassets/new-structure/about-the-ib/pdfs/dp-cp-provisional-statistical-bulletin-may-2023.pdf ; .../dp-cp-final-statistical-bulletin-may-2023.pdf | confirmed | 179,922 / 30.24 / 80.01 / 4.84; note "will no longer include ... 45 points" |
| Nov 2023 prov/final | https://www.ibo.org/globalassets/new-structure/about-the-ib/pdfs/dp-provisional-statistical-bulletin-november-2023.pdf ; .../dp-statistical-bulletin-november-2023_en.pdf | confirmed | |
| May 2024 prov/final | https://www.ibo.org/globalassets/new-structure/about-the-ib/pdfs/the-ib-dp-and-cp-statistical-bulletin_en.pdf (provisional) ; https://ibo.org/globalassets/new-structure/about-the-ib/pdfs/dp-final-statistical-bulletin-may-2024_en.pdf | confirmed | charts 2020-2024 (see CSV) |
| Nov 2024 final | https://www.ibo.org/globalassets/new-structure/about-the-ib/pdfs/dp-final-statistical-bulletin-november-2024_en.pdf | confirmed | |
| May 2025 prov/final | https://ibo.org/globalassets/new-structure/about-the-ib/pdfs/dpcp-provisional-statistical-bulletin-may-2025_en.pdf ; https://ibo.org/globalassets/new-structure/about-the-ib/pdfs/dpcp-final-statistical-bulletin-may-2025_en.pdf | confirmed | points-band table (40-45: 9,999 = 11.9%); candidates; pass 81.3 |
| Nov 2025 provisional | https://ibo.org/globalassets/new-structure/about-the-ib/pdfs/dp-provisional-statistical-bulletin-november-2025_en.pdf | confirmed | |
| May 2026 provisional | https://ibo.org/globalassets/publications/dpcp-provisional-statistical-bulletin-may-2026_en.pdf (given by requester; not surfaced by search) | to verify | candidates, pass rate, mean grade, mean total points, 40-45 band, Non-Exam Contingency note |

## Non-bulletin documents worth fetching
- IB 2011 press release "2011 IB Diploma Programme Results Again Show no Grade Inflation": https://prnewswire.co.uk/news-releases/2011-ib-diploma-programme-results-again-show-no-grade-inflation-145069745.html (pass rates 2007-2011; Jeff Beard quote).
- IB blog 2013 results post (pass rates 2009-2013, 29.81, 108 x 45): https://blogs.ibo.org/?p=1372
- IB reply to Danish parliament (means 2012/2013, all vs passing candidates): https://ft.dk/samling/20141/almdel/BUU/bilag/106/1502572.pdf
- Danish IB conversion table 2017: https://www.uvm.dk/-/media/filer/uvm/aktuelt/pdf-17/170629-ny-omregningstabel-ib.pdf
- IB research on statistically recommended boundaries (how standards are maintained): https://www.ibo.org/globalassets/new-structure/research/pdfs/executive-summary-srb-research-study-en.pdf
- IB May 2020 assessment-model letter: https://ibo.org/globalassets/new-structure/covid-19/pdfs/assessment-model-letter-may-2020-en.pdf
- IB results press releases: 2014 https://ibo.org/news/news-list/ib-announces-increase-in-diplomas-awarded-worldwide/ ; 2015 https://ibo.org/news/news-list/141831-dp-graduates-celebrate-2015-exam-results/ ; 2017 https://ibo.org/news/news-list/ib-results-day-july-2017/ ; 2018 https://ibo.org/news/news-list/ib-students-around-the-world-celebrate-their-results-during-the-ibs-50th-anniversary/ ; 2020 https://ibo.org/news/news-list/congratulations-2020-diploma-and-career-related-programme-graduates/ ; 2021 https://ibo.org/news/news-list/more-than-170000-students-across-the-world-receive-ib-results/ ; 2023 https://ibo.org/news/news-list/ib-students-worldwide-receive-their-results/ ; 2025 https://ibo.org/news/news-list/ib-students-worldwide-receive-their-results-2025/ ; 2026 https://ibo.org/news/news-list/more-than-209000-ib-students-worldwide-receive-their-dp-and-cp-results/
- Third-party transcription of the May/Nov 2024 bulletins (used here, verify against PDFs): https://raw.githubusercontent.com/DevChrisChan/CiteCount/main/bulletin-analysis/m24.html and n24.html
