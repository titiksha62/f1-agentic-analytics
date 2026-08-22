-- Model: podium_predictor
-- Purpose: Logistic regression to predict podium finishes based on pre-race features.

CREATE OR REPLACE MODEL `f1_data.podium_predictor`
OPTIONS(
    model_type='LOGISTIC_REG',
    input_label_cols=['is_podium']
) AS
SELECT
    is_podium,
    grid_position,
    driver_championship_pos_entering,
    constructor_championship_pos_entering
FROM `f1_data.v_bqml_features`
-- Train on pre-2024 data, hold out recent seasons for agent validation
WHERE season <= 2023;