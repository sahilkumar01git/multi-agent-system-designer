from crewai import Agent
from config.llm import llm


product_manager=Agent(
    role="Product manager",
    goal="Create product requirements without unnecessary searches",
    backstory="""expert in defining software features,
    user needs, and product goals.""",
    llm=llm,
    verbose=False
)

architect=Agent(
    role="Software Architect",
    goal="design system architecture",
    backstory="""expert in designing frontend and backend system design""",
    llm=llm,
    verbose=False
)

backend_dev=Agent(
    role="Backend Developer",
    goal="design APIs and database",
    backstory="""expert in REST APIs and database schemas""",
    llm=llm,
    verbose=False
)

project_planner=Agent(
    role="Project Planner",

    goal="""
    Create project timeline with phases and duration.
    """,
    backstory="""
    Expert in software planning and estimating project timelines.
    """,
    llm=llm,
    verbose=False
)
