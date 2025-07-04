import os
from dotenv import load_dotenv
from julep import Julep
import yaml
import time

load_dotenv()

client = Julep(
    api_key=os.getenv('JULEP_API_KEY'),
    environment=os.getenv('JULEP_ENVIRONMENT', 'production')
)

agent = client.agents.create(
    name="Writing Assistant",
    model="claude-3.5-sonnet",
    about="A helpful AI assistant that specializes in writing and editing."
)

import yaml 

task_definition = yaml.safe_load("""
name: Story Generator
description: Generate a short story based on a given topic
main:
- prompt:
  - role: system
    content: You are a creative story writer.
  - role: user
    content: $ f'Write a short story about {steps[0].input.topic}'
""")

task = client.tasks.create(
    agent_id=agent.id,
    **task_definition # Unpack the task definition
)

execution = client.executions.create(
    task_id=task.id,
    input={"topic": "a magical garden"}
)

# # Wait for the execution to complete
# while (result := client.executions.get(execution.id)).status not in ['succeeded', 'failed']:
#     print(result.status)
#     time.sleep(1)

# if result.status == "succeeded":
#     print(result.output)
# else:
#     print(f"Error: {result.error}")

from julep import Client
import time
import yaml



# Create the agent
agent = client.agents.create(
  name="Julep Trip Planning Agent",
  about="A Julep agent that can generate a detailed itinerary for visiting tourist attractions in some locations, considering the current weather conditions.",
)

# Load the task definition
with open('trip_planning_task.yaml', 'r') as file:
  task_definition = yaml.safe_load(file)

# Create the task
task = client.tasks.create(
  agent_id=agent.id,
  **task_definition
)

# Create the execution
execution = client.executions.create(
    task_id=task.id,
    input={
        "locations": ["New York", "London", "Paris", "Tokyo", "Sydney"]
    }
)

# Wait for the execution to complete
while (result := client.executions.get(execution.id)).status not in ['succeeded', 'failed']:
    print(result.status)
    time.sleep(1)

# Print the result
if result.status == "succeeded":
    print(result.output)
else:
    print(f"Error: {result.error}")