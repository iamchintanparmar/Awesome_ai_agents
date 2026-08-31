
import streamlit as st
from agno.agent import Agent
from agno.run.agent import RunOutput
from agno.team import Team
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.hackernews import HackerNewsTools
from agno.tools.newspaper4k import Newspaper4kTools
from agno.models.ollama import Ollama


st.title("Multi-Agent AI Researcher using Llama-3 🔍🤖")
st.caption("This app allows you to research top stories and users on HackerNews and write blogs, reports and social posts.")

hn_researcher = Agent(
    name="HackerNews Researcher",
    model=Ollama(id="llama3.2", max_tokens=1024),
    role="Gets top stories from hackernews.",
    tools=[HackerNewsTools()],
)

web_searcher = Agent(
    name="Web Searcher",
    model=Ollama(id="llama3.2", max_tokens=1024),
    role="Searches the web for information on a topic",
    tools=[DuckDuckGoTools()],
    add_datetime_to_context=True,
)

article_reader = Agent(
    name="Article Reader",
    model=Ollama(id="llama3.2", max_tokens=1024),
    role="Reads articles from URLs.",
    tools=[Newspaper4kTools()],
)

hackernews_team = Team(
    name="HackerNews Team",
    model=Ollama(id="llama3.2", max_tokens=1024),
    members=[hn_researcher, web_searcher, article_reader],
    instructions=[
        "First, search hackernews for what the user is asking about.",
        "Then, ask the article reader to read the links for the stories to get more information.",
        "Important: you must provide the article reader with the links to read.",
        "Then, ask the web searcher to search for each story to get more information.",
        "Finally, provide a thoughtful and engaging summary.",
    ],
    markdown=True,
    debug_mode=True,
    show_members_responses=True,
)


query = st.text_input("Enter your report query")

if query:
  
    response: RunOutput = hackernews_team.run(query, stream=False)
    st.write(response.content)
