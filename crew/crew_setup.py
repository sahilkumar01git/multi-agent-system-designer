from crewai import Crew

from crew.tasks import (
    pm_task,
    arch_task,
    backend_task,
    plan_task
)

crew = Crew(
    tasks=[
        pm_task,
        arch_task,
        backend_task,
        plan_task
    ],
    verbose=True
)