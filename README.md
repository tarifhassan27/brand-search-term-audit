# Brand Taxonomy & Search-Term Audit
### Does "Dove" mean soap — or something else?

---

## The Problem

Brand monitoring tools count YouTube mentions by searching for keywords.
But what if the keyword is ambiguous?

**"Dove"** returns four completely different things:
- Dove soap and beauty products
- Dove Cameron (pop star)
- Dove birds (wildlife videos)
- Dove chocolate

If you search "dove" and count everything as a brand mention, 47% of your
data is wrong. This project audits which search terms actually return brand
content — and which ones are noise.

---

## What I Built

A full audit pipeline: API data collection → PostgreSQL storage → manual
labeling → precision analysis → actionable recommendations.

| Phase | What happened |
|---|---|
| 0 | Test search confirmed Dove ambiguity problem |
| 1 | Defined business problem and labeling rules |
| 2 | Fetched 289 YouTube Shorts via YouTube Data API v3 |
| 3 | Loaded raw data into PostgreSQL (raw schema) |
| 4 | Labeled all 289 videos: BRAND / CELEBRITY / BIRD / OTHER |
| 5 | Built clean schema with term_tier classification |
| 6 | Calculated precision per search term |
| 7 | Taxonomy playbook: keep / review / drop recommendations |
| 8 | Executive brief for brand/media teams |

---

## Key Finding

| Metric | Result |
|---|---|
| Total videos audited | 289 |
| Brand-relevant results | 229 (79%) |
| Noise | 60 (21%) |
| Terms with perfect precision (1.0) | 13 of 20 |
| Terms with zero brand results | 4 of 20 |

**The bare term "dove" scores 0.53 precision.**
Including it in brand monitoring is a coin flip.

---

## Repo Structure

```
brand-search-term-audit/
├── 01_business_problem/
│   └── problem_statement.md      # Why this matters
├── 02_data/
│   ├── fetch_data.py             # YouTube API collector
│   ├── raw_results.csv           # 289 rows from API
│   ├── labeling_guideline.md     # Labeling rules
│   └── labeled_results.csv      # Labels applied
├── 03_sql/
│   ├── 01_create_tables.sql      # Schema setup
│   ├── 02_load_raw.sql           # Data load
│   └── 03_precision_analysis.sql # Core analysis query
├── 05_taxonomy_playbook/
│   └── taxonomy_playbook.md      # Keep/drop/add recommendations
├── 06_executive_brief/
│   └── executive_brief.md        # Summary for brand teams
└── test_search.py                # Phase 0 proof of concept
```

---

## Tech Stack

- **Python** — YouTube Data API v3, data collection
- **PostgreSQL** — raw + clean schema, precision calculations
- **SQL** — labeling, tier classification, aggregation
- **Git** — version controlled, phase-by-phase commits

---

## Precision Results

| Search Term | Tier | Precision |
|---|---|---|
| dove soap | brand_core | 1.00 |
| dove shampoo | brand_core | 1.00 |
| dove deodorant | brand_core | 1.00 |
| dove body wash | brand_core | 1.00 |
| dove beauty bar | brand_core | 1.00 |
| dove dry shampoo | brand_core | 1.00 |
| dove moisturizer | brand_core | 1.00 |
| dove face wash | brand_core | 1.00 |
| dove real beauty | campaign | 1.00 |
| dove self esteem | campaign | 1.00 |
| dove realbody | campaign | 1.00 |
| dove care | campaign | 1.00 |
| dov soap | misspelling | 1.00 |
| dove sop | misspelling | 0.93 |
| dove | ambiguous | 0.53 |
| doove | misspelling | 0.20 |
| dove bird | ambiguous | 0.00 |
| dove chocolate | ambiguous | 0.00 |
| dove cameron | ambiguous | 0.00 |
