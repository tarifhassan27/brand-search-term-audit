# Dove Brand Search-Term Taxonomy Playbook

## Summary
Audited 20 YouTube search terms across 289 Shorts.
13 terms returned 100% brand-relevant results.
4 ambiguous terms returned 0% brand results and should be dropped immediately.

---

## Term Recommendations

### KEEP — Precision 1.0 (13 terms)
These terms return only Dove brand content. No noise.

| Term | Tier | Precision |
|---|---|---|
| dove beauty bar | brand_core | 1.0 |
| dove deodorant | brand_core | 1.0 |
| dove dry shampoo | brand_core | 1.0 |
| dove moisturizer | brand_core | 1.0 |
| dove face wash | brand_core | 1.0 |
| dove soap | brand_core | 1.0 |
| dove shampoo | brand_core | 1.0 |
| dove body wash | brand_core | 1.0 |
| dove real beauty | campaign | 1.0 |
| dove self esteem | campaign | 1.0 |
| dove realbody | campaign | 1.0 |
| dove care | campaign | 1.0 |
| dov soap | misspelling | 1.0 |

### REVIEW — Precision 0.20-0.93 (2 terms)
Mostly brand but with noise. Monitor or refine.

| Term | Tier | Precision | Issue |
|---|---|---|---|
| dove sop | misspelling | 0.93 | 1 stray result - acceptable |
| dove | ambiguous | 0.53 | Half results are birds/celebrity - risky to include |

### DROP — Precision 0.0-0.20 (5 terms)
These terms pollute brand mention counts with irrelevant content.

| Term | Tier | Precision | Why |
|---|---|---|---|
| doove | misspelling | 0.20 | Attracts bird content, not brand |
| dove bird | ambiguous | 0.0 | 100% bird videos |
| dove chocolate | ambiguous | 0.0 | 100% chocolate brand |
| dove cameron | ambiguous | 0.0 | 100% celebrity content |

---

## Recommended Additions
Terms not in the original set that would likely return brand content:

- dove body lotion
- dove baby wash
- dove men+care
- dove deep moisture
- dove antiperspirant

---

## Key Finding
The bare term "dove" is the riskiest term in any brand monitoring setup.
At precision 0.53, including it inflates brand mention counts by ~47% with noise.
Always use product-specific terms instead.
