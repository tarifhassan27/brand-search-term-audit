# Business Problem

A brand monitoring tool counts YouTube mentions by searching keywords.
If the search terms are wrong, the mention count is wrong.

"Dove" returns soap ads, a celebrity (Dove Cameron), bird videos,
and music. A naive search treats all of these as brand mentions.

This project audits Dove's YouTube search terms to find which ones
are clean (mostly brand), which are mixed, and which are junk.
The output is a recommendation: keep, drop, or add an exclusion filter
for each search term.