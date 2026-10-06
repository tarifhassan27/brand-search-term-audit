-- RAW SCHEMA
CREATE SCHEMA IF NOT EXISTS raw;

CREATE TABLE IF NOT EXISTS raw.search_results (
    id              SERIAL PRIMARY KEY,
    search_term     TEXT,
    video_id        TEXT,
    title           TEXT,
    channel         TEXT,
    published_at    TIMESTAMP,
    label           TEXT,
    loaded_at       TIMESTAMP DEFAULT NOW()
);

-- CLEAN SCHEMA
CREATE SCHEMA IF NOT EXISTS clean;

CREATE TABLE IF NOT EXISTS clean.search_results (
    id              SERIAL PRIMARY KEY,
    search_term     TEXT,
    term_tier       TEXT,   -- brand_core / product / campaign / misspelling / ambiguous
    video_id        TEXT,
    title           TEXT,
    channel         TEXT,
    published_at    TIMESTAMP,
    label           TEXT,   -- BRAND / CELEBRITY / BIRD / OTHER
    loaded_at       TIMESTAMP DEFAULT NOW()
);