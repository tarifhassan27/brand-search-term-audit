-- Phase 6: Precision per search term
-- Precision = brand results / total results
-- A score of 1.0 = every result was Dove the brand
-- A score of 0.0 = zero brand results (pure noise)

SELECT
    search_term,
    term_tier,
    COUNT(*) AS total_videos,
    SUM(CASE WHEN label = 'BRAND' THEN 1 ELSE 0 END) AS brand_count,
    ROUND(
        SUM(CASE WHEN label = 'BRAND' THEN 1 ELSE 0 END)::NUMERIC / COUNT(*), 2
    ) AS precision_score
FROM clean.search_results
GROUP BY search_term, term_tier
ORDER BY precision_score DESC, total_videos DESC;