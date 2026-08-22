-- View: v_mclaren_race_results
-- Purpose: Clean, self-documenting layer for the AI agent to query without complex joins.
-- Schema design acts as prompt engineering for the LLM.

CREATE OR REPLACE VIEW `f1_data.v_mclaren_race_results` AS
SELECT 
    r.race_id,
    r.year AS season,
    c.name AS circuit_name,
    d.forename || ' ' || d.surname AS driver_name,
    res.position_order,
    -- Pre-compute boolean flags so the agent doesn't have to guess logic
    IF(res.position_order <= 3, TRUE, FALSE) AS is_podium,
    IF(res.position_order = 1, TRUE, FALSE) AS is_win
FROM `f1_data.results` res
JOIN `f1_data.races` r ON res.race_id = r.race_id
JOIN `f1_data.drivers` d ON res.driver_id = d.driver_id
JOIN `f1_data.constructors` cons ON res.constructor_id = cons.constructor_id
WHERE cons.constructor_ref = 'mclaren';