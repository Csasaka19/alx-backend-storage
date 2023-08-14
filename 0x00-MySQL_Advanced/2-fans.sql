--  script that ranks country origins of bands, ordered by the number of (non-unique) fans
--  that have the band in their top 10.
SELECT origin, COUNT(*) AS num_fans FROM metal_bands GROUP BY origin ORDER BY num_fans DESC;
