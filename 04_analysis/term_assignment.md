# Term Tier Assignment

## How Terms Were Assigned to Tiers

Each of the 20 search terms was assigned to one of four tiers before data collection:

| Tier | Definition | Example |
|---|---|---|
| brand_core | Product name + category; unambiguous brand signal | dove soap |
| campaign | Known Dove campaign name or hashtag | dove real beauty |
| misspelling | Common typo variants of "dove" or product terms | dov soap, dove sop |
| ambiguous | Terms where "dove" could mean something other than the brand | dove bird, dove cameron |

## Rationale

Tier assignment was done manually based on prior knowledge of the brand and
common search behavior. Ambiguous terms were included deliberately to measure
how much noise they introduce — the hypothesis being that bare or context-free
uses of "dove" would underperform product-specific terms.

The audit confirmed this: all brand_core and campaign terms scored precision 1.0,
while ambiguous terms ranged from 0.00 to 0.53.
