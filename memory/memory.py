import json
import os

MEMORY_FILE = "memory/history.json"

def load_memory():
    if not os.path.exists(MEMORY_FILE):
        return []

    with open(MEMORY_FILE, "r") as f:
        return json.load(f)

def save_memory(new_entry):
    memory = load_memory()
    memory.append(new_entry)

    with open(MEMORY_FILE, "w") as f:
        json.dump(memory, f, indent=2)