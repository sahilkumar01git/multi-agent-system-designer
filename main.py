from graph.workflow import run_workflow

idea = input("Enter product idea: ")
result = run_workflow(idea)

print("\n FINAL RESULT:\n")
print(result)