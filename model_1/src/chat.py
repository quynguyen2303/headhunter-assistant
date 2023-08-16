from langchain.agents import Tool
from langchain.agents import AgentType
from langchain.memory import ConversationBufferMemory
from langchain import OpenAI
from langchain.utilities import SerpAPIWrapper
from langchain.agents import initialize_agent

"""
Build an agent that can chat with a user. The agent should be able to:
    - Act as an headhunter assistant
    - Ask for the job role that the user is looking for
    - Ask for expected salary
    - Ask for reason for leaving previous job
    - Ask for the motivation for applying for the job
"""

# TODO: Add a function that can extract the job role from the user's response
# TODO: Add a function that can extract the expected salary from the user's response
# TODO: Add a function that can extract the reason for leaving previous job from the user's response
# TODO: Add a function that can extract the motivation for applying for the job from the user's response

# Function to chat with the user
