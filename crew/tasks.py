from crewai import Task
from crew.agents import product_manager, architect,backend_dev,project_planner

pm_task=Task(
    description="""
    You are a senior product manager.
    Based on this idea:
    {idea}
    Define:
    1. target users
    2. real-world use cases
    3. core features (only important ones)
    4. optional features
    5. constraints
    Avoid generic answers.
    Keep features practical.
    """,
    expected_output="""
    product requirements including:
    features
    target users
    goals
    """,
    agent=product_manager
)

arch_task = Task(
    description="""
    Design system architecture for:
    {idea}
    Select tech stack based on requirements.
    Explain:
    frontend framework (with reason)
    backend framework (with reason)
    database choice (SQL or NoSQL with reason)
    external services needed
    high-level architecture components
    Avoid always choosing same stack.
    Choose technologies appropriate for use case.
    """,
    expected_output="system architecture",
    agent=architect
)
backend_task = Task(
    description="""
    Design system architecture for:
    {idea}
    Select tech stack based on requirements.
    Explain:
    frontend framework (with reason)
    backend framework (with reason)
    database choice (SQL or NoSQL with reason)
    external services needed
    high-level architecture components
    Avoid always choosing same stack.
    Choose technologies appropriate for use case.
    """,
    expected_output="backend architecture",
    agent=backend_dev
)



plan_task =Task(
    description="""
    Create realistic development timeline for:
    {idea}
    Assume small startup team of 3 developers.
    Provide:
    phases
    estimated duration
    dependencies between tasks
    Avoid exaggerated timelines.
    """,
    expected_output="timeline",
    agent=project_planner
)