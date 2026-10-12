# Executive Brief: Dove YouTube Search-Term Audit

**Prepared by:** Tarif Hassan
**Date:** October 2026
**Scope:** 20 search terms · 289 YouTube Shorts · Brand: Dove (Unilever)

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
2. Fetched the top 15 YouTube Shorts per term via the YouTube Data API (289 videos).
3. Labeled each video as BRAND, CELEBRITY, BIRD, or OTHER.
4. Calculated precision per term: what % of results were actually Dove the brand.

---

## Key Findings

| Result | Count |
|---|---|
| Total videos audited | 289 |
| Brand-relevant (BRAND) | 229 (79%) |
| Noise (CELEBRITY + BIRD + OTHER) | 60 (21%) |

**Precision by term — selected highlights:**

| Term | Precision | Verdict |
|---|---|---|
| dove soap, dove shampoo, dove deodorant (+ 10 more) | 1.00 | Keep |
| dove sop (misspelling) | 0.93 | Keep |
| dove | 0.53 | Risky — drop or isolate |
| doove (misspelling) | 0.20 | Drop |
| dove cameron, dove bird, dove chocolate | 0.00 | Drop immediately |

---

## Recommendations

**Drop 5 terms** that return zero or near-zero brand content. Keeping them
inflates mention counts with irrelevant videos.

**Keep 13 terms** with precision 1.0 — these are clean signals.

**Flag "dove" as a standalone term.** At 0.53 precision, it is a coin flip.
Any report that includes it without filtering is overstating brand mentions.

**Add 5 product-specific terms** not currently monitored: dove body lotion,
dove baby wash, dove men+care, dove deep moisture, dove antiperspirant.

---

## Business Impact

If a team runs brand monitoring with all 20 terms unfiltered, 21% of what
they count as "brand mentions" is noise. On a high-volume campaign this could
mean hundreds of phantom mentions per week — leading to inflated performance
numbers and misallocated budget.

Fixing the term list takes one hour. The impact on data quality is permanent.
