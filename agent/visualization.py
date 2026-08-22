from google_adk import Agent, AgentTool, BuiltInCodeExecutor

VISUALIZATION_AGENT_DESCRIPTION = "An agent that writes and executes Python code to generate charts."
VISUALIZATION_INSTRUCTIONS = "Generate matplotlib charts using McLaren brand colors: HEX#FF8000 (papaya) and HEX#53565A (anthracite)."

# Create the isolated sub-agent with the Code Executor
visualization_agent = Agent(
    name="visualization_agent",
    model="gemini-3.6-flash",
    description=VISUALIZATION_AGENT_DESCRIPTION,
    instruction=VISUALIZATION_INSTRUCTIONS,
    code_executor=BuiltInCodeExecutor(),
)

# Wrap it so the root agent can call it like a standard tool
visualization_tool = AgentTool(agent=visualization_agent)