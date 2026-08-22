import google.auth
from google_adk import Agent
from google_adk.tools import BigQueryToolset, BigQueryCredentialsConfig
from visualization import visualization_tool

# 1. Authenticate and Connect to BigQuery securely (No hardcoded API keys)
credentials, _ = google.auth.default()
credentials_config = BigQueryCredentialsConfig(credentials=credentials)
bigquery_toolset = BigQueryToolset(credentials_config=credentials_config)

# 2. Define the ML Prediction Tool (Connects to the BQML Logistic Regression model)
def get_podium_predictions(driver_name: str, race_name: str) -> str:
    """Queries the trained BQML model to predict podium probability."""
    # In production, this executes: SELECT * FROM ML.PREDICT(...)
    return f"Executing BQML prediction for {driver_name} at {race_name}..."

# 3. Assemble the Root Agent (Orchestrator)
root_agent = Agent(
    name="mclaren_race_intelligence",
    model="gemini-3.6-flash",
    description="Primary data science agent with direct access to McLaren's BigQuery F1 telemetry.",
    instruction="You are a data science agent. Use the BigQuery toolset for stats, the prediction tool for probabilities, and the visualization tool for charts.",
    tools=[
        bigquery_toolset,       # Tool 1: Raw SQL execution
        get_podium_predictions, # Tool 2: Machine Learning Inference
        visualization_tool      # Tool 3: Sub-agent for Code Execution
    ],
)