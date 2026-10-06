COPY raw.search_results (search_term, video_id, title, channel, published_at, label)
FROM 'D:/brand-search-term-audit/02_data/raw_results.csv'
DELIMITER ','
CSV HEADER;