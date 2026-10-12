# Executive Brief: Dove YouTube Search-Term Audit

**Prepared by:** Tarif Hassan
**Date:** October 2026
**Scope:** 20 search terms · 289 results · Brand: Dove (Unilever)

---

## The Problem

Brand monitoring tools count YouTube mentions by search term. If the search terms
are wrong, the mention count is wrong — and so is every decision made from it.

"Dove" is an ambiguous word. The same search returns soap ads, Dove Cameron
music videos, bird footage, and chocolate commercials. Without auditing which
terms actually return brand content, a team could be measuring noise as signal.

---

## What We Did

1. Built a structured list of 20 search terms across 4 tiers: brand core,
   campaign, misspellings, and ambiguous terms.
2. Fetched the top 15 results per term via the YouTube Data API using
   `videoDuration=short` (videos under 4 minutes) — 289 results total.
3. Labeled each result by title: BRAND, CELEBRITY, BIRD, or OTHER.
4. Calculated precision per term: what % of results were actually Dove the brand.

---

## Key Findings

| Result | Count |
|---|---|
| Total results audited | 289 |
| Brand-relevant (BRAND) | 229 (79%) |
| Noise (CELEBRITY + BIRD + OTHER) | 60 (21%) |

**Precision by term — selected highlights:**

| Term | Precision | Verdict |
|---|---|---|
| dove soap, dove shampoo, dove deodorant (+ 11 more) | 1.00 | Keep |
| dove sop (misspelling) | 0.93 | Review |
| dove | 0.53 | Risky — flag or isolate |
| doove (misspelling) | 0.20 | Drop |
| dove cameron, dove bird, dove chocolate | 0.00 | Drop immediately |

---

## Recommendations

**Keep 14 terms** with precision 1.0 — no noise in the top 15 results.

**Review 2 terms** — `dove sop` (0.93) and `dove` (0.53). Flag these; do not
include unfiltered in brand mention counts.

**Drop 4 terms** that return zero or near-zero brand content: dove cameron,
dove bird, dove chocolate, doove.

**Add 5 product-specific terms** not currently monitored: dove body lotion,
dove baby wash, dove men+care, dove deep moisture, dove antiperspirant.

---

## Business Impact

If a team runs brand monitoring with all 20 terms unfiltered, 21% of what
they count as "brand mentions" is noise — 47% of "dove" results alone are
off-brand. Fixing the term list takes one afternoon. The impact on data
quality is permanent.

---

## Limitations

Videos were labeled by title only — no video content was watched. Title-based
labeling can misclassify results where the title is ambiguous but the content
is clearly brand-relevant (or vice versa). A tool that analyzes video content
directly would close this gap.
