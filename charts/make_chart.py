#!/usr/bin/env python3
"""DES005 - the pivotal chart: Norwegian grade inflation versus IB Diploma stability,
with PISA (Norway, mathematics) as the external yardstick.

Reads only CSV files under sources/ and writes
  charts/grade_inflation_vs_ib.png / .svg           (three small multiples, raw units)
  charts/grade_inflation_vs_ib_indexed.png / .svg   (one panel, every series indexed to BASE_YEAR = 100)

Exits non-zero, naming the file or series, when a required input is missing.
Run from the repository root:  .venv/bin/python charts/make_chart.py [--base-year 2009]
"""
import argparse
import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import pandas as pd  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "sources"
OUT = ROOT / "charts"

# dataviz skill reference palette (light surface): slot 1 blue, 2 orange, 3 aqua
COL_NO, COL_IB, COL_PISA, COL_REF = "#2a78d6", "#eb6834", "#1baf7a", "#9a9892"
INK, INK2, SURFACE = "#0b0b0b", "#52514e", "#fcfcfb"


def need(path: Path) -> pd.DataFrame:
    if not path.is_file():
        sys.exit(f"make_chart: required input missing: {path.relative_to(ROOT)}")
    df = pd.read_csv(path)
    if df.empty:
        sys.exit(f"make_chart: required input is empty: {path.relative_to(ROOT)}")
    return df


def series_or_exit(s: pd.Series, name: str) -> pd.Series:
    s = s.dropna()
    if len(s) < 2:
        sys.exit(f"make_chart: series '{name}' has fewer than two data points")
    return s.sort_index()


def load_series():
    # 1. Norway: grunnskolepoeng (national mean at end of lower secondary)
    gsp = need(SRC / "norway-grades" / "grunnskolepoeng.csv")
    gsp = gsp[gsp["value"].notna()].groupby("year")["value"].mean()
    norway = series_or_exit(gsp.astype(float), "grunnskolepoeng")

    # 2. IB Diploma: mean total points, May sessions
    ib = need(SRC / "ib-statistics" / "ib_session_stats.csv")
    ib = ib[(ib["month"].astype(int) == 5) & ib["mean_total_points"].notna()]
    ib_mean = series_or_exit(ib.set_index(ib["year"].astype(int))["mean_total_points"].astype(float), "IB mean total points")

    # 3. PISA mathematics, Norway and OECD average
    pisa = need(SRC / "pisa" / "pisa_country_year.csv")
    pisa = pisa[pisa["subject"].str.lower().eq("math") & pisa["mean"].notna()]
    def pick(name):
        sub = pisa[pisa["country"].str.lower().eq(name.lower())]
        return series_or_exit(sub.set_index(sub["year"].astype(int))["mean"].astype(float), f"PISA math {name}")
    pisa_no, pisa_oecd = pick("Norway"), pick("OECD average")
    return norway, ib_mean, pisa_no, pisa_oecd


def style(ax):
    ax.set_facecolor(SURFACE)
    for side in ("top", "right"):
        ax.spines[side].set_visible(False)
    for side in ("left", "bottom"):
        ax.spines[side].set_color("#d9d8d4")
    ax.tick_params(colors=INK2, labelsize=9)
    ax.grid(axis="y", color="#e6e5e1", linewidth=0.8)
    ax.set_axisbelow(True)


def endpoint_label(ax, s, color, fmt="{:.1f}"):
    for year in (s.index[0], s.index[-1]):
        ax.annotate(fmt.format(s[year]), (year, s[year]), textcoords="offset points", xytext=(0, 7),
                    ha="center", fontsize=9, color=INK)


