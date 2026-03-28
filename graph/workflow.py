from langgraph.graph import StateGraph
from graph.state import AgentState
from crew.crew_setup import crew
from memory.memory import save_memory


def crew_step(state: AgentState):
    result = crew.kickoff(
        inputs={
            "idea": state["idea"]
        }
    )
    save_memory({
        "idea": state["idea"],
        "result":str(result)
    })

    return {
        "output": str(result)
    }

builder = StateGraph(AgentState)
builder.add_node(
    "crew_step",
    crew_step
)
builder.set_entry_point("crew_step")
builder.set_finish_point("crew_step")

graph = builder.compile()

def run_workflow(user_idea):
    return graph.invoke(
        {
            "idea": user_idea
        }
    )