def small_multiples(norway, ib, pisa_no, pisa_oecd, xlim):
    fig, axes = plt.subplots(1, 3, figsize=(12, 4.6), facecolor=SURFACE)
    panels = [
        (axes[0], "Norwegian school grades rise", "Grunnskolepoeng, national mean (Udir)", norway, COL_NO, "{:.1f}"),
        (axes[1], "IB Diploma stays flat", "Mean total points, May session, worldwide (IB statistical bulletins)", ib, COL_IB, "{:.1f}"),
        (axes[2], "PISA falls", "PISA mathematics, mean score (OECD)", pisa_no, COL_PISA, "{:.0f}"),
    ]
    for ax, title, sub, s, col, fmt in panels:
        style(ax)
        ax.plot(s.index, s.values, color=col, linewidth=2, marker="o", markersize=4)
        endpoint_label(ax, s, col, fmt)
        ax.set_title(title, loc="left", fontsize=12, color=INK, fontweight="bold", pad=18)
        ax.text(0, 1.02, sub, transform=ax.transAxes, fontsize=8.5, color=INK2)
        ax.set_xlim(*xlim)
    axes[2].plot(pisa_oecd.index, pisa_oecd.values, color=COL_REF, linewidth=1.5, linestyle="--")
    axes[2].annotate("OECD average", (pisa_oecd.index[-1], pisa_oecd.values[-1]), textcoords="offset points",
                     xytext=(4, -10), fontsize=8.5, color=INK2)
    axes[2].annotate("Norway", (pisa_no.index[-1], pisa_no.values[-1]), textcoords="offset points",
                     xytext=(4, 2), fontsize=8.5, color=INK2)
    fig.suptitle("Three yardsticks, one period: teacher-set grades inflate, the exam-based IB does not, PISA declines",
                 x=0.01, ha="left", fontsize=13, color=INK)
    fig.text(0.01, 0.01, "Sources: sources/norway-grades/grunnskolepoeng.csv, sources/ib-statistics/ib_session_stats.csv, "
             "sources/pisa/pisa_country_year.csv (see each folder's REPORT.md). Values shown at series ends.",
             fontsize=7.5, color=INK2)
    fig.tight_layout(rect=(0, 0.04, 1, 0.93))
    return fig


def indexed(norway, ib, pisa_no, base_year):
    fig, ax = plt.subplots(figsize=(9, 5), facecolor=SURFACE)
    style(ax)
    series = [("Norwegian grunnskolepoeng (Udir)", norway, COL_NO),
              ("IB Diploma mean total points, May (IB bulletins)", ib, COL_IB),
              ("PISA mathematics, Norway (OECD)", pisa_no, COL_PISA)]
    for label, s, col in series:
        if base_year not in s.index:
            sys.exit(f"make_chart: base year {base_year} not present in series '{label}'; pass --base-year")
        idx = s / s[base_year] * 100
        ax.plot(idx.index, idx.values, color=col, linewidth=2, marker="o", markersize=4, label=label)
        ax.annotate(f"{idx.iloc[-1]:.1f}", (idx.index[-1], idx.iloc[-1]), textcoords="offset points",
                    xytext=(5, -3), fontsize=9, color=INK)
    ax.axhline(100, color="#d9d8d4", linewidth=1)
    ax.set_ylabel(f"Index, {base_year} = 100", color=INK2, fontsize=9)
    ax.set_title("Norwegian grades up, IB flat, PISA down", loc="left", fontsize=13, color=INK, fontweight="bold")
    ax.legend(frameon=False, fontsize=9, loc="upper left")
    fig.text(0.01, 0.01, "Indexing hides scale differences: read the small-multiples chart for raw values. "
             "Sources: see sources/*/REPORT.md.", fontsize=7.5, color=INK2)
    fig.tight_layout(rect=(0, 0.04, 1, 1))
    return fig


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--base-year", type=int, default=2009)
    ap.add_argument("--out", type=Path, default=OUT)
    args = ap.parse_args(argv)
    norway, ib, pisa_no, pisa_oecd = load_series()
    years = [int(s.index.min()) for s in (norway, ib, pisa_no)] + [int(s.index.max()) for s in (norway, ib, pisa_no)]
    xlim = (min(years) - 1, max(years) + 1)
    args.out.mkdir(parents=True, exist_ok=True)
    for name, fig in (("grade_inflation_vs_ib", small_multiples(norway, ib, pisa_no, pisa_oecd, xlim)),
                      ("grade_inflation_vs_ib_indexed", indexed(norway, ib, pisa_no, args.base_year))):
        for ext in ("png", "svg"):
            fig.savefig(args.out / f"{name}.{ext}", dpi=200, facecolor=SURFACE)
        plt.close(fig)
        print(f"wrote {args.out / name}.png/.svg")


if __name__ == "__main__":
    main()
